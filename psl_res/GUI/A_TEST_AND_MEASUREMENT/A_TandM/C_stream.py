#!/usr/bin/python
'''
Streaming Utility for PSLab.

Evaluates user defined python statements and plots
the return values as a function of time.
Useful for monitoring time evolution of parameters
measured by the PSLab
'''

from __future__ import print_function

import time,sys
from PSL_Apps.utilitiesClass import utilitiesClass
from templates import ui_arbitStream as arbitStream
from PyQt5 import QtCore, QtGui
import os,string

import pyqtgraph as pg
import numpy as np


params = {
'image' : 'ico_stream.png',
'name':'Data\nStreaming',
'hint':'A continuous data acquisition utility to visualize time dependent behaviour of any of the measurement functions contained in the PSLab python library.\nThese include get_freq,get_capacitance, and get_average_voltage'
}

class AppWindow(QtGui.QMainWindow, arbitStream.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)		
		self.funcs = {k: getattr(self.I, k) for k in dir(self.I)}
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()
		self.prescalerValue=0

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False); self.plot.setMouseEnabled(False,True)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)

		self.samples = 2000
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve = self.addCurve(self.plot,'INPUT')
		self.X=np.linspace(-10,0,self.samples);self.Y = np.zeros(self.samples)

		self.running=True
		self.timer = self.newTimer()
		self.timer.timeout.connect(self.run_np)
		self.num=0
		self.ST=time.time()
		self.LUT = 0
		self.timer.start(1)

		self.streamfunc=self.cmdlist.currentText()
		self.averagingSamples = 1

	def stream(self):
		self.timer.stop()
		self.streamfunc=self.cmdlist.currentText()
		self.X=np.linspace(-10,0,self.samples);self.Y = np.zeros(self.samples)
		self.timer = self.newTimer()
		self.timer.timeout.connect(self.run_np)
		self.num=0
		self.LUT = 0
		self.ST=time.time()
		self.timer.start(1)

	def pause(self,v):
		self.paused = v


	def setAveraging(self):
		self.averagingSamples = self.averageCount.value()


	def run_np(self):
		if self.pause.isChecked() or not self.running: return

		self.X = np.roll(self.X,-1)
		self.Y = np.roll(self.Y,-1)
		self.X[-1]=(time.time()-self.ST)
		val=np.average([eval(self.streamfunc,globals(),self.funcs) for a in range(self.averagingSamples)])
		self.Y[-1]=val
		self.num+=1
		if (self.X[-1]-self.LUT)>.2: #1 sec graph refresh
			if not np.all(self.Y==np.inf):self.curve.setData(self.X,self.Y)
			self.plot.enableAutoRange(axis = self.plot.plotItem.vb.XAxis)
			self.msg.setText('%.4f'%(val))
			self.LUT = self.X[-1]
	def saveData(self):
		self.pause.setChecked(True)
		self.saveDataWindow([self.curve],self.plot)

	def setDelay(self,d):
		self.timer.stop()
		self.timer.start(d)

	def parseFunc(self,fn):
		fn_name=fn.split('(')[0]
		args=str(fn.split('(')[1]).split(',')
		int_args=[]
		try:
			args[-1]=args[-1][:-1]
			int_args=[string.atoi(t) for t in args]
		except: 
			int_args=[]	#in case the function has zero arguments, args[-1] will fail.
		method = getattr(self.I,fn_name)
		if method == None :
			print ('no such command :',fn_name)
			return None
		else:
			print (method,int_args)
			return method,int_args

	def __del__(self):
		self.timer.stop()

	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True


if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
