# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/customFunc.ui'
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
        Form.resize(355, 33)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.enable = QtGui.QCheckBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable.sizePolicy().hasHeightForWidth())
        self.enable.setSizePolicy(sizePolicy)
        self.enable.setMinimumSize(QtCore.QSize(20, 0))
        self.enable.setText(_fromUtf8(""))
        self.enable.setObjectName(_fromUtf8("enable"))
        self.horizontalLayout.addWidget(self.enable)
        self.name = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.cmd = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd.sizePolicy().hasHeightForWidth())
        self.cmd.setSizePolicy(sizePolicy)
        self.cmd.setObjectName(_fromUtf8("cmd"))
        self.horizontalLayout.addWidget(self.cmd)
        self.toolButton = QtGui.QToolButton(Form)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("window-close"))
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 10)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.remove)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.name.setPlaceholderText(_translate("Form", "Name", None))
        self.cmd.setPlaceholderText(_translate("Form", "Enter An Expression", None))
        self.toolButton.setText(_translate("Form", "...", None))

