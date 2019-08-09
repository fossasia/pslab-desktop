import sys
import threading


class MulmetPlayback:
    def __init__(self):
        self.buffer = None
        self.isReading = False
        self.playback_thread = None
        self.index = 0

    def read_data_from_file(self, data_path):
        print('Reading files')
        sys.stdout.flush()

    def start_playback(self):
        self.playback_thread = threading.Thread(
            target=self.read_loop,
            name='mulmet_playback')

    def stop_playback(self):
        self.isReading = False
        # join here
        self.read_loop = None
        print('Stoping playback')
        sys.stdout.flush()

    def read_loop(self):
        # Also add index conditoin
        while self.isReading:
            # Read data and print
            print('reading data - line')
            sys.stdout.flush()
