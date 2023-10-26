import sys
import time
import threading
import json

from serial.tools import list_ports

from pslab import ScienceLab


class Device_detection:
    def __init__(self):
        self.device = None
        self.connected = False
        self.device_detection_thread = None
        pass

    def disconnect(self):
        self.connected = False
        self.device_detection_thread.join()

    def async_connect(self):
        # First connection attempt
        self.device = ScienceLab()
        output = None
        if not self.device.connected:
            # No device connected
            output = {'type': 'DEVICE_CONNECTION_STATUS',
                      'isConnected': False,
                      'message': 'Device not connected', }
        else:
            output = {'type': 'DEVICE_CONNECTION_STATUS',
                      'isConnected': True,
                      'message': 'Device connected',
                      'deviceName': str(self.device.get_version()),
                      'portName': self.device.interface.name
                      }
            self.connected = True
        print(json.dumps(output))
        sys.stdout.flush()

        self.device_detection_thread = threading.Thread(
            target=self.check_connection,
            name='conn_check')
        self.device_detection_thread.start()

    def check_connection(self):
        while self.connected:
            ports = [p.device for p in list_ports.comports()]
            if self.device.interface.name not in ports:
                output = {'type': 'DEVICE_CONNECTION_STATUS',
                          'isConnected': False,
                          'message': 'Device disconnected'}
                print(json.dumps(output))
                sys.stdout.flush()
                self.disconnect()
            time.sleep(0.5)
