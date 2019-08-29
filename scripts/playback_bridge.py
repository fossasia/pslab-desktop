import sys
import time
import json
from playback_robot import PlaybackRobot
from playback_la import LA

playbackRobot = PlaybackRobot()
la = LA()


def main():
    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']

        # # -------------------------- Script termination block ----------------------------
        if command == 'SAVE_CONFIG_ROB_ARM':
            output = {'type': 'FETCH_ROB_ARM'}
            print(json.dumps(output))
            sys.stdout.flush()

        if command == 'SAVE_DATA_LA':
            output = {'type': 'FETCH_LA'}
            print(json.dumps(output))
            sys.stdout.flush()

        if command == 'WRITE_ROB_ARM':
            servo1 = parsed_stream_data['servo1']
            servo2 = parsed_stream_data['servo2']
            servo3 = parsed_stream_data['servo3']
            servo4 = parsed_stream_data['servo4']
            data_path = parsed_stream_data['dataPath']
            playbackRobot.write(data_path, servo1, servo2, servo3, servo4)

        if command == 'WRITE_LA':
            la_1_voltage = parsed_stream_data['LA1Voltage']
            la_2_voltage = parsed_stream_data['LA2Voltage']
            la_3_voltage = parsed_stream_data['LA3Voltage']
            la_4_voltage = parsed_stream_data['LA4Voltage']
            la_1_time = parsed_stream_data['LA1Time']
            la_2_time = parsed_stream_data['LA2Time']
            la_3_time = parsed_stream_data['LA3Time']
            la_4_time = parsed_stream_data['LA4Time']
            number_of_channels = parsed_stream_data['numberOfChannels']
            data_path = parsed_stream_data['dataPath']
            la.write(data_path, number_of_channels, la_1_voltage, la_1_time,
                     la_2_voltage, la_2_time, la_3_voltage, la_3_time, la_4_voltage, la_4_time,)

        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
