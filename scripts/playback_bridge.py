import sys
import time
import json
from playback_robot import PlaybackRobot

playbackRobot = PlaybackRobot()


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

        if command == 'WRITE_ROB_ARM':
            servo1 = parsed_stream_data['servo1']
            servo2 = parsed_stream_data['servo2']
            servo3 = parsed_stream_data['servo3']
            servo4 = parsed_stream_data['servo4']
            data_path = parsed_stream_data['dataPath']
            playbackRobot.write(data_path, servo1, servo2, servo3, servo4)

        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
