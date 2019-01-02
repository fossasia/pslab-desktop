#!/usr/bin/python

"""

::

    This experiment is used to study........

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'ldr.png',
'name':"Light Dependent\nResistor",
'hint':'''
	Observe the workings of a light dependent Resistor.<br>
	Use it to study the 50 Hz fluctuation of flourescent lamps.
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Resistance', units=u"\u03A9",**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)

		self.tg=30.
		self.max_samples=1000
		self.samples = self.max_samples
		self.plot.setLimits(yMax=50e3,yMin=0,xMin=0,xMax=1e-6*self.tg*self.samples)
		self.plot.setYRange(1e3,30e3)
		self.timer = self.newTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'RESISTANCE (SEN)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		#Control widgets

		self.sqr = self.dialIcon(TITLE='SQR1',MIN=10,MAX=300,FUNC=self.I.sqr1,UNITS='Hz',TOOLTIP='Frequency of square wave generator #1\n0 for switched off, Max for On state')
		self.WidgetLayout.addWidget(self.sqr)
		
		self.voltmeter = self.displayIcon(TITLE = 'Average Resistance',UNITS=u"\u03A9",TOOLTIP='')
		self.WidgetLayout.addWidget(self.voltmeter)

		self.addPauseButton(self.bottomLayout,self.pause)
		self.running=True
		self.paused=False
		self.timer.singleShot(100,self.run)

	def pause(self,v):
		self.paused = v

	def run(self):
		if not self.running: return
		if self.paused:
			self.timer.singleShot(100,self.run)
			return
		try:
			self.I.capture_traces(1,self.samples,self.tg,'SEN',trigger=False)
			if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+10,self.plotData)
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
			V = np.clip(self.I.achans[0].get_yaxis(),0,3.2)
			I = (3.3-V)/5.1e3
			R = V/I
			self.curve1.setData(self.I.achans[0].get_xaxis()*1e-6,R,connect='finite')
			self.voltmeter.setValue(self.math.RMS(R))
			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[V],[(0,255,0)])		
			if self.running:self.timer.singleShot(100,self.run)
		except Exception as e:
			print (e)

	def crossHairEvent(self,plot,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		if plot.sceneBoundingRect().contains(pos):
			plot.mousePoint = plot.getPlotItem().vb.mapSceneToView(pos)
			plot.vLine.setPos(plot.mousePoint.x())
			plot.hLine.setPos(plot.mousePoint.y())
			self.displayCrossHairData(plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis()],[(0,255,0)])

	def saveData(self):
		self.saveDataWindow([self.curve1],self.plot)

		
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

