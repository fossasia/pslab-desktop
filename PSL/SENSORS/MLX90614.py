from __future__ import print_function


def connect(route, **args):
    return MLX90614(route, **args)


class MLX90614():
    NUMPLOTS = 1
    PLOTNAMES = ['Temp']
    ADDRESS = 0x5A
    name = 'PIR temperature'

    def __init__(self, I2C, **args):
        self.I2C = I2C
        self.ADDRESS = args.get('address', self.ADDRESS)
        self.OBJADDR = 0x07
        self.AMBADDR = 0x06

        self.source = self.OBJADDR

        self.name = 'Passive IR temperature sensor'
        self.params = {'readReg': {'dataType': 'integer', 'min': 0, 'max': 0x20, 'prefix': 'Addr: '},
                       'select_source': ['object temperature', 'ambient temperature']}

        try:
            print('switching baud to 100k')
            self.I2C.configI2C(100e3)
        except Exception as e:
            print('FAILED TO CHANGE BAUD RATE', e.message)

    def select_source(self, source):
        if source == 'object temperature':
            self.source = self.OBJADDR
        elif source == 'ambient temperature':
            self.source = self.AMBADDR

    def readReg(self, addr):
        x = self.getVals(addr, 2)
        print(hex(addr), hex(x[0] | (x[1] << 8)))

    def getVals(self, addr, numbytes):
        vals = self.I2C.readBulk(self.ADDRESS, addr, numbytes)
        return vals

    def getRaw(self):
        vals = self.getVals(self.source, 3)
        if vals:
            if len(vals) == 3:
                return [((((vals[1] & 0x007f) << 8) + vals[0]) * 0.02) - 0.01 - 273.15]
            else:
                return False
        else:
            return False

    def getObjectTemperature(self):
        self.source = self.OBJADDR
        val = self.getRaw()
        if val:
            return val[0]
        else:
            return False

    def getAmbientTemperature(self):
        self.source = self.AMBADDR
        val = self.getRaw()
        if val:
            return val[0]
        else:
            return False
