#!/usr/bin/python
'''
Study Current Voltage characteristics of PN junctions.
'''

from __future__ import print_function
import os

from PSL_Apps.utilitiesClass import utilitiesClass
from PyQt5 import QtCore, QtGui
import time,sys
from templates import ui_diodeIV as diodeIV

import sys

import pyqtgraph as pg

import numpy as np

params = {
'image' : 'diodeIV.png',
'helpfile': 'diodeIV.html',
'name':'Zener IV\nCharacteristics',
'hint':"Study Current-Voltage Characteristics of PN junctions.\n uses PV1 as the voltage source for sweeping voltage via a 1K current limiting resistor connected in series. \nThe voltage drop across the diode is monitored via CH3. "
}

class AppWindow(QtGui.QMainWindow, diodeIV.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Current -->', units='A',**labelStyle)
		self.plot.setLabel('bottom','Voltage -->', units='V',**labelStyle)
		self.startV.setValue(-5)
		
		self.totalpoints=2000
		self.X=[]
		self.Y=[]
		self.plotnum=0
				
		self.curves=[]
		self.curveLabels=[]
		self.looptimer = QtCore.QTimer()
		self.looptimer.timeout.connect(self.acquire)


	def savePlots(self):
		self.saveDataWindow(self.curves)

	def run(self):
		self.looptimer.stop()
		self.X=[];self.Y=[]
		self.plotnum+=1
		self.curves.append( self.addCurve(self.plot ,'Plot #%d'%(self.plotnum))  )

		self.V = self.startV.value()
		self.I.set_pv1(self.V) 
		time.sleep(0.2)

		P=self.plot.getPlotItem()
		P.enableAutoRange(True,True)
		self.plot.setXRange(-5,1)
		self.plot.setYRange(-4e-3,4e-3)
		self.looptimer.start(20)


	def acquire(self):
		V=self.I.set_pv1(self.V)
		VC =  self.I.get_voltage('CH1',samples=20)
		self.X.append(VC)
		self.Y.append((V-VC)/1.e3) # list( ( np.linspace(V,V+self.stepV.value(),1000)-VC)/1.e3)
		self.curves[-1].setData(self.X,self.Y)

		self.V+=self.stepV.value()
		if self.V>self.stopV.value():
			self.looptimer.stop()
			txt='<div style="text-align: center"><span style="color: #FFF;font-size:8pt;"># %d</span></div>'%(self.plotnum)
			text = pg.TextItem(html=txt, anchor=(0,0), border='w', fill=(0, 0, 255, 100))
			self.plot.addItem(text)
			text.setPos(self.X[-1],self.Y[-1])
			self.curveLabels.append(text)
			self.tracesBox.addItem('#%d'%(self.plotnum))

	def delete_curve(self):
		c = self.tracesBox.currentIndex()
		if c>-1:
			self.tracesBox.removeItem(c)
			self.removeCurve(self.plot,self.curves[c]);
			self.plot.removeItem(self.curveLabels[c]);
			self.curves.pop(c);self.curveLabels.pop(c);
			if len(self.curves)==0: # reset counter for plot numbers
				self.plotnum=0

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

