# Registers adapted from sample code for SEMTECH SX1276
from __future__ import print_function

import time


def connect(SPI, frq, **kwargs):
    return SX1276(SPI, frq, **kwargs)


class SX1276():
    name = 'SX1276'
    # registers
    REG_FIFO = 0x00
    REG_OP_MODE = 0x01
    REG_FRF_MSB = 0x06
    REG_FRF_MID = 0x07
    REG_FRF_LSB = 0x08
    REG_PA_CONFIG = 0x09
    REG_LNA = 0x0c
    REG_FIFO_ADDR_PTR = 0x0d
    REG_FIFO_TX_BASE_ADDR = 0x0e
    REG_FIFO_RX_BASE_ADDR = 0x0f
    REG_FIFO_RX_CURRENT_ADDR = 0x10
    REG_IRQ_FLAGS = 0x12
    REG_RX_NB_BYTES = 0x13
    REG_PKT_RSSI_VALUE = 0x1a
    REG_PKT_SNR_VALUE = 0x1b
    REG_MODEM_CONFIG_1 = 0x1d
    REG_MODEM_CONFIG_2 = 0x1e
    REG_PREAMBLE_MSB = 0x20
    REG_PREAMBLE_LSB = 0x21
    REG_PAYLOAD_LENGTH = 0x22
    REG_MODEM_CONFIG_3 = 0x26
    REG_RSSI_WIDEBAND = 0x2c
    REG_DETECTION_OPTIMIZE = 0x31
    REG_DETECTION_THRESHOLD = 0x37
    REG_SYNC_WORD = 0x39
    REG_DIO_MAPPING_1 = 0x40
    REG_VERSION = 0x42
    REG_PA_DAC = 0x4D
    # modes
    MODE_LONG_RANGE_MODE = 0x80
    MODE_SLEEP = 0x00
    MODE_STDBY = 0x01
    MODE_TX = 0x03
    MODE_RX_CONTINUOUS = 0x05
    MODE_RX_SINGLE = 0x06

    # PA config
    PA_BOOST = 0x80

    # IRQ masks
    IRQ_TX_DONE_MASK = 0x08
    IRQ_PAYLOAD_CRC_ERROR_MASK = 0x20
    IRQ_RX_DONE_MASK = 0x40

    MAX_PKT_LENGTH = 255

    PA_OUTPUT_RFO_PIN = 0
    PA_OUTPUT_PA_BOOST_PIN = 1
    _onReceive = 0
    _frequency = 10
    _packetIndex = 0
    packetLength = 0

    def __init__(self, SPI, frq, **kwargs):
        self.SPI = SPI
        self.SPI.set_parameters(2, 6, 1, 0)
        self.name = 'SX1276'
        self.frequency = frq

        self.reset()
        self.version = self.SPIRead(self.REG_VERSION, 1)[0]
        if self.version != 0x12:
            print('version error', self.version)
        self.sleep()
        self.setFrequency(self.frequency)

        # set base address
        self.SPIWrite(self.REG_FIFO_TX_BASE_ADDR, [0])
        self.SPIWrite(self.REG_FIFO_RX_BASE_ADDR, [0])

        # set LNA boost
        self.SPIWrite(self.REG_LNA, [self.SPIRead(self.REG_LNA)[0] | 0x03])

        # set auto ADC
        self.SPIWrite(self.REG_MODEM_CONFIG_3, [0x04])

        # output power 17dbm
        self.setTxPower(kwargs.get('power', 17),
                        self.PA_OUTPUT_PA_BOOST_PIN if kwargs.get('boost', True) else self.PA_OUTPUT_RFO_PIN)
        self.idle()

        # set bandwidth
        self.setSignalBandwidth(kwargs.get('BW', 125e3))
        self.setSpreadingFactor(kwargs.get('SF', 12))
        self.setCodingRate4(kwargs.get('CF', 5))

    def beginPacket(self, implicitHeader=False):
        self.idle()
        if implicitHeader:
            self.implicitHeaderMode()
        else:
            self.explicitHeaderMode()

        # reset FIFO & payload length
        self.SPIWrite(self.REG_FIFO_ADDR_PTR, [0])
        self.SPIWrite(self.REG_PAYLOAD_LENGTH, [0])

    def endPacket(self):
        # put in TX mode
        self.SPIWrite(self.REG_OP_MODE, [self.MODE_LONG_RANGE_MODE | self.MODE_TX])
        while 1:  # Wait for TX done
            if self.SPIRead(self.REG_IRQ_FLAGS, 1)[0] & self.IRQ_TX_DONE_MASK:
                break
            else:
                print('wait...')
                time.sleep(0.1)
        self.SPIWrite(self.REG_IRQ_FLAGS, [self.IRQ_TX_DONE_MASK])

    def parsePacket(self, size=0):
        self.packetLength = 0
        irqFlags = self.SPIRead(self.REG_IRQ_FLAGS, 1)[0]
        if size > 0:
            self.implicitHeaderMode()
            self.SPIWrite(self.REG_PAYLOAD_LENGTH, [size & 0xFF])
        else:
            self.explicitHeaderMode()
        self.SPIWrite(self.REG_IRQ_FLAGS, [irqFlags])
        if (irqFlags & self.IRQ_RX_DONE_MASK) and (irqFlags & self.IRQ_PAYLOAD_CRC_ERROR_MASK) == 0:
            self._packetIndex = 0
            if self._implicitHeaderMode:
                self.packetLength = self.SPIRead(self.REG_PAYLOAD_LENGTH, 1)[0]
            else:
                self.packetLength = self.SPIRead(self.REG_RX_NB_BYTES, 1)[0]
            self.SPIWrite(self.REG_FIFO_ADDR_PTR, self.SPIRead(self.REG_FIFO_RX_CURRENT_ADDR, 1))
            self.idle()
        elif self.SPIRead(self.REG_OP_MODE)[0] != (self.MODE_LONG_RANGE_MODE | self.MODE_RX_SINGLE):
            self.SPIWrite(self.REG_FIFO_ADDR_PTR, [0])
            self.SPIWrite(self.REG_OP_MODE, [self.MODE_LONG_RANGE_MODE | self.MODE_RX_SINGLE])
        return self.packetLength

    def packetRssi(self):
        return self.SPIRead(self.REG_PKT_RSSI_VALUE)[0] - (164 if self._frequency < 868e6 else 157)

    def packetSnr(self):
        return self.SPIRead(self.REG_PKT_SNR_VALUE)[0] * 0.25

    def write(self, byteArray):
        size = len(byteArray)
        currentLength = self.SPIRead(self.REG_PAYLOAD_LENGTH)[0]
        if (currentLength + size) > self.MAX_PKT_LENGTH:
            size = self.MAX_PKT_LENGTH - currentLength
        self.SPIWrite(self.REG_FIFO, byteArray[:size])
        self.SPIWrite(self.REG_PAYLOAD_LENGTH, [currentLength + size])
        return size

    def available(self):
        return self.SPIRead(self.REG_RX_NB_BYTES)[0] - self._packetIndex

    def checkRx(self):
        irqFlags = self.SPIRead(self.REG_IRQ_FLAGS, 1)[0]
        if (irqFlags & self.IRQ_RX_DONE_MASK) and (irqFlags & self.IRQ_PAYLOAD_CRC_ERROR_MASK) == 0:
            return 1
        return 0;

    def read(self):
        if not self.available(): return -1
        self._packetIndex += 1
        return self.SPIRead(self.REG_FIFO)[0]

    def readAll(self):
        p = []
        while self.available():
            p.append(self.read())
        return p

    def peek(self):
        if not self.available(): return -1
        self.currentAddress = self.SPIRead(self.REG_FIFO_ADDR_PTR)
        val = self.SPIRead(self.REG_FIFO)[0]
        self.SPIWrite(self.REG_FIFO_ADDR_PTR, self.currentAddress)
        return val

    def flush(self):
        pass

    def receive(self, size):
        if size > 0:
            self.implicitHeaderMode()
            self.SPIWrite(self.REG_PAYLOAD_LENGTH, [size & 0xFF])
        else:
            self.explicitHeaderMode()

        self.SPIWrite(self.REG_OP_MODE, [self.MODE_LONG_RANGE_MODE | self.MODE_RX_SINGLE])

    def reset(self):
        pass

    def idle(self):
        self.SPIWrite(self.REG_OP_MODE, [self.MODE_LONG_RANGE_MODE | self.MODE_STDBY])

    def sleep(self):
        self.SPIWrite(self.REG_OP_MODE, [self.MODE_LONG_RANGE_MODE | self.MODE_SLEEP])

    def setTxPower(self, level, pin):
        if pin == self.PA_OUTPUT_RFO_PIN:
            if level < 0:
                level = 0
            elif level > 14:
                level = 14
            self.SPIWrite(self.REG_PA_CONFIG, [0x70 | level])
        else:
            if level < 2:
                level = 2
            elif level > 17:
                level = 17
            if level == 17:
                print('max power output')
                self.SPIWrite(self.REG_PA_DAC, [0x87])
            else:
                self.SPIWrite(self.REG_PA_DAC, [0x84])
            self.SPIWrite(self.REG_PA_CONFIG, [self.PA_BOOST | 0x70 | (level - 2)])

        print('power', hex(self.SPIRead(self.REG_PA_CONFIG)[0]))

    def setFrequency(self, frq):
        self._frequency = frq
        frf = (int(frq) << 19) / 32000000
        print('frf', frf)
        print('freq', (frf >> 16) & 0xFF, (frf >> 8) & 0xFF, (frf) & 0xFF)
        self.SPIWrite(self.REG_FRF_MSB, [(frf >> 16) & 0xFF])
        self.SPIWrite(self.REG_FRF_MID, [(frf >> 8) & 0xFF])
        self.SPIWrite(self.REG_FRF_LSB, [frf & 0xFF])

    def setSpreadingFactor(self, sf):
        if sf < 6:
            sf = 6
        elif sf > 12:
            sf = 12

        if sf == 6:
            self.SPIWrite(self.REG_DETECTION_OPTIMIZE, [0xc5])
            self.SPIWrite(self.REG_DETECTION_THRESHOLD, [0x0c])
        else:
            self.SPIWrite(self.REG_DETECTION_OPTIMIZE, [0xc3])
            self.SPIWrite(self.REG_DETECTION_THRESHOLD, [0x0a])
        self.SPIWrite(self.REG_MODEM_CONFIG_2, [(self.SPIRead(self.REG_MODEM_CONFIG_2)[0] & 0x0F) | ((sf << 4) & 0xF0)])

    def setSignalBandwidth(self, sbw):
        bw = 9
        num = 0
        for a in [7.8e3, 10.4e3, 15.6e3, 20.8e3, 31.25e3, 41.7e3, 62.5e3, 125e3, 250e3]:
            if sbw <= a:
                bw = num
                break
            num += 1
        print('bandwidth: ', bw)
        self.SPIWrite(self.REG_MODEM_CONFIG_1, [(self.SPIRead(self.REG_MODEM_CONFIG_1)[0] & 0x0F) | (bw << 4)])

    def setCodingRate4(self, denominator):
        if denominator < 5:
            denominator = 5
        elif denominator > 8:
            denominator = 8
        self.SPIWrite(self.REG_MODEM_CONFIG_1,
                      [(self.SPIRead(self.REG_MODEM_CONFIG_1)[0] & 0xF1) | ((denominator - 4) << 4)])

    def setPreambleLength(self, length):
        self.SPIWrite(self.REG_PREAMBLE_MSB, [(length >> 8) & 0xFF])
        self.SPIWrite(self.REG_PREAMBLE_LSB, [length & 0xFF])

    def setSyncWord(self, sw):
        self.SPIWrite(self.REG_SYNC_WORD, [sw])

    def crc(self):
        self.SPIWrite(self.REG_MODEM_CONFIG_2, [self.SPIRead(self.REG_MODEM_CONFIG_2)[0] | 0x04])

    def noCrc(self):
        self.SPIWrite(self.REG_MODEM_CONFIG_2, [self.SPIRead(self.REG_MODEM_CONFIG_2)[0] & 0xFB])

    def random(self):
        return self.SPIRead(self.REG_RSSI_WIDEBAND)[0]

    def explicitHeaderMode(self):
        self._implicitHeaderMode = 0
        self.SPIWrite(self.REG_MODEM_CONFIG_1, [self.SPIRead(self.REG_MODEM_CONFIG_1)[0] & 0xFE])

    def implicitHeaderMode(self):
        self._implicitHeaderMode = 1
        self.SPIWrite(self.REG_MODEM_CONFIG_1, [self.SPIRead(self.REG_MODEM_CONFIG_1)[0] | 0x01])

    def handleDio0Rise(self):
        irqFlags = self.SPIRead(self.REG_IRQ_FLAGS, 1)[0]
        self.SPIWrite(self.REG_IRQ_FLAGS, [irqFlags])

        if (irqFlags & self.IRQ_PAYLOAD_CRC_ERROR_MASK) == 0:
            self._packetIndex = 0
            if self._implicitHeaderMode:
                self.packetLength = self.SPIRead(self.REG_PAYLOAD_LENGTH, 1)[0]
            else:
                self.packetLength = self.SPIRead(self.REG_RX_NB_BYTES, 1)[0]

            self.SPIWrite(self.REG_FIFO_ADDR_PTR, self.SPIRead(self.REG_FIFO_RX_CURRENT_ADDR, 1))
            if self._onReceive:
                print(self.packetLength)
        # self._onReceive(self.packetLength)

        self.SPIWrite(self.REG_FIFO_ADDR_PTR, [0])

    def SPIWrite(self, adr, byteArray):
        return self.SPI.xfer('CS1', [0x80 | adr] + byteArray)[1:]

    def SPIRead(self, adr, total_bytes=1):
        return self.SPI.xfer('CS1', [adr] + [0] * total_bytes)[1:]

    def getRaw(self):
        val = self.SPIRead(0x02, 1)
        return val


if __name__ == "__main__":
    RX = 0;
    TX = 1
    mode = RX
    from PSL import sciencelab

    I = sciencelab.connect()
    lora = SX1276(I.SPI, 434e6, boost=True, power=17, BW=125e3, SF=12, CR=5)  # settings for maximum range
    lora.crc()
    cntr = 0
    while 1:
        time.sleep(0.01)
        if mode == TX:
            lora.beginPacket()
            lora.write([cntr])
            # lora.write([ord(a) for a in ":"]+[cntr])
            print(time.ctime(), [ord(a) for a in ":"] + [cntr], hex(lora.SPIRead(lora.REG_OP_MODE)[0]))
            lora.endPacket()
            cntr += 1
            if cntr == 255: cntr = 0
        elif mode == RX:
            packet_size = lora.parsePacket()
            if packet_size:
                print('data', lora.readAll())
                print('Rssi', lora.packetRssi(), lora.packetSnr())
