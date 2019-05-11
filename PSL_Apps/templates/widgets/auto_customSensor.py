# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customSensor.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 70)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 3)
        self.dataOptions = QtWidgets.QComboBox(Form)
        self.dataOptions.setObjectName("dataOptions")
        self.gridLayout.addWidget(self.dataOptions, 2, 0, 1, 3)
        self.enable = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable.sizePolicy().hasHeightForWidth())
        self.enable.setSizePolicy(sizePolicy)
        self.enable.setMinimumSize(QtCore.QSize(20, 0))
        self.enable.setText("")
        self.enable.setObjectName("enable")
        self.gridLayout.addWidget(self.enable, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(Form)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.remove)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "title|address"))
        self.toolButton.setText(_translate("Form", "..."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
