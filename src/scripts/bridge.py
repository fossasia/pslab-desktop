from PSL import sciencelab
import sys
import threading
import time
import json


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

    def readData(self):
        # call appropriate function depending
        if(self.ch1 and self.ch2 and (self.ch3 or self.ch4)):
            # call all four channels
            pass
        elif(self.ch1 and self.ch2):
            # call two channels
            return threading.Thread(target=self.get_two_channel_data, name='osc_2')
        else:
            # call one channel
            return threading.Thread(target=self.get_one_channel_data, name='osc_1')

    def get_one_channel_data(self):
        self.isReading = True
        while self.isReading:
            x, y = self.device.capture1(
                'CH1', self.number_of_samples, self.time_gap)
            output = {'ch1': y.tolist()}
            print(json.dumps(output))
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)

    def get_two_channel_data(self):
        while self.isReading:
            x, y1, y2 = self.device.capture2(
                self.number_of_samples, self.time_gap)
            # print(y.tolist())
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)


def main():
    I = sciencelab.connect()
    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']


        # ---------------------------- Oscilloscope block ------------------------------
        if command == 'START_OSC':
            # for test
            I.set_sine1(1000)

            time_gap = parsed_stream_data['timeGap']
            number_of_samples = parsed_stream_data['numberOfSamples']
            delay = parsed_stream_data['delay']
            ch1 = parsed_stream_data['ch1']
            ch2 = parsed_stream_data['ch2']
            ch3 = parsed_stream_data['ch3']
            ch4 = parsed_stream_data['ch4']

            oscilloscope = Oscilloscope(
                I, time_gap, number_of_samples, delay, ch1, ch2, ch3, ch4)
            data_read_thread = oscilloscope.readData()

            data_read_thread.start()

            in_stream_data = input()
            parsed_stream_data = json.loads(in_stream_data)
            command = parsed_stream_data['command']
            if command == "STOP_OSC":
                oscilloscope.isReading = False

            data_read_thread.join()

        # -------------------------- Script termination block ---------------------------- 
        if command == 'KILL':
            break


if __name__ == '__main__':
    main()
