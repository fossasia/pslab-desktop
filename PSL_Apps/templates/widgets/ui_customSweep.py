# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/customSweep.ui'
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
        Form.resize(356, 63)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.name = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 2, 2, 1, 1)
        self.startBox = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBox.sizePolicy().hasHeightForWidth())
        self.startBox.setSizePolicy(sizePolicy)
        self.startBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.startBox.setFont(font)
        self.startBox.setMinimum(-100000.0)
        self.startBox.setMaximum(100000.0)
        self.startBox.setObjectName(_fromUtf8("startBox"))
        self.gridLayout.addWidget(self.startBox, 4, 2, 1, 1)
        self.stopBox = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBox.sizePolicy().hasHeightForWidth())
        self.stopBox.setSizePolicy(sizePolicy)
        self.stopBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.stopBox.setFont(font)
        self.stopBox.setMinimum(-100000.0)
        self.stopBox.setMaximum(100000.0)
        self.stopBox.setProperty("value", 100.0)
        self.stopBox.setObjectName(_fromUtf8("stopBox"))
        self.gridLayout.addWidget(self.stopBox, 4, 3, 1, 1)
        self.toolButton = QtGui.QToolButton(Form)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("window-close"))
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 2, 5, 1, 1)
        self.numBox = QtGui.QSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numBox.sizePolicy().hasHeightForWidth())
        self.numBox.setSizePolicy(sizePolicy)
        self.numBox.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.numBox.setFont(font)
        self.numBox.setMinimum(2)
        self.numBox.setMaximum(1000)
        self.numBox.setProperty("value", 10)
        self.numBox.setObjectName(_fromUtf8("numBox"))
        self.gridLayout.addWidget(self.numBox, 4, 4, 1, 2)
        self.enable = QtGui.QCheckBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable.sizePolicy().hasHeightForWidth())
        self.enable.setSizePolicy(sizePolicy)
        self.enable.setMinimumSize(QtCore.QSize(20, 0))
        self.enable.setText(_fromUtf8(""))
        self.enable.setObjectName(_fromUtf8("enable"))
        self.gridLayout.addWidget(self.enable, 2, 0, 1, 1)
        self.cmd = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd.sizePolicy().hasHeightForWidth())
        self.cmd.setSizePolicy(sizePolicy)
        self.cmd.setObjectName(_fromUtf8("cmd"))
        self.gridLayout.addWidget(self.cmd, 2, 3, 1, 2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.remove)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.name, self.cmd)
        Form.setTabOrder(self.cmd, self.toolButton)
        Form.setTabOrder(self.toolButton, self.startBox)
        Form.setTabOrder(self.startBox, self.stopBox)
        Form.setTabOrder(self.stopBox, self.numBox)
        Form.setTabOrder(self.numBox, self.enable)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.name.setPlaceholderText(_translate("Form", "title", None))
        self.startBox.setSuffix(_translate("Form", " start", None))
        self.stopBox.setSuffix(_translate("Form", " stop", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.numBox.setSuffix(_translate("Form", "points", None))
        self.cmd.setPlaceholderText(_translate("Form", "function name", None))

