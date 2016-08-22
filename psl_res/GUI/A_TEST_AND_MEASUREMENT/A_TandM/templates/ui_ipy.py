# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psl_res/GUI/A_TEST_AND_MEASUREMENT/A_TandM/templates/ipy.ui'
#
# Created: Sun Aug 21 23:13:15 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(898, 417)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layout = QtGui.QVBoxLayout(self.frame)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionNumpy = QtGui.QAction(MainWindow)
        self.actionNumpy.setObjectName(_fromUtf8("actionNumpy"))
        self.actionPylab = QtGui.QAction(MainWindow)
        self.actionPylab.setObjectName(_fromUtf8("actionPylab"))
        self.actionScipy = QtGui.QAction(MainWindow)
        self.actionScipy.setObjectName(_fromUtf8("actionScipy"))
        self.toolBar.addAction(self.actionNumpy)
        self.toolBar.addAction(self.actionScipy)
        self.toolBar.addAction(self.actionPylab)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionNumpy, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.importNumpy)
        QtCore.QObject.connect(self.actionScipy, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.importScipy)
        QtCore.QObject.connect(self.actionPylab, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.importPylab)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "iPython Console", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNumpy.setText(_translate("MainWindow", "Numpy", None))
        self.actionNumpy.setToolTip(_translate("MainWindow", "import numpy as np", None))
        self.actionNumpy.setShortcut(_translate("MainWindow", "Ctrl+Shift+N", None))
        self.actionPylab.setText(_translate("MainWindow", "PyLab", None))
        self.actionPylab.setToolTip(_translate("MainWindow", "from pylab import *", None))
        self.actionPylab.setShortcut(_translate("MainWindow", "Ctrl+Shift+P", None))
        self.actionScipy.setText(_translate("MainWindow", "Scipy", None))
        self.actionScipy.setToolTip(_translate("MainWindow", "import scipy", None))
        self.actionScipy.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))

