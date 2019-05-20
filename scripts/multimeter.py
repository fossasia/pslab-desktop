import threading
import sys
import time
import json
import numpy as np


class Multimeter:
    def __init__(self, I):
        self.multimeter_data_read_thread = None
        self.device = I
        self.is_reading = False
        self.active_catagory = 'VOLTAGE'
        self.active_subtype = 'CH1'
        self.parameter = None

    def set_config(self, active_catagory, active_subtype, parameter):
        self.active_catagory = active_catagory
        self.active_subtype = active_subtype
        self.parameter = parameter

    def get_config(self):
        output = {'type': 'GET_CONFIG_MUL_MET',
                  'activeCatagory': self.active_catagory,
                  'activeSubType': self.active_subtype,
                  'parameter': self.parameter}
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        self.multimeter_data_read_thread = threading.Thread(
            target=self.capture_loop,
            name='mul_met')
        self.multimeter_data_read_thread.start()

    def stop_read(self):
        self.is_reading = False
        self.multimeter_data_read_thread.join()

    def capture_loop(self):
        self.is_reading = True
        while self.is_reading:
            if self.active_catagory == 'VOLTAGE':
                self.read_voltage(self.active_subtype)
            elif self.active_catagory == 'PULSE':
                self.read_pulse(self.active_subtype, self.parameter)
            elif self.active_catagory == 'MISC':
                self.read_misc(self.active_subtype)

    def read_voltage(self, channel_name):
        voltage = self.device.get_average_voltage(channel_name)
        time.sleep(0.25)
        output = {'type': 'START_MUL_MET', 'data': voltage}
        print(json.dumps(output))
        sys.stdout.flush()

    def read_pulse(self, pin_name, reading_type):
        if reading_type == 'PULSE_COUNT':
            self.device.countPulses(pin_name)
            time.sleep(1)
            data = self.device.readPulseCount()
        elif reading_type == 'PULSE_FREQUENCY':
            data = self.device.get_freq(pin_name)
            time.sleep(0.25)
        output = {'type': 'START_MUL_MET', 'data': data}
        print(json.dumps(output))
        sys.stdout.flush()

    def read_misc(self, pin_name):
        if pin_name == 'RESISTOR':
            data = self.device.get_resistance()
            time.sleep(0.25)
        elif pin_name == 'CAPACITOR':
            time.sleep(1)
            pass
        output = {'type': 'START_MUL_MET', 'data': data}
        print(json.dumps(output))
        sys.stdout.flush()
