# -*- coding: utf-8; mode: python; indent-tabs-mode: t; tab-width:4 -*-
from Kalman import KalmanFilter


def connect(route, **args):
    return MPU925x(route, **args)


class MPU925x():
    '''
    Mandatory members:
    GetRaw : Function called by Graphical apps. Must return values stored in a list
    NUMPLOTS : length of list returned by GetRaw. Even single datapoints need to be stored in a list before returning
    PLOTNAMES : a list of strings describing each element in the list returned by GetRaw. len(PLOTNAMES) = NUMPLOTS
    name : the name of the sensor shown to the user
    params:
        A dictionary of function calls(single arguments only) paired with list of valid argument values. (Primitive. I know.)
        These calls can be used for one time configuration settings

    '''
    INT_PIN_CFG = 0x37
    GYRO_CONFIG = 0x1B
    ACCEL_CONFIG = 0x1C
    GYRO_SCALING = [131, 65.5, 32.8, 16.4]
    ACCEL_SCALING = [16384, 8192, 4096, 2048]
    AR = 3
    GR = 3
    NUMPLOTS = 7
    PLOTNAMES = ['Ax', 'Ay', 'Az', 'Temp', 'Gx', 'Gy', 'Gz']
    ADDRESS = 0x68
    AK8963_ADDRESS = 0x0C
    AK8963_CNTL = 0x0A
    name = 'Accel/gyro'

    def __init__(self, I2C, **args):
        self.I2C = I2C
        self.ADDRESS = args.get('address', self.ADDRESS)
        self.name = 'Accel/gyro'
        self.params = {'powerUp': None, 'setGyroRange': [250, 500, 1000, 2000], 'setAccelRange': [2, 4, 8, 16],
                       'KalmanFilter': [.01, .1, 1, 10, 100, 1000, 10000, 'OFF']}
        self.setGyroRange(2000)
        self.setAccelRange(16)
        self.powerUp()
        self.K = None

    def KalmanFilter(self, opt):
        if opt == 'OFF':
            self.K = None
            return
        noise = [[]] * self.NUMPLOTS
        for a in range(500):
            vals = self.getRaw()
            for b in range(self.NUMPLOTS): noise[b].append(vals[b])

        self.K = [None] * 7
        for a in range(self.NUMPLOTS):
            sd = std(noise[a])
            self.K[a] = KalmanFilter(1. / opt, sd ** 2)

    def getVals(self, addr, numbytes):
        return self.I2C.readBulk(self.ADDRESS, addr, numbytes)

    def powerUp(self):
        self.I2C.writeBulk(self.ADDRESS, [0x6B, 0])

    def setGyroRange(self, rs):
        self.GR = self.params['setGyroRange'].index(rs)
        self.I2C.writeBulk(self.ADDRESS, [self.GYRO_CONFIG, self.GR << 3])

    def setAccelRange(self, rs):
        self.AR = self.params['setAccelRange'].index(rs)
        self.I2C.writeBulk(self.ADDRESS, [self.ACCEL_CONFIG, self.AR << 3])

    def getRaw(self):
        '''
        This method must be defined if you want GUIs to use this class to generate plots on the fly.
        It must return a set of different values read from the sensor. such as X,Y,Z acceleration.
        The length of this list must not change, and must be defined in the variable NUMPLOTS.

        GUIs will generate as many plots, and the data returned from this method will be appended appropriately
        '''
        vals = self.getVals(0x3B, 14)
        if vals:
            if len(vals) == 14:
                raw = [0] * 7
                for a in range(3): raw[a] = 1. * int16(vals[a * 2] << 8 | vals[a * 2 + 1]) / self.ACCEL_SCALING[self.AR]
                for a in range(4, 7): raw[a] = 1. * int16(vals[a * 2] << 8 | vals[a * 2 + 1]) / self.GYRO_SCALING[
                    self.GR]
                raw[3] = int16(vals[6] << 8 | vals[7]) / 340. + 36.53
                if not self.K:
                    return raw
                else:
                    for b in range(self.NUMPLOTS):
                        self.K[b].input_latest_noisy_measurement(raw[b])
                        raw[b] = self.K[b].get_latest_estimated_measurement()
                    return raw

            else:
                return False
        else:
            return False

    def getAccel(self):
        '''
        Return a list of 3 values for acceleration vector

        '''
        vals = self.getVals(0x3B, 6)
        ax = int16(vals[0] << 8 | vals[1])
        ay = int16(vals[2] << 8 | vals[3])
        az = int16(vals[4] << 8 | vals[5])
        return [ax / 65535., ay / 65535., az / 65535.]

    def getTemp(self):
        '''
        Return temperature
        '''
        vals = self.getVals(0x41, 6)
        t = int16(vals[0] << 8 | vals[1])
        return t / 65535.

    def getGyro(self):
        '''
        Return a list of 3 values for angular velocity vector

        '''
        vals = self.getVals(0x43, 6)
        ax = int16(vals[0] << 8 | vals[1])
        ay = int16(vals[2] << 8 | vals[3])
        az = int16(vals[4] << 8 | vals[5])
        return [ax / 65535., ay / 65535., az / 65535.]

    def getMag(self):
        '''
        Return a list of 3 values for magnetic field vector

        '''
        vals = self.I2C.readBulk(self.AK8963_ADDRESS, 0x03,
                                 7)  # 6+1 . 1(ST2) should not have bit 4 (0x8) true. It's ideally 16 . overflow bit
        ax = int16(vals[0] << 8 | vals[1])
        ay = int16(vals[2] << 8 | vals[3])
        az = int16(vals[4] << 8 | vals[5])
        if not vals[6] & 0x08:
            return [ax / 65535., ay / 65535., az / 65535.]
        else:
            return None

    def WhoAmI(self):
        '''
        Returns the ID.
        It is 71 for MPU9250.
        '''
        v = self.I2C.readBulk(self.ADDRESS, 0x75, 1)[0]
        if v not in [0x71, 0x73]: return 'Error %s' % hex(v)

        if v == 0x73:
            return 'MPU9255 %s' % hex(v)
        elif v == 0x71:
            return 'MPU9250 %s' % hex(v)

    def WhoAmI_AK8963(self):
        '''
        Returns the ID fo magnetometer AK8963 if found.
        It should be 0x48.
        '''
        self.initMagnetometer()
        v = self.I2C.readBulk(self.AK8963_ADDRESS, 0, 1)[0]
        if v == 0x48:
            return 'AK8963 at %s' % hex(v)
        else:
            return 'AK8963 not found. returned :%s' % hex(v)

    def initMagnetometer(self):
        '''
        For MPU925x with integrated magnetometer.
        It's called a 10 DoF sensor, but technically speaking ,
        the 3-axis Accel , 3-Axis Gyro, temperature sensor are integrated in one IC, and the 3-axis magnetometer is implemented in a
        separate IC which can be accessed via an I2C passthrough.
        Therefore , in order to detect the magnetometer via an I2C scan, the passthrough must first be enabled on IC#1 (Accel,gyro,temp)
        '''
        self.I2C.writeBulk(self.ADDRESS, [self.INT_PIN_CFG, 0x22])  # I2C passthrough
        self.I2C.writeBulk(self.AK8963_ADDRESS, [self.AK8963_CNTL, 0])  # power down mag
        self.I2C.writeBulk(self.AK8963_ADDRESS,
                           [self.AK8963_CNTL, (1 << 4) | 6])  # mode   (0=14bits,1=16bits) <<4 | (2=8Hz , 6=100Hz)


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    A = connect(I.I2C)
    t, x, y, z = I.I2C.capture(A.ADDRESS, 0x43, 6, 5000, 1000, 'int')
    # print (t,x,y,z)
    from pylab import *

    plot(t, x)
    plot(t, y)
    plot(t, z)
    show()
