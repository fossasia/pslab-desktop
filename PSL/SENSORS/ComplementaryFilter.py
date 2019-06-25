import numpy as np


class ComplementaryFilter:
    def __init__(self, ):
        self.pitch = 0
        self.roll = 0
        self.dt = 0.001

    def addData(self, accData, gyrData):
        self.pitch += (gyrData[0]) * self.dt  # Angle around the X-axis
        self.roll -= (gyrData[1]) * self.dt  # Angle around the Y-axis
        forceMagnitudeApprox = abs(accData[0]) + abs(accData[1]) + abs(accData[2]);
        pitchAcc = np.arctan2(accData[1], accData[2]) * 180 / np.pi
        self.pitch = self.pitch * 0.98 + pitchAcc * 0.02
        rollAcc = np.arctan2(accData[0], accData[2]) * 180 / np.pi
        self.roll = self.roll * 0.98 + rollAcc * 0.02

    def getData(self):
        return self.roll, self.pitch
