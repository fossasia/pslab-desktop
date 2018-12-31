# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepper.ui'

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(245, 167)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"#centralwidget{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.steps = QtGui.QSpinBox(self.centralwidget)
        self.steps.setMinimum(-10000)
        self.steps.setMaximum(10000)
        self.steps.setProperty("value", 10)
        self.steps.setObjectName(_fromUtf8("steps"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.steps)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.delay = QtGui.QSpinBox(self.centralwidget)
        self.delay.setMinimum(1)
        self.delay.setMaximum(1000)
        self.delay.setProperty("value", 10)
        self.delay.setObjectName(_fromUtf8("delay"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.delay)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setAutoRepeat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.line)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.takeSteps)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.stepBackward)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.stepForward)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Steps", None))
        self.label_2.setText(_translate("MainWindow", "Delay(mS)", None))
        self.pushButton_2.setText(_translate("MainWindow", "StepBackward", None))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Left", None))
        self.pushButton.setText(_translate("MainWindow", "Take Steps", None))
        self.pushButton_3.setText(_translate("MainWindow", "StepForward", None))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Right", None))

