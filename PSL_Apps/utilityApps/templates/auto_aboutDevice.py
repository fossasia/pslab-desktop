# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDevice.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setAutoScrollMargin(10)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(100)
        self.table.setColumnCount(6)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.horizontalHeader().setMinimumSectionSize(40)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setDefaultSectionSize(20)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setMinimumSectionSize(15)
        self.verticalLayout.addWidget(self.table)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.headerBox = QtWidgets.QCheckBox(self.frame)
        self.headerBox.setChecked(True)
        self.headerBox.setObjectName("headerBox")
        self.horizontalLayout.addWidget(self.headerBox)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.delims = QtWidgets.QComboBox(self.frame)
        self.delims.setMaximumSize(QtCore.QSize(200, 16777215))
        self.delims.setObjectName("delims")
        self.delims.addItem("")
        self.delims.addItem("")
        self.delims.addItem("")
        self.delims.addItem("")
        self.horizontalLayout.addWidget(self.delims)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About Device"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.headerBox.setText(_translate("MainWindow", "Include Headers"))
        self.label.setText(_translate("MainWindow", "Separator:"))
        self.delims.setItemText(0, _translate("MainWindow", "space"))
        self.delims.setItemText(1, _translate("MainWindow", "tab"))
        self.delims.setItemText(2, _translate("MainWindow", "comma"))
        self.delims.setItemText(3, _translate("MainWindow", "semicolon"))
        self.pushButton_2.setText(_translate("MainWindow", "Save to file"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
