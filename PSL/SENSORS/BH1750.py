from __future__ import print_function


def connect(route, **args):
    return BRIDGE(route, **args)


class BRIDGE():
    POWER_ON = 0x01
    RESET = 0x07
    RES_1000mLx = 0x10
    RES_500mLx = 0x11
    RES_4000mLx = 0x13

    gain_choices = [RES_500mLx, RES_1000mLx, RES_4000mLx]
    gain_literal_choices = ['500mLx', '1000mLx', '4000mLx']
    gain = 0
    scaling = [2, 1, .25]

    # --------------Parameters--------------------
    # This must be defined in order to let GUIs automatically create menus
    # for changing various options of this sensor
    # It's a dictionary of the string representations of functions matched with an array
    # of options that each one can accept
    params = {'init': None,
              'setRange': gain_literal_choices,
              }

    NUMPLOTS = 1
    PLOTNAMES = ['Lux']
    ADDRESS = 0x23
    name = 'Luminosity'

    def __init__(self, I2C, **args):
        self.I2C = I2C
        self.ADDRESS = args.get('address', 0x23)
        self.init()

    def init(self):
        self.I2C.writeBulk(self.ADDRESS, [self.RES_500mLx])

    def setRange(self, g):
        self.gain = self.gain_literal_choices.index(g)
        self.I2C.writeBulk(self.ADDRESS, [self.gain_choices[self.gain]])

    def getVals(self, numbytes):
        vals = self.I2C.simpleRead(self.ADDRESS, numbytes)
        return vals

    def getRaw(self):
        vals = self.getVals(2)
        if vals:
            if len(vals) == 2:
                return [(vals[0] << 8 | vals[1]) / 1.2]  # /self.scaling[self.gain]
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    A = connect(I.I2C)
    print(A.getRaw())
