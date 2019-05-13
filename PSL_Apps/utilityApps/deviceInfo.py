#!/usr/bin/python
'''
Output Peripheral control for FOSSASIA PSLab - version 1.0.0.
'''

from __future__ import print_function

import os

os.environ['QT_API'] = 'pyqt'
import PyQt5.sip as sip

sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

from PyQt5 import QtGui
from .templates import auto_aboutDevice as aboutDevice
import sys

unicode = str  # Python 3


class AppWindow(QtGui.QMainWindow, aboutDevice.Ui_MainWindow):
    def __init__(self, parent=None, **kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I = kwargs.get('I', None)

        self.setWindowTitle('About Device : ' + self.I.hexid)
        self.table.setColumnWidth(0, 200)
        if self.I.connected:
            xpos = 0;
            ypos = 0
            for a in self.I.aboutArray:
                xpos = 0
                for b in a:
                    item = QtGui.QTableWidgetItem()
                    self.table.setItem(ypos, xpos, item)
                    item.setText('%s' % b)
                    xpos += 1
                ypos += 1

    def save(self):  # Save as CSV
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '~/', 'CSV(*.csv)')
        if path:
            import csv
            with open(unicode(path), 'wb') as stream:
                delim = [' ', '\t', ',', ';']
                writer = csv.writer(stream, delimiter=delim[self.delims.currentIndex()])
                if self.headerBox.isChecked():
                    try:
                        headers = []
                        for column in range(self.table.columnCount()): headers.append(
                            self.table.horizontalHeaderItem(column).text())
                        writer.writerow(headers)
                    except:
                        pass

                # writer.writeheader()
                for row in range(self.table.rowCount()):
                    rowdata = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            rowdata.append(unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)

    def __del__(self):
        print('bye')


if __name__ == "__main__":
    from PSL import sciencelab

    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())
