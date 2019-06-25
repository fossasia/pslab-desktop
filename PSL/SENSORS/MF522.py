# -*- coding: utf-8 -*-
# MF522 - Software stack to access the MF522 RFID reader via  FOSSASIA PSLab
#
from __future__ import print_function


def connect(I, cs):
    return MF522(I, cs)


class MF522:
    # Constants from https://github.com/miguelbalboa/rfid ( Open source License : UNLICENSE)
    CommandReg = 0x01 << 1  # starts and stops command execution
    ComIEnReg = 0x02 << 1  # enable and disable interrupt request control bits
    DivIEnReg = 0x03 << 1  # enable and disable interrupt request control bits
    ComIrqReg = 0x04 << 1  # interrupt request bits
    DivIrqReg = 0x05 << 1  # interrupt request bits
    ErrorReg = 0x06 << 1  # error bits showing the error status of the last command executed
    Status1Reg = 0x07 << 1  # communication status bits
    Status2Reg = 0x08 << 1  # receiver and transmitter status bits
    FIFODataReg = 0x09 << 1  # input and output of 64 byte FIFO buffer
    FIFOLevelReg = 0x0A << 1  # number of bytes stored in the FIFO buffer
    WaterLevelReg = 0x0B << 1  # level for FIFO underflow and overflow warning
    ControlReg = 0x0C << 1  # miscellaneous control registers
    BitFramingReg = 0x0D << 1  # adjustments for bit-oriented frames
    CollReg = 0x0E << 1  # bit position of the first bit-collision detected on the RF sciencelab

    ModeReg = 0x11 << 1  # defines general modes for transmitting and receiving
    TxModeReg = 0x12 << 1  # defines transmission data rate and framing
    RxModeReg = 0x13 << 1  # defines reception data rate and framing
    TxControlReg = 0x14 << 1  # controls the logical behavior of the antenna driver pins TX1 and TX2
    TxASKReg = 0x15 << 1  # controls the setting of the transmission modulation
    TxSelReg = 0x16 << 1  # selects the internal sources for the antenna driver
    RxSelReg = 0x17 << 1  # selects internal receiver settings
    RxThresholdReg = 0x18 << 1  # selects thresholds for the bit decoder
    DemodReg = 0x19 << 1  # defines demodulator settings
    MfTxReg = 0x1C << 1  # controls some MIFARE communication transmit parameters
    MfRxReg = 0x1D << 1  # controls some MIFARE communication receive parameters
    SerialSpeedReg = 0x1F << 1  # selects the speed of the serial UART sciencelab

    CRCResultRegH = 0x21 << 1  # shows the MSB and LSB values of the CRC calculation
    CRCResultRegL = 0x22 << 1
    ModWidthReg = 0x24 << 1  # controls the ModWidth setting?
    RFCfgReg = 0x26 << 1  # configures the receiver gain
    GsNReg = 0x27 << 1  # selects the conductance of the antenna driver pins TX1 and TX2 for modulation
    CWGsPReg = 0x28 << 1  # defines the conductance of the p-driver output during periods of no modulation
    ModGsPReg = 0x29 << 1  # defines the conductance of the p-driver output during periods of modulation
    TModeReg = 0x2A << 1  # defines settings for the internal timer
    TPrescalerReg = 0x2B << 1  # the lower 8 bits of the TPrescaler value. The 4 high bits are in TModeReg.
    TReloadRegH = 0x2C << 1  # defines the 16-bit timer reload value
    TReloadRegL = 0x2D << 1
    TCounterValueRegH = 0x2E << 1  # shows the 16-bit timer value
    TCounterValueRegL = 0x2F << 1

    TestSel1Reg = 0x31 << 1  # general test signal configuration
    TestSel2Reg = 0x32 << 1  # general test signal configuration
    TestPinEnReg = 0x33 << 1  # enables pin output driver on pins D1 to D7
    TestPinValueReg = 0x34 << 1  # defines the values for D1 to D7 when it is used as an I/O bus
    TestBusReg = 0x35 << 1  # shows the status of the internal test bus
    AutoTestReg = 0x36 << 1  # controls the digital self test
    VersionReg = 0x37 << 1  # shows the software version
    AnalogTestReg = 0x38 << 1  # controls the pins AUX1 and AUX2
    TestDAC1Reg = 0x39 << 1  # defines the test value for TestDAC1
    TestDAC2Reg = 0x3A << 1  # defines the test value for TestDAC2
    TestADCReg = 0x3B << 1  # shows the value of ADC I and Q channels

    # MFRC522 commands. Described in chapter 10 of the datasheet.
    PCD_Idle = 0x00  # no action, cancels current command execution
    PCD_Mem = 0x01  # stores 25 bytes into the internal buffer
    PCD_GenerateRandomID = 0x02  # generates a 10-byte random ID number
    PCD_CalcCRC = 0x03  # activates the CRC coprocessor or performs a self test
    PCD_Transmit = 0x04  # transmits data from the FIFO buffer
    PCD_NoCmdChange = 0x07
    PCD_Receive = 0x08  # activates the receiver circuits
    PCD_Transceive = 0x0C  # transmits data from FIFO buffer to antenna and automatically activates the receiver after transmission
    PCD_MFAuthent = 0x0E  # performs the MIFARE standard authentication as a reader
    PCD_SoftReset = 0x0F  # resets the MFRC522

    RxGain_18dB = 0x00 << 4  # 000b - 18 dB, minimum
    RxGain_23dB = 0x01 << 4  # 001b - 23 dB
    RxGain_18dB_2 = 0x02 << 4  # 010b - 18 dB, it seems 010b is a duplicate for 000b
    RxGain_23dB_2 = 0x03 << 4  # 011b - 23 dB, it seems 011b is a duplicate for 001b
    RxGain_33dB = 0x04 << 4  # 100b - 33 dB, average, and typical default
    RxGain_38dB = 0x05 << 4  # 101b - 38 dB
    RxGain_43dB = 0x06 << 4  # 110b - 43 dB
    RxGain_48dB = 0x07 << 4  # 111b - 48 dB, maximum
    RxGain_min = 0x00 << 4  # 000b - 18 dB, minimum, convenience for RxGain_18dB
    RxGain_avg = 0x04 << 4  # 100b - 33 dB, average, convenience for RxGain_33dB
    RxGain_max = 0x07 << 4  # 111b - 48 dB, maximum, convenience for RxGain_48dB

    # The commands used by the PCD to manage communication with several PICCs (ISO 14443-3, Type A, section 6.4)
    PICC_CMD_REQA = 0x26  # REQuest command, Type A. Invites PICCs in state IDLE to go to READY and prepare for anticollision or selection
    PICC_CMD_WUPA = 0x52  # Wake-UP command, prepare for anticollision or selection. 7 bit frame.
    PICC_CMD_CT = 0x88  # Cascade Tag. Not really a command, but used during anti collision.
    PICC_CMD_SEL_CL1 = 0x93  # Anti collision/Select, Cascade Level 1
    PICC_CMD_SEL_CL2 = 0x95  # Anti collision/Select, Cascade Level 2
    PICC_CMD_SEL_CL3 = 0x97  # Anti collision/Select, Cascade Level 3
    PICC_CMD_HLTA = 0x50  # HaLT command, Type A. Instructs an ACTIVE PICC to go to state HALT.
    # The commands used for MIFARE Classic (from http://www.mouser.com/ds/2/302/MF1S503x-89574.pdf, Section 9)
    # Use PCD_MFAuthent to authenticate access to a sector, then use these commands to read/write/modify the blocks on the sector.
    # The read/write commands can also be used for MIFARE Ultralight.
    PICC_CMD_MF_AUTH_KEY_A = 0x60  # Perform authentication with Key A
    PICC_CMD_MF_AUTH_KEY_B = 0x61  # Perform authentication with Key B
    PICC_CMD_MF_READ = 0x30  # Reads one 16 byte block from the authenticated sector of the PICC. Also used for MIFARE Ultralight.
    PICC_CMD_MF_WRITE = 0xA0  # Writes one 16 byte block to the authenticated sector of the PICC. Called "COMPATIBILITY WRITE" for MIFARE Ultralight.
    PICC_CMD_MF_DECREMENT = 0xC0  # Decrements the contents of a block and stores the result in the internal data register.
    PICC_CMD_MF_INCREMENT = 0xC1  # Increments the contents of a block and stores the result in the internal data register.
    PICC_CMD_MF_RESTORE = 0xC2  # Reads the contents of a block into the internal data register.
    PICC_CMD_MF_TRANSFER = 0xB0  # Writes the contents of the internal data register to a block.

    NRSTPD = 22
    MAX_LEN = 16
    MI_OK = 0
    MI_NOTAGERR = 1
    MI_ERR = 2

    PCD_CALCCRC = 0x03

    PICC_REQIDL = 0x26
    PICC_REQALL = 0x52
    PICC_ANTICOLL = 0x93
    PICC_SElECTTAG = 0x93
    PICC_AUTHENT1A = 0x60
    PICC_AUTHENT1B = 0x61
    PICC_READ = 0x30
    PICC_WRITE = 0xA0
    PICC_DECREMENT = 0xC0
    PICC_INCREMENT = 0xC1
    PICC_RESTORE = 0xC2
    PICC_TRANSFER = 0xB0
    PICC_HALT = 0x50

    # The commands used for MIFARE Ultralight (from http://www.nxp.com/documents/data_sheet/MF0ICU1.pdf, Section 8.6)
    # The PICC_CMD_MF_READ and PICC_CMD_MF_WRITE can also be used for MIFARE Ultralight.
    PICC_CMD_UL_WRITE = 0xA2  # Writes one 4 byte page to the PICC.

    MF_ACK = 0xA  # The MIFARE Classic uses a 4 bit ACK/NAK. Any other value than 0xA is NAK.
    MF_KEY_SIZE = 6  # A Mifare Crypto1 key is 6 bytes.

    def __init__(self, I, cs='CS1'):
        self.cs = cs
        self.I = I
        self.I.SPI.set_parameters(2, 1, 1, 0)
        if not self.reset():
            self.connected = False
            return None
        self.write(self.TModeReg, 0x80)
        self.write(self.TPrescalerReg, 0xA9)
        self.write(self.TReloadRegH, 0x03)
        self.write(self.TReloadRegL, 0xE8)

        self.write(self.TxASKReg, 0x40)
        self.write(self.ModeReg, 0x3D)

        # Enable the antenna
        self.enableAntenna()
        self.connected = True

    def enableAntenna(self):
        val = self.read(self.TxControlReg);
        if ((val & 0x03) != 0x03):
            self.write(self.TxControlReg, val | 0x03);

    def reset(self):
        self.write(self.CommandReg, self.PCD_SoftReset)
        s = time.time()
        while (self.read(self.CommandReg) & (1 << 4)):
            print('wait')
            time.sleep(0.1)
            if time.time() - s > .5: return False
        return True

    def write(self, register, val):
        self.I.SPI.set_cs(self.cs, 0)
        ret = self.I.SPI.send16(((register & 0x7F) << 8) | val)
        self.I.SPI.set_cs(self.cs, 1)
        return ret & 0xFF

    def read(self, register):
        self.I.SPI.set_cs(self.cs, 0)
        ret = self.I.SPI.send16((register | 0x80) << 8)
        self.I.SPI.set_cs(self.cs, 1)
        return ret & 0xFF

    def readMany(self, register, total):
        self.I.SPI.set_cs(self.cs, 0)
        self.I.SPI.send8(register)
        vals = []
        for a in range(total - 1):
            vals.append(I.SPI.send8(register))
        vals.append(I.SPI.send8(0))
        self.I.SPI.set_cs(self.cs, 1)
        return vals

    def getStatus(self):
        return self.read(self.Status1Reg)

    def getVersion(self):
        ver = self.read(self.VersionReg)
        if ver == 0x88:
            print('Cloned version: Fudan Semiconductors')
        elif ver == 0x90:
            print('version 1.0')
        elif ver == 0x91:
            print('version 1.0')
        elif ver == 0x92:
            print('version 2.0')
        else:
            print('Unknown version ', ver)
        return ver

    def SetBitMask(self, reg, mask):
        tmp = self.read(reg)
        self.write(reg, tmp | mask)

    def ClearBitMask(self, reg, mask):
        tmp = self.read(reg);
        self.write(reg, tmp & (~mask))

    def MFRC522_ToCard(self, command, sendData):
        returnedData = []
        backLen = 0
        status = self.MI_ERR
        irqEn = 0x00
        waitIRq = 0x00
        lastBits = None
        n = 0
        i = 0

        if command == self.PCD_MFAuthent:
            irqEn = 0x12
            waitIRq = 0x10
        if command == self.PCD_Transceive:
            irqEn = 0x77
            waitIRq = 0x30

        self.write(self.ComIEnReg, irqEn | 0x80)
        self.ClearBitMask(self.ComIrqReg, 0x80)
        self.SetBitMask(self.FIFOLevelReg, 0x80)

        self.write(self.CommandReg, self.PCD_Idle);

        for a in sendData:
            self.write(self.FIFODataReg, a)
        self.write(self.CommandReg, command)

        if command == self.PCD_Transceive:
            self.SetBitMask(self.BitFramingReg, 0x80)

        i = 2000
        while True:
            n = self.read(self.ComIrqReg)
            i = i - 1
            if ~((i != 0) and ~(n & 0x01) and ~(n & waitIRq)):
                break

        self.ClearBitMask(self.BitFramingReg, 0x80)

        if i != 0:
            if (self.read(self.ErrorReg) & 0x1B) == 0x00:
                status = self.MI_OK

                if n & irqEn & 0x01:
                    status = self.MI_NOTAGERR

                if command == self.PCD_Transceive:
                    n = self.read(self.FIFOLevelReg)
                    lastBits = self.read(self.ControlReg) & 0x07
                    if lastBits != 0:
                        backLen = (n - 1) * 8 + lastBits
                    else:
                        backLen = n * 8

                    if n == 0:
                        n = 1
                    if n > self.MAX_LEN:
                        n = self.MAX_LEN

                    i = 0
                    while i < n:
                        returnedData.append(self.read(self.FIFODataReg))
                        i = i + 1;
            else:
                status = self.MI_ERR
        return (status, returnedData, backLen)

    def MFRC522_Request(self, reqMode):
        status = None
        backBits = None
        TagType = []

        self.write(self.BitFramingReg, 0x07)

        TagType.append(reqMode);
        (status, returnedData, backBits) = self.MFRC522_ToCard(self.PCD_Transceive, TagType)

        if ((status != self.MI_OK) | (backBits != 0x10)):
            status = self.MI_ERR
        return (status, backBits)

    def MFRC522_Anticoll(self):
        returnedData = []
        serNumCheck = 0

        serNum = []

        self.write(self.BitFramingReg, 0x00)

        serNum.append(self.PICC_ANTICOLL)
        serNum.append(0x20)

        (status, returnedData, backBits) = self.MFRC522_ToCard(self.PCD_Transceive, serNum)

        if (status == self.MI_OK):
            i = 0
            if len(returnedData) == 5:
                while i < 4:
                    serNumCheck = serNumCheck ^ returnedData[i]
                    i = i + 1
                if serNumCheck != returnedData[i]:
                    status = self.MI_ERR
            else:
                status = self.MI_ERR

        return (status, returnedData)

    def CalulateCRC(self, pIndata):
        self.ClearBitMask(self.DivIrqReg, 0x04)
        self.SetBitMask(self.FIFOLevelReg, 0x80);
        for a in pIndata:
            self.write(self.FIFODataReg, a)
        self.write(self.CommandReg, self.PCD_CALCCRC)
        for i in range(0xFF):
            n = self.read(self.DivIrqReg)
            if (n & 0x04):
                break
        pOutData = []
        pOutData.append(self.read(self.CRCResultRegL))
        pOutData.append(self.read(self.CRCResultRegH))
        return pOutData

    def MFRC522_SelectTag(self, serNum):
        returnedData = []
        buf = []
        buf.append(self.PICC_SElECTTAG)
        buf.append(0x70)
        i = 0
        while i < 5:
            buf.append(serNum[i])
            i = i + 1
        pOut = self.CalulateCRC(buf)
        buf.append(pOut[0])
        buf.append(pOut[1])
        (status, returnedData, backLen) = self.MFRC522_ToCard(self.PCD_Transceive, buf)

        if (status == self.MI_OK) and (backLen == 0x18):
            return returnedData[0]
        else:
            return 0

    def MFRC522_Auth(self, authMode, BlockAddr, Sectorkey, serNum):
        buff = []
        # First byte should be the authMode (A or B)
        buff.append(authMode)
        # Second byte is the trailerBlock (usually 7)
        buff.append(BlockAddr)
        # Now we need to append the authKey which usually is 6 bytes of 0xFF
        i = 0
        while (i < len(Sectorkey)):
            buff.append(Sectorkey[i])
            i = i + 1
        i = 0

        # Next we append the first 4 bytes of the UID
        while (i < 4):
            buff.append(serNum[i])
            i = i + 1

        # Now we start the authentication itself
        (status, returnedData, backLen) = self.MFRC522_ToCard(self.PCD_MFAuthent, buff)

        # Check if an error occurred
        if not (status == self.MI_OK):
            print("AUTH ERROR!!")
        if not (self.read(self.Status2Reg) & 0x08) != 0:
            print("AUTH ERROR(status2reg & 0x08) != 0")

        # Return the status
        return status

    def MFRC522_StopCrypto1(self):
        self.ClearBitMask(self.Status2Reg, 0x08)
        self.SetBitMask(self.CommandReg, 0x10)

    def MFRC522_Read(self, blockAddr):
        recvData = []
        recvData.append(self.PICC_READ)
        recvData.append(blockAddr)
        pOut = self.CalulateCRC(recvData)
        recvData.append(pOut[0])
        recvData.append(pOut[1])
        (status, returnedData, backLen) = self.MFRC522_ToCard(self.PCD_Transceive, recvData)
        if not (status == self.MI_OK):
            print("Error while reading!")
        i = 0
        return returnedData

    def MFRC522_Write(self, blockAddr, writeData):
        buff = []
        buff.append(self.PICC_WRITE)
        buff.append(blockAddr)
        crc = self.CalulateCRC(buff)
        buff.append(crc[0])
        buff.append(crc[1])
        (status, returnedData, backLen) = self.MFRC522_ToCard(self.PCD_Transceive, buff)
        if not (status == self.MI_OK) or not (backLen == 4) or not ((returnedData[0] & 0x0F) == 0x0A):
            status = self.MI_ERR

        print(str(backLen) + " returnedData &0x0F == 0x0A " + str(returnedData[0] & 0x0F))
        if status == self.MI_OK:
            i = 0
            buf = []
            while i < 16:
                buf.append(writeData[i])
                i = i + 1
            crc = self.CalulateCRC(buf)
            buf.append(crc[0])
            buf.append(crc[1])
            (status, returnedData, backLen) = self.MFRC522_ToCard(self.PCD_Transceive, buf)
            if not (status == self.MI_OK) or not (backLen == 4) or not ((returnedData[0] & 0x0F) == 0x0A):
                print("Error while writing")
            if status == self.MI_OK:
                print("Data written")

    def MFRC522_DumpClassic1K(self, key, uid):
        i = 0
        while i < 64:
            status = self.MFRC522_Auth(self.PICC_AUTHENT1A, i, key, uid)
            # Check if authenticated
            if status == self.MI_OK:
                self.MFRC522_Read(i)
            else:
                print("Authentication error")
            i = i + 1


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    A = MF522(I, 'CS1')
    ret = A.getStatus()
    print(ret, hex(ret), bin(ret))
    A.getVersion()
    import time

    while 1:
        (status, TagType) = A.MFRC522_Request(A.PICC_CMD_REQA)
        if status == A.MI_OK:
            print("Card detected")
            (status, uid) = A.MFRC522_Anticoll()
            if status == A.MI_OK:
                print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                A.MFRC522_SelectTag(uid)
                status = A.MFRC522_Auth(A.PICC_AUTHENT1A, 8, key, uid)
                if status == A.MI_OK:
                    print(A.MFRC522_Read(8))
                    '''
                    # Variable for the data to write
                    data = []
                    # Fill the data with 0xFF
                    for x in range(0,16):
                        data.append(0xFF)
                    print ("Sector 8 looked like this:")
                    # Read block 8
                    A.MFRC522_Read(8)
                    print ("\n")
                    print ("Sector 8 will now be filled with 0xFF:")
                    # Write the data
                    A.MFRC522_Write(8, data)
                    print ("\n")
                    print ("It now looks like this:")
                    # Check to see if it was written
                    A.MFRC522_Read(8)
                    print ("\n")
                    '''
                    A.MFRC522_StopCrypto1()
                else:
                    print("Authentication error")
        else:
            print('not detected')

# A.reset()
