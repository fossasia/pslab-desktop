#!/usr/bin/python

"""

::

    This experiment is used to study ...


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'water.png',
'name':"Resistance of\nWater",
'hint':'''
	Measure the AC , and DC resistance of water.
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)

		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.I=kwargs.get('I',None)
		self.I.set_pv3(2.0)
		self.setWindowTitle(params.get('name','').replace('\n',' ') )
		self.prescalerValue=0
		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','V (CH1)', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)

		self.I.select_range('CH1',4)
		self.I.select_range('CH2',4)

		self.p2=self.enableRightAxis(self.plot)
		self.plot.getAxis('right').setLabel('V (CH2)', units='V', color='#ff0000')

		self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
		self.tg=5.
		self.max_samples=2000; self.samples = self.max_samples
		self.plot.setLimits(yMax=4,yMin=-4,xMin=0,xMax=self.samples*self.tg*1e-6);self.plot.setYRange(-4,4)
		self.p2.setLimits(yMax=4,yMin=-4); self.p2.setYRange(-4,4)

		self.timer = self.newTimer()
		self.sinewidget = self.addW1(self.I)
		self.WidgetLayout.addWidget(self.sinewidget)
		self.sinewidget.dial.setValue(500)

		self.legend = self.plot.addLegend(offset=(-10,-30))
		self.curve1 = self.addCurve(self.plot,'Voltage Drop across R(CH1)')
		self.curve2 = self.addCurve(self.p2,'Original Voltage (CH2)',pen=(255,0,0))
		self.legend.addItem(self.curve2,'Original Voltage (CH2)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		#Control widgets

		self.res = self.spinIcon(TITLE = 'Resistance(R)',MIN=100,MAX=20000,TOOLTIP="Enter the value of the resistor you connected between CH1 and GND",FUNC=lambda x:x,UNITS=u"\u03A9")
		self.res.spinBox.setValue(10000)
		self.WidgetLayout.addWidget(self.res)
		self.meterCH1 = self.displayIcon(TITLE = 'Voltages',TOOLTIP="Displays RMS voltage of CH1 and CH2")
		self.WidgetLayout.addWidget(self.meterCH1)
		self.meterCH2 = self.displayIcon(TITLE = 'Current and resistance',TOOLTIP="Displays current flow")
		self.WidgetLayout.addWidget(self.meterCH2)

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
			self.I.configure_trigger(1,'CH2',0)
			self.I.capture_traces(2,self.samples,self.tg)
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
			self.I.__fetch_channel__(2)
			
			Y1 = self.I.achans[0].get_yaxis()
			Y2 = self.I.achans[1].get_yaxis()
			self.curve1.setData(self.I.achans[0].get_xaxis()*1e-6,Y1,connect='finite')
			self.curve2.setData(self.I.achans[1].get_xaxis()*1e-6,Y2,connect='finite')

			RMS1 = self.math.RMS(Y1)
			RMS2 = self.math.RMS(Y2)			
			self.meterCH1.setValue('Voltage(CH1)=%s\nVoltage(CH2)=%s'%(self.applySIPrefix(RMS1,'V'),self.applySIPrefix(RMS2,'V')))
			try:
				I = RMS1/self.res.spinBox.value()
				self.meterCH2.setValue('Resistance(water)=%s\nCurrent=%s'%(self.applySIPrefix((RMS2-RMS1)/I,u"\u03A9"),self.applySIPrefix(I,'A')))
			except:
				pass

			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis(),self.I.achans[1].get_yaxis()],[(0,255,0),(255,0,0)])
		
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
		self.saveDataWindow([self.curve1,self.curve2],self.plot)

		
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

