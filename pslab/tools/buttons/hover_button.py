from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Button(QPushButton):

    mouseHover = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, name="", shortcut="", details="", obj="",
                 tooltip="", style="", connect=None, hintfn=None):
        super(Button, self).__init__()
        self.setMouseTracking(True)
        self.details = details
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.set_font()
        self.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(True)
        self.setStyleSheet(style)
        self.setCheckable(False)
        self.setFlat(False)
        self.setObjectName(obj)
        self.setToolTip(tooltip)
        self.setText(name)
        self.setShortcut(shortcut)
        self.clicked.connect(connect)
        self.mouseHover.connect(hintfn)

    def set_font(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setFont(font)

    def enterEvent(self, QEvent):
        self.mouseHover.emit(self.details)

    def leaveEvent(self, QEvent):
        self.mouseHover.emit('')
