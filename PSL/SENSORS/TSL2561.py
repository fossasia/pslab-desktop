'''
Adapted from https://github.com/janheise/TSL2561
'''

from __future__ import print_function
import time


def connect(route, **args):
    return TSL2561(route, **args)


class TSL2561:
    VISIBLE = 2  # channel 0 - channel 1
    INFRARED = 1  # channel 1
    FULLSPECTRUM = 0  # channel 0

    READBIT = 0x01
    COMMAND_BIT = 0x80  # Must be 1

    CONTROL_POWERON = 0x03
    CONTROL_POWEROFF = 0x00

    REGISTER_CONTROL = 0x00
    REGISTER_TIMING = 0x01
    REGISTER_ID = 0x0A

    INTEGRATIONTIME_13MS = 0x00  # 13.7ms
    INTEGRATIONTIME_101MS = 0x01  # 101ms
    INTEGRATIONTIME_402MS = 0x02  # 402ms

    GAIN_1X = 0x00  # No gain
    GAIN_16X = 0x10  # 16x gain

    ADDRESS = 0x39  # addr normal
    timing = INTEGRATIONTIME_13MS
    gain = GAIN_16X
    name = 'TSL2561 Luminosity'
    ADDRESS = 0x39
    NUMPLOTS = 3
    PLOTNAMES = ['Full', 'IR', 'Visible']

    def __init__(self, I2C, **args):
        self.ADDRESS = args.get('address', 0x39)
        self.I2C = I2C
        # set timing 101ms & 16x gain
        self.enable()
        self.wait()
        self.I2C.writeBulk(self.ADDRESS, [0x80 | 0x01, 0x01 | 0x10])
        # full scale luminosity
        infra = self.I2C.readBulk(self.ADDRESS, 0x80 | 0x20 | 0x0E, 2)
        full = self.I2C.readBulk(self.ADDRESS, 0x80 | 0x20 | 0x0C, 2)
        full = (full[1] << 8) | full[0]
        infra = (infra[1] << 8) | infra[0]

        print("Full:     %04x" % full)
        print("Infrared: %04x" % infra)
        print("Visible:  %04x" % (full - infra))

        # self.I2C.writeBulk(self.ADDRESS,[0x80,0x00])

        self.params = {'setGain': ['1x', '16x'], 'setTiming': [0, 1, 2]}

    def getID(self):
        ID = self.I2C.readBulk(self.ADDRESS, self.REGISTER_ID, 1)
        print(hex(ID))
        return ID

    def getRaw(self):
        infra = self.I2C.readBulk(self.ADDRESS, 0x80 | 0x20 | 0x0E, 2)
        full = self.I2C.readBulk(self.ADDRESS, 0x80 | 0x20 | 0x0C, 2)
        if infra and full:
            full = (full[1] << 8) | full[0]
            infra = (infra[1] << 8) | infra[0]
            return [full, infra, full - infra]
        else:
            return False

    def setGain(self, gain):
        if (gain == '1x'):
            self.gain = self.GAIN_1X
        elif (gain == '16x'):
            self.gain = self.GAIN_16X
        else:
            self.gain = self.GAIN_0X

        self.I2C.writeBulk(self.ADDRESS, [self.COMMAND_BIT | self.REGISTER_TIMING, self.gain | self.timing])

    def setTiming(self, timing):
        print([13, 101, 402][timing], 'mS')
        self.timing = timing
        self.I2C.writeBulk(self.ADDRESS, [self.COMMAND_BIT | self.REGISTER_TIMING, self.gain | self.timing])

    def enable(self):
        self.I2C.writeBulk(self.ADDRESS, [self.COMMAND_BIT | self.REGISTER_CONTROL, self.CONTROL_POWERON])

    def disable(self):
        self.I2C.writeBulk(self.ADDRESS, [self.COMMAND_BIT | self.REGISTER_CONTROL, self.CONTROL_POWEROFF])

    def wait(self):
        if self.timing == self.INTEGRATIONTIME_13MS:
            time.sleep(0.014)
        if self.timing == self.INTEGRATIONTIME_101MS:
            time.sleep(0.102)
        if self.timing == self.INTEGRATIONTIME_402MS:
            time.sleep(0.403)
