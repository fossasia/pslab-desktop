# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialAndDoubleSpin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(104, 105)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(100, 105))
        Form.setMaximumSize(QtCore.QSize(104, 105))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("QFrame.PeripheralCollection{\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 rgb(97, 146, 121), stop: 0.5 rgb(65, 89, 111));\n"
"\n"
"}\n"
" QLabel {\n"
"color: white;\n"
"background:transparent;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetFrameOuter = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setMinimumSize(QtCore.QSize(80, 0))
        self.widgetFrameOuter.setStyleSheet("")
        self.widgetFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetFrameOuter.setObjectName("widgetFrameOuter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QLabel(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
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
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.ImageFrame = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageFrame.sizePolicy().hasHeightForWidth())
        self.ImageFrame.setSizePolicy(sizePolicy)
        self.ImageFrame.setMinimumSize(QtCore.QSize(90, 70))
        self.ImageFrame.setStyleSheet("")
        self.ImageFrame.setObjectName("ImageFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ImageFrame)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dial = QtWidgets.QDial(self.ImageFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setMinimum(10)
        self.dial.setMaximum(5000)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.gridLayout_3.addWidget(self.dial, 0, 0, 1, 1)
        self.value = QtWidgets.QDoubleSpinBox(self.ImageFrame)
        self.value.setMaximumSize(QtCore.QSize(16777215, 18))
        self.value.setObjectName("value")
        self.gridLayout_3.addWidget(self.value, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        self.dial.valueChanged['int'].connect(Form.setValue)
        self.value.editingFinished.connect(Form.setDoubleValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget"))
        self.title.setText(_translate("Form", "title"))
        self.value.setSuffix(_translate("Form", " "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
