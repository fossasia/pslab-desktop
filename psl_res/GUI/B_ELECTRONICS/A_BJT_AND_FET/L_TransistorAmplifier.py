#!/usr/bin/python

"""

::

    This experiment is used to study non-inverting amplifiers

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'transamp.png',
'name':'BJT\nAmplifier',
'hint':'''
	Study a simple transistor based amplifier.<br>
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

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.enableCrossHairs(self.plot,[])
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','V (CH1)', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time', units='S',**labelStyle)
		self.plot.setYRange(-8.5,8.5)

		self.p2=self.enableRightAxis(self.plot)
		self.plot.getAxis('right').setLabel('V (CH2)', units='V', color='#ff0000')


		self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
		self.tg=2
		self.max_samples=2000
		self.samples = self.max_samples
		self.timer = self.newTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curveCH1 = self.addCurve(self.plot,'INPUT(CH1)')
		self.curveCH2 = self.addCurve(self.plot,'OUTPUT(CH2)')
		self.curveCH2=self.addCurve(self.p2,'OUTPUT(CH2)')
		self.curveCH2.setPen(color=(255,0,0))
		self.autoRange()
		
		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		self.ControlsLayout.setAlignment(QtCore.Qt.AlignRight)

		#Utility widgets
		self.sinewidget = self.addW1(self.I)
		self.WidgetLayout.addWidget(self.sinewidget)
		self.sinewidget.dial.setValue(500)

		pv = self.addPV3(self.I)
		self.WidgetLayout.addWidget(pv)
		pv.dial.setValue(2048)  #midpoint


		a1={'TITLE':'Measure Gain','FUNC':self.measureGain,'TOOLTIP':'Curve fit the traces and find the gain of the circuit'}
		self.ampGain = self.buttonIcon(**a1)
		self.WidgetLayout.addWidget(self.ampGain)


		#Control widgets
		a1={'TITLE':'TIMEBASE','MIN':0,'MAX':9,'FUNC':self.set_timebase,'UNITS':'S','TOOLTIP':'Set Timebase of the oscilloscope'}
		self.ControlsLayout.addWidget(self.dialIcon(**a1))

		G = self.gainIcon(FUNC=self.I.set_gain,LINK=self.gainChanged)
		self.ControlsLayout.addWidget(G)
		G.g1.setCurrentIndex(7)
		G.g2.setCurrentIndex(1)

		self.running=True
		self.fit = False
		self.timer.singleShot(100,self.run)

	def measureGain(self):
		self.fit=True
		return 'measuring..'

	def gainChanged(self,g):
		self.autoRange()

	def set_timebase(self,g):
		timebases = [1.5,2,4,8,16,32,128,256,512,1024]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
		self.tg=timebases[g]
		self.samples = int(self.max_samples*samplescaling[g])
		return self.autoRange()

	def autoRange(self):
		xlen = self.tg*self.samples*1e-6
		self.plot.autoRange();
		chan = self.I.analogInputSources['CH1']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
		self.plot.setYRange(min(R),max(R))			
		self.plot.setXRange(0,xlen)

		chan = self.I.analogInputSources['CH2']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.p2.setYRange(min(R),max(R))			
		self.p2.setLimits(yMax=max(R),yMin=min(R))

		return self.samples*self.tg*1e-6



	def run(self):
		if not self.running: return
		try:
			self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
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
			
			self.curveCH1.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
			self.curveCH2.setData(self.I.achans[1].get_xaxis()*1e-6,self.I.achans[1].get_yaxis(),connect='finite')
			
			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[self.I.achans[0].get_yaxis(),self.I.achans[1].get_yaxis()],[(0,255,0),(255,0,0)])
			
			if self.fit:
				self.fit = False
				try:
					fitres = self.math.sineFit(self.I.achans[0].get_xaxis(),self.I.achans[0].get_yaxis())
					fitres2 = self.math.sineFit(self.I.achans[1].get_xaxis(),self.I.achans[1].get_yaxis())
					if fitres and fitres2:
						amp,freq,offset,phase = fitres
						amp2,freq2,offset2,phase2 = fitres2
						if abs(freq-freq2)<10: #Within error
							self.ampGain.value.setText('CH1=%s\nCH2=%s\nGain = %.3f'%(self.applySIPrefix(amp,'V'),self.applySIPrefix(amp2,'V'),amp2/amp))
						else: self.ampGain.value.setText('Fit Error')
				except:
					self.ampGain.value.setText('Fit Error')
					pass
				
			
			if self.running:self.timer.singleShot(200,self.run)
		except Exception as e:
			print (e)

	def saveData(self):
		self.saveDataWindow([self.curveCH1,self.curveCH2],self.plot)

		
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

