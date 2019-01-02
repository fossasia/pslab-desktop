#!/usr/bin/python

"""

::

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from templates import ui_template_transient as template_transient
from PSL.SENSORS import MPU6050
import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys

params = {
'image' : 'transient.png',
#'helpfile': 'https://en.wikipedia.org/wiki/LC_circuit',
'name':'MPU6050 IMU\nPendulum',
'hint':'''
	Use an accelerometer and gyroscope(MPU6050) to study position versus time, and velocity versus time of pendulums.
	'''
}

class AppWindow(QtGui.QMainWindow, template_transient.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.IMU = MPU6050.connect(self.I.I2C)
		from PSL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot1=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot1.setLabel('left','Acceleration -->', units='V',**labelStyle)
		self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)

		self.tg=2000
		self.samples = 1000
		self.tgLabel.setText(str(self.samples*self.tg*1e-3)+'mS')
		self.curveGx = self.addCurve(self.plot1,'Gx')
		self.curveGy = self.addCurve(self.plot1,'Gy')
		self.curveGz = self.addCurve(self.plot1,'Gz')
		self.plot2 = self.addAxis(self.plot1)
		self.curveAx = self.addCurve(self.plot2,'Ax')
		self.curveAy = self.addCurve(self.plot2,'Ay')
		self.curveAz = self.addCurve(self.plot2,'Az')
		self.curves = [self.curveAx,self.curveAy,self.curveAz,self.curveGx,self.curveGy,self.curveGz]
		self.curveNames=['Ax','Ay','Az','Gx','Gy','Gz']
		self.legend=self.plot1.addLegend(offset=(-10,30))

		for a in range(6):
			self.legend.addItem(self.curves[a],self.curveNames[a])

		self.datasets = [[],[],[],[],[],[]]
		self.looptimer=QtCore.QTimer()
		self.region = pg.LinearRegionItem([self.tg*50*1e-6,self.tg*800*1e-6])
		self.region.setZValue(-10)
		self.plot1.addItem(self.region)		
		self.lognum=0
		self.msg.setText("Fitting fn :\noff+amp*exp(-damp*x)*sin(x*freq+ph)")
		self.Params=[]
		
	def run(self):
		t = self.I.I2C.__captureStart__(self.IMU.ADDRESS,0x3B,14,self.samples,self.tg)
		self.plot1.setXRange(0,t)
		self.plot1.setLimits(xMin = 0,xMax=t)

		print ("Sleeping for",t,"S",t)
		self.loop=self.delayedTask(t*1e3,self.plotData)  #t+10uS per sample

	def plotData(self):
		data = self.I.I2C.__retrievebuffer__()
		self.t,self.Ax,self.Ay,self.Az,_,self.Gx,self.Gy,self.Gz = self.I.I2C.__dataProcessor__(data,'int')
		print (len(self.t),len(self.Ax))
		self.curveAx.setData(self.t*1e-6,self.Ax)
		self.curveAy.setData(self.t*1e-6,self.Ay)
		self.curveAz.setData(self.t*1e-6,self.Az)
		self.curveGx.setData(self.t*1e-6,self.Gx)
		self.curveGy.setData(self.t*1e-6,self.Gy)
		self.curveGz.setData(self.t*1e-6,self.Gz)
		self.datasets = [self.Ax,self.Ay,self.Az,self.Gx,self.Gy,self.Gz]


	def setTimebase(self,T):
		self.tgs = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
		self.tg = self.tgs[T]
		self.tgLabel.setText(str(self.samples*self.tg*1e-3)+'mS')

	def fit(self):
		if(not len(self.t)):return
		start,end=self.region.getRegion()
		print (start,end,self.tg)
		if(start>0):start = int(round(1.e6*start/self.tg ))
		else: start=0
		if(end>0):end = int(round(1.e6*end/self.tg ))
		else:end=0
		DT = self.t[start:end]-self.t[start]
		msg = ''
		for a in range(6):
			guess = self.CC.getGuessValues(DT*1e-6,self.datasets[a][start:end],func='damped sine')
			Csuccess,Cparams,chisq = self.CC.arbitFit(DT*1e-6,self.datasets[a][start:end],self.CC.dampedSine,guess=guess)
			if Csuccess:
				msg+="%s: A:%.2f\tF:%.3f Hz\tPh:%.1f\tDamp:%.3e\n"%(self.curveNames[a],Cparams[0],abs(Cparams[1])/(2*np.pi),Cparams[2]*180/(np.pi),Cparams[4])
				self.curves[a].setData(self.t[start:end]*1e-6,self.CC.dampedSine(DT*1e-6,*Cparams))
			else:
				msg+="Fit Failed. Change selected region.\n"
				#self.curves[a].clear()
		self.displayDialog(msg)

	def showData(self):
		self.displayDialog('nothing')

	def saveData(self):
		self.saveDataWindow([self.curveGx,self.curveGy,self.curveGz,self.curveAx,self.curveAy,self.curveAz],self.plot1)

		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

