# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensors.ui'


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
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: rgb(21, 107, 113);\n"
""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollLayout = QtGui.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 214, 216))
        self.scrollLayout.setObjectName(_fromUtf8("scrollLayout"))
        self.nodeArea = QtGui.QVBoxLayout(self.scrollLayout)
        self.nodeArea.setSpacing(0)
        self.nodeArea.setMargin(0)
        self.nodeArea.setObjectName(_fromUtf8("nodeArea"))
        self.label = QtGui.QLabel(self.scrollLayout)
        self.label.setObjectName(_fromUtf8("label"))
        self.nodeArea.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.nodeArea.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.scrollArea_2 = QtGui.QScrollArea(Form)
        self.scrollArea_2.setStyleSheet(_fromUtf8("background-color: rgb(21, 107, 113);\n"
""))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scroll2layout = QtGui.QWidget()
        self.scroll2layout.setGeometry(QtCore.QRect(0, 0, 214, 215))
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
        self.gridLayout.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Under ACtive development", None))

