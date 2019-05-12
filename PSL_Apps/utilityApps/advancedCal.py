#!/usr/bin/python
'''
Output Peripheral control for FOSSASIA PSLab - version 1.0.0.
'''

from __future__ import print_function

import os
import struct
import sys
import time

import PyQt5.sip as sip
from PyQt5 import QtCore, QtGui

from PSL_Apps.utilitiesClass import utilitiesClass
from PSL_Apps.utilityApps.templates import auto_advancedCal as advancedCal

os.environ['QT_API'] = 'pyqt'

sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


class myTable(QtGui.QTableWidget):
    def __init__(self, parent=None):
        QtGui.QTableWidget.__init__(self, parent)
        # initially construct the visible table
        self.setRowCount(512)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Actual', 'Read', 'scale factor'])
        self.setVerticalHeaderLabels(
            ['socket', '330pF', '680pF', '2220pF', 'PCS', '', '550uA', '.55uA', '5.5uA', '55uA', ''])

        self.setTextElideMode(QtCore.Qt.ElideRight)
        self.setGridStyle(QtCore.Qt.DashLine)
        self.setRowCount(11)
        self.horizontalHeader().setDefaultSectionSize(90)
        self.horizontalHeader().setMinimumSectionSize(90)
        self.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setStretchLastSection(True)

        num = 0
        for a in ['0', '329.5e-12', '698e-12', '2168e-12', '1e-3']:
            item = QtGui.QTableWidgetItem()
            self.setItem(num, 0, item)
            item.setText(a)

            item = QtGui.QTableWidgetItem()
            self.setItem(num, 1, item)
            item.setText(a)

            item = QtGui.QTableWidgetItem()
            self.setItem(num + 5, 2, item)
            item.setText('1')

            num += 1
        item = QtGui.QTableWidgetItem()
        self.setItem(num - 1, 2, item)
        item.setText('1')

        item = QtGui.QTableWidgetItem()
        self.setItem(num, 2, item)
        item.setText('0')


class AppWindow(QtGui.QMainWindow, advancedCal.Ui_MainWindow, utilitiesClass):
    def __init__(self, parent=None, **kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I = kwargs.get('I', None)

        self.setWindowTitle('Calibrate Capacitance and PCS ' + self.I.H.version_string.decode("utf-8"))
        self.table = myTable()
        self.tableLayout.addWidget(self.table)

        # Reset existing calibration in software!
        self.reset()

    def reset(self):
        # Reset existing calibration in software!
        self.I.__calibrate_ctmu__([1., 1., 1., 1.])
        self.I.SOCKET_CAPACITANCE = 0
        # Re read socket capacitance
        self.calSock()

    def get_capacitance(self, CR):  # read capacitance using various current ranges
        GOOD_VOLTS = [2.5, 2.8]
        CT = 10
        iterations = 0
        start_time = time.time()
        try:
            while (time.time() - start_time) < 1:
                if CT > 65000:
                    self.displayDialog('CT too high')
                    return 0
                V, C = self.I.__get_capacitance__(CR, 0, CT)
                if V > GOOD_VOLTS[0] and V < GOOD_VOLTS[1]:
                    print('Done', V, C)
                    return C
                elif CT > 30000 and V < 0.1:
                    self.displayDialog('Capacitance too high for this method')
                    return 0
                elif V < GOOD_VOLTS[0] and V > 0.01 and CT < 30000:
                    if GOOD_VOLTS[0] / V > 1.1 and iterations < 10:
                        CT = int(CT * GOOD_VOLTS[0] / V)
                        iterations += 1
                    elif iterations == 10:
                        return 0
                    else:
                        print('Done', V, C, CT)
                        return C
        except Exception as ex:
            self.displayDialog(ex.message)

    def stoa(self, s):
        return [ord(a) for a in s]

    def recover(self):
        cap_and_pcs = self.I.read_bulk_flash(self.I.CAP_AND_PCS, 7 * 4 + 5)  # READY+calibration_string
        if cap_and_pcs[:5] == 'READY':
            scalers = struct.unpack('7f', cap_and_pcs[5:])
            print(cap_and_pcs, scalers)
        # self.__calibrate_ctmu__(self,scalers[:4])
        # self.DAC.CHANS['PCS'].load_calibration_twopoint(scalers[4],scalers[5]) #Slope and offset for current source
        # self.aboutArray.append(['Capacitance scaling']+scalers[:4])
        # self.aboutArray.append(['PCS slope,offset']+scalers[4:])
        else:
            self.displayDialog('Cap and PCS calibration invalid')

    def upload(self):
        vals = [self.socketCap]
        for a in range(6):
            item = self.table.item(a + 4, 2)
            vals.append(float(item.text()))
        print(vals, self.stoa(struct.pack('7f', *vals)))
        # READY + clibration_string
        self.I.write_bulk_flash(self.I.CAP_AND_PCS, self.stoa('READY' + struct.pack('7f', *vals)))
        self.I.SOCKET_CAPACITANCE = vals[0]
        self.I.__calibrate_ctmu__(vals[3:])
        self.I.DAC.CHANS['PCS'].load_calibration_twopoint(vals[1], vals[2])  # Slope and offset for current source

    def __del__(self):
        print('bye')

    def calSock(self):  # Open socket caibration
        self.I.SOCKET_CAPACITANCE = 0
        self.socketCap = self.I.get_capacitance()
        if self.socketCap > 100e-12:
            print('Socket capacitance is unusually high', self.socketCap)
            self.socketCap = 42e-12
        self.I.SOCKET_CAPACITANCE = self.socketCap

        item = self.table.item(0, 0)
        item.setText('%.3e' % self.socketCap)
        item = self.table.item(0, 1)
        item.setText('%.3e' % self.socketCap)

    def cal480(self):  # calibration
        CR = 1
        cap = self.get_capacitance(CR)
        if cap:
            self.table.item(1, 1).setText('%.3e' % cap)
            self.table.item(6 + CR, 2).setText('%.3e' % (cap / float(self.table.item(1, 0).text())))

        CR = 2
        cap = self.get_capacitance(CR)
        if cap:
            self.table.item(1, 1).setText('%.3e' % cap)
            self.table.item(6 + CR, 2).setText('%.3e' % (cap / float(self.table.item(1, 0).text())))

    def cal1(self):  # Cap calibration
        CR = 2
        cap = self.get_capacitance(CR)
        self.table.item(2, 1).setText('%.3e' % cap)
        actual = float(self.table.item(2, 0).text())
        self.table.item(6 + CR, 2).setText('%.3e' % (cap / actual))

    def cal100(self):  # Cap calibration
        CR = 3
        cap = self.get_capacitance(CR)
        self.table.item(3, 1).setText('%.3e' % cap)
        actual = float(self.table.item(3, 0).text())
        self.table.item(6 + CR, 2).setText('%.3e' % (cap / actual))

        CR = 0
        cap = self.get_capacitance(CR)
        self.table.item(3, 1).setText('%.3e' % cap)
        actual = float(self.table.item(3, 0).text())
        self.table.item(6 + CR, 2).setText('%.3e' % (cap / actual))

    def calPCS(self):
        v = self.I.set_pcs(1.0e-3)
        rv = self.I.get_average_voltage('CH3')
        print(v, rv)
        pass


if __name__ == "__main__":
    from PSL import sciencelab

    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect(verbose=True))
    myapp.show()
    sys.exit(app.exec_())
