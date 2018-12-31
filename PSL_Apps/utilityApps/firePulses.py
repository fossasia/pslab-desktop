#!/usr/bin/python
'''
Output Peripheral control for FOSSASIA PSLab - version 1.0.0.
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt5 import QtCore, QtGui
from .templates import ui_firePulses as firePulses
from PSL_Apps.utilitiesClass import utilitiesClass

import sys,os,string,functools,time
import numpy as np


class myTable(QtGui.QTableWidget):
	def __init__(self,parent=None):
		QtGui.QTableWidget.__init__(self,parent)
		# initially construct the visible table
		self.setRowCount(512)
		self.setColumnCount(2)
		# set the shortcut ctrl+v for paste
		QtGui.QShortcut(QtGui.QKeySequence('Ctrl+v'),self).activated.connect(self._handlePaste)
		self.setHorizontalHeaderLabels(['State','Time(uS)'])

		self.setTextElideMode(QtCore.Qt.ElideRight)
		self.setGridStyle(QtCore.Qt.DashLine)
		self.setRowCount(200)
		self.setColumnCount(2)
		self.horizontalHeader().setDefaultSectionSize(70)
		self.horizontalHeader().setMinimumSectionSize(70)
		self.horizontalHeader().setSortIndicatorShown(False)
		self.horizontalHeader().setStretchLastSection(True)
		self.verticalHeader().setStretchLastSection(True)

		for a in range(200):
			item =self.item(a,1)
			if item==None:
				item = QtGui.QTableWidgetItem()
				self.setItem(a,0,item)
			item.setText(['ON','OFF'][a%2])

	# paste the value  
	def _handlePaste(self):
		txt = QtGui.QApplication.instance().clipboard().text()
		row = 0; col = 0;
		for a in txt.split('\n'):
			for b in a.split('\t'):
				item = QtGui.QTableWidgetItem()
				item.setText(b)
				self.setItem(row, col, item)
				col+=1
			row+=1;col=0


class AppWindow(QtGui.QMainWindow, firePulses.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle('Fire Pulses on SQR1(beta. May cause comm errors) : '+self.I.H.version_string.decode("utf-8"))
		self.table = myTable()
		self.tableLayout.addWidget(self.table)
		a1={'TITLE':'SQR1','MIN':100,'MAX':100000,'FUNC':self.presetSQR1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1'}
		self.widgetLayout.addWidget(self.dialAndDoubleSpinIcon(**a1))

	def presetSQR1(self,val):
		return self.I.sqr1(val,50,True)

	def fire(self):
		tbl = []
		for a in range(200):
			item = self.table.item(a,1)
			if item:
				try:
					tbl.append (float(item.text()))
				except:
					QtGui.QMessageBox.about(self, 'Error','Check data points')
					return
			else:
				break
		if len(tbl):
			print (tbl)
		self.I.sqr1_pattern(tbl)


	def __del__(self):
		print ('bye')
				
if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())
