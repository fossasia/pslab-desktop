# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/dualButton.ui'
#
# Created: Tue Aug  9 01:56:31 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(104, 105)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(100, 105))
        Form.setMaximumSize(QtCore.QSize(104, 105))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet(_fromUtf8(" QLabel {\n"
"color: white;\n"
"background:transparent;\n"
"}\n"
"\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widgetFrameOuter = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setMinimumSize(QtCore.QSize(80, 0))
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(3, 2, 2, 2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.title = QtGui.QLabel(self.widgetFrameOuter)
        self.title.setText(_fromUtf8(""))
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout_3.addWidget(self.title)
        self.ImageFrame = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageFrame.sizePolicy().hasHeightForWidth())
        self.ImageFrame.setSizePolicy(sizePolicy)
        self.ImageFrame.setMinimumSize(QtCore.QSize(90, 70))
        self.ImageFrame.setStyleSheet(_fromUtf8(""))
        self.ImageFrame.setObjectName(_fromUtf8("ImageFrame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.ImageFrame)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.buttonA = QtGui.QPushButton(self.ImageFrame)
        self.buttonA.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonA.setStyleSheet(_fromUtf8(""))
        self.buttonA.setText(_fromUtf8(""))
        self.buttonA.setObjectName(_fromUtf8("buttonA"))
        self.gridLayout_3.addWidget(self.buttonA, 0, 0, 1, 1)
        self.buttonB = QtGui.QPushButton(self.ImageFrame)
        self.buttonB.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonB.setStyleSheet(_fromUtf8(""))
        self.buttonB.setText(_fromUtf8(""))
        self.buttonB.setObjectName(_fromUtf8("buttonB"))
        self.gridLayout_3.addWidget(self.buttonB, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.buttonB, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.clickedB)
        QtCore.QObject.connect(self.buttonA, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.clickedA)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget", None))

