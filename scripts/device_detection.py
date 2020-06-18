from PSL import sciencelab
import sys
import time
import threading
import json


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
        self.device = sciencelab.ScienceLab(verbose=False)
        output = None
        if not self.device.connected:
            if len(self.device.H.occupiedPorts):
                # device connected but being used by some other program
                output = {'type': 'DEVICE_CONNECTION_STATUS',
                          'isConnected': False,
                          'message': 'Device port busy'}
            else:
                # No device connected
                output = {'type': 'DEVICE_CONNECTION_STATUS',
                          'isConnected': False,
                          'message': 'Device not connected', }
        else:
            output = {'type': 'DEVICE_CONNECTION_STATUS',
                      'isConnected': True,
                      'message': 'Device connected',
                      'deviceName': str(self.device.get_version()),
                      'portName': self.device.H.portname
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
            if self.device.H.portname not in self.device.H.listPorts():
                output = {'type': 'DEVICE_CONNECTION_STATUS',
                          'isConnected': False,
                          'message': 'Device disconnected'}
                print(json.dumps(output))
                sys.stdout.flush()
                self.disconnect()
            time.sleep(0.5)
