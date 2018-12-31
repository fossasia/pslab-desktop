#!/usr/bin/python

"""

::

    This experiment is used to study.....


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time
import random

params = {
'image' : 'ico_random.png',
'name':"Random\nSampling",
'hint':'''
	measure voltages of an input signal at random intervals, and plot a histogram that shows the time spent in each amplitude range	
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
		self.bins=200

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Points', units='',**labelStyle)
		self.plot.setLabel('bottom','Voltage', units='V',**labelStyle)
		self.plot.enableAutoRange(True,True)
		self.I.set_gain('CH1',1)
		self.plot.setLimits(xMin=-6,xMax=6)
		self.timer = self.newTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT (CH1)')

		#Control widgets
		self.WidgetLayout.addWidget(self.dualButtonIcon(A='START',B='STOP',FUNCA=self.start,FUNCB=self.stop,TITLE='sampling'))
		self.WidgetLayout.addWidget(self.dualButtonIcon(A='Sinusoidal',B='Triangular',FUNCA=self.set_sine,FUNCB=self.set_tria,TITLE='W1 type'))
		self.WidgetLayout.addWidget(self.simpleButtonIcon(FUNC=self.clear,TITLE='CLEAR\nPLOT'))
		self.binIcon = self.dialIcon(FUNC=self.setBins,TITLE='# of Bins',MIN=10,MAX=300)
		self.binIcon.dial.setValue(200)
		self.WidgetLayout.addWidget(self.binIcon)

		self.W1 = self.addWG(self.I,{'type':'W1','name':'SINE1'},self.ControlsLayout)
		self.SQR1 =self.addWG(self.I,{'type':'SQR1','name':'SQR1'},self.ControlsLayout)
		self.W1.dial.setMinimum(70)
		self.W1.dial.setMaximum(250)

		self.SQR1.dial.setMinimum(20)
		self.SQR1.dial.setMaximum(150)

		self.running=True
		self.vals=[]
		self.timer.timeout.connect(self.run)

	def setBins(self,b):
		self.bins = b
		return b

	def clear(self):
		self.plot.enableAutoRange(True,True)
		self.timer.stop()
		self.vals=[]
		self.curve1.clear()

	def start(self):
		self.timer.start(0)

	def stop(self):
		self.timer.stop()

	def set_sine(self):
		self.I.load_equation('W1','sine')

	def set_tria(self):
		self.I.load_equation('W1','tria')

	def run(self):
		if not self.running: return
		self.vals.append(self.I.get_average_voltage('CH1'))
		if len(self.vals)%100==0:
			if len(self.vals)>10:
				y,x = np.histogram(self.vals, bins=np.linspace(min(self.vals), max(self.vals), self.bins))
				self.curve1.setData(x,y, stepMode=True, fillLevel=0, brush=(0,0,255,150))
		time.sleep(random.random()*1e-6)

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

