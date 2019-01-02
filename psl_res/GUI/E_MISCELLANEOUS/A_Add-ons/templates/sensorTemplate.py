# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensorTemplate.ui'

from PyQt5 import QtCore, QtGui

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
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollLayout = QtGui.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 745, 265))
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
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 745, 265))
        self.scroll2layout.setStyleSheet(_fromUtf8(""))
        self.scroll2layout.setObjectName(_fromUtf8("scroll2layout"))
        self.paramMenus = QtGui.QVBoxLayout(self.scroll2layout)
        self.paramMenus.setSpacing(0)
        self.paramMenus.setMargin(0)
        self.paramMenus.setObjectName(_fromUtf8("paramMenus"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.paramMenus.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scroll2layout)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.plot_area = QtGui.QVBoxLayout(self.frame_2)
        self.plot_area.setSpacing(0)
        self.plot_area.setMargin(5)
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.scan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.pushButton.setText(_translate("MainWindow", "Auto Scan", None))

