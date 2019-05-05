import threading
import sys
import time
import json
import numpy as np


class Oscilloscope:
    def __init__(self, I, time_gap, number_of_samples, delay, ch1, ch2, ch3, ch4):
        self.device = I
        self.isReading = False
        self.time_gap = time_gap
        self.number_of_samples = number_of_samples
        self.delay = delay
        self.ch1 = ch1
        self.ch2 = ch2
        self.ch3 = ch3
        self.ch4 = ch4
        self.number_of_channels = ch1 + ch2 + ch3 + ch4

    def readData(self):
        # call appropriate function depending
        if(self.number_of_channels == 1):
            # call one channel
            return threading.Thread(
                target=self.get_one_channel_data,
                name='osc_1')
        elif(self.number_of_channels == 2):
            # call two channels
            return threading.Thread(
                target=self.get_two_channel_data,
                name='osc_2')
        else:
            # call four channel
            return threading.Thread(
                target=self.get_four_channel_data,
                name='osc_4')

    def get_one_channel_data(self):
        active_channel = None
        if self.ch1:
            active_channel = 'ch1'
        elif self.ch2:
            active_channel = 'ch2'
        elif self.ch3:
            active_channel = 'ch3'
        else:
            active_channel = 'ch4'

        self.isReading = True
        while self.isReading:
            x, y = self.device.capture1(
                active_channel.upper(), self.number_of_samples, self.time_gap)
            output = {'type': 'START_OSC', 'data': np.stack(
                (x, y)).T.tolist(), 'keys': ['timeGap', active_channel],
                'numberOfChannels': 2}
            print(json.dumps(output))
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)

    def get_two_channel_data(self):
        self.isReading = True
        while self.isReading:
            x, y1, y2 = self.device.capture2(
                self.number_of_samples, self.time_gap)
            output = {'type': 'START_OSC', 'data': np.stack(
                (x, y1, y2)).T.tolist(), 'keys': ['timeGap', 'ch1', 'ch2'],
                'numberOfChannels': 2}
            print(json.dumps(output))
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)

    def get_four_channel_data(self):
        while self.isReading:
            x, y1, y2 = self.device.capture2(
                self.number_of_samples, self.time_gap)
            # print(y.tolist())
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)
