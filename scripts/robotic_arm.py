class RoboticArm:
    def __init__(self, I, file_write):
        self.prev_angle = [0, 0, 0, 0]
        self.device = I

    def setServo(self, a1, a2, a3, a4):
        if a1 is None:
            a1 = self.prev_angle[0]
        else:
            self.prev_angle[0] = a1

        if a2 is None:
            a2 = self.prev_angle[1]
        else:
            self.prev_angle[1] = a2

        if a3 is None:
            a3 = self.prev_angle[2]
        else:
            self.prev_angle[2] = a3

        if a4 is None:
            a4 = self.prev_angle[3]
        else:
            self.prev_angle[3] = a4
        self.device.servo4(a1, a2, a3, a4)
