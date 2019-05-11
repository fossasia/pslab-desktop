# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepper.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(245, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.steps = QtWidgets.QSpinBox(self.centralwidget)
        self.steps.setMinimum(-10000)
        self.steps.setMaximum(10000)
        self.steps.setProperty("value", 10)
        self.steps.setObjectName("steps")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.steps)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.delay = QtWidgets.QSpinBox(self.centralwidget)
        self.delay.setMinimum(1)
        self.delay.setMaximum(1000)
        self.delay.setProperty("value", 10)
        self.delay.setObjectName("delay")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delay)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setAutoRepeat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.takeSteps)
        self.pushButton_2.clicked.connect(MainWindow.stepBackward)
        self.pushButton_3.clicked.connect(MainWindow.stepForward)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Steps"))
        self.label_2.setText(_translate("MainWindow", "Delay(mS)"))
        self.pushButton_2.setText(_translate("MainWindow", "StepBackward"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Left"))
        self.pushButton.setText(_translate("MainWindow", "Take Steps"))
        self.pushButton_3.setText(_translate("MainWindow", "StepForward"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Right"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
