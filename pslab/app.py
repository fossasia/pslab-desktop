import sys
from argparse import ArgumentParser

# PyQt5 imports ###############################################################
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication as QApp
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDesktopWidget as QDesktop
from PyQt5.QtWidgets import QLabel as QLabel
from PyQt5.QtWidgets import QMainWindow as QWindow
from PyQt5.QtWidgets import QMessageBox as QMessage
from PyQt5.QtWidgets import QProgressBar as QProgress
from PyQt5.QtWidgets import QSplashScreen as QSplash

# PSLab library imports #######################################################
from PSL import sciencelab as PSLab
# UI imports ##################################################################
from layouts import main_window
from instruments import multimeter
from instruments import powersource
from tools.buttons import hover_button
from resources.styles import splash_style
from resources.styles import app_style

# Setting up PORT arguments ###################################################
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
        """  ##################################################################
        Display splash screen to start configure libraries and PSLab device
        """
        self.show_splash()
        self.update_splash(10, 'Setting up UI ...')  # 10
        """  ##################################################################
        Configure user interfaces and layouts related to notifications
        """
        self.setupUi(self)
        self.statusLabel = QLabel()
        self.statusBar().addWidget(self.statusLabel)
        self.update_splash(20, 'Searching for devices ...')  # 30
        self.portList = []
        if args.PortName:
            self.I = PSLab.ScienceLab(port=args.PortName)
        else:
            self.I = PSLab.ScienceLab(verbose=False)
        try:
            if not self.I.connected:
                # Display an error dialog with the probable cause
                if len(self.I.H.occupiedPorts):
                    self.display_dialog(QMessage.Warning,
                                        title="Connection Error",
                                        message="Cannot find a PSLab device",
                                        details="Software already running" +
                                        "for ports: %s"
                                        % list(self.I.H.occupiedPorts),
                                        information="PSLab device detected")
                else:
                    self.display_dialog(QMessage.Warning,
                                        title="Connection Error",
                                        message="Cannot find a PSLab device",
                                        details="Make sure PSLab device is " +
                                        "connected and status LEDs are ON")

                # Make the window looks reddish to indicate error
                self.show_statusbar('Error: PSLab device not connected')
            else:
                # Display device ID at the status bar
                self.show_statusbar(self.I.generic_name +
                                    ': ' + hex(self.I.device_id() & 0xFFFF))
        except:
            self.update_splash(30, 'Connection Error ...')  # 60
        self.setup_instrument_buttons()
        """  ##################################################################
        Run a timer to scan device connection and detection
        """
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.discover_devices)
        self.timer.start(500)
        """  ##################################################################
        Window placement at the center of the screen
        """
        frameDimensions = self.frameGeometry()
        windowCenterPoint = QDesktop().availableGeometry().center()
        frameDimensions.moveCenter(windowCenterPoint)
        self.move(frameDimensions.topLeft())

    def set_inactive_window_mode(self):
        """  ##################################################################
        Make the window look reddish to warn user about device disconnection
        """
        self.app_window.setStyleSheet(app_style.inactive_window)
        self.pslab_main_menu.setStyleSheet(app_style.inactive_menu)
        self.pslab_status_bar.setStyleSheet(app_style.inactive_statusbar)

    def setup_instrument_buttons(self):
        """  ##################################################################
        Populate instrument buttons with specific details to them
        """
        self.button_oscilloscope = hover_button.Button(
            name="Oscilloscope", shortcut="Ctrl+Shift+O",
            details="This is oscilloscope", obj="button_oscilloscope",
            connect=self.baction_open_instrument,
            hintfn=self.display_instrument_details)
        self.grid_instruments.addWidget(self.button_oscilloscope, 0, 0)
        self.button_logic_analyzer = hover_button.Button(
            name="Logic Analyzer", shortcut="Ctrl+Shift+L",
            details="This is logic analyzer", obj="button_logic_analyzer",
            connect=self.baction_open_instrument,
            hintfn=self.display_instrument_details)
        self.grid_instruments.addWidget(self.button_logic_analyzer, 1, 0)
        self.button_multimeter = hover_button.Button(
            name="Multimeter", shortcut="Ctrl+Shift+M",
            details="This is Multimeter", obj="button_oscilloscope",
            connect=self.baction_open_instrument,
            hintfn=self.display_instrument_details)
        self.grid_instruments.addWidget(self.button_multimeter, 2, 0)
        self.button_waveform_generator = hover_button.Button(
            name="Waveform Generator", shortcut="Ctrl+Shift+W",
            details="This is Wave generator", obj="button_waveform_generator",
            connect=self.baction_open_instrument,
            hintfn=self.display_instrument_details)
        self.grid_instruments.addWidget(self.button_waveform_generator, 3, 0)
        self.button_power_source = hover_button.Button(
            name="Power Source", shortcut="Ctrl+Shift+P",
            details="This is Power Source", obj="button_power_source",
            connect=self.baction_open_instrument,
            hintfn=self.display_instrument_details)
        self.grid_instruments.addWidget(self.button_power_source, 4, 0)

    def display_instrument_details(self, hint):
        """  ##################################################################
        Displays a summary about the instrument
        """
        self.text_instrument_details.setHtml(hint)

    def baction_open_instrument(self):
        """  ##################################################################
        Run a timer to scan device connection and detection
        """
        buttonName = self.sender().text()
        if (buttonName == "Oscilloscope"):
            pass
        elif (buttonName == "Logic Analyzer"):
            pass
        elif (buttonName == "Multimeter"):
            multimeter.Instrument(self).show()
            self.app_tabs.setCurrentIndex(1)
        elif (buttonName == "Waveform Generator"):
            pass
        elif (buttonName == "Power Source"):
            powersource.Instrument(self).show()
            self.app_tabs.setCurrentIndex(1)

    def maction_reconnect_device(self):
        """  ##################################################################
        Disconnects and reconnects the device
        """
        if self.I:
            if self.I.connected:
                self.I.resetHardware()
                self.I.H.fd.close()
                self.I.reconnect()

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

    def maction_experiments(self):
        menu = self.sender().text()
        if (menu == "Sensors..."):
            self.app_tabs.setCurrentIndex(2)
        elif (menu == ""):
            pass

    def discover_devices(self):
        """  ##################################################################
        This method will be called periodically to detect if a new device is 
        connected. It will detect a new connection by comparing number of USB 
        devices connected with the locally saved device connection list
        """
        # List of /dev/ttyACM or /dev/ttyUSB ports
        ports = self.I.H.listPorts()
        differentPorts = False
        # Port list changes for new connections as well as disconnections
        if ports != self.portList:
            differentPorts = True
            self.portList = ports

        # Check for, and handle disconnect event
        if differentPorts:
            # If there was a device connected already, check if it's there
            if self.I.connected:
                # Device is missing. Update status for a disconnected device
                if self.I.H.portname not in self.portList:
                    self.show_statusbar('Error: PSLab device not connected')
                    # If there are any open windows, close them
                    if self.runningApp:
                        self.runningApp.close()
                    self.I.connected = False
            # Try connect to an available port
            elif self.portList:
                if QMessage.question(self,
                                     'Connection', 'Device Found. Connect?',
                                     QtGui.QMessageBox.No,
                                     QtGui.QMessageBox.Yes) == QMessage.Yes:
                    self.selectDevice()

    def selectDevice(self):
        """  ##################################################################
        Connect to device
        """
        self.splash.show()
        port = self.portList[0]
        self.progressBar.setValue(0)
        self.update_splash(20, 'Reconnecting to %s' % (port))
        if self.I:
            try:
                self.I.reconnect(port=port)
            except Exception as e:
                self.updateSplash(30, 'Connection Error!')

            if not self.I.connected:
                if len(self.I.H.occupiedPorts):
                    diag = QtGui.QMessageBox.warn(self, 'Error', 'Could not ' +
                                                  'find available device.\n' +
                                                  'Software already running ' +
                                                  'for ports: %s' % list(
                                                      self.I.H.occupiedPorts))
                else:
                    diag = QtGui.QMessageBox.warn(
                        self, 'Error', 'Could not find available device')
                self.show_statusbar('')
            else:
                self.update_splash(20, 'Reconnected ...')
                self.display_dialog(QMessage.Information, 'Device Found',
                                    'Reconnected to ' +
                                    self.I.H.version_string[1:-1], '')
                self.show_statusbar(self.I.generic_name +
                                    ': ' + hex(self.I.device_id() & 0xFFFF))
        self.splash.close()

    def show_statusbar(self, statusMsg):
        """  ##################################################################
        Display status at the bottom of the window
        """
        self.statusLabel.setText(statusMsg)

    def show_splash(self):
        """  ##################################################################
        Prepare and display a splash screen until initiation is complete
        """
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
        """  ##################################################################
        Update the progress and text in splash window
        """
        self.progressBar.setValue(self.progressBar.value() + x)
        if (len(txt)):
            self.splashMsg.setText('  ' + txt)
        self.splash.repaint()

    def display_dialog(self, icon, title, message, details="", information=""):
        dialog = QMessage()
        dialog.setIcon(icon)
        dialog.setWindowTitle(title)
        dialog.setText(message)
        if len(information) > 0:
            dialog.setInformativeText(information)
        if len(details) > 0:
            dialog.setDetailedText(details)
        dialog.exec_()
        return dialog

    def __del__(self):
        """  ##################################################################
        This will be called once the app is being closed. It will close PSLab 
        connections to clean the system
        """
        pass


def start_pslab_app():
    app = QApp(sys.argv)
    myapp = PSLabDesktopApp()
    myapp.show()
    myapp.splash.finish(myapp)
    app.exec_()


if __name__ == '__main__':
    start_pslab_app()
