# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_experiments.ui'


from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(995, 565)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"QFrame.PeripheralCollection{\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #6af, stop: 0.1 #689);\n"
"}\n"
"QFrame.PeripheralCollection QLabel {\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner QLabel{\n"
"color: black;\n"
"}\n"
"\n"
"QWidget.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"QWidget.PeripheralCollectionInner QLabel{\n"
"color: black;\n"
"}\n"
"\n"
"#SCF2,#SCF1\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.experimentFrameOuter = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentFrameOuter.sizePolicy().hasHeightForWidth())
        self.experimentFrameOuter.setSizePolicy(sizePolicy)
        self.experimentFrameOuter.setMinimumSize(QtCore.QSize(360, 0))
        self.experimentFrameOuter.setMaximumSize(QtCore.QSize(360, 16777215))
        self.experimentFrameOuter.setStyleSheet(_fromUtf8(""))
        self.experimentFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.experimentFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.experimentFrameOuter.setObjectName(_fromUtf8("experimentFrameOuter"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.experimentFrameOuter)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.experimentFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.scrollArea_4 = QtGui.QScrollArea(self.experimentFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet(_fromUtf8(""))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.SCF1 = QtGui.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 356, 466))
        self.SCF1.setStyleSheet(_fromUtf8(""))
        self.SCF1.setObjectName(_fromUtf8("SCF1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.SCF1)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_5 = QtGui.QFrame(self.SCF1)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ExperimentLayout = QtGui.QGridLayout()
        self.ExperimentLayout.setMargin(5)
        self.ExperimentLayout.setSpacing(7)
        self.ExperimentLayout.setObjectName(_fromUtf8("ExperimentLayout"))
        self.gridLayout_7.addLayout(self.ExperimentLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.verticalLayout_5.addWidget(self.scrollArea_4)
        self.verticalLayout.addWidget(self.experimentFrameOuter)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(360, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(360, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(94, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.deviceCombo = QtGui.QComboBox(self.frame_2)
        self.deviceCombo.setObjectName(_fromUtf8("deviceCombo"))
        self.horizontalLayout.addWidget(self.deviceCombo)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.helpFrameOuter = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpFrameOuter.sizePolicy().hasHeightForWidth())
        self.helpFrameOuter.setSizePolicy(sizePolicy)
        self.helpFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.helpFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.helpFrameOuter.setObjectName(_fromUtf8("helpFrameOuter"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.helpFrameOuter)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.helpTitle = QtGui.QLabel(self.helpFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpTitle.sizePolicy().hasHeightForWidth())
        self.helpTitle.setSizePolicy(sizePolicy)
        self.helpTitle.setObjectName(_fromUtf8("helpTitle"))
        self.verticalLayout_2.addWidget(self.helpTitle)
        self.helpLayout = QtGui.QVBoxLayout()
        self.helpLayout.setObjectName(_fromUtf8("helpLayout"))
        self.verticalLayout_2.addLayout(self.helpLayout)
        self.horizontalLayout_2.addWidget(self.helpFrameOuter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUtilities = QtGui.QMenu(self.menubar)
        self.menuUtilities.setObjectName(_fromUtf8("menuUtilities"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionIPython_Console = QtGui.QAction(MainWindow)
        self.actionIPython_Console.setObjectName(_fromUtf8("actionIPython_Console"))
        self.actionIPython = QtGui.QAction(MainWindow)
        self.actionIPython.setObjectName(_fromUtf8("actionIPython"))
        self.actionReset_Device = QtGui.QAction(MainWindow)
        self.actionReset_Device.setObjectName(_fromUtf8("actionReset_Device"))
        self.menuUtilities.addAction(self.actionIPython_Console)
        self.menuUtilities.addAction(self.actionReset_Device)
        self.menuHelp.addAction(self.actionIPython)
        self.menubar.addAction(self.menuUtilities.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.selectDevice)
        QtCore.QObject.connect(self.actionIPython_Console, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.addConsole)
        QtCore.QObject.connect(self.actionIPython, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.ipythonHelp)
        QtCore.QObject.connect(self.actionReset_Device, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.resetDevice)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SEELablet: Control Panel", None))
        self.experimentFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_4.setText(_translate("MainWindow", "Experiments", None))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.pushButton.setText(_translate("MainWindow", "SET", None))
        self.helpFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.helpTitle.setText(_translate("MainWindow", "Experiment Details", None))
        self.menuUtilities.setTitle(_translate("MainWindow", "Utilities", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionIPython_Console.setText(_translate("MainWindow", "iPython Console", None))
        self.actionIPython.setText(_translate("MainWindow", "iPython Console", None))
        self.actionReset_Device.setText(_translate("MainWindow", "Reset Device", None))

