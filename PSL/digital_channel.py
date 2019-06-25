from __future__ import print_function
import numpy as np

digital_channel_names = ['ID1', 'ID2', 'ID3', 'ID4', 'SEN', 'EXT', 'CNTR']


class digital_channel:
    EVERY_SIXTEENTH_RISING_EDGE = 5
    EVERY_FOURTH_RISING_EDGE = 4
    EVERY_RISING_EDGE = 3
    EVERY_FALLING_EDGE = 2
    EVERY_EDGE = 1
    DISABLED = 0

    def __init__(self, a):
        self.gain = 0
        self.channel_number = a
        self.digital_channel_names = digital_channel_names
        self.name = self.digital_channel_names[a]
        self.xaxis = np.zeros(20000)
        self.yaxis = np.zeros(20000)
        self.timestamps = np.zeros(10000)
        self.length = 100
        self.initial_state = 0
        self.prescaler = 0
        self.datatype = 'int'
        self.trigger = 0
        self.dlength = 0
        self.plot_length = 0
        self.maximum_time = 0
        self.maxT = 0
        self.initial_state_override = False
        self.mode = self.EVERY_EDGE

    def set_params(self, **keys):
        self.channel_number = keys.get('channel_number', self.channel_number)
        self.name = keys.get('name', 'ErrOr')

    def load_data(self, initial_state, timestamps):
        if self.initial_state_override:
            self.initial_state = (self.initial_state_override - 1) == 1
            self.initial_state_override = False
        else:
            self.initial_state = initial_state[self.name]
        self.timestamps = timestamps
        self.dlength = len(self.timestamps)
        # print('dchan.py',self.channel_number,self.name,initial_state,self.initial_state)
        self.timestamps = np.array(self.timestamps) * [1. / 64, 1. / 8, 1., 4.][self.prescaler]

        if self.dlength:
            self.maxT = self.timestamps[-1]
        else:
            self.maxT = 0

    def generate_axes(self):
        HIGH = 1  # (4-self.channel_number)*(3)
        LOW = 0  # HIGH - 2.5
        state = HIGH if self.initial_state else LOW

        if self.mode == self.DISABLED:
            self.xaxis[0] = 0
            self.yaxis[0] = state
            n = 1
            self.plot_length = n

        elif self.mode == self.EVERY_EDGE:
            self.xaxis[0] = 0
            self.yaxis[0] = state
            n = 1
            for a in range(self.dlength):
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = state
                state = LOW if state == HIGH else HIGH
                n += 1
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = state
                n += 1

            self.plot_length = n

        elif self.mode == self.EVERY_FALLING_EDGE:
            self.xaxis[0] = 0
            self.yaxis[0] = HIGH
            n = 1
            for a in range(self.dlength):
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = HIGH
                n += 1
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = LOW
                n += 1
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = HIGH
                n += 1
            state = HIGH
            self.plot_length = n

        elif self.mode == self.EVERY_RISING_EDGE or self.mode == self.EVERY_FOURTH_RISING_EDGE or self.mode == self.EVERY_SIXTEENTH_RISING_EDGE:
            self.xaxis[0] = 0
            self.yaxis[0] = LOW
            n = 1
            for a in range(self.dlength):
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = LOW
                n += 1
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = HIGH
                n += 1
                self.xaxis[n] = self.timestamps[a]
                self.yaxis[n] = LOW
                n += 1
            state = LOW
            self.plot_length = n
            # print(self.channel_number,self.dlength,self.mode,len(self.yaxis),self.plot_length)

    def get_xaxis(self):
        return self.xaxis[:self.plot_length]

    def get_yaxis(self):
        return self.yaxis[:self.plot_length]
