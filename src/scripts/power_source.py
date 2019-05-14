import sys
import json


class Power_source:
    def __init__(self, I):
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
        pcs_value = self.device.get_pcs()
        pv1_value = self.device.get_pv1()
        pv2_value = self.device.get_pv2()
        pv3_value = self.device.get_pv3()
        output = {'type': 'GET_CONFIG_PWR_SRC',
                  'pcs': pcs_value,
                  'pv1': pv1_value,
                  'pv2': pv2_value,
                  'pv3': pv3_value}
        print(json.dumps(output))
        sys.stdout.flush()
