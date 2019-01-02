#!/usr/bin/python
'''

'''

from __future__ import print_function
import os

from PSL_Apps.utilitiesClass import utilitiesClass
from PyQt5 import QtCore, QtGui
import time,sys

import sys

import pyqtgraph as pg
from PSL_Apps.templates import ui_template_bandpass as template_bandpass

import numpy as np

params = {
'image' : 'bodeplot.jpg',
'helpfile': 'transistorCE.html',
'name':'Piezo Bandwidth\nCharacteristics',
'hint':'''
	Study frequency response of a piezo buzzer using an audio microphone.<br>
	Curve fitting routines extract data and plot the dependence of amplitude on input frequency.
	'''

}

class AppWindow(QtGui.QMainWindow, template_bandpass.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.I.set_gain('CH1',2)
		self.I.set_gain('CH2',2)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )


		self.plot1=self.add2DPlot(self.plot_area)
		self.plot2=self.add2DPlot(self.plot_area)
		
		self.legend = self.plot1.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot1,'INPUT (CH2)')
		self.curve2 = self.addCurve(self.plot1,'OUTPUT(MIC)')
		self.plot2.getAxis('left').setLabel('Amplitude', color='#ffffff')

		self.plot1.getAxis('bottom').setLabel('Time',units='S' ,color='#ffffff')
		self.plot2.getAxis('bottom').setLabel('Frequency',units='Hz', color='#ffffff')
		self.curveAmp = self.addCurve(self.plot2,'AMPLITUDE',pen=[255,255,255])

		self.samples = 5000
		self.X=[]
		self.Y=[]
		
		self.curves=[]
		self.curveLabels=[]

		from PSL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		self.I.configure_trigger(1,'CH2',0)
		self.I.set_sine1(2)
		self.I.set_gain('CH2',2)
		self.startFreq.setValue(3000)
		self.stopFreq.setValue(4000)

		self.freqs=[]
		self.amps=[]
		self.dP=[]
		self.STARTFRQ=self.startFreq.value()		
		self.ENDFRQ=self.stopFreq.value()
		self.STEPFRQ=self.stepFreq.value()
		self.loop=None
		self.plot2.setXRange(self.STARTFRQ,self.ENDFRQ)
		self.plot2.setYRange(0,1.)
		self.plot1.setLimits(xMin = 0,yMin=-8,yMax=8)		
		self.running = False


	def setStartFreq(self,val):
		self.STARTFRQ=val		
	def setStopFreq(self,val):
		self.ENDFRQ=val		
	def setFreqStep(self,val):
		self.STEPFRQ=val
		self.DELTAFRQ = (self.ENDFRQ-self.STARTFRQ)/self.STEPFRQ		

	def run(self):
		if(self.running): return
		self.running=True
		self.freqs=[]
		self.amps=[]
		self.dP=[]

		self.STARTFRQ=self.startFreq.value()
		self.ENDFRQ=self.stopFreq.value()
		self.STEPFRQ=self.stepFreq.value()
		self.DELTAFRQ = (self.ENDFRQ-self.STARTFRQ)/self.STEPFRQ
		print ('from %d to %d in %.3fHz steps'%(self.STARTFRQ,self.ENDFRQ,self.DELTAFRQ))
		self.frq=self.STARTFRQ
		self.I.set_sine1(self.frq)
		self.plot2.setXRange(self.STARTFRQ,self.ENDFRQ)
		self.plot2.setLimits(xMax=self.ENDFRQ,xMin = self.STARTFRQ)			

		if self.running:self.loop = self.delayedTask(100,self.newset)

	def stop(self):
		self.running = False
		self.progress.setValue(100)

	def stopSweep(self):
		self.running=False
		
	def newset(self):
		if(not self.running):return
		frq = self.I.set_sine1(self.frq)
		time.sleep(0.01)
		tg=int(1e6/frq/500)+1
		
		self.I.capture_traces(2,self.samples,tg,'MIC',trigger=True)
		self.loop=self.delayedTask(self.samples*self.I.timebase*1e-3+10,self.plotData,frq)		
		self.plot1.setLimits(xMin = 0,xMax = self.samples*self.I.timebase*1e-6)


		self.frq+=self.DELTAFRQ
		pos = 100*(1.*(self.frq-self.STARTFRQ)/(self.ENDFRQ-self.STARTFRQ))
		self.progress.setValue(pos)
		if(self.frq>self.ENDFRQ and self.DELTAFRQ>0) or (self.frq<self.ENDFRQ and self.DELTAFRQ<0):
			print ('og',self.frq,self.ENDFRQ,self.DELTAFRQ)
			self.running=False
			#txt='<div style="text-align: center"><span style="color: #FFF;font-size:8pt;">%d-%d</span></div>'%(self.STARTFRQ,self.ENDFRQ)
			#text = pg.TextItem(html=txt, anchor=(0,0), border='w', fill=(0, 0, 255, 100))
			#self.plot2.addItem(text)
			#text.setPos(self.X[-1],self.Y[-1])
			#self.curveLabels.append(text)
			self.curves.append(self.curveAmp)
			self.I.set_w1(0.2)

	def plotData(self,frq):		
		if(not self.running):return
		x,y=self.I.fetch_trace(2)   #CH2 . Input
		self.curve1.setData(x*1e-6,y)

		x,y=self.I.fetch_trace(1)   #Microphone
		self.curve2.setData(x*1e-6,y)
		pars2 = self.CC.sineFit(x,y)#),freq=self.frq)
		if pars2:
			a2,f2,o2,p2 = pars2
			if a2 and (abs(f2-frq)<10):
				#self.msg.setText("Set F:%.1f\tFitted F:%.1f"%(frq,f1))
				self.freqs.append(frq)
				self.amps.append(a2)
			else:
				print ('err!')
			#print chisq2[0]
			self.curveAmp.setData(self.freqs,self.amps)
		if self.running:self.loop = self.delayedTask(10,self.newset)
		
		

	def showData(self):
		self.displayObjectContents({'Frequency Response':np.column_stack([self.freqs,self.amps,self.dP])})

	def savePlots(self):
		self.saveDataWindow([self.curveAmp],self.plot2)


	def clearData(self):
		self.freqs=[]
		self.amps=[]
		self.dP=[]
		self.curveAmp.clear()
		self.frq=self.STARTFRQ
		print ('cleared data')

	def delete_curve(self):
		c = self.tracesBox.currentIndex()
		if c>-1:
			self.tracesBox.removeItem(c)
			#self.plot.removeItem(self.curves[c]);self.plot.removeItem(self.curveLabels[c]);
			#self.curves.pop(c);self.curveLabels.pop(c);


	def __del__(self):
		print ('bye')

	def closeEvent(self, event):
		self.finished=True
		self.running =False


if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

