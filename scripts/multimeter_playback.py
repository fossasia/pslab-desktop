class MulmetPlayback:
    def __init__(self):
        self.f = None
        self.data = None

    def read(self, data_path):
        self.f = open(data_path, "r")
        lines = self.f.readlines()
        data = lines[3:]

    def start(self):
        pass

    def stop(self):
        pass