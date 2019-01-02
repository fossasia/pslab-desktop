#!/usr/bin/python

"""

::

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass
from PSL.analyticsClass import analyticsClass

from templates import ui_simplePendulum

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,time

params = {
'image' : 'transient.png',
'name':'Simple Pendulum',
'hint':'''
	Study Simple pendulum's velocity oscillations.<br>
	Connect a pendulum to the shaft of a simple DC motor.<br>
	Connect one terminal of the motor to GND, and the other to CH3.<br>
	The voltage output from the motor due to the rotating shaft has low amplitude, so connect a 100 ohm resistor from Rg to GND.<br>
	This sets a gain of around 100x, and allows clear visualization of oscillations
	'''

}

class AppWindow(QtGui.QMainWindow, ui_simplePendulum.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.CC = analyticsClass()
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time -->', units='S',**labelStyle)

		self.plot.setYRange(-8.5,8.5)
		self.tg=100
		self.tgLabel.setText('total time: ' + str(5000*self.tg*1e-3)+'mS')
		self.x=[]
		self.CParams=[0,0,0,0,0]

		self.FitTable.setHorizontalHeaderLabels(['Amp','Freq','Phase','Offset','Damping'])
		for a in range(5):
			item = QtGui.QTableWidgetItem()
			self.FitTable.setItem(0,a,item)
			item.setText('Nil')


		self.curveCH1 = self.addCurve(self.plot,'CH3')
		self.CH1Fit = self.addCurve(self.plot,'CH3 Fit')
		self.region = pg.LinearRegionItem([self.tg*50*1e-6,self.tg*800*1e-6])
		self.region.setZValue(-10)
		self.plot.addItem(self.region)		
		self.msg.setText("Function:offset+A*exp(-damp*x)*sin(x*freq+ph)")
		self.running=True
		self.Params=[]
		self.looptimer=QtCore.QTimer()
		self.looptimer.timeout.connect(self.updateProgress)
		self.I.set_w1(1)
	
	def updateProgress(self):
		v=(time.time()-self.curT)*100/(self.maxT-self.curT)
		if time.time()>self.maxT:
				self.looptimer.stop()
				v=100
		self.progressBar.setValue(v)
		
	def start(self):
		if not self.running:return
		self.I.__capture_fullspeed_hr__('CH3',5000,self.tg)
		self.CH1Fit.setData([],[])
		self.curT = time.time()
		self.maxT = self.curT+5000*self.tg*1e-6
		self.looptimer.start(300)
		self.loop=self.delayedTask(5000*self.I.timebase*1e-3+10,self.plotData)

	def plotData(self):	
		self.x,self.VMID=self.I.__retrieveBufferData__('CH3',self.I.samples,self.I.timebase)#self.I.fetch_trace(1)
		self.VMID = self.I.analogInputSources['CH3'].calPoly12(self.VMID)
		self.curveCH1.setData(self.x*1e-6,self.VMID)

	def setTimebase(self,T):
		self.tgs = [100,200,300,500,800,1000,2000,3000,5000,8000]
		self.tg = self.tgs[T]
		self.tgLabel.setText('total time: ' + str(5000*self.tg*1e-3)+'mS')

	def fit(self):
		if(not len(self.x)):return
		start,end=self.region.getRegion()
		print (start,end,self.I.timebase)
		if(start>0):start = int(round(1.e6*start/self.I.timebase ))
		else: start=0
		if(end>0):end = int(round(1.e6*end/self.I.timebase ))
		else:end=0
		guess = self.CC.getGuessValues(self.x[start:end]-self.x[start],self.VMID[start:end],func='damped sine')
		Csuccess,Cparams,chisq = self.CC.arbitFit(self.x[start:end]-self.x[start],self.VMID[start:end],self.CC.dampedSine,guess=guess)

		if Csuccess:
			showVals = [Cparams[0],1e6*abs(Cparams[1])/(2*np.pi),Cparams[2]*180/np.pi,Cparams[3],Cparams[4]]
			for a in range(5):
				item = self.FitTable.item(0,a)
				item.setText('%.2e'%showVals[a])
			self.CH1Fit.setData(self.x[start:end]*1e-6,self.CC.dampedSine(self.x[start:end]-self.x[start],*Cparams))
			self.CParams=Cparams
		else:
			for a in range(5):
				item = self.FitTable.item(0,a)
				item.setText('Nil')
			self.CH1Fit.clear()

	def saveData(self):
		self.saveDataWindow([self.curveCH1,self.CH1Fit],self.plot)


	def closeEvent(self, event):
		self.running=False
		self.looptimer.stop()

		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

