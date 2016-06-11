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


from PyQt4 import QtCore, QtGui
from .templates import loadSineTable
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


class AppWindow(QtGui.QMainWindow, loadSineTable.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle('Load arbitrary waveforms : '+self.I.H.version_string.decode("utf-8"))
		self.table = myTable()
		self.tableLayout.addWidget(self.table)
		

	def reset1(self):
		self.I.load_equation('W1','sine')
		y1=np.sin(np.linspace(0,np.pi*2,512+1)[:-1])
		for a in range(512):
			item =self.table.item(a,0)
			if item==None:
				item = QtGui.QTableWidgetItem()
				self.table.setItem(a,0,item)
			item.setText('%.5f'%y1[a])
		QtGui.QMessageBox.about(self, 'Sine Wave','Table Contents set to sine')

	def reset2(self):
		self.I.load_equation('W2','sine')
		y1=np.sin(np.linspace(0,np.pi*2,512+1)[:-1])
		for a in range(512):
			item =self.table.item(a,1)
			if item==None:
				item = QtGui.QTableWidgetItem()
				self.table.setItem(a,1,item)
			item.setText('%.5f'%y1[a])
		QtGui.QMessageBox.about(self, 'Sine Wave','Table Contents set to sine')


	def setTria1(self):
		function = lambda x: abs(x%4-2)-1
		span = np.linspace(-1,3,512)
		for a in range(512):
			item =self.table.item(a,0)
			if item==None:
				item = QtGui.QTableWidgetItem()
				self.table.setItem(a,0,item)
			item.setText('%d'%abs(a-256))
			item.setText('%d'%(512*function(span[a])) )
		self.loadSine1('tria')
		QtGui.QMessageBox.about(self, 'Triangular Wave','Table Contents set to Triangular')

	def setTria2(self):
		function = lambda x: abs(x%4-2)-1
		span = np.linspace(-1,3,512)
		for a in range(512):
			item =self.table.item(a,1)
			if item==None:
				item = QtGui.QTableWidgetItem()
				self.table.setItem(a,1,item)
			item.setText('%d'%(512*function(span[a])))
		self.loadSine2('tria')
		QtGui.QMessageBox.about(self, 'Triangular Wave','Table Contents set to Triangular')


	def loadSine1(self,mode='arbit'):
		tbl = []
		for a in range(512):
			item = self.table.item(a,0)
			if item:
				try:
					tbl.append (float(item.text()))
				except:
					break
			else:
				break
		if len(tbl)==512:
			print ('loading table')
			self.I.load_table('W1',tbl,mode)
		else:
			QtGui.QMessageBox.about(self, 'Error','Check data points')

	def loadSine2(self,mode='arbit'):
		tbl = []
		for a in range(512):
			item = self.table.item(a,1)
			if item:
				try:
					tbl.append (float(item.text()))
				except:
					break
			else:
				break
		if len(tbl)==512:
			print ('loading table')
			self.I.load_table('W2',tbl,mode)
		else:
			QtGui.QMessageBox.about(self, 'Error','Check data points')

	def __del__(self):
		print ('bye')
				
if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())
