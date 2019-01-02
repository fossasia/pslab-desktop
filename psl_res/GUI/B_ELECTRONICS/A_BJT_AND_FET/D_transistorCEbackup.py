#!/usr/bin/python
'''
Study Common Emitter Characteristics of NPN transistors.
Saturation currents, and their dependence on base current 
can be easily visualized.

'''

from __future__ import print_function
import time,sys,os

from PSL_Apps.utilitiesClass import utilitiesClass
from templates import ui_transistor as transistor
from PyQt5 import QtCore, QtGui
import pyqtgraph as pg

import numpy as np

params = {

'image' : 'transistorCE.png',
'name':'BJT CE\nBackup',
'hint':'''
	Study the dependence of common emitter Characteristics of NPN transistors on base current .\n uses PV1 as the voltage source for setting collector voltage,\n and PV2 with a 200K resistor connected in series as the base current source.\nThe collector voltage is monitored via CH1. 
	'''
}
class AppWindow(QtGui.QMainWindow, transistor.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.I.set_gain('CH1',2)

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.curves={0:[],1:[],2:[]}
		self.curveLabels={0:[],1:[],2:[]}

		self.sig = self.rightClickToZoomOut(self.plot)
		
		self.xlabels = ['Collector-Emitter Voltage','Base-Emitter Voltage','Collector-Emitter Voltage']
		self.ylabels = ['Collector-Emitter Current','Collector-Emitter Current','Collector-Base-Current']

		self.titles=['Output Characteristics','Input Characteristics','Transfer Characteristics']
		self.biasLabels = ['Base Voltage (PV2)','Collector Voltage(PV1)','Emitter Voltage Voltage(PV2)']
		self.biasValues = [1,-1,-1]
		self.sweepLabels = ['Collector Sweep(PV1)','Base Sweep(PV2)','Base Sweep(PV2)']
		self.sweepLimits=[5,3.3,3.3]
		self.biasLimits=[3.3,5,3.3]

		self.plotType = 0
		self.optionsBox.addItems(['Output Characteristics (Ice  -  Vce)','Input Characteristics (Ice  -  Vbe)','Transfer Characteristics (Ibe  -  Ice)'])

		self.totalpoints=2000
		self.X=[]
		self.Y=[]
		self.BR = 200e3
		self.CR = 1e3
		
		self.looptimer = self.newTimer()
		self.looptimer.timeout.connect(self.acquire)
		self.running = True
		self.START=0
		self.STOP=4
		self.STEP =0.2
		self.XMIN = 0; self.XMAX = 4

	def savePlots(self):
		self.saveDataWindow(self.curves[self.plotType],self.plot)
		print (self.curves[self.plotType])

	def typeChanged(self,num):
		self.plotType = num
		for a in self.curves:
			for b in self.curves[a]:
				if num==a:b.setEnabled(True)
				else:b.setEnabled(False)

		self.plot.setLabel('left',self.ylabels[num], units='A')
		self.plot.setLabel('bottom',self.xlabels[num], units='V')
		self.msg.setText(self.titles[num])
		self.biasLabel.setText(self.biasLabels[num])
		self.biasV.setValue(self.biasValues[num])

		self.biasV.setMinimum(self.biasLimits[num]*-1); self.biasV.setMaximum(self.biasLimits[num])
		self.sweepLabel.setText(self.sweepLabels[num])
		self.startV.setMinimum(self.sweepLimits[num]*-1); self.startV.setMaximum(self.sweepLimits[num])
		self.stopV.setMinimum(self.sweepLimits[num]*-1); self.stopV.setMaximum(self.sweepLimits[num])



	def run(self):
		self.looptimer.stop()
		self.X=[];self.Y=[]
		self.BV = self.biasV.value()

		self.START = self.startV.value()
		self.STOP = self.stopV.value()
		self.STEP = (self.STOP-self.START)/self.totalPoints.value()
		self.V = self.START

		P=self.plot.getPlotItem()
		if self.plotType==0:   #'Ice  -  Vce'
			#Calculate base current by measuring drop across 200K resistor
			vpv = self.I.set_pv2(self.BV) # set base current. pv2+200K resistor
			Vbe = self.I.get_average_voltage('CH3')
			self.base_current = (vpv-Vbe)/200e3
			print (vpv,Vbe,self.base_current)
			self.traceName = 'Ibe = %s'%self.applySIPrefix(self.base_current,'A')
			self.plot.setXRange(self.START,self.STOP)
			self.plot.setYRange(-5e-3,5e-3)
			self.I.set_pv1(self.V)

		elif self.plotType==1:   # 'Ice  -  Vbe'
			#Calculate collector current by measuring drop across 1K resistor
			vpv = self.I.set_pv1(self.BV) # set collector current. pv1+1K resistor
			Vce = self.I.get_average_voltage('CH1')
			BI = (vpv-Vce)/1e3
			print (vpv,Vce,BI)
			self.traceName = 'Ice = %s'%self.applySIPrefix(BI,'A')
			self.plot.setXRange(self.START,self.STOP)
			self.plot.setYRange(-30e-6,30e-6)
			self.I.set_pv1(self.V)

		else: #'Ibe  -  Ice'
			pass


		self.curves[self.plotType].append( self.addCurve(self.plot ,self.traceName) )		
		time.sleep(0.2)
		if len(self.curves[self.plotType])>1:P.enableAutoRange(True,True)
		if self.running:self.looptimer.start(20)


	def acquire(self):
		if self.plotType==0:
			V=self.I.set_pv1(self.V)
			VC =  self.I.get_average_voltage('CH1',samples=10)
			self.X.append(VC)
			self.Y.append((V-VC)/self.CR) # list( ( np.linspace(V,V+self.stepV.value(),1000)-VC)/1.e3)
		elif self.plotType==1: #set pv2, measure ch3
			V=self.I.set_pv2(self.V)
			VC =  self.I.get_average_voltage('CH3',samples=10)
			self.X.append(VC)
			self.Y.append((V-VC)/self.BR) # list( ( np.linspace(V,V+self.stepV.value(),1000)-VC)/1.e3)
		elif self.plotType==2: #set pv2, measure ch3
			V=self.I.set_pv2(self.V)
			VC =  self.I.get_average_voltage('CH3',samples=10)
			self.X.append(VC)
			self.Y.append((V-VC)/self.BR) # list( ( np.linspace(V,V+self.stepV.value(),1000)-VC)/1.e3)


		self.curves[self.plotType][-1].setData(self.X,self.Y)
		self.V+=self.STEP
		pos = 100*(1.*(self.V-self.START)/(self.STOP-self.START))
		self.progress.setValue(pos)
		if self.V>self.stopV.value():
			self.looptimer.stop()
			txt='<div style="text-align: center"><span style="color: #FFF;font-size:8pt;">%s</span></div>'%(self.traceName)
			text = pg.TextItem(html=txt, anchor=(0,0), border='w', fill=(0, 0, 255, 100))
			self.plot.addItem(text)
			text.setPos(self.X[-1],self.Y[-1])
			self.curveLabels[self.plotType].append(text)
			self.tracesBox.addItem(self.traceName)

	def delete_curve(self):
		c = self.tracesBox.currentIndex()
		if c>-1:
			self.tracesBox.removeItem(c)
			self.removeCurve(self.plot,self.curves[self.plotType][c]);
			self.plot.removeItem(self.curveLabels[self.plotType][c]);
			self.curves[self.plotType].pop(c);self.curveLabels[self.plotType].pop(c);


	def __del__(self):
		self.looptimer.stop()
		print ('bye')

	def closeEvent(self, event):
		self.looptimer.stop()
		self.finished=True


if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())





