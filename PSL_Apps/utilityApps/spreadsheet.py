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
from .templates import ui_aboutDevice as aboutDevice
import sys

try:
    unicode        # Python 2
except NameError:
    unicode = str  # Python 3


class AppWindow(QtGui.QMainWindow, aboutDevice.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.data = kwargs.get('data',[])
		self.setWindowTitle('Data')
		self.table.setColumnWidth(0,200)
		self.table.setRowCount(len(self.data)+1)
		xpos=0;ypos=0
		for a in self.data:
			xpos=0
			for b in a:
				item = QtGui.QTableWidgetItem()
				self.table.setItem(ypos,xpos,item)
				item.setText('%s'%b)
				xpos+=1
			ypos+=1
		self.maxRows=ypos
		self.maxCols=xpos

	def setColumn(self,col,data):
		ypos=0
		if col > self.maxCols:
			self.maxCols = col
			self.table.setColumnCount(col+1)

		if len(data) > self.maxRows:
			self.maxRows = len(data)
			self.table.setRowCount(self.maxRows+1)


		for a in data:
			item = QtGui.QTableWidgetItem()
			self.table.setItem(ypos,col,item)
			item.setText('%s'%a)
			ypos+=1


	def save(self):  #Save as CSV
		path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '~/', 'CSV(*.csv)')
		if path:
			import csv
			with open(unicode(path), 'wb') as stream:
				delim = [' ','\t',',',';']
				writer = csv.writer(stream, delimiter = delim[self.delims.currentIndex()])
				if self.headerBox.isChecked():
					headers = []
					try:
						for column in range(self.table.columnCount()):headers.append(self.table.horizontalHeaderItem(column).text())
						writer.writerow(headers)
					except:
						pass
				#writer.writeheader()
				for row in range(self.table.rowCount()):
					rowdata = []
					for column in range(self.table.columnCount()):
						item = self.table.item(row, column)
						if item is not None:
							rowdata.append(	unicode(item.text()).encode('utf8'))
						else:
							rowdata.append('')
					writer.writerow(rowdata)
		

	def __del__(self):
		print ('bye')
                
if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(data=[[0,1],[1,2]])
    myapp.show()
    sys.exit(app.exec_())
