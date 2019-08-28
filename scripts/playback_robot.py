import time
import datetime
import sys
import json


class PlaybackRobot:
    def write(self, data_path, servo1, servo2, servo3, servo4):
        file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:000")
        file_pointed = open(data_path + '/' + file_name + '.csv', "w+")
        file_pointed.write("%s, %s \n\n" % (
            'RobotArm', str(datetime.datetime.now())))
        file_pointed.write(
            "Time, Servo1, Servo2, Servo3, Servo4, Latitude, Longitude\n")
        for i in range(len(servo1)):
            file_pointed.write(
                "%s, %s, %s, %s, %s\n" % (
                    str(i + 1), str(servo1[i]), str(servo2[i]), str(servo3[i]), str(servo4[i])))
        file_pointed.close()
        print(json.dumps({'type': 'DATA_WRITING_STATUS',
                          'message': 'Config saved', }))
        sys.stdout.flush()
