#!/usr/bin/python

"""

::

    This experiment is used to study Full wave rectifiers


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass
from PSL.analyticsClass import analyticsClass

from PSL_Apps.templates import template_graph_nofft

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'fullwave.png',
'name':'Full Wave\nRectifier',
'hint':'''
	Study Full Wave rectifiers.<br>
	Connect Wavegen 1 to a diode as well as CH1.<br>
	Connect Wavegen 2 to a reversed diode as well as CH2.<br>
	connect the other end of both the diodes to CH3.<br>
	Provide a load resistor(1K) from CH2 to ground.<br>
	Set 180 phase difference between the wave generators and Observe full wave rectification.<br>
	Add a capacitor in parallel to the load resistor and observe filter effects.
	
	'''

}

class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.tg=2
		self.I.configure_trigger(0,'CH1',0)
		self.I.set_gain('CH1',2)
		self.I.set_gain('CH2',2)
		self.samples = 2000
		self.max_samples=2000
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time -->', units='S',**labelStyle)
		self.plot.setYRange(-5.3,5.3)
		self.plot.setLimits(yMax=5.3,yMin=-5.3,xMin=0, xMax = self.samples*self.tg*1e-6)
		self.timer = QtCore.QTimer()

		self.curveCH1 = self.addCurve(self.plot,'INPUT 1(CH1)')
		self.curveCH2 = self.addCurve(self.plot,'INPUT 2(CH2)')
		self.curveCH3 = self.addCurve(self.plot,'OUTPUT(CH3)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		self.sineSection = self.sineWidget(self.I)
		self.WidgetLayout.addWidget(self.sineSection)

		self.sinewidget = self.addW1(self.I,self.updateLabels)
		self.WidgetLayout.addWidget(self.sinewidget)
		self.sinewidget.dial.setValue(500)
		self.WidgetLayout.addWidget(self.addTimebase(self.I,self.set_timebase))


		self.running=True
		self.timer.singleShot(100,self.run)

		
		
	def run(self):
		if not self.running:return
		self.I.capture_traces(3,self.samples,self.tg)
		if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+10,self.plotData)

	def saveData(self):
		self.saveDataWindow([self.curveCH1,self.curveCH2,self.curveCH3],self.plot)

	def plotData(self): 
		n=0
		while(not self.I.oscilloscope_progress()[0]):
			time.sleep(0.1)
			print (self.timebase,'correction required',n)
			n+=1
			if n>10:
				if self.running:self.timer.singleShot(100,self.run)
				return
		self.I.__fetch_channel__(1)
		self.I.__fetch_channel__(2)
		self.I.__fetch_channel__(3)
		self.curveCH1.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
		self.curveCH2.setData(self.I.achans[1].get_xaxis()*1e-6,self.I.achans[1].get_yaxis(),connect='finite')
		self.curveCH3.setData(self.I.achans[2].get_xaxis()*1e-6,self.I.achans[2].get_yaxis(),connect='finite')
		if self.running:self.timer.singleShot(100,self.run)

	def setSineWaves(self,freq):
		return self.I.set_waves(freq,180)

	def updateLabels(self,value,units=''):
		self.sineSection.WAVE1_FREQ.setText('%.3f %s '%(value,units))
		self.sineSection.WAVE2_FREQ.setText('%.3f %s '%(value,units))
		self.sineSection.SINEPHASE.setValue(180)



	def set_timebase(self,g):
		try:
			timebases = [1.5,2,4,8,16,32,128,256,512,1024]
			self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
			samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
			self.tg=timebases[g]
			self.samples = int(self.max_samples*samplescaling[g])
			xlen = self.samples*self.tg*1e-6
			self.plot.setLimits(xMax = xlen)
			self.plot.setXRange(0,xlen)
			return xlen
		except Exception,e:
			print(e)
		
	def closeEvent(self, event):
		self.running=False
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print ('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

