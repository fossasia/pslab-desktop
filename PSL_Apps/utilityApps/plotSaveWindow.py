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
from templates import plotSave
import sys,os,time
import pyqtgraph as pg



class AppWindow(QtGui.QMainWindow, plotSave.Ui_MainWindow):
	def __init__(self, parent ,curveList,plot):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self), QtCore.SIGNAL('activated()'), self.close)
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(plotSave._translate("MainWindow", "Ctrl+P", None)), self), QtCore.SIGNAL('activated()'), self.printImage)
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(plotSave._translate("MainWindow", "Ctrl+C", None)), self), QtCore.SIGNAL('activated()'), self.copyToClipboard)
		
		self.table.setColumnWidth(0,200)
		colnum=0;labels=[]
		self.maxRows=0
		self.maxCols=0
		for a in curveList:
			x,y = a.getData()
			name = a.name()
			if x!=None and y!=None:
				self.setColumn(colnum,x);colnum+=1
				self.setColumn(colnum,y);colnum+=1
				labels.append('%s(X)'%(name));labels.append('%s(Y)'%(name));
		self.table.setHorizontalHeaderLabels(labels)		

		self.plot = plot
		if plot:
			self.imageWidthBox.setEnabled(True)
			self.saveImageButton.setEnabled(True)
			self.imageWidthBox.setValue(self.plot.plotItem.width())
			
			
			
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
			item.setText('%.3e'%a)
			ypos+=1


	def saveImage(self):  #Save as png or something
		path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '~/')
		if path:
			pieces = path.split('.')
			if len(pieces)<2: #No extension specified
				path+='.png'
			elif pieces[-1] not in QtGui.QImageWriter.supportedImageFormats(): #Wrong extension specified
				import string
				path = string.join(pieces[:-1]+['png'],'.')
				QtGui.QMessageBox.about(self,'Invalid Filename','Modified : '+path)
			import pyqtgraph.exporters
			exporter = pg.exporters.ImageExporter(self.plot.plotItem)
			exporter.parameters()['width'] = self.imageWidthBox.value()
			exporter.export(path)

	def printImage(self): 
		import pyqtgraph.exporters
		self.exporter = pg.exporters.PrintExporter(self.plot.plotItem)
		#exporter.parameters()['width'] = self.imageWidthBox.value()
		self.exporter.export()

	def copyToClipboard(self): 
		import pyqtgraph.exporters
		self.exporter = pg.exporters.ImageExporter(self.plot.plotItem)
		self.exporter.parameters()['width'] = self.imageWidthBox.value()
		self.exporter.export(copy=True)
		QtGui.QMessageBox.about(self,'Copy Plot','Plot Image Copied to clipboard')

	

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
