from __future__ import print_function
import numpy as np

gains = [1, 2, 4, 5, 8, 10, 16, 32, 1 / 11.]

# -----------------------Classes for input sources----------------------
allAnalogChannels = ['CH1', 'CH2', 'CH3', 'MIC', 'CAP', 'SEN', 'AN8']

bipolars = ['CH1', 'CH2', 'CH3', 'MIC']

inputRanges = {'CH1': [16.5, -16.5],  # Specify inverted channels explicitly by reversing range!!!!!!!!!
               'CH2': [16.5, -16.5],
               'CH3': [-3.3, 3.3],  # external gain control analog input
               'MIC': [-3.3, 3.3],  # connected to MIC amplifier
               'CAP': [0, 3.3],
               'SEN': [0, 3.3],
               'AN8': [0, 3.3]
               }

picADCMultiplex = {'CH1': 3, 'CH2': 0, 'CH3': 1, 'MIC': 2, 'AN4': 4, 'SEN': 7, 'CAP': 5, 'AN8': 8, }


class analogInputSource:
    gain_values = gains
    gainEnabled = False
    gain = None
    gainPGA = None
    inverted = False
    inversion = 1.
    calPoly10 = np.poly1d([0, 3.3 / 1023, 0.])
    calPoly12 = np.poly1d([0, 3.3 / 4095, 0.])
    calibrationReady = False
    defaultOffsetCode = 0

    def __init__(self, name, **args):
        self.name = name  # The generic name of the input. like 'CH1', 'IN1' etc
        self.CHOSA = picADCMultiplex[self.name]
        self.adc_shifts = []
        self.polynomials = {}

        self.R = inputRanges[name]

        if self.R[1] - self.R[0] < 0:
            self.inverted = True
            self.inversion = -1

        self.scaling = 1.
        if name == 'CH1':
            self.gainEnabled = True
            self.gainPGA = 1
            self.gain = 0  # This is not the gain factor. use self.gain_values[self.gain] to find that.
        elif name == 'CH2':
            self.gainEnabled = True
            self.gainPGA = 2
            self.gain = 0
        else:
            pass

        self.gain = 0
        self.regenerateCalibration()

    def setGain(self, g):
        if not self.gainEnabled:
            print('Analog gain is not available on', self.name)
            return False
        self.gain = self.gain_values.index(g)
        self.regenerateCalibration()

    def inRange(self, val):
        v = self.voltToCode12(val)
        return 0 <= v <= 4095

    def __conservativeInRange__(self, val):
        v = self.voltToCode12(val)
        return 50 <= v <= 4000

    def loadCalibrationTable(self, table, slope, intercept):
        self.adc_shifts = np.array(table) * slope - intercept

    def __ignoreCalibration__(self):
        self.calibrationReady = False

    def loadPolynomials(self, polys):
        for a in range(len(polys)):
            epoly = [float(b) for b in polys[a]]
            self.polynomials[a] = np.poly1d(epoly)

    def regenerateCalibration(self):
        B = self.R[1]
        A = self.R[0]
        intercept = self.R[0]

        if self.gain is not None:
            gain = self.gain_values[self.gain]
            B /= gain
            A /= gain

        slope = B - A
        intercept = A
        if self.calibrationReady and self.gain != 8:  # special case for 1/11. gain
            self.calPoly10 = self.__cal10__
            self.calPoly12 = self.__cal12__

        else:
            self.calPoly10 = np.poly1d([0, slope / 1023., intercept])
            self.calPoly12 = np.poly1d([0, slope / 4095., intercept])

        self.voltToCode10 = np.poly1d([0, 1023. / slope, -1023 * intercept / slope])
        self.voltToCode12 = np.poly1d([0, 4095. / slope, -4095 * intercept / slope])

    def __cal12__(self, RAW):
        avg_shifts = (self.adc_shifts[np.int16(np.floor(RAW))] + self.adc_shifts[np.int16(np.ceil(RAW))]) / 2.
        RAW -= 4095 * avg_shifts / 3.3
        return self.polynomials[self.gain](RAW)

    def __cal10__(self, RAW):
        RAW *= 4095 / 1023.
        avg_shifts = (self.adc_shifts[np.int16(np.floor(RAW))] + self.adc_shifts[np.int16(np.ceil(RAW))]) / 2.
        RAW -= 4095 * avg_shifts / 3.3
        return self.polynomials[self.gain](RAW)


'''
for a in ['CH1']:
	x=analogInputSource(a)
	print (x.name,x.calPoly10#,calfacs[x.name][0])
	print ('CAL:',x.calPoly10(0),x.calPoly10(1023))
	x.setOffset(1.65)
	x.setGain(32)
	print (x.name,x.calPoly10#,calfacs[x.name][0])
	print ('CAL:',x.calPoly10(0),x.calPoly10(1023))
'''


# ---------------------------------------------------------------------


class analogAcquisitionChannel:
    """
    This class takes care of oscilloscope data fetched from the device.
    Each instance may be linked to a particular input.
    Since only up to two channels may be captured at a time with the PSLab, only two instances will be required

    Each instance will be linked to a particular inputSource instance by the capture routines.
    When data is requested , it will return after applying calibration and gain details
    stored in the selected inputSource
    """

    def __init__(self, a):
        self.name = ''
        self.gain = 0
        self.channel = a
        self.channel_names = allAnalogChannels
        # REFERENCE VOLTAGE = 3.3 V
        self.calibration_ref196 = 1.  # measured reference voltage/3.3
        self.resolution = 10
        self.xaxis = np.zeros(10000)
        self.yaxis = np.zeros(10000)
        self.length = 100
        self.timebase = 1.
        self.source = analogInputSource('CH1')  # use CH1 for initialization. It will be overwritten by set_params

    def fix_value(self, val):
        # val[val>1020]=np.NaN
        # val[val<2]=np.NaN
        if self.resolution == 12:
            return self.calibration_ref196 * self.source.calPoly12(val)
        else:
            return self.calibration_ref196 * self.source.calPoly10(val)

    def set_yval(self, pos, val):
        self.yaxis[pos] = self.fix_value(val)

    def set_xval(self, pos, val):
        self.xaxis[pos] = val

    def set_params(self, **keys):
        self.gain = keys.get('gain', self.gain)
        self.name = keys.get('channel', self.channel)
        self.source = keys.get('source', self.source)
        self.resolution = keys.get('resolution', self.resolution)
        l = keys.get('length', self.length)
        t = keys.get('timebase', self.timebase)
        if t != self.timebase or l != self.length:
            self.timebase = t
            self.length = l
            self.regenerate_xaxis()

    def regenerate_xaxis(self):
        for a in range(int(self.length)): self.xaxis[a] = self.timebase * a

    def get_xaxis(self):
        return self.xaxis[:int(self.length)]

    def get_yaxis(self):
        return self.yaxis[:int(self.length)]
