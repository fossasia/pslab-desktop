# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interactivePlot.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 365)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plot_area = QtWidgets.QVBoxLayout(self.frame)
        self.plot_area.setContentsMargins(0, 0, 0, 0)
        self.plot_area.setSpacing(0)
        self.plot_area.setObjectName("plot_area")
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 83, 336))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ControlsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.ControlsLayout.setContentsMargins(0, 0, 0, 0)
        self.ControlsLayout.setSpacing(2)
        self.ControlsLayout.setObjectName("ControlsLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 7)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.saveData)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Save Data"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
