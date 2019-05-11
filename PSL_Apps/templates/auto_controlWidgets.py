# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlWidgets.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMinimumSize(QtCore.QSize(350, 0))
        self.scrollArea_4.setMaximumSize(QtCore.QSize(370, 16777215))
        self.scrollArea_4.setStyleSheet("")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.SCF1 = QtWidgets.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 355, 589))
        self.SCF1.setStyleSheet("")
        self.SCF1.setObjectName("SCF1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SCF1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.SCF1)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.WidgetLayout = QtWidgets.QGridLayout()
        self.WidgetLayout.setContentsMargins(5, 5, 5, 5)
        self.WidgetLayout.setSpacing(7)
        self.WidgetLayout.setObjectName("WidgetLayout")
        self.gridLayout_8.addLayout(self.WidgetLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.gridLayout.addWidget(self.scrollArea_4, 0, 0, 2, 1)
        self.advancedControlsLayout = QtWidgets.QVBoxLayout()
        self.advancedControlsLayout.setObjectName("advancedControlsLayout")
        self.gridLayout.addLayout(self.advancedControlsLayout, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
