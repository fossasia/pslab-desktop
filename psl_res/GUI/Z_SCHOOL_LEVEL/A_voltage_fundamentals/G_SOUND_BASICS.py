#!/usr/bin/python

"""

::

    This experiment is used to study ..


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
'image' : 'ampmod.png',
'name':"Frequency of\nSound",
'hint':'''
	Study various sounds, and analyze their frequencies
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)

		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.I=kwargs.get('I',None)
		self.setWindowTitle(params.get('name','').replace('\n',' ') )
		self.prescalerValue=0
		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','V (CH1)', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)

		self.plotF=self.add2DPlot(self.plot_area,enableMenu=False)
		self.plotF.setLabel('bottom', 'Frequency', units='Hz')
		self.plotF.autoRange();self.plotF.getPlotItem().setMouseEnabled(True,False)


		self.tg=20.
		self.max_samples=5000; self.samples = self.max_samples
		self.plot.setLimits(yMax=3,yMin=-3,xMin=0,xMax=self.samples*self.tg*1e-6);self.plot.setYRange(-3,3)
		
		self.plotF.setLimits(yMax=3,yMin=-0.001,xMin=70,xMax=20e3);self.plotF.setYRange(-0.001,3)

		self.timer = self.newTimer()
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT (MIC)')
		self.curveFFT = self.addCurve(self.plotF,'Fourier Transform')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		#Control widgets

		self.voltmeterF = self.displayIcon(TITLE = 'Analysis',TOOLTIP="Displays amplitude, frequency of MIC input")
		self.WidgetLayout.addWidget(self.voltmeterF)

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
			self.I.capture_traces(1,self.samples,self.tg,'MIC')
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
			yaxis = self.I.achans[0].get_yaxis()
			F_center = 50.#self.dial.dial.value()
			yaxis = self.math.butter_notch_filter(yaxis,F_center-2,F_center+2,1e6/self.I.timebase,2)
			self.curve1.setData(self.I.achans[0].get_xaxis()*1e-6,yaxis,connect='finite')
			self.math.sineFitAndDisplay(self.I.achans[0],self.voltmeterF)

			x,y = self.math.fft(yaxis,self.I.timebase*1e-6)
			self.curveFFT.setData(x,y,connect='finite');self.plotF.autoRange();

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

