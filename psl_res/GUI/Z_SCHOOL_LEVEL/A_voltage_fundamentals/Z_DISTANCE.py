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
'image' : 'HCSR04.png',
'name':"Ultrasonic\nRange Finder",
'hint':'''
	Measure distances using an ultrasound based distance sensor HC-SR04<br> This sensor measures distances to flat surfaces placed in front of it by bouncing sound pulses off it, and measuring the round trip delay
	'''
}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)		
		self.I.set_state(SQR2=1)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False); self.plot.setMouseEnabled(False,True)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Distance', units='M',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.plot.setYRange(0,.5)
		self.plot.setLimits(yMax=2,yMin=0)

		self.samples = 1000
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'Distance(METERS)')
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
		D = self.I.estimateDistance()
		if D<0.5:
			self.msg.setText('%.1f cms'%(D*100))
			self.X = np.roll(self.X,-1)
			self.Y = np.roll(self.Y,-1)
			self.X[-1]=(time.time()-self.ST)
			self.Y[-1]=D
			self.num+=1
			if self.num%10==0:
				self.curve1.setData(self.X,self.Y)
		else:
			self.msg.setText('Object not detected')
			
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

