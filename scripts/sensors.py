import datetime
import json
import sys
import threading
import time
from PSL.SENSORS.SHT21 import SHT21

class Sensors:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.multimeter_data_read_thread = None
        self.device = I
        self.is_reading = False
        self.active_category = 'SCAN'

    def set_config(self, active_category):
        self.active_category = active_category

    def get_config(self):
        output = {'type': 'GET_CONFIG_SENSORS',
                  'activeCategory': self.active_category}
        print(json.dumps(output))
        sys.stdout.flush()

    def start_read(self):
        self.sensor_data_read_thread = threading.Thread(
            target=self.capture_loop,
            name='sensors')
        self.sensor_data_read_thread.start()

    def stop_read(self):
        self.is_reading = False
        self.sensor_data_read_thread.join()

    def capture_loop(self):
        self.is_reading = True
        while self.is_reading:
            if self.active_category == 'SCAN':
                self.scan()

    def read(self):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()

        sensor = SHT21(self.device.I2C)
        data = sensor.getRaw()

        self.file_write.update_buffer(
            "SENSOR_DATA", timestamp=timestamp, datetime=datetime_data, data='sensor_data', value=data)
        time.sleep(0.25)

        output = {'type': 'SENSORS_READ', 'data': data}
        print(json.dumps(output))
        sys.stdout.flush()


    def scan(self):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()

        data = self.device.i2c.scan()
        self.file_write.update_buffer(
            "SENSORS", timestamp=timestamp, datetime=datetime_data, data='scan', value=data)
        time.sleep(0.25)

        output = {'type': 'SENSORS_SCAN', 'data': data}
        print(json.dumps(output))
        sys.stdout.flush()
