#!/usr/bin/python

"""

::

    This experiment is used to study .......


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'cap.png',
'name':"Capacitor\nDischarge",
'hint':'''
	Observe the voltage across a slowly discharging capacitor.<br>Also study how charge distributes across capacitors connected in parallel
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

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False); self.plot.setMouseEnabled(False,True)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Voltage', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.plot.setYRange(-.2,5)
		self.plot.setLimits(yMax=8,yMin=-0.2)
		self.plot.getViewBox().enableAutoRange(self.plot.getViewBox().XAxis)

		self.tg=100;self.samples = 1000
		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'Voltage(CH1)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		self.WidgetLayout.addWidget(self.simpleButtonIcon(TITLE='START',FUNC=self.start))
		self.WidgetLayout.addWidget(self.simpleButtonIcon(TITLE='STOP',FUNC=self.stop))
		self.ControlsLayout.addWidget(self.wideButtonIcon(TITLE='Voltage(CH1)',FUNC=self.get_voltage,UNITS='V'))
		self.addPauseButton(self.bottomLayout,self.pause)

		self.paused=False;self.running=True
		self.timer = self.newTimer()
		self.timer.timeout.connect(self.run_np)
		self.num=0
		self.I.set_state(SQR1=1)

	def get_voltage(self):
		return self.I.get_voltage('CAP')

	def pause(self,v):
		self.paused = v

	def start(self):
		self.num = 0
		self.X=[]
		self.Y=[]
		self.ST=time.time()
		self.timer.start(self.tg)
		return '%s'%self.applySIPrefix(self.I.get_voltage('CH1'),'V')

	def stop(self):
		self.timer.stop()
		return '%s'%self.applySIPrefix(self.I.get_voltage('CH1'),'V')


	def run_np(self):
		if self.paused or not self.running: return
		V=self.I.get_voltage('CH1')
		self.msg.setText('V = %.2f'%(V))
		self.X.append((time.time()-self.ST))
		self.Y.append(V)
		self.curve1.setData(self.X,self.Y)
		self.num+=1
		if self.num==self.samples:
			self.timer.stop()
			self.msg.setText("Finished logging")
			
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

