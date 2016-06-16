#!/usr/bin/python

"""

::

    This experiment is used to study non-inverting amplifiers

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import template_graph_nofft

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'halfwave.png',
'name':'TCD1304AP\nCCD',
'hint':'''
	Acquire and plot data from a linear CCD array TCD1304AP.<br>
	Experimental feature. Sine waves will be disabled while it runs.<br>
	'''

}

class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()
		self.prescalerValue=0

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot,[])
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','V (CH1)', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.plot.setYRange(-8.5,8.5)

		self.I.configure_trigger(0,'CH3',0,prescaler = self.prescalerValue)
		self.tg=1; self.icg=10000;self.tp=4
		self.max_samples=2000
		self.chan = 'CH1'
		self.samples = self.max_samples
		self.timer = QtCore.QTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curveCH1 = self.addCurve(self.plot,'INPUT(CH1)')
		self.autoRange()
		
		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		self.ControlsLayout.setAlignment(QtCore.Qt.AlignRight)

		#Utility widgets
		self.I.set_pv1(4)

		#Control widgets
		a1={'TITLE':'TIMEBASE','MIN':1,'MAX':10,'FUNC':self.set_timebase,'UNITS':'S','TOOLTIP':'Set Timebase of the oscilloscope'}
		self.ControlsLayout.addWidget(self.dialIcon(**a1))

		a1={'TITLE':'ICG','MIN':1,'MAX':10000,'UNITS':'S','FUNC':self.set_icg,'UNITS':'S','TOOLTIP':'Set ICG'}
		self.WidgetLayout.addWidget(self.dialIcon(**a1))

		a1={'TITLE':'TP','MIN':64,'MAX':100,'UNITS':'S','FUNC':self.set_tp,'UNITS':'S','TOOLTIP':'Set TP'}
		self.WidgetLayout.addWidget(self.dialIcon(**a1))


		self.running=True
		self.fit = False
		self.timer.singleShot(100,self.run)



	def set_timebase(self,g):
		self.tg=g
		self.samples = int(self.max_samples)
		return self.autoRange()

	def set_icg(self,g):
		self.icg = g
		return g*1e-6

	def set_tp(self,g):
		self.tp = g
		return g*1e-6

	def autoRange(self):
		xlen = self.tg*self.samples*1e-6
		self.plot.autoRange();
		chan = self.I.analogInputSources[self.chan]
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
		self.plot.setYRange(min(R),max(R))			
		self.plot.setXRange(0,xlen)

		return self.samples*self.tg*1e-6



	def run(self):
		if not self.running: return
		try:
			self.I.opticalArray(self.tg,self.icg,self.tp,channel = self.chan)
			if self.running:self.timer.singleShot(self.samples*self.tg*1e-3+10+self.icg*1e-3,self.plotData)
		except:
			pass

	def plotData(self): 
		if not self.running: return
		try:
			n=0
			while(not self.I.oscilloscope_progress()[0]):
				time.sleep(0.1)
				n+=1
				if n>10:
					self.timer.singleShot(100,self.run)
					return
			self.I.__fetch_channel__(1)
			self.curveCH1.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
				
			
			if self.running:self.timer.singleShot(200,self.run)
		except Exception,e:
			print (e)

	def saveData(self):
		self.saveDataWindow([self.curveCH1,self.curveCH2],self.plot)

		
	def closeEvent(self, event):
		self.running=False
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

