import threading
import sys
import time
import datetime
import json
import numpy as np


class Multimeter:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.multimeter_data_read_thread = None
        self.device = I
        self.is_reading = False
        self.active_category = 'VOLTAGE'
        self.active_subtype = 'CH1'
        self.parameter = 'PULSE_FREQUENCY'

    def set_config(self, active_category, active_subtype, parameter):
        self.active_category = active_category
        self.active_subtype = active_subtype
        self.parameter = parameter

    def get_config(self):
        output = {'type': 'GET_CONFIG_MUL_MET',
                  'activeCategory': self.active_category,
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
            if self.active_category == 'VOLTAGE':
                self.read_voltage(self.active_subtype)
            elif self.active_category == 'PULSE':
                self.read_pulse(self.active_subtype, self.parameter)
            elif self.active_category == 'MISC':
                self.read_misc(self.active_subtype)

    def read_voltage(self, channel_name):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()

        voltage = self.device.get_voltage(channel_name)
        self.file_write.update_buffer(
            "MUL_MET", timestamp=timestamp, datetime=datetime_data, data=channel_name, value=voltage)
        voltage, prefix = self.precision_control(voltage)
        time.sleep(0.25)
        output = {'type': 'START_MUL_MET', 'data': voltage, 'prefix': prefix}
        print(json.dumps(output))
        sys.stdout.flush()

    def read_pulse(self, pin_name, reading_type):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()

        data = None
        prefix = None
        if reading_type == 'PULSE_COUNT':
            self.device.countPulses(pin_name)
            time.sleep(1)
            data = self.device.readPulseCount()
            self.file_write.update_buffer(
                "MUL_MET", timestamp=timestamp, datetime=datetime_data, data=pin_name, value=data)
        elif reading_type == 'PULSE_FREQUENCY':
            data = self.device.get_freq(pin_name, timeout=0.5)
            self.file_write.update_buffer(
                "MUL_MET", timestamp=timestamp, datetime=datetime_data, data=pin_name, value=data)
            data, prefix = self.precision_control(data)
            time.sleep(0.25)

        output = {'type': 'START_MUL_MET', 'data': data, 'prefix': prefix}
        print(json.dumps(output))
        sys.stdout.flush()

    def read_misc(self, pin_name):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()

        data = None
        prefix = None
        if pin_name == 'RESISTOR':
            data = self.device.get_resistance()
            time.sleep(0.25)
        elif pin_name == 'CAPACITOR':
            try:
                data = self.device.get_capacitance()
            except NotImplementedError:
                data = 0
            time.sleep(1.5)
            pass
        self.file_write.update_buffer(
            "MUL_MET", timestamp=timestamp, datetime=datetime_data, data=pin_name, value=data)
        data, prefix = self.precision_control(data)
        output = {'type': 'START_MUL_MET', 'data': data, 'prefix': prefix}
        print(json.dumps(output))
        sys.stdout.flush()

    def precision_control(self, value):
        if abs(value) >= 1e6:
            return (round(value / 1e6, 3), 'M')
        elif abs(value) >= 1e3:
            return (round(value / 1e3, 3), 'k')
        elif abs(value) <= 1e-10:
            return (0, None)
        elif abs(value) <= 1e-12:
            return (round(value / 1e-12, 3), 'p')
        elif abs(value) <= 1e-9:
            return (round(value / 1e-9, 3), 'n')
        elif abs(value) <= 1e-6:
            return (round(value / 1e-6, 3), 'μ')
        elif abs(value) <= 1e-3:
            return (round(value / 1e-3, 3), 'm')
        else:
            return (round(value, 3), None)
