import sys
from math import log
# PyQt5 imports ################################################################
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication as QApp
from PyQt5.QtWidgets import QDesktopWidget as QDesktop
from PyQt5.QtWidgets import QLabel as QLabel
from PyQt5.QtWidgets import QMainWindow as QWindow
from PyQt5.QtWidgets import QMessageBox as QMessage
from PyQt5.QtWidgets import QProgressBar as QProgress
from PyQt5.QtWidgets import QSplashScreen as QSplash

from layouts.instrument_layouts import multimeter_window


class Instrument(QWindow, multimeter_window.Ui_multimeter_window):

    def __init__(self, parent=None, **kwargs):
        super(Instrument, self).__init__(parent)
        self.setupUi(self)
        self.lcd_multimeter.display("0.00")
        """  ###################################################################
        Window placement at the center of the screen
        """
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())

    def update_refrest_rate(self, value):
        self.update_interval = round((1 / 50) * (value + 1), 2)
        self.label_update_interval.setText(
            'Every ' +
            str("{0:.2f}".format(self.update_interval)) + '\nseconds')

    def read_knob(self, value):
        if (value == 1):
            self.measure_voltage("CH1")
        elif (value == 2):
            self.measure_voltage("CH2")
        elif (value == 3):
            self.measure_voltage("CH3")
        elif (value == 4):
            self.measure_voltage("VOL")
        elif (value == 5):
            self.measure_resistance()
        elif (value == 6):
            self.measure_capacitance()
        elif (value == 7):
            self.count_pulses("LA1")
        elif (value == 8):
            self.count_pulses("LA2")
        elif (value == 9):
            self.count_pulses("LA3")
        elif (value == 10):
            self.count_pulses("LA4")
        else:
            self.label_unit_display.setText("")

    def measure_voltage(self, pin):
        self.label_unit_display.setText("V")
        if (pin == "CH1"):
            print("CH1")
        elif (pin == "CH2"):
            print("CH2")
        elif (pin == "CH3"):
            print("CH3")
        elif (pin == "VOL"):
            print("VOL")

    def measure_resistance(self):
        self.label_unit_display.setText("Ω")
        print("Ω")

    def measure_capacitance(self):
        self.label_unit_display.setText("pF")
        print("pF")

    def count_pulses(self, pin):
        self.label_unit_display.setText("pulses")
        if (pin == "LA1"):
            print("LA1")
        elif (pin == "LA2"):
            print("LA2")
        elif (pin == "LA3"):
            print("LA3")
        elif (pin == "LA4"):
            print("LA4")
