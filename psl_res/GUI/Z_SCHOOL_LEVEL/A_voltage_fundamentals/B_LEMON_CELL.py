#!/usr/bin/python

"""

::

    This experiment is used to..


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'lemon_cell.png',
'name':"Lemon Cell",
'hint':'''
	Make a cell using a lemon and study the output voltage.<br>
	Measure its internal resistance, as well as connect a few cells in series to drive an LED.
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.prescalerValue=0

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.plot.setYRange(-8.5,8.5)
		self.I.set_gain('CH1',1)
		self.I.set_gain('CH2',1)
		self.I.set_pv2(0);self.I.set_pv3(0)
		self.plot.setLimits(yMax=8,yMin=-8,xMin=0,xMax=4e-3)

		self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
		self.tg=5.
		self.max_samples=2000
		self.samples = self.max_samples
		self.autoRange()
		self.timer = self.newTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT (CH1)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		#Control widgets

		self.voltmeter = self.displayIcon(TITLE = 'CH1 Voltage',UNITS='V',TOOLTIP='Displays instantaneous voltage on CH1 using the voltmeter')
		self.WidgetLayout.addWidget(self.voltmeter)

		self.addPauseButton(self.bottomLayout,self.pause)
		self.running=True
		self.paused=False
		self.timer.singleShot(100,self.run)

	def pause(self,v):
		self.paused = v

	def autoRange(self):
		xlen = self.tg*self.samples*1e-6
		self.plot.autoRange();
		chan = self.I.analogInputSources['CH1']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
		self.plot.setYRange(min(R),max(R))			
		self.plot.setXRange(0,xlen)

		return self.samples*self.tg*1e-6

	def run(self):
		if not self.running: return
		if self.paused:
			self.timer.singleShot(100,self.run)
			return
		self.voltmeter.setValue(self.I.get_average_voltage('CH1'))
		
		try:
			self.I.configure_trigger(0,'CH1',0)
			self.I.capture_traces(1,self.samples,self.tg)
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
			
			self.curve1.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis()],[(0,255,0)])
		
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

