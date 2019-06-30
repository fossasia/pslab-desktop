import time
import datetime
import sys
import json


class FileWrite:
    def __init__(self):
        self.is_writing = False
        self.data_path = None
        self.device_type = None
        self.file_pointed = None
        self.data_buffer = []

    def update_buffer(self, inst_type, **kwargs):
        if self.is_writing:
            data = None
            if inst_type == 'OSC':
                xData = ' '.join(map(str, kwargs['xData'].tolist()))
                yData = ' '.join(map(str, kwargs['yData'].tolist()))
                data = str(kwargs['timestamp']) + ", " + str(kwargs['datetime']) + ", " + \
                    kwargs['channel'] + ", " + xData + ", " + \
                    yData + ", " + str(kwargs['timebase']) + "\n"

            self.data_buffer.append(data)

    def start_recording(self, data_path, device_type):
        file_name = str(int(time.time()))
        self.file_pointed = open(data_path + '/' + file_name + '.csv', "w+")
        self.file_pointed.write("%s, %s \n\n" % (
            device_type, str(datetime.datetime.now())))
        if device_type == 'Oscilloscope':
            self.file_pointed.write(
                "Timestamp, DateTime, Channel, xData, yData, Timebase\n")
        self.is_writing = True
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Data recording started', }))
        sys.stdout.flush()

    def stop_recording(self):
        if len(self.data_buffer) != 0:
            self.file_pointed.writelines(self.data_buffer)
            self.data_buffer = None
        self.file_pointed.close()
        self.is_writing = False
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Data recording stopped', }))
        sys.stdout.flush()
