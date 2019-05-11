# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensorTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollLayout = QtWidgets.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 745, 265))
        self.scrollLayout.setObjectName("scrollLayout")
        self.nodeArea = QtWidgets.QVBoxLayout(self.scrollLayout)
        self.nodeArea.setContentsMargins(0, 0, 0, 0)
        self.nodeArea.setSpacing(0)
        self.nodeArea.setObjectName("nodeArea")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.nodeArea.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scroll2layout = QtWidgets.QWidget()
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 745, 265))
        self.scroll2layout.setStyleSheet("")
        self.scroll2layout.setObjectName("scroll2layout")
        self.paramMenus = QtWidgets.QVBoxLayout(self.scroll2layout)
        self.paramMenus.setContentsMargins(0, 0, 0, 0)
        self.paramMenus.setSpacing(0)
        self.paramMenus.setObjectName("paramMenus")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.paramMenus.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scroll2layout)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.plot_area = QtWidgets.QVBoxLayout(self.frame_2)
        self.plot_area.setContentsMargins(5, 5, 5, 5)
        self.plot_area.setSpacing(0)
        self.plot_area.setObjectName("plot_area")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.scan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.pushButton.setText(_translate("MainWindow", "Auto Scan"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
