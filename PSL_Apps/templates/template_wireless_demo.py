# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nrf.ui'


from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(216, 438)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 0))
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("QTextEdit {color: rgb(0, 0, 0);}\n"
"QLineEdit {color: rgb(0, 0, 0);}\n"
"QLineEdit:selected {color: rgb(0, 0, 0);}\n"
"QSpinBox{color: rgb(0, 0, 0);}\n"
"QCheckBox{color:rgb(255,255,255);}\n"
"\n"
"QWebView,QScrollAreaWidgetContents{background-color: rgb(21, 107, 113);}\n"
"\n"
""))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: rgb(21, 107, 113);\n"
""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollLayout = QtGui.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 214, 112))
        self.scrollLayout.setObjectName(_fromUtf8("scrollLayout"))
        self.nodeArea = QtGui.QVBoxLayout(self.scrollLayout)
        self.nodeArea.setSpacing(0)
        self.nodeArea.setMargin(0)
        self.nodeArea.setObjectName(_fromUtf8("nodeArea"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.nodeArea.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.scrollArea_2 = QtGui.QScrollArea(Form)
        self.scrollArea_2.setStyleSheet(_fromUtf8("background-color: rgb(21, 107, 113);\n"
""))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scroll2layout = QtGui.QWidget()
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 214, 111))
        self.scroll2layout.setStyleSheet(_fromUtf8("QMenu{color:rgb(255,255,255);}\n"
""))
        self.scroll2layout.setObjectName(_fromUtf8("scroll2layout"))
        self.paramMenus = QtGui.QVBoxLayout(self.scroll2layout)
        self.paramMenus.setSpacing(0)
        self.paramMenus.setMargin(0)
        self.paramMenus.setObjectName(_fromUtf8("paramMenus"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.paramMenus.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scroll2layout)
        self.gridLayout.addWidget(self.scrollArea_2, 5, 0, 1, 1)
        self.logs = QtWebKit.QWebView(Form)
        self.logs.setMaximumSize(QtCore.QSize(250, 150))
        self.logs.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.logs.setObjectName(_fromUtf8("logs"))
        self.gridLayout.addWidget(self.logs, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), Form.toggleListen)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.reloadNodelist)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Refresh Node List", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Register New Nodes", None, QtGui.QApplication.UnicodeUTF8))

from PyQt5 import QtWebKit
