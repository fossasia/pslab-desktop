# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ipy.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionNumpy = QtWidgets.QAction(MainWindow)
        self.actionNumpy.setObjectName("actionNumpy")
        self.actionPylab = QtWidgets.QAction(MainWindow)
        self.actionPylab.setObjectName("actionPylab")
        self.actionScipy = QtWidgets.QAction(MainWindow)
        self.actionScipy.setObjectName("actionScipy")
        self.toolBar.addAction(self.actionNumpy)
        self.toolBar.addAction(self.actionScipy)
        self.toolBar.addAction(self.actionPylab)

        self.retranslateUi(MainWindow)
        self.actionNumpy.triggered.connect(MainWindow.importNumpy)
        self.actionScipy.triggered.connect(MainWindow.importScipy)
        self.actionPylab.triggered.connect(MainWindow.importPylab)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iPython Console"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNumpy.setText(_translate("MainWindow", "Numpy"))
        self.actionNumpy.setToolTip(_translate("MainWindow", "import numpy as np"))
        self.actionNumpy.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionPylab.setText(_translate("MainWindow", "PyLab"))
        self.actionPylab.setToolTip(_translate("MainWindow", "from pylab import *"))
        self.actionPylab.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionScipy.setText(_translate("MainWindow", "Scipy"))
        self.actionScipy.setToolTip(_translate("MainWindow", "import scipy"))
        self.actionScipy.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
