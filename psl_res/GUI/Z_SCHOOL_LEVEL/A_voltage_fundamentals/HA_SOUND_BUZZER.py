#!/usr/bin/python

"""

::

    This experiment is used to ...


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from scipy.signal import butter, lfilter
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'beats.png',
'name':"Piezo\nBuzzer",
'hint':'''
	Using a piezo buzzer with the function generator, and measuring its output using the microphone input
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)

		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.I=kwargs.get('I',None)
		self.I.configure_trigger(0,'MIC',0,prescaler = 1)
		
		self.setWindowTitle(params.get('name','').replace('\n',' ') )
		self.prescalerValue=0
		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','V (CH1)', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)

		self.tg=5.
		self.max_samples=2000; self.samples = self.max_samples
		self.plot.setLimits(yMax=3.3,yMin=-3.3,xMin=0,xMax=self.samples*self.tg*1e-6);self.plot.setYRange(-3.3,3.3)
		
		self.timer = self.newTimer()
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT (MIC)')
		self.curve2 = self.addCurve(self.plot,'INPUT (CH2)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		#Control widgets
		self.w1 = self.addW1(self.I)
		self.WidgetLayout.addWidget(self.w1)

		self.M1 = self.displayIcon(TITLE = 'CH2 Analysis',TOOLTIP="Displays amplitude, frequency of CH2 input")
		self.WidgetLayout.addWidget(self.M1)

		self.M2 = self.displayIcon(TITLE = 'MIC Analysis',TOOLTIP="Displays amplitude, frequency of MIC input")
		self.WidgetLayout.addWidget(self.M2)

		#self.dial = self.dialIcon(TITLE = 'F center',MIN=10,MAX=10000,FUNC=lambda x:x,TOOLTIP="Displays amplitude, frequency of MIC input")
		#self.WidgetLayout.addWidget(self.dial)

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
			self.I.capture_traces(2,self.samples,self.tg,'MIC')
			if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+50,self.plotData)
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
			self.I.__fetch_channel__(2)
			yaxis = self.I.achans[0].get_yaxis()
			F_center = 50.#self.dial.dial.value()
			yaxis = self.math.butter_notch_filter(yaxis,F_center-2,F_center+2,1e6/self.I.timebase,2)
			self.curve1.setData(self.I.achans[0].get_xaxis()*1e-6,yaxis,connect='finite')
			self.curve2.setData(self.I.achans[1].get_xaxis()*1e-6,self.I.achans[1].get_yaxis(),connect='finite')
			self.math.sineFitAndDisplay(self.I.achans[0],self.M2)
			self.math.sineFitAndDisplay(self.I.achans[1],self.M1)
			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis()],[(0,255,0),(255,0,0)])		
			if self.running:self.timer.singleShot(100,self.run)
		except Exception as e:
			print (e)

	def crossHairEvent(self,plot,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		if plot.sceneBoundingRect().contains(pos):
			plot.mousePoint = plot.getPlotItem().vb.mapSceneToView(pos)
			plot.vLine.setPos(plot.mousePoint.x())
			plot.hLine.setPos(plot.mousePoint.y())
			self.displayCrossHairData(plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis(),self.I.achans[1].get_yaxis()],[(0,255,0),(255,0,0)])

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

