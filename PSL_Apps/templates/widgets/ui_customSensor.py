# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/customSensor.ui'
#
# Created: Mon Aug  8 20:50:32 2016
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
        Form.resize(316, 70)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 3)
        self.dataOptions = QtGui.QComboBox(Form)
        self.dataOptions.setObjectName(_fromUtf8("dataOptions"))
        self.gridLayout.addWidget(self.dataOptions, 2, 0, 1, 3)
        self.enable = QtGui.QCheckBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable.sizePolicy().hasHeightForWidth())
        self.enable.setSizePolicy(sizePolicy)
        self.enable.setMinimumSize(QtCore.QSize(20, 0))
        self.enable.setText(_fromUtf8(""))
        self.enable.setObjectName(_fromUtf8("enable"))
        self.gridLayout.addWidget(self.enable, 1, 0, 1, 1)
        self.title = QtGui.QLabel(Form)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(Form)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("window-close"))
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 1, 2, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.remove)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.title.setText(_translate("Form", "title|address", None))
        self.toolButton.setText(_translate("Form", "...", None))

