# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gainWidget.ui'


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
"background:transparent;\n"
"}\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widgetFrameOuter = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
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
        self.verticalLayout_3.setContentsMargins(3, 2, 3, 3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.g1 = QtGui.QComboBox(self.ImageFrame)
        self.g1.setObjectName(_fromUtf8("g1"))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.g1.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.g1, 1, 0, 1, 1)
        self.title_2 = QtGui.QLabel(self.ImageFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName(_fromUtf8("title_2"))
        self.gridLayout_3.addWidget(self.title_2, 0, 0, 1, 1)
        self.g2 = QtGui.QComboBox(self.ImageFrame)
        self.g2.setObjectName(_fromUtf8("g2"))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.g2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.g2, 3, 0, 1, 1)
        self.title_3 = QtGui.QLabel(self.ImageFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_3.sizePolicy().hasHeightForWidth())
        self.title_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title_3.setFont(font)
        self.title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_3.setObjectName(_fromUtf8("title_3"))
        self.gridLayout_3.addWidget(self.title_3, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.g1, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Form.setGainCH1)
        QtCore.QObject.connect(self.g2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Form.setGainCH2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        Form.setToolTip(_translate("Form", "Change the voltage range for the selected channel", None))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget", None))
        self.title.setText(_translate("Form", "set ranges", None))
        self.g1.setItemText(0, _translate("Form", "+/-16V", None))
        self.g1.setItemText(1, _translate("Form", "+/-8V", None))
        self.g1.setItemText(2, _translate("Form", "+/-4V", None))
        self.g1.setItemText(3, _translate("Form", "+/-3V", None))
        self.g1.setItemText(4, _translate("Form", "+/-2V", None))
        self.g1.setItemText(5, _translate("Form", "+/-1.5V", None))
        self.g1.setItemText(6, _translate("Form", "+/-1V", None))
        self.g1.setItemText(7, _translate("Form", "+/-500mV", None))
        self.g1.setItemText(8, _translate("Form", "+/-160V", None))
        self.title_2.setText(_translate("Form", "CH1", None))
        self.g2.setItemText(0, _translate("Form", "+/-16V", None))
        self.g2.setItemText(1, _translate("Form", "+/-8V", None))
        self.g2.setItemText(2, _translate("Form", "+/-4V", None))
        self.g2.setItemText(3, _translate("Form", "+/-3V", None))
        self.g2.setItemText(4, _translate("Form", "+/-2V", None))
        self.g2.setItemText(5, _translate("Form", "+/-1.5V", None))
        self.g2.setItemText(6, _translate("Form", "+/-1V", None))
        self.g2.setItemText(7, _translate("Form", "+/-500mV", None))
        self.g2.setItemText(8, _translate("Form", "+/-160V", None))
        self.title_3.setText(_translate("Form", "CH2", None))

