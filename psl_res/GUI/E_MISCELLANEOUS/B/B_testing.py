#!/usr/bin/python
'''
Streaming Utility for FOSSASIA PSLab - version 1.0.0.

Evaluates user defined python statements and plots
the return values as a function of time.
Useful for monitoring time evolution of parameters
measured by the PSLab
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt4 import QtCore, QtGui
import time,sys
from .templates import arbitStream

import sys,os,string
import time
import sys

import pyqtgraph as pg

import numpy as np


err_count=0
trial = 0
start_time = time.time()
fps = None
dacval=0


params = {
'image' : 'stream.png',
'name':'Testing',
'hint':'A continuous data acquisition utility to visualize time dependent behaviour of any of the measurement functions contained in thePSLab  python library.\nThese include get_freq,get_capacitance, and get_average_voltage'
}

class AppWindow(QtGui.QMainWindow, arbitStream.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=pg.PlotWidget()
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Value -->', units='',**labelStyle)

		self.totalpoints=2000
		self.X=np.arange(self.totalpoints)
		self.Y=np.zeros(self.totalpoints)

		self.plot.setXRange(0,self.totalpoints)
		self.plot.setYRange(-16,16)
		self.curve = self.plot.plot(name='C1'); self.curve.setPen(color=[255,255,255], width=1)

		self.streamfunc="I."+self.cmdlist.currentText()
		self.start_time=time.time()
		self.num=0
		self.arrow=pg.ArrowItem(angle=90)
		self.plot.addItem(self.arrow)
		self.plot_area.addWidget(self.plot)

		self.looptimer = QtCore.QTimer()
		self.looptimer.timeout.connect(self.acquire)
		self.looptimer.start(1)

		self.nm=0
		self.start_time=time.time()
		self.averagingSamples = 1
		self.I.set_sine2(4)
		self.I.DAC.setVoltage('PV1',-2)
		self.I.DAC.setVoltage('PV2',-1)
		self.I.DAC.setVoltage('PV3',1)

	def stream(self):
		self.looptimer.stop()
		self.streamfunc="I."+self.cmdlist.currentText()
		self.X=np.arange(self.totalpoints)
		self.Y=np.zeros(self.totalpoints)
		self.num=0

		self.looptimer = QtCore.QTimer()
		self.looptimer.timeout.connect(self.acquire)
		self.looptimer.start(1)

	def setAveraging(self):
		self.averagingSamples = self.averageCount.value()

	def acquire(self):
		#if(self.nm<4095):
		#	self.ad.set_voltage(self.nm)
		#	self.nm+=1
		#self.Y=np.roll(self.Y,-1)
		val=np.average([eval(self.streamfunc,{'I':self.I}) for a in range(self.averagingSamples)])
		self.Y[self.num]=val	#self.mag.read()[1]
		self.msg.setText('%.4f'%(val))
		try:
			self.arrow.setPos(self.num,self.Y[self.num])
		except:
			print (self.num)
		self.num+=1
		if self.num>=self.totalpoints:
			self.num=0
		T=time.time()
		if T-self.start_time>0.5:
			self.curve.setData(self.X,self.Y)
			self.start_time = T

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
		self.looptimer.stop()
		print ('bye')

	def closeEvent(self, event):
		self.looptimer.stop()
		self.finished=True


if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
