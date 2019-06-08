import functools
import importlib
import inspect
import os
import pkgutil
import sys
from argparse import ArgumentParser

import pkg_resources
# PSLab library imports ########################################################
from PSL import sciencelab
# UI imports ###################################################################
from .layouts import main_window
# PyQt5 imports ################################################################
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication as QApp
from PyQt5.QtWidgets import QDesktopWidget as QDesktop
from PyQt5.QtWidgets import QFileDialog as QFileDialog
from PyQt5.QtWidgets import QFrame as QFrame
from PyQt5.QtWidgets import QLabel as QLabel
from PyQt5.QtWidgets import QMainWindow as QWindow
from PyQt5.QtWidgets import QMessageBox as QMessage
from PyQt5.QtWidgets import QProgressBar as QProgress
from PyQt5.QtWidgets import QSplashScreen as QSplash

class PSLabDesktopApp(QWindow, main_window.Ui_pslab_main_window):

    def __init__(self, **kwargs):
        super(PSLabDesktopApp, self).__init__()
        self.setupUi(self)
        """  ###################################################################
                Window placement at the center of the screen
        """  ###################################################################
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())

    def maction_reconnect_device(self):
        print("Reconnecting")

    def maction_test_device(self):
        print("Testing")

    def maction_about_device(self):
        print("About Device")

    def maction_pinlayout(self):
        print("Pin Layout")

    def maction_datasheet(self):
        print("Datasheet")


def start_pslab_app():
    app = QApp(sys.argv)
    myapp = PSLabDesktopApp()
    myapp.show()
    app.exec_()