import threading
import sys
import time
import datetime
import json
import numpy as np

from PSL.digital_channel import MODES

MODES = {v: k for k, v in MODES.items()}


class LogicAnalyser:
    def __init__(self, I, file_write):
        self.file_write = file_write
        self.capture_time = 0.1
        self.device = I
        self.la_read_thread = None
        self.is_reading = False
        self.channel_mode = 3
        self.number_of_channels = 4
        self.trigger1_type = 1
        self.trigger2_type = 1
        self.trigger3_type = 1
        self.trigger4_type = 1

    def set_config(self, number_of_channels, trigger1_type, trigger2_type, trigger3_type, trigger4_type, capture_time):
        self.number_of_channels = int(number_of_channels)
        self.trigger1_type = int(trigger1_type)
        self.trigger2_type = int(trigger2_type)
        self.trigger3_type = int(trigger3_type)
        self.trigger4_type = int(trigger4_type)
        self.capture_time = int(capture_time)

    def get_config(self):
        output = {'type': 'GET_CONFIG_LA',
                  'numberOfChannels': self.number_of_channels,
                  'trigger1Type': self.trigger1_type,
                  'trigger2Type': self.trigger2_type,
                  'trigger3Type': self.trigger3_type,
                  'trigger4Type': self.trigger4_type,
                  'captureTime': self.capture_time
                  }
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        self.la_read_thead = threading.Thread(
            target=self.capture,
            name='la')
        self.la_read_thead.start()

    def stop_read(self):
        if self.is_reading:
            self.is_reading = False
            self.device.logic_analyzer.stop()
            self.la_read_thead.join()

    def capture(self):
        self.is_reading = True
        self.device.logic_analyzer.capture(
                self.number_of_channels,
                modes=[
                        MODES[self.trigger1_type],
                        MODES[self.trigger2_type],
                        MODES[self.trigger3_type],
                        MODES[self.trigger4_type],
                ],
                block=False
        )
        time.sleep(self.capture_time / 1e3)
        self.device.logic_analyzer.stop()
        timestamps = self.device.logic_analyzer.fetch_data()
        xy = 8 * [np.array([])]
        xy[: self.number_of_channels * 2] = self.device.logic_analyzer.get_xy(timestamps)
        x1, y1, x2, y2, x3, y3, x4, y4 = xy

        output = {
            'type': 'START_LA',
            'time1': x1.tolist(),
            'voltage1': (y1 + 0.).tolist(),
            'time2': x2.tolist(),
            'voltage2': (y2 + 2.).tolist(),
            'time3': x3.tolist(),
            'voltage3': (y3 + 4.).tolist(),
            'time4': x4.tolist(),
            'voltage4': (y4 + 6.).tolist(),
            'numberOfChannels': self.number_of_channels,
        }
        if self.is_reading:
            print(json.dumps(output))
            sys.stdout.flush()
        self.is_reading = False
