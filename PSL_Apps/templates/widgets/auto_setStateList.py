# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setStateList.ui'
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
"\n"
"QLabel,QCheckBox {\n"
"color: white;\n"
"font-weight: bold;\n"
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
        self.B1 = QtWidgets.QCheckBox(self.ImageFrame)
        self.B1.setObjectName("B1")
        self.gridLayout_3.addWidget(self.B1, 0, 0, 1, 1)
        self.B3 = QtWidgets.QCheckBox(self.ImageFrame)
        self.B3.setObjectName("B3")
        self.gridLayout_3.addWidget(self.B3, 2, 0, 1, 1)
        self.B4 = QtWidgets.QCheckBox(self.ImageFrame)
        self.B4.setObjectName("B4")
        self.gridLayout_3.addWidget(self.B4, 3, 0, 1, 1)
        self.B2 = QtWidgets.QCheckBox(self.ImageFrame)
        self.B2.setObjectName("B2")
        self.gridLayout_3.addWidget(self.B2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        self.B1.clicked['bool'].connect(Form.toggle1)
        self.B2.clicked['bool'].connect(Form.toggle2)
        self.B3.clicked['bool'].connect(Form.toggle3)
        self.B4.clicked['bool'].connect(Form.toggle4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.widgetFrameOuter.setToolTip(_translate("Form", "Disable square waves and set them to High/Low"))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget"))
        self.title.setText(_translate("Form", "Digital Outputs"))
        self.B1.setText(_translate("Form", "SQR1"))
        self.B3.setText(_translate("Form", "SQR3"))
        self.B4.setText(_translate("Form", "SQR4"))
        self.B2.setText(_translate("Form", "SQR2"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
