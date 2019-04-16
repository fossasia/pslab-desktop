from PSL import sciencelab
import sys
import threading
import time
import json


class Oscilloscope:
    def __init__(self, I):
        self.device = I
        self.isReading = False
        self.time_gap = int(sys.argv[2])
        self.number_of_samples = int(sys.argv[3])
        self.delay = int(sys.argv[4])
        self.ch1 = int(sys.argv[5])
        self.ch2 = int(sys.argv[6])
        self.ch3 = int(sys.argv[7])
        self.ch4 = int(sys.argv[8])

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
            x, y = self.device.capture1(
                'CH1', self.number_of_samples, self.time_gap)
            print(y.tolist())
            sys.stdout.flush()
            time.sleep(0.001 * self.delay)


def main():
    try:
        I = sciencelab.connect()
        instrument_type = sys.argv[1]

        if instrument_type == 'OSC':
            # for test
            I.set_sine1(1000)

            oscilloscope = Oscilloscope(I)
            data_read_thread = oscilloscope.readData()

            data_read_thread.start()

            command = input()
            if command == "STOP":
                oscilloscope.isReading = False

            data_read_thread.join()

    except:
        # Print error code for connection error
        pass


if __name__ == '__main__':
    main()
