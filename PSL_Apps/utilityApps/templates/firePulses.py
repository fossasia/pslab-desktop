# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firePulses.ui'


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
        MainWindow.resize(257, 588)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_7 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.Frame_4 = QtGui.QFrame(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_4.sizePolicy().hasHeightForWidth())
        self.Frame_4.setSizePolicy(sizePolicy)
        self.Frame_4.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_4.setObjectName(_fromUtf8("Frame_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Frame_4)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.line = QtGui.QFrame(self.Frame_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 2)
        self.tableLayout = QtGui.QVBoxLayout()
        self.tableLayout.setObjectName(_fromUtf8("tableLayout"))
        self.gridLayout_4.addLayout(self.tableLayout, 1, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.Frame_4)
        self.widgetLayout = QtGui.QHBoxLayout()
        self.widgetLayout.setObjectName(_fromUtf8("widgetLayout"))
        self.pushButton_8 = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.widgetLayout.addWidget(self.pushButton_8)
        self.verticalLayout_5.addLayout(self.widgetLayout)
        self.verticalLayout.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.fire)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.frame_7.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_4.setText(_translate("MainWindow", "SQR1: Output oscillating packets", None))
        self.Frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.pushButton_8.setText(_translate("MainWindow", "FIRE", None))

