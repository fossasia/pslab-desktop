def connect(route, **args):
    return HMC5883L(route, **args)


class HMC5883L():
    CONFA = 0x00
    CONFB = 0x01
    MODE = 0x02
    STATUS = 0x09

    # --------CONFA register bits. 0x00-----------
    samplesToAverage = 0
    samplesToAverage_choices = [1, 2, 4, 8]

    dataOutputRate = 6
    dataOutputRate_choices = [0.75, 1.5, 3, 7.5, 15, 30, 75]

    measurementConf = 0

    # --------CONFB register bits. 0x01-----------
    gainValue = 7  # least sensitive
    gain_choices = [8, 7, 6, 5, 4, 3, 2, 1]
    scaling = [1370., 1090., 820., 660., 440., 390., 330., 230.]

    # --------------Parameters--------------------
    # This must be defined in order to let GUIs automatically create menus
    # for changing various options of this sensor
    # It's a dictionary of the string representations of functions matched with an array
    # of options that each one can accept
    params = {'init': None,
              'setSamplesToAverage': samplesToAverage_choices,
              'setDataOutputRate': dataOutputRate_choices,
              'setGain': gain_choices,
              }
    ADDRESS = 0x1E
    name = 'Magnetometer'
    NUMPLOTS = 3
    PLOTNAMES = ['Bx', 'By', 'Bz']

    def __init__(self, I2C, **args):
        self.I2C = I2C
        self.ADDRESS = args.get('address', self.ADDRESS)
        self.name = 'Magnetometer'
        '''
        try:
            print 'switching baud to 400k'
            self.I2C.configI2C(400e3)
        except:
            print 'FAILED TO CHANGE BAUD RATE'
        '''
        self.init()

    def init(self):
        self.__writeCONFA__()
        self.__writeCONFB__()
        self.I2C.writeBulk(self.ADDRESS, [self.MODE, 0])  # enable continuous measurement mode

    def __writeCONFB__(self):
        self.I2C.writeBulk(self.ADDRESS, [self.CONFB, self.gainValue << 5])  # set gain

    def __writeCONFA__(self):
        self.I2C.writeBulk(self.ADDRESS, [self.CONFA, (self.dataOutputRate << 2) | (self.samplesToAverage << 5) | (
            self.measurementConf)])

    def setSamplesToAverage(self, num):
        self.samplesToAverage = self.samplesToAverage_choices.index(num)
        self.__writeCONFA__()

    def setDataOutputRate(self, rate):
        self.dataOutputRate = self.dataOutputRate_choices.index(rate)
        self.__writeCONFA__()

    def setGain(self, gain):
        self.gainValue = self.gain_choices.index(gain)
        self.__writeCONFB__()

    def getVals(self, addr, numbytes):
        vals = self.I2C.readBulk(self.ADDRESS, addr, numbytes)
        return vals

    def getRaw(self):
        vals = self.getVals(0x03, 6)
        if vals:
            if len(vals) == 6:
                return [int16(vals[a * 2] << 8 | vals[a * 2 + 1]) / self.scaling[self.gainValue] for a in range(3)]
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    I.set_sine1(.5)
    A = connect(I.I2C)
    A.setGain(2)
    t, x, y, z = I.I2C.capture(A.ADDRESS, 0x03, 6, 400, 10000, 'int')
    # print (t,x,y,z)
    from pylab import *

    plot(t, x)
    plot(t, y)
    plot(t, z)
    show()
