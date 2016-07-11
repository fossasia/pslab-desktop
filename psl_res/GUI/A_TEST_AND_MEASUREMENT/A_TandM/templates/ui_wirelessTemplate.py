# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psl_res/GUI/A_TEST_AND_MEASUREMENT/A_TandM/templates/wirelessTemplate.ui'
#
# Created: Mon Jul 11 21:45:32 2016
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.splitter.setFrameShadow(QtGui.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.logs = QtWebKit.QWebView(self.frame)
        self.logs.setMaximumSize(QtCore.QSize(16777215, 150))
        self.logs.setObjectName(_fromUtf8("logs"))
        self.verticalLayout.addWidget(self.logs)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollLayout = QtGui.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 246, 172))
        self.scrollLayout.setObjectName(_fromUtf8("scrollLayout"))
        self.nodeArea = QtGui.QVBoxLayout(self.scrollLayout)
        self.nodeArea.setSpacing(0)
        self.nodeArea.setMargin(0)
        self.nodeArea.setObjectName(_fromUtf8("nodeArea"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.nodeArea.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtGui.QScrollArea(self.frame)
        self.scrollArea_2.setStyleSheet(_fromUtf8(""))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scroll2layout = QtGui.QWidget()
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 246, 347))
        self.scroll2layout.setStyleSheet(_fromUtf8(""))
        self.scroll2layout.setObjectName(_fromUtf8("scroll2layout"))
        self.paramMenus = QtGui.QVBoxLayout(self.scroll2layout)
        self.paramMenus.setSpacing(0)
        self.paramMenus.setMargin(0)
        self.paramMenus.setObjectName(_fromUtf8("paramMenus"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.paramMenus.addItem(spacerItem1)
        self.frame_3 = QtGui.QFrame(self.scroll2layout)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pauseBox = QtGui.QCheckBox(self.frame_3)
        self.pauseBox.setObjectName(_fromUtf8("pauseBox"))
        self.horizontalLayout_2.addWidget(self.pauseBox)
        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.paramMenus.addWidget(self.frame_3)
        self.scrollArea_2.setWidget(self.scroll2layout)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)
        self.frame_2 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.plot_area = QtGui.QVBoxLayout(self.frame_2)
        self.plot_area.setSpacing(0)
        self.plot_area.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.plot_area.setMargin(5)
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.toggleListen)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.reloadNodeList)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.checkBox.setText(_translate("MainWindow", "Auto Listen", None))
        self.pushButton.setText(_translate("MainWindow", "Generate Menus", None))
        self.pauseBox.setText(_translate("MainWindow", "Pause", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save Data", None))

from PyQt4 import QtWebKit
