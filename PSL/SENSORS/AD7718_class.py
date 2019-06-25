from __future__ import print_function

import time

import numpy as np

'''
The running directory must have caldata.py containing dictionary called 'calibs' in it.
The entries of the dictionary will be of the form
calibs={
'AIN6AINCOM':[6.993123e-07,-1.563294e-06,9.994211e-01,-4.596018e-03], 
...
}

'''


def _bv(x):
    return 1 << x


class AD7718:
    VREF = 3.3

    STATUS = 0
    MODE = 1
    ADCCON = 2
    FILTER = 3
    ADCDATA = 4
    ADCOFFSET = 5
    ADCGAIN = 6
    IOCON = 7
    TEST1 = 12
    TEST2 = 13
    ID = 15
    # bit definitions
    MODE_PD = 0
    MODE_IDLE = 1
    MODE_SINGLE = 2
    MODE_CONT = 3
    MODE_INT_ZEROCAL = 4
    MODE_INT_FULLCAL = 5
    MODE_SYST_ZEROCAL = 6
    MODE_SYST_FULLCAL = 7

    MODE_OSCPD = _bv(3)
    MODE_CHCON = _bv(4)
    MODE_REFSEL = _bv(5)
    MODE_NEGBUF = _bv(6)
    MODE_NOCHOP = _bv(7)

    CON_AIN1AINCOM = 0 << 4
    CON_AIN2AINCOM = 1 << 4
    CON_AIN3AINCOM = 2 << 4
    CON_AIN4AINCOM = 3 << 4
    CON_AIN5AINCOM = 4 << 4
    CON_AIN6AINCOM = 5 << 4
    CON_AIN7AINCOM = 6 << 4
    CON_AIN8AINCOM = 7 << 4
    CON_AIN1AIN2 = 8 << 4
    CON_AIN3AIN4 = 9 << 4
    CON_AIN5AIN6 = 10 << 4
    CON_AIN7AIN8 = 11 << 4
    CON_AIN2AIN2 = 12 << 4
    CON_AINCOMAINCOM = 13 << 4
    CON_REFINREFIN = 14 << 4
    CON_OPEN = 15 << 4
    CON_UNIPOLAR = _bv(3)

    CON_RANGE0 = 0  # +-20mV
    CON_RANGE1 = 1  # +-40mV
    CON_RANGE2 = 2  # +-80mV
    CON_RANGE3 = 3  # +-160mV
    CON_RANGE4 = 4  # +-320mV
    CON_RANGE5 = 5  # +-640mV
    CON_RANGE6 = 6  # +-1280mV
    CON_RANGE7 = 7  # +-2560mV
    gain = 1
    CHAN_NAMES = ['AIN1AINCOM', 'AIN2AINCOM', 'AIN3AINCOM', 'AIN4AINCOM', 'AIN5AINCOM',
                  'AIN6AINCOM', 'AIN7AINCOM', 'AIN8AINCOM']

    def __init__(self, I, calibs):
        self.cs = 'CS1'
        self.I = I
        self.calibs = calibs
        self.I.SPI.set_parameters(2, 1, 0, 1)
        self.writeRegister(self.FILTER, 20)
        self.writeRegister(self.MODE, self.MODE_SINGLE | self.MODE_CHCON | self.MODE_REFSEL)
        self.caldata = {}
        for a in calibs.keys():
            self.caldata[a] = np.poly1d(calibs[a])
        print('Loaded calibration', self.caldata)

    def start(self):
        self.I.SPI.start(self.cs)

    def stop(self):
        self.I.SPI.stop(self.cs)

    def send8(self, val):
        return self.I.SPI.send8(val)

    def send16(self, val):
        return self.I.SPI.send16(val)

    def write(self, regname, value):
        pass

    def readRegister(self, regname):
        self.start()
        val = self.send16(0x4000 | (regname << 8))
        self.stop()
        # print (regname,val)
        val &= 0x00FF
        return val

    def readData(self):
        self.start()
        val = self.send16(0x4000 | (self.ADCDATA << 8))
        val &= 0xFF
        val <<= 16
        val |= self.send16(0x0000)
        self.stop()
        return val

    def writeRegister(self, regname, value):
        self.start()
        val = self.send16(0x0000 | (regname << 8) | value)
        self.stop()
        return val

    def internalCalibration(self, chan=1):
        self.start()
        val = self.send16(0x0000 | (self.ADCCON << 8) | (chan << 4) | 7)  # range=7

        start_time = time.time()
        caldone = False
        val = self.send16(0x0000 | (self.MODE << 8) | 4)
        while caldone != 1:
            time.sleep(0.5)
            caldone = self.send16(0x4000 | (self.MODE << 8)) & 7
            print('waiting for zero scale calibration... %.2f S, %d' % (time.time() - start_time, caldone))

        print('\n')
        caldone = False
        val = self.send16(0x0000 | (self.MODE << 8) | 5)
        while caldone != 1:
            time.sleep(0.5)
            caldone = self.send16(0x4000 | (self.MODE << 8)) & 7
            print('waiting for full scale calibration... %.2f S %d' % (time.time() - start_time, caldone))

        print('\n')

        self.stop()

    def readCalibration(self):
        self.start()
        off = self.send16(0x4000 | (self.ADCOFFSET << 8))
        off &= 0xFF
        off <<= 16
        off |= self.send16(0x0000)

        gn = self.send16(0x4000 | (self.ADCGAIN << 8))
        gn &= 0xFF
        gn <<= 16
        gn |= self.send16(0x0000)
        self.stop()
        return off, gn

    def configADC(self, adccon):
        self.writeRegister(self.ADCCON, adccon)  # unipolar channels , range
        self.gain = 2 ** (7 - adccon & 3)

    def printstat(self):
        stat = self.readRegister(self.STATUS)
        P = ['PLL LOCKED', 'RES', 'RES', 'ADC ERROR', 'RES', 'CAL DONE', 'RES', 'READY']
        N = ['PLL ERROR', 'RES', 'RES', 'ADC OKAY', 'RES', 'CAL LOW', 'RES', 'NOT READY']
        s = ''
        for a in range(8):
            if stat & (1 << a):
                s += '\t' + P[a]
            else:
                s += '\t' + N[a]
        print(stat, s)

    def convert_unipolar(self, x):
        return (1.024 * self.VREF * x) / (self.gain * 2 ** 24)

    def convert_bipolar(self, x):
        return ((x / 2 ** 24) - 1) * (1.024 * self.VREF) / (self.gain)

    def __startRead__(self, chan):
        if chan not in self.CHAN_NAMES:
            print('invalid channel name. try AIN1AINCOM')
            return False
        chanid = self.CHAN_NAMES.index(chan)
        self.configADC(self.CON_RANGE7 | self.CON_UNIPOLAR | (chanid << 4))
        self.writeRegister(self.MODE, self.MODE_SINGLE | self.MODE_CHCON | self.MODE_REFSEL)
        return True

    def __fetchData__(self, chan):
        while True:
            stat = self.readRegister(self.STATUS)
            if stat & 0x80:
                data = float(self.readData())
                data = self.convert_unipolar(data)
                if int(chan[3]) > 4: data = (data - 3.3 / 2) * 4
                return self.caldata[chan](data)
            else:
                time.sleep(0.1)
                print('increase delay')
        return False

    def readVoltage(self, chan):
        if not self.__startRead__(chan):
            return False
        time.sleep(0.15)
        return self.__fetchData__(chan)

    def __fetchRawData__(self, chan):
        while True:
            stat = self.readRegister(self.STATUS)
            if stat & 0x80:
                data = float(self.readData())
                return self.convert_unipolar(data)
            else:
                time.sleep(0.01)
                print('increase delay')
        return False

    def readRawVoltage(self, chan):
        if not self.__startRead__(chan):
            return False
        time.sleep(0.15)
        return self.__fetchRawData__(chan)


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    calibs = {
        'AIN6AINCOM': [6.993123e-07, -1.563294e-06, 9.994211e-01, -4.596018e-03],
        'AIN7AINCOM': [3.911521e-07, -1.706405e-06, 1.002294e+00, -1.286302e-02],
        'AIN3AINCOM': [-3.455831e-06, 2.861689e-05, 1.000195e+00, 3.802349e-04],
        'AIN1AINCOM': [8.220199e-05, -4.587100e-04, 1.001015e+00, -1.684517e-04],
        'AIN5AINCOM': [-1.250787e-07, -9.203838e-07, 1.000299e+00, -1.262684e-03],
        'AIN2AINCOM': [5.459186e-06, -1.749624e-05, 1.000268e+00, 1.907896e-04],
        'AIN9AINCOM': [7.652808e+00, 1.479229e+00, 2.832601e-01, 4.495232e-02],
        'AIN8AINCOM': [8.290843e-07, -7.129532e-07, 9.993159e-01, 3.307947e-03],
        'AIN4AINCOM': [4.135213e-06, -1.973478e-05, 1.000277e+00, 2.115374e-04], }
    A = AD7718(I, calibs)
    for a in range(10):
        print(A.readRawVoltage('AIN1AINCOM'))
        time.sleep(0.3)
