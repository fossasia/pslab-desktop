# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensorGrid.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 594)
        MainWindow.setMinimumSize(QtCore.QSize(370, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SCF2 = QtWidgets.QWidget(MainWindow)
        self.SCF2.setStyleSheet("")
        self.SCF2.setObjectName("SCF2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SCF2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.SCF2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_4.setStyleSheet("")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.SCF1 = QtWidgets.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 699, 555))
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
        self.gridLayout_7.addLayout(self.ExperimentLayout, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.verticalLayout.addWidget(self.scrollArea_4)
        self.pushButton = QtWidgets.QPushButton(self.SCF2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.SCF2)
        self.actionIPython_Console = QtWidgets.QAction(MainWindow)
        self.actionIPython_Console.setObjectName("actionIPython_Console")
        self.actionIPython = QtWidgets.QAction(MainWindow)
        self.actionIPython.setObjectName("actionIPython")
        self.actionReset_Device = QtWidgets.QAction(MainWindow)
        self.actionReset_Device.setObjectName("actionReset_Device")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.autoScan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SEELablet:Sensors Control Panel"))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.frame_5.setToolTip(_translate("MainWindow", "Widgets specific to detected sensors will be displayed\n"
"                                                here after you click the button below\n"
"                                            "))
        self.pushButton.setToolTip(_translate("MainWindow", "Scan the I2C BUS for sensors\n"
"                                and generate widgets\n"
"                            "))
        self.pushButton.setText(_translate("MainWindow", "Auto Scan"))
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
