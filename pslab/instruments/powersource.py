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

from layouts.instrument_layouts import powersource_window


class Instrument(QWindow, powersource_window.Ui_powersource_window):

    def __init__(self, parent=None, **kwargs):
        super(Instrument, self).__init__(parent)
        self.setupUi(self)
        """  ###################################################################
        Define user set power values
        """
        self.MIN_PV1 = -5.0
        self.MAX_PV1 = 5.0
        self.RES_PV1 = 1000
        self.MIN_PV2 = -3.3
        self.MAX_PV2 = 3.3
        self.RES_PV2 = 660
        self.MIN_PV3 = 0.0
        self.MAX_PV3 = 3.3
        self.RES_PV3 = 330
        self.MIN_PCS = 0
        self.MAX_PCS = 30
        self.RES_PCS = 30
        self.pv1_value = 0.0
        self.pv2_value = 0.0
        self.pv3_value = 0.0
        self.pcs_value = 0
        """  ###################################################################
        Window placement at the center of the screen
        """
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        windowCenterPoint.setX(windowCenterPoint.x() -
                               frameDimensions.width() - 9)
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())

    def map_power_to_sliders(self, min_value, max_value, min_ref, max_ref, value):
        print(min_value, max_value, min_ref, max_ref, value)
        if (max_value == value):
            return max_ref
        A = min_ref
        B = (max_ref * ((value - min_value) / (max_value - value)))
        C = (1 + ((value - min_value) / (max_value - value)))
        return round((A + B) / C, 2)

    def power_dial_changed(self, value):
        dial = self.sender().objectName()
        if (dial == "dial_pv1"):
            v = self.map_power_to_sliders(
                0, self.RES_PV1, self.MIN_PV1, self.MAX_PV1, value)
            self.pv1_value = v
            self.spinner_pv1.setValue(v)
            self.slider_pv1.setValue(value)
        elif (dial == "dial_pv2"):
            v = self.map_power_to_sliders(
                0, self.RES_PV2, self.MIN_PV2, self.MAX_PV2, value)
            self.pv2_value = v
            self.spinner_pv2.setValue(v)
            self.slider_pv2.setValue(value)
        elif (dial == "dial_pv3"):
            v = self.map_power_to_sliders(
                0, self.RES_PV3, self.MIN_PV3, self.MAX_PV3, value)
            self.pv3_value = v
            self.spinner_pv3.setValue(v)
            self.slider_pv3.setValue(value)
        elif (dial == "dial_pcs"):
            v = self.map_power_to_sliders(
                0, self.RES_PCS, self.MIN_PCS, self.MAX_PCS, value)
            self.pcs_value = v
            self.spinner_pcs.setValue(v)
            self.slider_pcs.setValue(value)

    def power_slider_changed(self, value):
        slider = self.sender().objectName()
        if (slider == "slider_pv1"):
            v = self.map_power_to_sliders(
                0, self.RES_PV1, self.MIN_PV1, self.MAX_PV1, value)
            self.pv1_value = v
            self.spinner_pv1.setValue(v)
            self.dial_pv1.setValue(value)
        elif (slider == "slider_pv2"):
            v = self.map_power_to_sliders(
                0, self.RES_PV2, self.MIN_PV2, self.MAX_PV2, value)
            self.pv2_value = v
            self.spinner_pv2.setValue(v)
            self.dial_pv2.setValue(value)
        elif (slider == "slider_pv3"):
            v = self.map_power_to_sliders(
                0, self.RES_PV3, self.MIN_PV3, self.MAX_PV3, value)
            self.pv3_value = v
            self.spinner_pv3.setValue(v)
            self.dial_pv3.setValue(value)
        elif (slider == "slider_pcs"):
            v = self.map_power_to_sliders(
                0, self.RES_PCS, self.MIN_PCS, self.MAX_PCS, value)
            self.pcs_value = v
            self.spinner_pcs.setValue(v)
            self.dial_pcs.setValue(value)

    def power_spinner_changed(self, value):
        spinner = self.sender().objectName()
        if (spinner == "spinner_pv1"):
            if type(value) is str:
                value = value[:-2]
            self.pv1_value = round(float(value), 2)
            v = self.map_power_to_sliders(
                self.MIN_PV1, self.MAX_PV1, 0, self.RES_PV1, self.pv1_value)
            self.dial_pv1.setValue(v)
            self.slider_pv1.setValue(v)
        elif (spinner == "spinner_pv2"):
            if type(value) is str:
                value = value[:-2]
            self.pv2_value = round(float(value), 2)
            v = self.map_power_to_sliders(
                self.MIN_PV2, self.MAX_PV2, 0, self.RES_PV2, self.pv2_value)
            self.dial_pv2.setValue(v)
            self.slider_pv2.setValue(v)
        elif (spinner == "spinner_pv3"):
            if type(value) is str:
                value = value[:-2]
            self.pv3_value = round(float(value), 2)
            v = self.map_power_to_sliders(
                self.MIN_PV3, self.MAX_PV3, 0, self.RES_PV3, self.pv3_value)
            self.dial_pv3.setValue(v)
            self.slider_pv3.setValue(v)
        elif (spinner == "spinner_pcs"):
            if type(value) is str:
                value = value[:-3]
            self.pcs_value = int(value)
            v = self.map_power_to_sliders(
                self.MIN_PCS, self.MAX_PCS, 0, self.RES_PCS, self.pcs_value)
            self.dial_pcs.setValue(v)
            self.slider_pcs.setValue(v)
