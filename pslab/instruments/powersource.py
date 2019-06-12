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

from ..layouts.instrument_layouts import powersource_window


class Instrument(QWindow, powersource_window.Ui_powersource_window):

    def __init__(self, parent=None, **kwargs):
        super(Instrument, self).__init__(parent)
        self.setupUi(self)
        """  ###################################################################
        Window placement at the center of the screen
        """
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())
