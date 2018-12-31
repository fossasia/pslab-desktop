# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stream.ui'


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
        Form.resize(276, 420)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmdlist = QtGui.QComboBox(Form)
        self.cmdlist.setMinimumSize(QtCore.QSize(250, 0))
        self.cmdlist.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.cmdlist.setEditable(True)
        self.cmdlist.setObjectName(_fromUtf8("cmdlist"))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cmdlist)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.frame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 10))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.averageCount = QtGui.QSpinBox(self.frame)
        self.averageCount.setMinimum(1)
        self.averageCount.setMaximum(501)
        self.averageCount.setObjectName(_fromUtf8("averageCount"))
        self.horizontalLayout.addWidget(self.averageCount)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lastReading = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lastReading.setFont(font)
        self.lastReading.setAlignment(QtCore.Qt.AlignCenter)
        self.lastReading.setObjectName(_fromUtf8("lastReading"))
        self.verticalLayout.addWidget(self.lastReading)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.stream)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.setAverageCount)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cmdlist.setItemText(0, _translate("Form", "get_average_voltage(\'CH1\')", None))
        self.cmdlist.setItemText(1, _translate("Form", "get_freq(\'ID1\')", None))
        self.cmdlist.setItemText(2, _translate("Form", "get_high_freq(\'ID1\')", None))
        self.cmdlist.setItemText(3, _translate("Form", "DutyCycle(\'ID1\')[1]", None))
        self.cmdlist.setItemText(4, _translate("Form", "MeasureInterval(\'ID1\',\'ID2\',\'rising\',\'rising\')", None))
        self.pushButton.setText(_translate("Form", "Start Monitoring", None))
        self.label.setText(_translate("Form", "Averaging", None))
        self.pushButton_2.setText(_translate("Form", "Set", None))
        self.lastReading.setText(_translate("Form", "Result", None))

