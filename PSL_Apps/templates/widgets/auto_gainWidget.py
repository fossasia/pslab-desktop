# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gainWidget.ui'
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
"QLabel {\n"
"color: white;\n"
"background:transparent;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetFrameOuter = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
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
        self.verticalLayout_3.setContentsMargins(3, 2, 3, 3)
        self.verticalLayout_3.setSpacing(2)
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
        self.g1 = QtWidgets.QComboBox(self.ImageFrame)
        self.g1.setObjectName("g1")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.g1.addItem("")
        self.gridLayout_3.addWidget(self.g1, 1, 0, 1, 1)
        self.title_2 = QtWidgets.QLabel(self.ImageFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
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
        self.title_2.setObjectName("title_2")
        self.gridLayout_3.addWidget(self.title_2, 0, 0, 1, 1)
        self.g2 = QtWidgets.QComboBox(self.ImageFrame)
        self.g2.setObjectName("g2")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.g2.addItem("")
        self.gridLayout_3.addWidget(self.g2, 3, 0, 1, 1)
        self.title_3 = QtWidgets.QLabel(self.ImageFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
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
        self.title_3.setObjectName("title_3")
        self.gridLayout_3.addWidget(self.title_3, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        self.g1.currentIndexChanged['int'].connect(Form.setGainCH1)
        self.g2.currentIndexChanged['int'].connect(Form.setGainCH2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setToolTip(_translate("Form", "Change the voltage range for the selected channel"))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget"))
        self.title.setText(_translate("Form", "set ranges"))
        self.g1.setItemText(0, _translate("Form", "+/-16V"))
        self.g1.setItemText(1, _translate("Form", "+/-8V"))
        self.g1.setItemText(2, _translate("Form", "+/-4V"))
        self.g1.setItemText(3, _translate("Form", "+/-3V"))
        self.g1.setItemText(4, _translate("Form", "+/-2V"))
        self.g1.setItemText(5, _translate("Form", "+/-1.5V"))
        self.g1.setItemText(6, _translate("Form", "+/-1V"))
        self.g1.setItemText(7, _translate("Form", "+/-500mV"))
        self.g1.setItemText(8, _translate("Form", "+/-160V"))
        self.title_2.setText(_translate("Form", "CH1"))
        self.g2.setItemText(0, _translate("Form", "+/-16V"))
        self.g2.setItemText(1, _translate("Form", "+/-8V"))
        self.g2.setItemText(2, _translate("Form", "+/-4V"))
        self.g2.setItemText(3, _translate("Form", "+/-3V"))
        self.g2.setItemText(4, _translate("Form", "+/-2V"))
        self.g2.setItemText(5, _translate("Form", "+/-1.5V"))
        self.g2.setItemText(6, _translate("Form", "+/-1V"))
        self.g2.setItemText(7, _translate("Form", "+/-500mV"))
        self.g2.setItemText(8, _translate("Form", "+/-160V"))
        self.title_3.setText(_translate("Form", "CH2"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
