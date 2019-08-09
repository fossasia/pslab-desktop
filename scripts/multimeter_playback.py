import sys


class MulmetPlayback:
    def __init__(self):
        self.buffer = None

    def read_data_from_file(self, data_path):
        print('Reading files')
        sys.stdout.flush()

    def start_playback(self):
        print('starting playback')
        sys.stdout.flush()

    def stop_playback(self):
        print('Stoping playback')
        sys.stdout.flush()
