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

            if inst_type == 'MUL_MET':
                data = str(kwargs['timestamp']) + ", " + str(kwargs['datetime']) + ", " + \
                    kwargs['data'] + ", " + str(kwargs['value']) + "\n"

            self.data_buffer.append(data)

    def start_recording(self, data_path, device_type):
        file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:000")
        self.file_pointed = open(data_path + '/' + file_name + '.csv', "w+")
        self.file_pointed.write("%s, %s \n\n" % (
            device_type, str(datetime.datetime.now())))
        if device_type == 'Oscilloscope':
            self.file_pointed.write(
                "Timestamp, DateTime, Channel, xData, yData, Timebase\n")
        if device_type == 'Multimeter':
            self.file_pointed.write(
                "Timestamp, DateTime, Data, Value\n")
        self.is_writing = True
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Data recording started', }))
        sys.stdout.flush()

    def save_config(self, data_path, device_type, **kwargs):
        file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:000")
        self.file_pointed = open(data_path + '/' + file_name + '.csv', "w+")
        self.file_pointed.write("%s, %s \n\n" % (
            device_type, str(datetime.datetime.now())))

        if device_type == 'WaveGenerator':
            buffer = []
            self.file_pointed.write(
                "Timestamp, DateTime, Wave, Digital, S1_Frequency, S1_Shape, S2_Frequency, S2_Phase, S2_Shape, PWM_Frequency, SQR1_Duty, SQR2_Phase, SQR2_Duty, SQR3_Phase, SQR3_Duty, SQR4_Phase, SQR4_Duty, \n")
            data = str(kwargs['timestamp']) + ", " + str(kwargs['datetime']) + ", " + \
                str(kwargs['wave']) + ", " + str(kwargs['digital']) + ", " + str(kwargs['s1_f']) + ", " + str(kwargs['s1_shape']) + ", " + \
                str(kwargs['s2_f']) + ", " + str(kwargs['s2_p']) + ", " + str(kwargs["s2_shape"]) + ", " + \
                str(kwargs['pwm_f']) + ", " + \
                str(kwargs['dc_1']) + ", " + \
                str(kwargs['p2']) + ", " + str(kwargs['dc_2']) + ", " + \
                str(kwargs['p3']) + ", " + str(kwargs['dc_3']) + ", " + \
                str(kwargs['p4']) + ", " + str(kwargs['dc_4']) + "\n"
            buffer.append(data)
            self.file_pointed.writelines(buffer)

        if device_type == 'PowerSource':
            buffer = []
            self.file_pointed.write(
                "Timestamp, DateTime, PCS, PV1, PV2, PV3 \n")
            data = str(kwargs['timestamp']) + ", " + str(kwargs['datetime']) + ", " + \
                str(kwargs['pcs']) + ", " + str(kwargs['pv1']) + ", " + \
                str(kwargs['pv2']) + ", " + str(kwargs['pv3']) + "\n"
            buffer.append(data)
            self.file_pointed.writelines(buffer)

        self.file_pointed.close()
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Config saved', }))
        sys.stdout.flush()

    def get_config_from_file(self, data_path, device_type):
        if device_type == 'WaveGenerator':
            f = open(data_path, "r")
            lines = f.readlines()
            data = lines[3].split(',')
            output = {'type': 'GET_CONFIG_WAV_GEN',
                      'wave': data[2],
                      'digital': data[3],
                      's1Frequency': data[4],
                      's2Frequency': data[5],
                      's2Phase': data[6],
                      'waveFormS1': data[7],
                      'waveFormS2': data[8],
                      'pwmFrequency': data[9],
                      'sqr1DutyCycle': data[10],
                      'sqr2DutyCycle': data[11],
                      'sqr2Phase': data[12],
                      'sqr3DutyCycle': data[13],
                      'sqr3Phase': data[14],
                      'sqr4DutyCycle': data[15],
                      'sqr4Phase': data[16],
                      }
        print(json.dumps(output))
        sys.stdout.flush()
        print(json.dumps(output))
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

    def get_config_from_file(self, data_path, device_type):
        if device_type == 'PowerSource':
            f = open(data_path, "r")
            lines = f.readlines()
            data = lines[3].split(',')
            output = {'type': 'GET_CONFIG_PWR_SRC',
                      'pcs': data[2],
                      'pv1': data[3],
                      'pv2': data[4],
                      'pv3': data[5]}
            print(json.dumps(output))
            sys.stdout.flush()
