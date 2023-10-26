import sys
import json
import time
import datetime


class Power_source:
    def __init__(self, device, file_write):
        self.file_write = file_write
        self.power_supply = device.power_supply

    def set_config(self, pcs_value, pv1_value, pv2_value, pv3_value):
        self.power_supply.pcs = pcs_value / 1000  # mA
        self.power_supply.pv1 = pv1_value
        self.power_supply.pv2 = pv2_value
        self.power_supply.pv3 = pv3_value

    def get_config(self):
        output = {'type': 'GET_CONFIG_PWR_SRC',
                  'pcs': self.power_supply.pcs,
                  'pv1': self.power_supply.pv1,
                  'pv2': self.power_supply.pv2,
                  'pv3': self.power_supply.pv3}
        print(json.dumps(output))
        sys.stdout.flush()

    def get_config_from_file(self, data_path):
        self.file_write.get_config_from_file(data_path, "PowerSource")

    def save_config(self, data_path):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()
        self.file_write.save_config(
            data_path, "PowerSource",  timestamp=timestamp, datetime=datetime_data,
            pcs=self.power_supply.pcs, pv1=self.power_supply.pv1, pv2=self.power_supply.pv2,
            pv3=self.power_supply.pv3)
