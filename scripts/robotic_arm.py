from PSL.digital_channel import DIGITAL_OUTPUTS
from PSL.motor import Servo


class RoboticArm:
    def __init__(self, device, file_write):
        self.servos = [Servo(pin, device.pwm_generator) for pin in DIGITAL_OUTPUTS]

    def setServo(self, a1, a2, a3, a4):
        for servo, angle in zip(self.servos, [a1, a2, a3, a4]):
            if angle is not None:
                servo.angle = angle
