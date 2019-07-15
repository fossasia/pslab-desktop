class RoboticArm:
    def __init__(self, I, file_write):
        self.device = I

    def setServo(self, a1, a2, a3, a4):
        self.device.servo4(a1, a2, a3, a4)
