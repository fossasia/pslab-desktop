import threading
import sys
import time
import datetime
import json
import numpy as np
from PSL import analyticsClass

analytics = analyticsClass.analyticsClass()


class Oscilloscope:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.oscilloscope_voltage_read_thread = None
        self.oscilloscope_fft_read_thread = None
        self.oscilloscope_xy_plot_read_thread = None
        self.device = I
        self.is_reading_voltage = False
        self.is_reading_fft = False
        self.is_reading_xy_plot = False

        self.number_of_samples = 1000
        self.time_base = 0.5
        self.ch1 = True
        self.ch2 = False
        self.ch3 = False
        self.mic = False
        self.ch1_map = 'CH1'
        self.ch2_map = 'CH2'
        self.mic_map = 'Inbuilt'
        self.trigger_voltage = 0
        self.trigger_channel = 'CH1'
        self.is_trigger_active = False
        self.is_fourier_transform_active = False
        self.fit_type = 'Sine'
        self.fit_channel1 = 'None'
        self.fit_channel2 = 'None'
        self.is_xy_plot_active = False
        self.plot_channel1 = 'CH1'
        self.plot_channel2 = 'CH2'

        self.number_of_channels = self.ch1 + self.ch2 + self.ch3 + self.mic
        self.channels_to_read = self.calculate_channels_to_read(
            self.ch1, self.ch2, self.ch3, self.mic)
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)

    def set_config(self, time_base, number_of_samples, ch1, ch2, ch3, mic,
                   is_trigger_active, trigger_channel, trigger_voltage,
                   is_fourier_transform_active, fit_type, fit_channel1,
                   fit_channel2, is_xy_plot_active, plot_channel1,
                   plot_channel2):
        self.time_base = time_base
        self.number_of_samples = number_of_samples
        self.ch1 = ch1
        self.ch2 = ch2
        self.ch3 = ch3
        self.mic = mic
        self.is_trigger_active = is_trigger_active
        self.trigger_channel = trigger_channel
        self.trigger_voltage = trigger_voltage
        self.is_fourier_transform_active = is_fourier_transform_active
        self.fit_type = fit_type
        self.fit_channel1 = fit_channel1
        self.fit_channel2 = fit_channel2
        self.is_xy_plot_active = is_xy_plot_active
        self.plot_channel1 = plot_channel1
        self.plot_channel2 = plot_channel2

        self.number_of_channels = ch1 + ch2 + ch3 + mic
        self.channels_to_read = self.calculate_channels_to_read(
            self.ch1, self.ch2, self.ch3, self.mic)
        self.delay, self.time_gap = self.calculate_delay_time_gap(
            self.time_base, self.number_of_samples)
        self.device.oscilloscope.configure_trigger(
            self.trigger_channel, self.trigger_voltage)

    def get_config(self):
        output = {'type': 'GET_CONFIG_OSC',
                  'timeBase': self.time_base,
                  'ch1': self.ch1,
                  'ch2': self.ch2,
                  'ch3': self.ch3,
                  'mic': self.mic,
                  'ch1Map': self.ch1_map,
                  'ch2Map': self.ch2_map,
                  'micMap': self.mic_map,
                  'isTriggerActive': self.is_trigger_active,
                  'triggerVoltage': self.trigger_voltage,
                  'triggerChannel': self.trigger_channel,
                  'isFourierTransformActive': self.is_fourier_transform_active,
                  'fitType': self.fit_type,
                  'fitChannel1': self.fit_channel1,
                  'fitChannel2': self.fit_channel2,
                  'isXYPlotActive': self.is_xy_plot_active,
                  'plotChannel1': self.plot_channel1,
                  'plotChannel2': self.plot_channel2,
                  }
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        if self.is_fourier_transform_active:
            self.oscilloscope_fft_read_thread = threading.Thread(
                target=self.capture_loop_fft,
                name='osc_fft')
            self.oscilloscope_fft_read_thread.start()
        elif self.is_xy_plot_active:
            self.oscilloscope_xy_plot_read_thread = threading.Thread(
                target=self.capture_loop_xy_plot,
                name='osc_xy_plot')
            self.oscilloscope_xy_plot_read_thread.start()
        else:
            self.oscilloscope_voltage_read_thread = threading.Thread(
                target=self.capture_loop_voltage,
                name='osc_voltage')
            self.oscilloscope_voltage_read_thread.start()

    def stop_read(self):
        if self.is_reading_voltage:
            self.is_reading_voltage = False
            self.oscilloscope_voltage_read_thread.join()
        if self.is_reading_fft:
            self.is_reading_fft = False
            self.oscilloscope_fft_read_thread.join()
        if self.is_xy_plot_active:
            self.is_reading_xy_plot = False
            self.oscilloscope_xy_plot_read_thread.join()

    def capture_loop_voltage(self):
        self.is_reading_voltage = True
        x = None
        y1 = None
        y2 = None
        y3 = None
        y4 = None
        while self.is_reading_voltage:
            self.device.oscilloscope.trigger_enabled = self.is_trigger_active
            x = self.device.oscilloscope.capture_nonblocking(
                self.channels_to_read, self.number_of_samples, self.time_gap)
            time.sleep(self.delay)
            keys = ['time']
            datetime_data = datetime.datetime.now()
            timestamp = time.time()
            vector = ()
            if self.ch1:
                y1 = self.device.oscilloscope.fetch_data(self.ch1_map)
                keys.append('ch1')
                vector = vector + (y1, )
                self.file_write.update_buffer(
                    "OSC", timestamp=timestamp, datetime=datetime_data, channel='CH1', xData=x, yData=y1, timebase=self.time_gap)
            if self.ch2:
                y2 = self.device.oscilloscope.fetch_data("CH2")
                keys.append('ch2')
                vector = vector + (y2, )
                self.file_write.update_buffer(
                    "OSC", timestamp=timestamp, datetime=datetime_data, channel='CH2', xData=x, yData=y2, timebase=self.time_gap)
            if self.ch3:
                y3 = self.device.oscilloscope.fetch_data("CH3")
                keys.append('ch3')
                vector = vector + (y3, )
                self.file_write.update_buffer(
                    "OSC", timestamp=timestamp, datetime=datetime_data, channel='CH3', xData=x, yData=y3, timebase=self.time_gap)
            if self.mic:
                y4 = self.device.oscilloscope.fetch_data("MIC")
                keys.append('mic')
                vector = vector + (y4, )
                self.file_write.update_buffer(
                    "OSC", timestamp=timestamp, datetime=datetime_data, channel='MIC', xData=x, yData=y4, timebase=self.time_gap)
            vector = (x * 1e-3, ) + vector
            output = {
                'type': 'START_OSC',
                'data': np.stack(vector).T.tolist(),
                'keys': keys,
                'numberOfChannels': self.number_of_channels,
            }
            print(json.dumps(output))
            sys.stdout.flush()

    def capture_loop_fft(self):
        self.is_reading_fft = True
        x = None
        y1 = None
        y2 = None
        y3 = None
        y4 = None
        fit_output1_sine = False
        fit_output2_sine = False
        fit_output1_square = False
        fit_output2_square = False
        while self.is_reading_fft:
            self.device.oscilloscope.trigger_enabled = self.is_trigger_active
            x = self.device.oscilloscope.capture_nonblocking(
                self.channels_to_read, self.number_of_samples, self.time_gap)
            time.sleep(self.delay)
            keys = ['frequency']
            vector = ()
            frequency = None
            if self.ch1:
                y1 = self.device.oscilloscope.fetch_data(self.ch1_map)
                frequency, amp1 = self.fft(y1, self.time_gap * 1e-3)
                keys.append('ch1')
                vector = vector + (amp1, )
            if self.ch2:
                y2 = self.device.oscilloscope.fetch_data("CH2")
                frequency, amp2 = self.fft(y2, self.time_gap * 1e-3)
                keys.append('ch2')
                vector = vector + (amp2, )
            if self.ch3:
                y3 = self.device.oscilloscope.fetch_data("CH3")
                frequency, amp3 = self.fft(y3, self.time_gap * 1e-3)
                keys.append('ch3')
                vector = vector + (amp3, )
            if self.mic:
                y4 = self.device.oscilloscope.fetch_data("MIC")
                frequency, amp4 = self.fft(y4, self.time_gap * 1e-3)
                keys.append('mic')
                vector = vector + (amp4, )
            vector = (frequency, ) + vector

            if self.fit_channel1 != 'None':
                if self.fit_type == 'Sine':
                    try:
                        if self.fit_channel1 == 'CH1' and self.ch1:
                            fit_output1_sine = analytics.sineFit(x, y1)
                        elif self.fit_channel1 == 'CH2' and self.ch2:
                            fit_output1_sine = analytics.sineFit(x, y2)
                        elif self.fit_channel1 == 'CH3' and self.ch3:
                            fit_output1_sine = analytics.sineFit(x, y3)
                        elif self.fit_channel1 == 'MIC' and self.mic:
                            fit_output1_sine = analytics.sineFit(x, y4)
                        else:
                            fit_output1_sine = False
                    except:
                        fit_output1_sine = False
                elif self.fit_type == 'Square':
                    try:
                        if self.fit_channel1 == 'CH1' and self.ch1:
                            fit_output1_square = analytics.squareFit(x, y1)
                        elif self.fit_channel1 == 'CH2' and self.ch2:
                            fit_output1_square = analytics.squareFit(x, y2)
                        elif self.fit_channel1 == 'CH3' and self.ch3:
                            fit_output1_square = analytics.squareFit(x, y3)
                        elif self.fit_channel1 == 'MIC' and self.mic:
                            fit_output1_square = analytics.squareFit(x, y4)
                        else:
                            fit_output1_square = False
                    except:
                        fit_output1_square = False

            if self.fit_channel2 != 'None':
                if self.fit_type == 'Sine':
                    try:
                        if self.fit_channel2 == 'CH1':
                            fit_output2_sine = analytics.sineFit(x, y1)
                        elif self.fit_channel2 == 'CH2':
                            fit_output2_sine = analytics.sineFit(x, y2)
                        elif self.fit_channel2 == 'CH3':
                            fit_output2_sine = analytics.sineFit(x, y3)
                        elif self.fit_channel2 == 'MIC':
                            fit_output2_sine = analytics.sineFit(x, y4)
                        else:
                            fit_output2_sine = False
                    except:
                        fit_output2_sine = False
                elif self.fit_type == 'Square':
                    try:
                        if self.fit_channel2 == 'CH1':
                            fit_output2_square = analytics.squareFit(x, y1)
                        elif self.fit_channel2 == 'CH2':
                            fit_output2_square = analytics.squareFit(x, y2)
                        elif self.fit_channel2 == 'CH3':
                            fit_output2_square = analytics.squareFit(x, y3)
                        elif self.fit_channel2 == 'MIC':
                            fit_output2_square = analytics.squareFit(x, y4)
                        else:
                            fit_output2_square = False
                    except:
                        fit_output2_square = False

            output = {
                'type': 'START_OSC',
                'isFFT': True,
                'data': np.stack(vector).T.tolist(),
                'keys': keys,
                'numberOfChannels': self.number_of_channels,
                'fitType': self.fit_type if self.is_fourier_transform_active else None,
                'fitOutput1Sine': fit_output1_sine,
                'fitOutput2Sine': fit_output2_sine,
                'fitOutput1Square': fit_output1_square,
                'fitOutput2Square': fit_output2_square
            }
            print(json.dumps(output))
            sys.stdout.flush()

    def capture_loop_xy_plot(self):
        self.is_reading_xy_plot = True
        y1 = None
        y2 = None
        y3 = None
        y4 = None
        while self.is_reading_xy_plot:
            self.device.oscilloscope.trigger_enabled = self.is_trigger_active
            x = self.device.oscilloscope.capture_nonblocking(
                self.channels_to_read, self.number_of_samples, self.time_gap)
            time.sleep(self.delay)
            vector = ()
            if self.ch1 and self.plot_channel1 == 'CH1':
                y1 = self.device.oscilloscope.fetch_data(self.ch1_map)
                vector = vector + (y1, )
            if self.ch2 and self.plot_channel1 == 'CH2':
                y2 = self.device.oscilloscope.fetch_data("CH2")
                vector = vector + (y2, )
            if self.ch3 and self.plot_channel1 == 'CH3':
                y3 = self.device.oscilloscope.fetch_data("CH3")
                vector = vector + (y3, )
            if self.mic and self.plot_channel1 == 'MIC':
                y4 = self.device.oscilloscope.fetch_data("MIC")
                vector = vector + (y4, )

            if self.ch1 and self.plot_channel2 == 'CH1':
                y1 = self.device.oscilloscope.fetch_data(self.ch1_map)
                vector = vector + (y1, )
            if self.ch2 and self.plot_channel2 == 'CH2':
                y2 = self.device.oscilloscope.fetch_data("CH2")
                vector = vector + (y2, )
            if self.ch3 and self.plot_channel2 == 'CH3':
                y3 = self.device.oscilloscope.fetch_data("CH3")
                vector = vector + (y3, )
            if self.mic and self.plot_channel2 == 'MIC':
                y4 = self.device.oscilloscope.fetch_data("MIC")
                vector = vector + (y4, )

            output = {
                'type': 'START_OSC',
                'isXYPlot': True,
                'data': np.stack(vector).T.tolist(),
                'keys': ['plotChannel1', 'plotChannel2'],
            }
            print(json.dumps(output))
            sys.stdout.flush()

    def calculate_delay_time_gap(self, time_base, number_of_samples):
        time_gap = (time_base * 10 * 1e3) / number_of_samples
        delay = time_gap * number_of_samples * 1e-6
        if delay < 0.05:
            if self.is_fourier_transform_active:
                return (0.075, time_gap)
            elif self.is_xy_plot_active:
                return (0.15, time_gap)
            else:
                return (0.05, time_gap)
        else:
            return (delay, time_gap)

    def calculate_channels_to_read(self, ch1, ch2, ch3, mic):
        if ch3 or mic:
            return 4
        elif ch2:
            return 2
        elif ch1:
            return 1
        else:
            return 0

    def fft(self, ya, si):
        ns = len(ya)
        if ns % 2 == 1:
            ns -= 1
            ya = ya[:-1]
        v = np.array(ya)
        tr = abs(np.fft.fft(v)) / ns
        frq = np.fft.fftfreq(ns, si)
        x = frq.reshape(2, ns // 2)
        y = tr.reshape(2, ns // 2)
        return x[0], y[0]
