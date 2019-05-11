# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensors.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(216, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 0))
        Form.setWindowOpacity(1.0)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("background-color: rgb(21, 107, 113);\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollLayout = QtWidgets.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 214, 216))
        self.scrollLayout.setObjectName("scrollLayout")
        self.nodeArea = QtWidgets.QVBoxLayout(self.scrollLayout)
        self.nodeArea.setContentsMargins(0, 0, 0, 0)
        self.nodeArea.setSpacing(0)
        self.nodeArea.setObjectName("nodeArea")
        self.label = QtWidgets.QLabel(self.scrollLayout)
        self.label.setObjectName("label")
        self.nodeArea.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.nodeArea.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setStyleSheet("background-color: rgb(21, 107, 113);\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scroll2layout = QtWidgets.QWidget()
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 214, 215))
        self.scroll2layout.setStyleSheet("QMenu{color:rgb(255,255,255);}\n"
"")
        self.scroll2layout.setObjectName("scroll2layout")
        self.paramMenus = QtWidgets.QVBoxLayout(self.scroll2layout)
        self.paramMenus.setContentsMargins(0, 0, 0, 0)
        self.paramMenus.setSpacing(0)
        self.paramMenus.setObjectName("paramMenus")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.paramMenus.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scroll2layout)
        self.gridLayout.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Under ACtive development"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
