# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psl_res/GUI/A_TEST_AND_MEASUREMENT/A_TandM/templates/sensorGrid.ui'
#
# Created: Sun Aug 21 23:13:15 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(701, 594)
        MainWindow.setMinimumSize(QtCore.QSize(370, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SCF2 = QtGui.QWidget(MainWindow)
        self.SCF2.setStyleSheet(_fromUtf8(""))
        self.SCF2.setObjectName(_fromUtf8("SCF2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.SCF2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_4 = QtGui.QScrollArea(self.SCF2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_4.setStyleSheet(_fromUtf8(""))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.SCF1 = QtGui.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 699, 555))
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
        self.gridLayout_7.addLayout(self.ExperimentLayout, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.verticalLayout.addWidget(self.scrollArea_4)
        self.pushButton = QtGui.QPushButton(self.SCF2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.SCF2)
        self.actionIPython_Console = QtGui.QAction(MainWindow)
        self.actionIPython_Console.setObjectName(_fromUtf8("actionIPython_Console"))
        self.actionIPython = QtGui.QAction(MainWindow)
        self.actionIPython.setObjectName(_fromUtf8("actionIPython"))
        self.actionReset_Device = QtGui.QAction(MainWindow)
        self.actionReset_Device.setObjectName(_fromUtf8("actionReset_Device"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.autoScan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SEELablet:Sensors Control Panel", None))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.frame_5.setToolTip(_translate("MainWindow", "Widgets specific to detected sensors will be displayed\n"
"here after you click the button below", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Scan the I2C BUS for sensors\n"
"and generate widgets", None))
        self.pushButton.setText(_translate("MainWindow", "Auto Scan", None))
        self.actionIPython_Console.setText(_translate("MainWindow", "iPython Console", None))
        self.actionIPython.setText(_translate("MainWindow", "iPython Console", None))
        self.actionReset_Device.setText(_translate("MainWindow", "Reset Device", None))

