import sys
import time
import json


def main():
    print('script started')
    sys.stdout.flush()
    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']

        # # -------------------------- Script termination block ----------------------------
        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
    print("app exited successfully")
    sys.stdout.flush()
