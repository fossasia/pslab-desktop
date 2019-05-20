import threading
import sys
import time
import json
import numpy as np


class Oscilloscope:
    def __init__(self, I):
        self.oscilloscope_data_read_thread = None
        self.device = I
        self.is_reading = False
        self.number_of_samples = 1000
        self.time_base = 5
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)
        self.ch1 = True
        self.ch2 = False
        self.ch3 = False
        self.ch4 = False
        self.ch1_map = 'CH1'
        self.ch2_map = 'CH2'
        self.ch4_map = 'Inbuilt'
        self.number_of_channels = self.ch1 + self.ch2 + self.ch3 + self.ch4
        self.trigger_voltage = 0
        self.trigger_channel = 'CH1'
        self.is_trigger_active = False
        self.is_fourier_transform_active = False
        self.transform_type = 'Sine'
        self.transform_channel1 = 'CH1'
        self.transform_channel2 = 'CH2'
        self.is_xy_plot_active = False
        self.plot_channel1 = 'CH1'
        self.plot_channel2 = 'CH2'
        # initialized values here including trigger values

    def calculate_delay_time_gap(self, time_base, number_of_samples):
        time_gap = (time_base * 10 * 1e3) / number_of_samples
        delay = time_gap * number_of_samples * 1e-6
        if delay < 0.075:
            return (0.075, time_gap)
        else:
            return (delay, time_gap)

    def set_config(self, time_base, number_of_samples, ch1, ch2, ch3, ch4, trigger_channel, trigger_voltage, is_trigger_active):
        self.time_base = time_base
        self.number_of_samples = number_of_samples
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)
        self.ch1 = ch1
        self.ch2 = ch2
        self.ch3 = ch3
        self.ch4 = ch4
        self.number_of_channels = ch1 + ch2 + ch3 + ch4
        self.is_trigger_active = is_trigger_active
        self.trigger_channel = trigger_channel
        self.trigger_voltage = trigger_voltage
        self.device.configure_trigger(
            0, self.trigger_channel, self.trigger_voltage)

    def get_config(self):
        output = {'type': 'GET_CONFIG_OSC',
                  'timeBase': self.time_base,
                  'ch1': self.ch1,
                  'ch2': self.ch2,
                  'ch3': self.ch3,
                  'isMicActive': self.ch4,
                  'ch1Map': self.ch1_map,
                  'ch2Map': self.ch2_map,
                  'ch4Map': self.ch4_map,
                  'triggerVoltage': self.trigger_voltage,
                  'triggerVoltageChannel': self.trigger_channel,
                  'isTriggerActive': self.is_trigger_active,
                  'isFourierTransformActive': self.is_fourier_transform_active,
                  'transformType': self.transform_type,
                  'transformChannel1': self.transform_channel1,
                  'transformChannel2': self.transform_channel2,
                  'isXYPlotActive': self.is_xy_plot_active,
                  'plotChannel1': self.plot_channel1,
                  'plotChannel2': self.plot_channel2,
                  }
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        self.oscilloscope_data_read_thread = threading.Thread(
            target=self.capture_loop,
            name='osc')
        self.oscilloscope_data_read_thread.start()

    def stop_read(self):
        self.is_reading = False
        self.oscilloscope_data_read_thread.join()

    def capture_loop(self):
        self.is_reading = True
        while self.is_reading:
            self.device.capture_traces(
                self.number_of_channels, self.number_of_samples, self.time_gap, trigger=self.is_trigger_active)
            time.sleep(self.delay)
            keys = ['timeGap']
            vector = ()
            x = None
            if self.ch1:
                x, y1 = self.device.fetch_trace(1)
                keys.append('ch1')
                vector = vector + (y1, )
            if self.ch2:
                x, y2 = self.device.fetch_trace(2)
                keys.append('ch2')
                vector = vector + (y2, )
            if self.ch3:
                x, y3 = self.device.fetch_trace(3)
                keys.append('ch3')
                vector = vector + (y3, )
            if self.ch4:
                x, y4 = self.device.fetch_trace(4)
                keys.append('ch4')
                vector = vector + (y4, )
            x = x * 1e-3
            vector = (x, ) + vector
            output = {'type': 'START_OSC', 'data': np.stack(
                vector).T.tolist(), 'keys': keys,
                'numberOfChannels': self.number_of_channels}
            print(json.dumps(output))
            sys.stdout.flush()
