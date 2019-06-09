import sys
from argparse import ArgumentParser

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

# PSLab library imports ########################################################
# from PSL import sciencelab as PSLab
# UI imports ###################################################################
from .layouts import main_window
from .resources.styles import splash_style

# Setting up PORT arguments ####################################################
# In case if a user wants to add multiple devices, connect using a port name
parser = ArgumentParser()
parser.add_argument("-P",
                    dest="PortName",
                    help="Provide port for multiple devices; e.g /dev/ttyACM0",
                    metavar="PORT_NAME")
args = parser.parse_args()


class PSLabDesktopApp(QWindow, main_window.Ui_pslab_main_window):

    def __init__(self, **kwargs):
        super(PSLabDesktopApp, self).__init__()
        """  ###################################################################
        Display splash screen to start configure libraries and PSLab device
        """  ###################################################################
        self.show_splash()
        self.update_splash(10, 'Setting up UI ...')  # 10
        """  ###################################################################
        Configure user interfaces and layouts related to notifications
        """  ###################################################################
        self.setupUi(self)
        self.statusLabel = QLabel()
        self.statusBar().addWidget(self.statusLabel)
        self.display_dialog(QMessage.Warning,
                            title="Connection Error",
                            message="Cannot find a PSLab device",
                            details="Software already running for ports",
                            information="We have detected a PSLab device")
        """  ###################################################################
        Run a timer to scan device connection and detection
        """  ###################################################################
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.locate_devices)
        self.timer.start(500)
        """  ###################################################################
        Window placement at the center of the screen
        """  ###################################################################
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())

    def maction_reconnect_device(self):
        pass

    def maction_test_device(self):
        pass

    def maction_about_device(self):
        pass

    def maction_pinlayout(self):
        pass

    def maction_datasheet(self):
        pass

    def maction_about_pslab(self):
        pass

    def locate_devices(self):
        pass

    def show_statusbar(self, statusMsg):
        """  ###################################################################
        Display status at the bottom of the window
        """  ###################################################################
        self.statusLabel.setText(statusMsg)

    def show_splash(self):
        """  ###################################################################
        Prepare and display a splash screen until initiation is complete
        """  ###################################################################
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
        self.splash.setStyleSheet(splash_style.style)
        self.splash.setMask(splash_pix.mask())
        self.splash.show()

    def update_splash(self, x, txt=''):
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
