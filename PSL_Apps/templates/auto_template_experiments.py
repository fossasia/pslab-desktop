# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_experiments.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 565)
        MainWindow.setStyleSheet("QPushButton {\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.experimentFrameOuter = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentFrameOuter.sizePolicy().hasHeightForWidth())
        self.experimentFrameOuter.setSizePolicy(sizePolicy)
        self.experimentFrameOuter.setMinimumSize(QtCore.QSize(360, 0))
        self.experimentFrameOuter.setMaximumSize(QtCore.QSize(360, 16777215))
        self.experimentFrameOuter.setStyleSheet("")
        self.experimentFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experimentFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experimentFrameOuter.setObjectName("experimentFrameOuter")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.experimentFrameOuter)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.experimentFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.experimentFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet("")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.SCF1 = QtWidgets.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 356, 466))
        self.SCF1.setStyleSheet("")
        self.SCF1.setObjectName("SCF1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.SCF1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.SCF1)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ExperimentLayout = QtWidgets.QGridLayout()
        self.ExperimentLayout.setContentsMargins(5, 5, 5, 5)
        self.ExperimentLayout.setSpacing(7)
        self.ExperimentLayout.setObjectName("ExperimentLayout")
        self.gridLayout_7.addLayout(self.ExperimentLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.verticalLayout_5.addWidget(self.scrollArea_4)
        self.verticalLayout.addWidget(self.experimentFrameOuter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(360, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(360, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(94, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.deviceCombo = QtWidgets.QComboBox(self.frame_2)
        self.deviceCombo.setObjectName("deviceCombo")
        self.horizontalLayout.addWidget(self.deviceCombo)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.helpFrameOuter = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpFrameOuter.sizePolicy().hasHeightForWidth())
        self.helpFrameOuter.setSizePolicy(sizePolicy)
        self.helpFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpFrameOuter.setObjectName("helpFrameOuter")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.helpFrameOuter)
        self.verticalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.helpTitle = QtWidgets.QLabel(self.helpFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpTitle.sizePolicy().hasHeightForWidth())
        self.helpTitle.setSizePolicy(sizePolicy)
        self.helpTitle.setObjectName("helpTitle")
        self.verticalLayout_2.addWidget(self.helpTitle)
        self.helpLayout = QtWidgets.QVBoxLayout()
        self.helpLayout.setObjectName("helpLayout")
        self.verticalLayout_2.addLayout(self.helpLayout)
        self.horizontalLayout_2.addWidget(self.helpFrameOuter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 25))
        self.menubar.setObjectName("menubar")
        self.menuUtilities = QtWidgets.QMenu(self.menubar)
        self.menuUtilities.setObjectName("menuUtilities")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionIPython_Console = QtWidgets.QAction(MainWindow)
        self.actionIPython_Console.setObjectName("actionIPython_Console")
        self.actionIPython = QtWidgets.QAction(MainWindow)
        self.actionIPython.setObjectName("actionIPython")
        self.actionReset_Device = QtWidgets.QAction(MainWindow)
        self.actionReset_Device.setObjectName("actionReset_Device")
        self.menuUtilities.addAction(self.actionIPython_Console)
        self.menuUtilities.addAction(self.actionReset_Device)
        self.menuHelp.addAction(self.actionIPython)
        self.menubar.addAction(self.menuUtilities.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.selectDevice)
        self.actionIPython_Console.triggered.connect(MainWindow.addConsole)
        self.actionIPython.triggered.connect(MainWindow.ipythonHelp)
        self.actionReset_Device.triggered.connect(MainWindow.resetDevice)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSLab: Control Panel"))
        self.experimentFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.label_4.setText(_translate("MainWindow", "Experiments"))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.pushButton.setText(_translate("MainWindow", "SET"))
        self.helpFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.helpTitle.setText(_translate("MainWindow", "Experiment Details"))
        self.menuUtilities.setTitle(_translate("MainWindow", "Utilities"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionIPython_Console.setText(_translate("MainWindow", "iPython Console"))
        self.actionIPython.setText(_translate("MainWindow", "iPython Console"))
        self.actionReset_Device.setText(_translate("MainWindow", "Reset Device"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
