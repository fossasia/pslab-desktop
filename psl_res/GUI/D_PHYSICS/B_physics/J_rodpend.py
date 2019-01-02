#!/usr/bin/python

"""

::

    This experiment is used to calculate the value of acceleration due
    to gravity by measuring the time period of a pendulum

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from templates import ui_rodpendulum

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'transient.png',
'helpfile': '',
'name':'Pendulum\nTime period',
'hint':'''
	Calculate the time period of a pendulum by making it oscillate between a photogate. Using the obtained time period, and known equations of motion of the oscillating body, calculate the value of g
	'''
}

class AppWindow(QtGui.QMainWindow, ui_rodpendulum.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.max_points = 100
		self.pendulum='simple'
		self.resultsTable.setRowCount(self.max_points)
		for x in range(self.max_points):
				item = QtGui.QTableWidgetItem();self.resultsTable.setItem(x, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)

		self.progressBar.setMaximum(self.max_points)
		self.updatetimer = QtCore.QTimer()
		self.updatetimer.timeout.connect(self.update)
		self.updatetimer.start(200)



		self.resultsTable.setHorizontalHeaderLabels(['Time difference(uS)'])
		self.running=False
		self.currentRow=0		
		self.curpos=0
		self.overflowTime=time.time()
		self.setTotalPoints()
		
		
	def setTotalPoints(self):
		self.totalPoints = self.pointBox.value()*2+1
		self.progressBar.setMaximum(self.totalPoints)

	def clearTable(self):
		self.currentRow=0
		for x in range(100):
			self.resultsTable.item(x,0).setText('')

	def update(self):
		if self.running:
			states = self.I.get_LA_initial_states()
			a,b,c,d,e=states  #points acquired by ID1..4 , e=states of ID1..4
			
			if a==self.I.MAX_SAMPLES/4:a=0
			self.progressBar.setValue(a)

			if a >self.curpos:  #new datapoints available. load to table
				if a!=self.I.MAX_SAMPLES/4:
					tmp = self.I.fetch_long_data_from_LA(a,1)
					self.I.dchans[0].load_data(e,tmp)
					while self.currentRow < len(self.I.dchans[0].timestamps)/2-1:  #Alternate points will be used
							index = self.currentRow*2
							dt = self.I.dchans[0].timestamps[index+2]-self.I.dchans[0].timestamps[index]
							item = QtGui.QTableWidgetItem();item.setText('%.3e'%(dt)); self.resultsTable.setItem(self.currentRow, 0, item); item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
							self.currentRow+=1
					self.curpos = a


			if a>=self.totalPoints+1:
				self.I.stop_LA()
				self.displayDialog("Point Limit reached. Acquisition stopped ")
				self.running=False
				return

			if (time.time() - self.overflowTime)>60:
				self.I.stop_LA()
				self.displayDialog("One minute timeout exceeded. Please restart acquisition")
				self.running=False
			else:
				self.timerProgress.setValue(60+self.overflowTime-time.time() )


	def run(self):
		self.clearTable()
		self.I.start_one_channel_LA(channel='SEN',channel_mode=2,trigger_mode=0)  #every falling edge
		self.curpos=0;self.overflowTime=time.time()
		self.currentRow=0
		self.running=True
		

	def stop(self):
		self.I.stop_LA()
		self.running=False

	def calcAvg(self):
		x=self.fetchSelectedItemsFromColumns(self.resultsTable,1)[0]
		if len(x):self.averageLabel.setText('%.3e uS'%(np.average(x)))
		else:self.averageLabel.setText('Select some data')
		pass

	def setPendulumType(self,t):
		if t==0: #simple pendulum
			self.pendulum = 'simple'
		elif t==1: #rod pendulum
			self.pendulum = 'rod'

	def calculateg(self):
		x=self.fetchSelectedItemsFromColumns(self.resultsTable,1)[0]
		if len(x):
			t = np.average(x)*1e-6 #Convert to seconds
			length = self.lenBox.value()*1e-2 #Convert to metres
			if self.pendulum=='simple':
				g = length*4*np.pi*np.pi/(t*t)
				self.gLabel.setText('%.3f m/s^2'%(g))
			elif self.pendulum=='rod':
				length*=2/3.
				g = length*4*np.pi*np.pi/(t*t)
				self.gLabel.setText('%.3f m/s^2'%(g))
		else:
			self.gLabel.setText('Select some data')


	def saveData(self):
		self.saveToCSV(self.resultsTable)

	def closeEvent(self, event):
		self.running=False
		self.updatetimer.stop()
		self.finished=True

	def __del__(self):
		self.updatetimer.stop()
		print ('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

