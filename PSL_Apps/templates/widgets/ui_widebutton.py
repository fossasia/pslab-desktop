# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/widebutton.ui'
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
        Form.resize(300, 105)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(100, 105))
        Form.setMaximumSize(QtCore.QSize(300, 105))
        Form.setStyleSheet(_fromUtf8("QFrame.PeripheralCollection{\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 rgb(97, 146, 121), stop: 0.5 rgb(65, 89, 111));\n"
"\n"
"}\n"
"QLabel {\n"
"color: white;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"}\n"
""))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widgetFrameOuter = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setMinimumSize(QtCore.QSize(300, 0))
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.NoFrame)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widgetFrameOuter)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.title = QtGui.QLabel(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)
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
        self.gridLayout_3.setContentsMargins(0, 2, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.value = QtGui.QLabel(self.ImageFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.value.setFont(font)
        self.value.setText(_fromUtf8(""))
        self.value.setScaledContents(True)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setObjectName(_fromUtf8("value"))
        self.gridLayout_3.addWidget(self.value, 0, 0, 2, 1)
        self.gridLayout_2.addWidget(self.ImageFrame, 0, 1, 2, 1)
        self.pushButton = QtGui.QPushButton(self.widgetFrameOuter)
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.read)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget", None))
        self.title.setText(_translate("Form", "title", None))
        self.pushButton.setText(_translate("Form", "Read", None))

