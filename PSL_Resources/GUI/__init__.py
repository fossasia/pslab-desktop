import os

os.environ['QT_API'] = 'pyqt'
import PyQt5.sip as sip

sip.setapi("QString", 2)
sip.setapi("QVariant", 2)
