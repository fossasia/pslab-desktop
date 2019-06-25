# -*- coding: utf-8; mode: python; indent-tabs-mode: t; tab-width:4 -*-
from __future__ import print_function

import time

from numpy import int16

try:
    from collections import OrderedDict
except ImportError:
    # fallback: try to use the ordereddict backport when using python 2.6
    from ordereddict import OrderedDict


def connect(route, **args):
    return ADS1115(route, **args)


class ADS1115:
    ADDRESS = 0x48  # addr pin grounded. floating

    REG_POINTER_MASK = 0x3
    REG_POINTER_CONVERT = 0
    REG_POINTER_CONFIG = 1
    REG_POINTER_LOWTHRESH = 2
    REG_POINTER_HITHRESH = 3

    REG_CONFIG_OS_MASK = 0x8000
    REG_CONFIG_OS_SINGLE = 0x8000
    REG_CONFIG_OS_BUSY = 0x0000
    REG_CONFIG_OS_NOTBUSY = 0x8000

    REG_CONFIG_MUX_MASK = 0x7000
    REG_CONFIG_MUX_DIFF_0_1 = 0x0000  # Differential P = AIN0, N = AIN1 =default)
    REG_CONFIG_MUX_DIFF_0_3 = 0x1000  # Differential P = AIN0, N = AIN3
    REG_CONFIG_MUX_DIFF_1_3 = 0x2000  # Differential P = AIN1, N = AIN3
    REG_CONFIG_MUX_DIFF_2_3 = 0x3000  # Differential P = AIN2, N = AIN3
    REG_CONFIG_MUX_SINGLE_0 = 0x4000  # Single-ended AIN0
    REG_CONFIG_MUX_SINGLE_1 = 0x5000  # Single-ended AIN1
    REG_CONFIG_MUX_SINGLE_2 = 0x6000  # Single-ended AIN2
    REG_CONFIG_MUX_SINGLE_3 = 0x7000  # Single-ended AIN3

    REG_CONFIG_PGA_MASK = 0x0E00  # bits 11:9
    REG_CONFIG_PGA_6_144V = (0 << 9)  # +/-6.144V range = Gain 2/3
    REG_CONFIG_PGA_4_096V = (1 << 9)  # +/-4.096V range = Gain 1
    REG_CONFIG_PGA_2_048V = (2 << 9)  # +/-2.048V range = Gain 2 =default)
    REG_CONFIG_PGA_1_024V = (3 << 9)  # +/-1.024V range = Gain 4
    REG_CONFIG_PGA_0_512V = (4 << 9)  # +/-0.512V range = Gain 8
    REG_CONFIG_PGA_0_256V = (5 << 9)  # +/-0.256V range = Gain 16

    REG_CONFIG_MODE_MASK = 0x0100  # bit 8
    REG_CONFIG_MODE_CONTIN = (0 << 8)  # Continuous conversion mode
    REG_CONFIG_MODE_SINGLE = (1 << 8)  # Power-down single-shot mode =default)

    REG_CONFIG_DR_MASK = 0x00E0
    REG_CONFIG_DR_8SPS = (0 << 5)  # 8 SPS
    REG_CONFIG_DR_16SPS = (1 << 5)  # 16 SPS
    REG_CONFIG_DR_32SPS = (2 << 5)  # 32 SPS
    REG_CONFIG_DR_64SPS = (3 << 5)  # 64 SPS
    REG_CONFIG_DR_128SPS = (4 << 5)  # 128 SPS
    REG_CONFIG_DR_250SPS = (5 << 5)  # 260 SPS
    REG_CONFIG_DR_475SPS = (6 << 5)  # 475 SPS
    REG_CONFIG_DR_860SPS = (7 << 5)  # 860 SPS

    REG_CONFIG_CMODE_MASK = 0x0010
    REG_CONFIG_CMODE_TRAD = 0x0000
    REG_CONFIG_CMODE_WINDOW = 0x0010

    REG_CONFIG_CPOL_MASK = 0x0008
    REG_CONFIG_CPOL_ACTVLOW = 0x0000
    REG_CONFIG_CPOL_ACTVHI = 0x0008

    REG_CONFIG_CLAT_MASK = 0x0004
    REG_CONFIG_CLAT_NONLAT = 0x0000
    REG_CONFIG_CLAT_LATCH = 0x0004

    REG_CONFIG_CQUE_MASK = 0x0003
    REG_CONFIG_CQUE_1CONV = 0x0000
    REG_CONFIG_CQUE_2CONV = 0x0001
    REG_CONFIG_CQUE_4CONV = 0x0002
    REG_CONFIG_CQUE_NONE = 0x0003
    gains = OrderedDict([('GAIN_TWOTHIRDS', REG_CONFIG_PGA_6_144V), ('GAIN_ONE', REG_CONFIG_PGA_4_096V),
                         ('GAIN_TWO', REG_CONFIG_PGA_2_048V), ('GAIN_FOUR', REG_CONFIG_PGA_1_024V),
                         ('GAIN_EIGHT', REG_CONFIG_PGA_0_512V), ('GAIN_SIXTEEN', REG_CONFIG_PGA_0_256V)])
    gain_scaling = OrderedDict(
        [('GAIN_TWOTHIRDS', 0.1875), ('GAIN_ONE', 0.125), ('GAIN_TWO', 0.0625), ('GAIN_FOUR', 0.03125),
         ('GAIN_EIGHT', 0.015625), ('GAIN_SIXTEEN', 0.0078125)])
    type_selection = OrderedDict(
        [('UNI_0', 0), ('UNI_1', 1), ('UNI_2', 2), ('UNI_3', 3), ('DIFF_01', '01'), ('DIFF_23', '23')])
    sdr_selection = OrderedDict(
        [(8, REG_CONFIG_DR_8SPS), (16, REG_CONFIG_DR_16SPS), (32, REG_CONFIG_DR_32SPS), (64, REG_CONFIG_DR_64SPS),
         (128, REG_CONFIG_DR_128SPS), (250, REG_CONFIG_DR_250SPS), (475, REG_CONFIG_DR_475SPS),
         (860, REG_CONFIG_DR_860SPS)])  # sampling data rate

    NUMPLOTS = 1
    PLOTNAMES = ['mV']

    def __init__(self, I2C, **args):
        self.ADDRESS = args.get('address', self.ADDRESS)
        self.I2C = I2C
        self.channel = 'UNI_0'
        self.gain = 'GAIN_ONE'
        self.rate = 128

        self.setGain('GAIN_ONE')
        self.setChannel('UNI_0')
        self.setDataRate(128)
        self.conversionDelay = 8
        self.name = 'ADS1115 16-bit ADC'
        self.params = {'setGain': self.gains.keys(), 'setChannel': self.type_selection.keys(),
                       'setDataRate': self.sdr_selection.keys()}

    def __readInt__(self, addr):
        return int16(self.__readUInt__(addr))

    def __readUInt__(self, addr):
        vals = self.I2C.readBulk(self.ADDRESS, addr, 2)
        v = 1. * ((vals[0] << 8) | vals[1])
        return v

    def initTemperature(self):
        self.I2C.writeBulk(self.ADDRESS, [self.REG_CONTROL, self.CMD_TEMP])
        time.sleep(0.005)

    def readRegister(self, register):
        vals = self.I2C.readBulk(self.ADDRESS, register, 2)
        return (vals[0] << 8) | vals[1]

    def writeRegister(self, reg, value):
        self.I2C.writeBulk(self.ADDRESS, [reg, (value >> 8) & 0xFF, value & 0xFF])

    def setGain(self, gain):
        '''
        options : 'GAIN_TWOTHIRDS','GAIN_ONE','GAIN_TWO','GAIN_FOUR','GAIN_EIGHT','GAIN_SIXTEEN'
        '''
        self.gain = gain

    def setChannel(self, channel):
        '''
        options 'UNI_0','UNI_1','UNI_2','UNI_3','DIFF_01','DIFF_23'
        '''
        self.channel = channel

    def setDataRate(self, rate):
        '''
        data rate options 8,16,32,64,128,250,475,860 SPS
        '''
        self.rate = rate

    def readADC_SingleEnded(self, chan):
        if chan > 3: return None
        # start with default values
        config = (self.REG_CONFIG_CQUE_NONE  # Disable the comparator (default val)
                  | self.REG_CONFIG_CLAT_NONLAT  # Non-latching (default val)
                  | self.REG_CONFIG_CPOL_ACTVLOW  # Alert/Rdy active low   (default val)
                  | self.REG_CONFIG_CMODE_TRAD  # Traditional comparator (default val)
                  | self.sdr_selection[self.rate]  # 1600 samples per second (default)
                  | self.REG_CONFIG_MODE_SINGLE)  # Single-shot mode (default)

        # Set PGA/voltage range
        config |= self.gains[self.gain]

        if chan == 0:
            config |= self.REG_CONFIG_MUX_SINGLE_0
        elif chan == 1:
            config |= self.REG_CONFIG_MUX_SINGLE_1
        elif chan == 2:
            config |= self.REG_CONFIG_MUX_SINGLE_2
        elif chan == 3:
            config |= self.REG_CONFIG_MUX_SINGLE_3
        # Set 'start single-conversion' bit
        config |= self.REG_CONFIG_OS_SINGLE
        self.writeRegister(self.REG_POINTER_CONFIG, config);
        time.sleep(1. / self.rate + .002)  # convert to mS to S
        return self.readRegister(self.REG_POINTER_CONVERT) * self.gain_scaling[self.gain]

    def readADC_Differential(self, chan='01'):
        # start with default values
        config = (self.REG_CONFIG_CQUE_NONE  # Disable the comparator (default val)
                  | self.REG_CONFIG_CLAT_NONLAT  # Non-latching (default val)
                  | self.REG_CONFIG_CPOL_ACTVLOW  # Alert/Rdy active low   (default val)
                  | self.REG_CONFIG_CMODE_TRAD  # Traditional comparator (default val)
                  | self.sdr_selection[self.rate]  # samples per second
                  | self.REG_CONFIG_MODE_SINGLE)  # Single-shot mode (default)

        # Set PGA/voltage range
        config |= self.gains[self.gain]
        if chan == '01':
            config |= self.REG_CONFIG_MUX_DIFF_0_1
        elif chan == '23':
            config |= self.REG_CONFIG_MUX_DIFF_2_3
        # Set 'start single-conversion' bit
        config |= self.REG_CONFIG_OS_SINGLE
        self.writeRegister(self.REG_POINTER_CONFIG, config);
        time.sleep(1. / self.rate + .002)  # convert to mS to S
        return int16(self.readRegister(self.REG_POINTER_CONVERT)) * self.gain_scaling[self.gain]

    def getLastResults(self):
        return int16(self.readRegister(self.REG_POINTER_CONVERT)) * self.gain_scaling[self.gain]

    def getRaw(self):
        '''
        return values in mV
        '''
        chan = self.type_selection[self.channel]
        if self.channel[:3] == 'UNI':
            return [self.readADC_SingleEnded(chan)]
        elif self.channel[:3] == 'DIF':
            return [self.readADC_Differential(chan)]
