import time
import datetime
import sys
import json


class LA:
    def write(self, data_path, number_of_channels, la_1_voltage, la_1_time,
              la_2_voltage, la_2_time, la_3_voltage, la_3_time, la_4_voltage, la_4_time):
        file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:000")
        file_pointed = open(data_path + '/' + file_name + '.csv', "w+")
        file_pointed.write("%s, %s \n\n" % (
            'LogicAnalyzer', str(datetime.datetime.now())))
        file_pointed.write(
            "Number of Channels, Voltage 1, Time 1, Voltage 2, Time 2, Voltage 3, Time 3, Voltage 4, Time 4\n")
        file_pointed.write(
            "%s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (
                str(number_of_channels),
                ' '.join(map(str, la_1_voltage)), ' '.join(
                    map(str, la_1_time)),
                ' '.join(map(str, la_2_voltage)), ' '.join(
                    map(str, la_2_time)),
                ' '.join(map(str, la_3_voltage)), ' '.join(
                    map(str, la_3_time)),
                ' '.join(map(str, la_4_voltage)), ' '.join(map(str, la_4_time)),))
        file_pointed.close()
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Data saved', }))
        sys.stdout.flush()
