#!/usr/bin/python

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from templates import ui_dsm501 as dsm501

import numpy as np
from PyQt5 import QtGui,QtCore
import sys,time

params = {
'image' : 'DSM501.png',
'helpfile': 'http://www.takingspace.org/make-your-own-aircasting-particle-monitor/',
'name':'Dust Sensor\nDSM501',
'hint':'''
	Study the concentration of PM2.5 particles over time using a DSM501/PPD42NS sensor. Connect PIN2 of the sensor to ID1, PIN3 to 5V, PIN5 to GND
	'''
}

class AppWindow(QtGui.QMainWindow, dsm501.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		self.plot1=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)
		self.plot1.getAxis('left').setLabel('Concentration -->>', color='#ffffff')
		self.plot1.setLimits(xMin=0,yMin=0)

		self.total_samples = 100
		self.acquired_samples = 0
		self.timegap = 10 #mS
		self.sampling_time = 2000 #mS
		
		self.timer2 = QtCore.QTimer()
		self.timer2.timeout.connect(self.updateProgress)
		self.timer2.start(500)
		self.I.set_state(SQR1=True)
		
		self.curve = self.addCurve(self.plot1,'Concentration')
		self.resultsTable.setRowCount(self.total_samples)
		self.resultsTable.setColumnCount(3)
		self.resultsTable.setHorizontalHeaderLabels(['time','Ratio %','Concentration mg/m^3'])

		self.running=False
		self.start_time = time.time()
		self.samplingStartTime=time.time()

		self.timer = self.newTimer()
		#self.running=True
		#self.timer.singleShot(0,self.run)
		
		self.X=[]
		self.Y=[]

	def start(self):
		self.X=[]
		self.Y=[]
		self.running = True
		self.timer.singleShot(0,self.run)

	def stop(self):
		self.running=False
		
	def updateProgress(self):
		if not self.running:return
		val = 1e5*(time.time()-self.samplingStartTime)/(self.sampling_time)
		self.timeProgressBar.setValue(val)
		
	def run(self):
		if not self.running:return
		self.samplingStartTime = time.time()
		self.sampling_time = self.integrationBox.value()*1e3 #convert to mS
		self.I.start_one_channel_LA(channel='ID1',channel_mode=1,trigger_mode=0)  #every edge
		if self.running: self.timer.singleShot(self.sampling_time,self.plotData)

	def plotData(self): 
		if not self.running:return
		a,b,c,d,e = self.I.get_LA_initial_states()
		if a==self.I.MAX_SAMPLES/4:	a = 0
		tmp = self.I.fetch_long_data_from_LA(a,1)
		print (a,b,c,d,e,tmp)
		self.I.dchans[0].load_data(e,tmp)
		#print (self.I.dchans[0].timestamps,self.I.dchans[0].initial_state)
		stamps = self.I.dchans[0].timestamps
		if len(stamps)>2:
			if not self.I.dchans[0].initial_state:
				stamps = stamps[1:] - stamps[0]
			diff = np.diff(stamps)
			lows = diff[::2]
			highs = diff[1::2]
			#print(stamps,sum(lows),sum(highs))
			low_occupancy = 100*sum(lows)/stamps[-1] #Occupancy ratio
			self.progressBar.setValue(low_occupancy)
			concentration = 1.1*pow(low_occupancy,3)-3.8*pow(low_occupancy,2)+520*low_occupancy+0.62; #From the spec sheet curve
			self.X.append(time.time()-self.start_time)
			self.Y.append(concentration)
			self.curve.setData(self.X,self.Y)
			item = QtGui.QTableWidgetItem();item.setText('%s'%(time.strftime("%H:%M:%S %d-%h")));self.resultsTable.setItem(self.acquired_samples, 0, item);#item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
			item = QtGui.QTableWidgetItem();item.setText('%.3f'%(low_occupancy));self.resultsTable.setItem(self.acquired_samples, 1, item);#item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
			item = QtGui.QTableWidgetItem();item.setText('%.3f'%(concentration));self.resultsTable.setItem(self.acquired_samples, 2, item);#item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
			self.acquired_samples +=1
			if self.acquired_samples==self.total_samples:
				self.total_samples = self.acquired_samples+10
				self.resultsTable.setRowCount(self.total_samples)
		if self.running: self.timer.singleShot(self.timegap,self.run)

	def saveData(self):
		self.saveDataWindow([self.curve],self.plot1)
		
	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True
		self.running = False
		

	def __del__(self):
		self.timer.stop()

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

