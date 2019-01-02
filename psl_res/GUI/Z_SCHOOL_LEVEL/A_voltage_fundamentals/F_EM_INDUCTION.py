#!/usr/bin/python

"""

::

    This experiment is used to study phase shift oscillators


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'acgen.png',
'name':"Electromagnetic\nInduction",
'hint':'''
	Study the voltage induced in a coil due a changing magnetic field.<br>A pendulum with a neodymium magnet as the bob is made to oscillate near a coil<br>
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

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False); self.plot.setMouseEnabled(False,True)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.I.set_gain('CH1',7)
		self.plot.setYRange(-.5,.5)
		self.plot.setLimits(yMax=.5,yMin=-.5)

		self.samples = 2000
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT (CH1)')
		self.X=np.linspace(-10,0,self.samples);self.Y = np.zeros(self.samples)
		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		self.addPauseButton(self.bottomLayout,self.pause)
		self.paused=False;self.running=True
		self.timer = self.newTimer()
		self.timer.timeout.connect(self.run_np)
		self.num=0
		self.ST=time.time()
		self.timer.start(3)

	def pause(self,v):
		self.paused = v


	def run_np(self):
		if self.paused or not self.running: return
		
		self.X = np.roll(self.X,-1)
		self.Y = np.roll(self.Y,-1)
		self.X[-1]=(time.time()-self.ST)
		self.Y[-1]=self.I.get_average_voltage('CH1')
		self.num+=1
		if self.num%10==0:
			self.curve1.setData(self.X,self.Y)
			self.plot.enableAutoRange(axis = self.plot.plotItem.vb.XAxis)


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

