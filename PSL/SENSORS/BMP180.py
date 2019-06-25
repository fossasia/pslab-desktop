from __future__ import print_function

import time

from numpy import int16


def connect(route, **args):
    return BMP180(route, **args)


class BMP180:
    ADDRESS = 0x77
    REG_CONTROL = 0xF4
    REG_RESULT = 0xF6
    CMD_TEMP = 0x2E
    CMD_P0 = 0x34
    CMD_P1 = 0x74
    CMD_P2 = 0xB4
    CMD_P3 = 0xF4
    oversampling = 0
    NUMPLOTS = 3
    PLOTNAMES = ['Temperature', 'Pressure', 'Altitude']
    name = 'Altimeter BMP180'

    def __init__(self, I2C, **args):
        self.ADDRESS = args.get('address', self.ADDRESS)

        self.I2C = I2C

        self.MB = self.__readInt__(0xBA)

        self.c3 = 160.0 * pow(2, -15) * self.__readInt__(0xAE)
        self.c4 = pow(10, -3) * pow(2, -15) * self.__readUInt__(0xB0)
        self.b1 = pow(160, 2) * pow(2, -30) * self.__readInt__(0xB6)
        self.c5 = (pow(2, -15) / 160) * self.__readUInt__(0xB2)
        self.c6 = self.__readUInt__(0xB4)
        self.mc = (pow(2, 11) / pow(160, 2)) * self.__readInt__(0xBC)
        self.md = self.__readInt__(0xBE) / 160.0
        self.x0 = self.__readInt__(0xAA)
        self.x1 = 160.0 * pow(2, -13) * self.__readInt__(0xAC)
        self.x2 = pow(160, 2) * pow(2, -25) * self.__readInt__(0xB8)
        self.y0 = self.c4 * pow(2, 15)
        self.y1 = self.c4 * self.c3
        self.y2 = self.c4 * self.b1
        self.p0 = (3791.0 - 8.0) / 1600.0
        self.p1 = 1.0 - 7357.0 * pow(2, -20)
        self.p2 = 3038.0 * 100.0 * pow(2, -36)
        self.T = 25
        print('calib:', self.c3, self.c4, self.b1, self.c5, self.c6, self.mc, self.md, self.x0, self.x1, self.x2,
              self.y0, self.y1, self.p0, self.p1, self.p2)
        self.params = {'setOversampling': [0, 1, 2, 3]}
        self.name = 'BMP180 Altimeter'
        self.initTemperature()
        self.readTemperature()
        self.initPressure()
        self.baseline = self.readPressure()

    def __readInt__(self, addr):
        return int16(self.__readUInt__(addr))

    def __readUInt__(self, addr):
        vals = self.I2C.readBulk(self.ADDRESS, addr, 2)
        v = 1. * ((vals[0] << 8) | vals[1])
        return v

    def initTemperature(self):
        self.I2C.writeBulk(self.ADDRESS, [self.REG_CONTROL, self.CMD_TEMP])
        time.sleep(0.005)

    def readTemperature(self):
        vals = self.I2C.readBulk(self.ADDRESS, self.REG_RESULT, 2)
        if len(vals) == 2:
            T = (vals[0] << 8) + vals[1]
            a = self.c5 * (T - self.c6)
            self.T = a + (self.mc / (a + self.md))
            return self.T
        else:
            return False

    def setOversampling(self, num):
        self.oversampling = num

    def initPressure(self):
        os = [0x34, 0x74, 0xb4, 0xf4]
        delays = [0.005, 0.008, 0.014, 0.026]
        self.I2C.writeBulk(self.ADDRESS, [self.REG_CONTROL, os[self.oversampling]])
        time.sleep(delays[self.oversampling])

    def readPressure(self):
        vals = self.I2C.readBulk(self.ADDRESS, self.REG_RESULT, 3)
        if len(vals) == 3:
            P = 1. * (vals[0] << 8) + vals[1] + (vals[2] / 256.0)
            s = self.T - 25.0
            x = (self.x2 * pow(s, 2)) + (self.x1 * s) + self.x0
            y = (self.y2 * pow(s, 2)) + (self.y1 * s) + self.y0
            z = (P - x) / y
            self.P = (self.p2 * pow(z, 2)) + (self.p1 * z) + self.p0
            return self.P
        else:
            return False

    def altitude(self):
        # baseline pressure needs to be provided
        return (44330.0 * (1 - pow(self.P / self.baseline, 1 / 5.255)))

    def sealevel(self, P, A):
        '''
        given a calculated pressure and altitude, return the sealevel
        '''
        return (P / pow(1 - (A / 44330.0), 5.255))

    def getRaw(self):
        self.initTemperature()
        self.readTemperature()
        self.initPressure()
        self.readPressure()
        return [self.T, self.P, self.altitude()]
