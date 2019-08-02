import threading
import sys
import time
import datetime
import json
import numpy as np


class LogicAnalyser:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.device = I
        self.la_read_thread = None
        self.is_reading = False
        self.channel_mode = 3
        self.number_of_channels = 4
        self.trigger1_type = 1
        self.trigger2_type = 1
        self.trigger3_type = 1
        self.trigger4_type = 1

    def set_config(self, number_of_channels, trigger1_type, trigger2_type, trigger3_type, trigger4_type):
        self.number_of_channels = int(number_of_channels)
        self.trigger1_type = int(trigger1_type)
        self.trigger2_type = int(trigger2_type)
        self.trigger3_type = int(trigger3_type)
        self.trigger4_type = int(trigger4_type)

    def get_config(self):
        output = {'type': 'GET_CONFIG_LA',
                  'numberOfChannels': self.number_of_channels,
                  'trigger1Type': self.trigger1_type,
                  'trigger2Type': self.trigger2_type,
                  'trigger3Type': self.trigger3_type,
                  'trigger4Type': self.trigger4_type,
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
            self.device.stop_LA()
            self.la_read_thead.join()

    def capture(self):
        self.is_reading = True
        ts1 = None
        v1 = None
        ts2 = None
        v2 = None
        ts3 = None
        v3 = None
        ts4 = None
        v4 = None
        if self.number_of_channels == 1:
            self.device.start_one_channel_LA(
                channel="ID1", channel_mode=self.trigger1_type)
            time.sleep(0.1)
            self.device.fetch_LA_channels()
            ts1 = self.device.dchans[0].get_xaxis().tolist()
            v1 = self.device.dchans[0].get_yaxis().tolist()
        elif self.number_of_channels == 2:
            self.device.start_two_channel_LA(
                channel=["ID1", "ID2"], channel_mode=[self.trigger1_type, self.trigger2_type])
            time.sleep(0.1)
            self.device.fetch_LA_channels()
            ts1 = self.device.dchans[0].get_xaxis().tolist()
            v1 = self.device.dchans[0].get_yaxis().tolist()
            ts2 = self.device.dchans[1].get_xaxis()
            v2 = self.device.dchans[1].get_yaxis() + 2
            v2 = v2.tolist()
        elif self.number_of_channels == 3:
            self.device.start_two_channel_LA(
                channel=["ID1", "ID2", "ID3"], channel_mode=[self.trigger1_type, self.trigger2_type, self.trigger3_type])
            time.sleep(0.1)
            self.device.fetch_LA_channels()
            ts1 = self.device.dchans[0].get_xaxis().tolist()
            v1 = self.device.dchans[0].get_yaxis().tolist()
            ts2 = self.device.dchans[1].get_xaxis().tolist()
            v2 = self.device.dchans[1].get_yaxis() + 2
            v2 = v2.tolist()
            ts3 = self.device.dchans[2].get_xaxis().tolist()
            v3 = self.device.dchans[2].get_yaxis() + 4
            v3 = v3.tolist()
        elif self.number_of_channels == 4:
            self.device.start_four_channel_LA(
                mode=[self.trigger1_type, self.trigger2_type, self.trigger3_type, self.trigger4_type])
            time.sleep(0.1)
            self.device.fetch_LA_channels()
            ts1 = self.device.dchans[0].get_xaxis().tolist()
            v1 = self.device.dchans[0].get_yaxis().tolist()
            ts2 = self.device.dchans[1].get_xaxis().tolist()
            v2 = self.device.dchans[1].get_yaxis() + 2
            v2 = v2.tolist()
            ts3 = self.device.dchans[2].get_xaxis().tolist()
            v3 = self.device.dchans[2].get_yaxis() + 4
            v3 = v3.tolist()
            ts4 = self.device.dchans[3].get_xaxis().tolist()
            v4 = self.device.dchans[3].get_yaxis() + 6
            v4 = v4.tolist()
        output = {
            'type': 'START_LA',
            'ts1': ts1,
            'v1': v1,
            'ts2': ts2,
            'v2': v2,
            'ts3': ts3,
            'v3': v3,
            'ts4': ts4,
            'v4': v4,
            'numberOfChannels': self.number_of_channels,
        }
        if self.is_reading:
            print(json.dumps(output))
            sys.stdout.flush()
        self.is_reading = False
