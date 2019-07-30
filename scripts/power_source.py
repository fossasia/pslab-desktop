import sys
import json
import time
import datetime


class Power_source:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.device = I
        self.device.set_pcs(0)
        self.device.set_pv1(0)
        self.device.set_pv2(0)
        self.device.set_pv3(0)

    def set_config(self, pcs_value, pv1_value, pv2_value, pv3_value):
        self.device.set_pcs(pcs_value)
        self.device.set_pv1(pv1_value)
        self.device.set_pv2(pv2_value)
        self.device.set_pv3(pv3_value)

    def get_config(self):
        output = {'type': 'GET_CONFIG_PWR_SRC',
                  'pcs': self.device.get_pcs(),
                  'pv1': self.device.get_pv1(),
                  'pv2': self.device.get_pv2(),
                  'pv3': self.device.get_pv3()}
        print(json.dumps(output))
        sys.stdout.flush()

    def get_config_from_file(self, data_path):
        self.file_write.get_config_from_file(data_path, "PowerSource")

    def save_config(self, data_path):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()
        self.file_write.save_config(
            data_path, "PowerSource",  timestamp=timestamp, datetime=datetime_data,
            pcs=self.device.get_pcs(), pv1=self.device.get_pv1(), pv2=self.device.get_pv2(),
            pv3=self.device.get_pv3())
