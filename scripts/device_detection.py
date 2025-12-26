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
        # Debug: List all ports
        found_ports = list_ports.comports()
        sys.stderr.write(f"Scanning {len(found_ports)} ports:\n")
        pslab_port = None
        for p in found_ports:
            sys.stderr.write(f" - {p.device}: VID={p.vid}, PID={p.pid}\n")
            if p.vid == 0x04D8 and p.pid == 0x00DF:
                pslab_port = p.device

        # First connection attempt
        try:
            if pslab_port:
                sys.stderr.write(f"Attempting to connect to PSLab on {pslab_port}\n")
                self.device = ScienceLab(port=pslab_port)
            else:
                sys.stderr.write("PSLab not found in port scan, trying auto-detect\n")
                self.device = ScienceLab()
        except TypeError:
            sys.stderr.write("ScienceLab does not accept 'port' argument, falling back to auto-detect\n")
            self.device = ScienceLab()
        except Exception as e:
            sys.stderr.write(f"Error during connection: {e}\n")
            # Create a dummy device object if instantiation failed completely
            # so that self.device.connected check doesn't crash
            class DummyDevice:
                connected = False
            self.device = DummyDevice()

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
