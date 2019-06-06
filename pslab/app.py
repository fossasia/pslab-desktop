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

        # Display splash screen to start configure libraries and PSLab device
        self.showSplash()
        self.updateSplash(10, 'Setting up UI ...')  # 10

        self.setupUi(self)
        self.statusLabel = QLabel()
        self.statusBar().addWidget(self.statusLabel)

        self.display_dialog(QMessage.Warning,
                            title="Connection Error",
                            message="Cannot find a PSLab device",
                            details="Software already running for ports",
                            information= "We have detected a PSLab device")
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

    def showStatusBar(self, statusMsg):
        """  ###################################################################
        Display status at the bottom of the window
        """  ###################################################################
        self.statusLabel.setText(statusMsg)

    def showSplash(self):
        """  ###########################################################################################################
        Prepare and display a splash screen until initiation is complete
        """  ###########################################################################################################
        splash_pix = QtGui.QPixmap(":/pslab/splash/splash.png")
        self.splash = QSplash(splash_pix)
        # Create a progress bar at the bottom of Splash screen
        self.progressBar = QProgress(self.splash)
        self.progressBar.move(0, self.splash.height() - 20)
        self.splashMsg = QLabel(self.splash)
        self.splashMsg.setStyleSheet("font-weight:bold; color:white")
        self.progressBar.resize(self.splash.width(), 20)
        self.splashMsg.setText('Starting PSLab Desktop App ...')
        self.splashMsg.resize(self.progressBar.width(), 20)
        self.splashMsg.move(0, self.splash.height() - 20)
        css = pkg_resources.resource_string('PSL_Apps', "stylesheets/splash.css").decode("utf-8")
        if css:
            self.splash.setStyleSheet(css)
        self.splash.setMask(splash_pix.mask())
        self.splash.show()

    def updateSplash(self, x, txt=''):
        """  ###################################################################
        Update the progress and text in splash window
        """  ###################################################################
        self.progressBar.setValue(self.progressBar.value() + x)
        if (len(txt)): self.splashMsg.setText('  ' + txt)
        self.splash.repaint()

    def display_dialog(self, icon, title, message, details="", information=""):
        dialog = QMessage()
        dialog.setIcon(icon)
        dialog.setWindowTitle(title)
        dialog.setText(message)
        if len(information) > 0: dialog.setInformativeText(information)
        if len(details) > 0: dialog.setDetailedText(details)
        dialog.exec_()
        return dialog

def start_pslab_app():
    app = QApp(sys.argv)
    myapp = PSLabDesktopApp()
    myapp.show()
    myapp.splash.finish(myapp)
    app.exec_()
