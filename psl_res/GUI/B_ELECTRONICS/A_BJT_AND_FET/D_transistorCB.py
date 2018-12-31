#!/usr/bin/python
'''
Study NJFET
Saturation currents, and their dependence on gate voltage 
can be easily visualized.

'''

from __future__ import print_function
import time,sys,os

from PSL_Apps.utilitiesClass import utilitiesClass
from .templates import ui_NFET as NFET
from PyQt5 import QtCore, QtGui
import pyqtgraph as pg

import numpy as np

params = {

'image' : 'transistorCE.png',
'name':'BJT CB\nCharacteristics',
'hint':'''
	Study the common base Characteristics of NPN transistors .
	'''
}
class AppWindow(QtGui.QMainWindow, NFET.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.I.set_gain('CH1',2)

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.sig = self.rightClickToZoomOut(self.plot)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Drain Current', units='A',**labelStyle)
		self.plot.setLabel('bottom','Drain-Source Voltage', units='V',**labelStyle)
		
		self.sweepLabel.setText('Collector Sweep(PV1)')
		self.biasLabel.setText('Emitter Voltage(PV2)')
		self.totalpoints=2000
		self.X=[]
		self.Y=[]
		self.RESISTANCE = 560
		
		self.curves=[]
		self.curveLabels=[]
		self.looptimer = self.newTimer()
		self.looptimer.timeout.connect(self.acquire)
		self.running = True
		self.START=0
		self.STOP=4
		self.STEP =0.2

	def savePlots(self):
		self.saveDataWindow(self.curves,self.plot)


	def run(self):
		self.looptimer.stop()
		self.X=[];self.Y=[]
		self.base_voltage = self.biasV.value()

		self.curves.append( self.addCurve(self.plot ,'Vb = %.3f'%(self.base_voltage))  )

		self.I.set_pv2(self.base_voltage) # set base current. pv2+200K resistor

		self.START = self.startV.value()
		self.STOP = self.stopV.value()
		self.STEP = (self.STOP-self.START)/self.totalPoints.value()
		#print ('from %d to %d in %.3fV steps'%(self.START,self.STOP,self.STEP))
		
		self.V = self.START
		self.I.set_pv1(self.V) 
		time.sleep(0.2)

		P=self.plot.getPlotItem()
		self.plot.setXRange(-2,self.stopV.value())
		self.plot.setYRange(-5e-3,5e-3)
		if len(self.curves)>1:P.enableAutoRange(True,True)

		if self.running:self.looptimer.start(20)

	def acquire(self):
		V=self.I.set_pv1(self.V)
		VC =  self.I.get_average_voltage('CH1',samples=10)
		self.X.append(VC)
		self.Y.append((V-VC)/self.RESISTANCE) # list( ( np.linspace(V,V+self.stepV.value(),1000)-VC)/1.e3)
		self.curves[-1].setData(self.X,self.Y)

		self.V+=self.STEP
		if self.V>self.stopV.value():
			self.looptimer.stop()
			txt='<div style="text-align: center"><span style="color: #FFF;font-size:8pt;">%.3f V</span></div>'%(self.base_voltage)
			text = pg.TextItem(html=txt, anchor=(0,0), border='w', fill=(0, 0, 255, 100))
			self.plot.addItem(text)
			text.setPos(self.X[-1],self.Y[-1])
			self.curveLabels.append(text)
			self.tracesBox.addItem('Vb = %.3f'%(self.base_voltage))

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

