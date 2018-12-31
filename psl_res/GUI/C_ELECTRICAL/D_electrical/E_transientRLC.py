#!/usr/bin/python

"""

::

	This experiment is used to study the transient response of circuits
	
	The effect of a level change in the input voltage is monitored using the oscilloscope.

.. raw:: html

	<!-- Include the core jQuery and jQuery UI -->
	<script type='text/javascript' src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>

	<!-- Include the core media player JavaScript. -->
	<script type="text/javascript" src="js/osmplayer.compressed.js"></script>

	<!-- Include the DarkHive ThemeRoller jQuery UI theme. -->
	<link rel="stylesheet" href="js/jquery-ui.css">

	<!-- Include the Default template CSS and JavaScript. -->
	<link rel="stylesheet" href="js/osmplayer_default.css">
	<script type="text/javascript" src="js/osmplayer.default.js"></script>

	<script type="text/javascript">
	  $(function() {
		$("video").osmplayer({
		  width: '100%',
		  height: '400px'
		});
	  });
	</script>

	<video src="videos/lissajous.ogv" showcontrols="1"></video>



"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from .templates import ui_template_transient as template_transient

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,time

params = {
'image' : 'transient.png',
#'helpfile': 'https://en.wikipedia.org/wiki/LC_circuit',
'name':'Transient RLC\nResponse',
'hint':'''
	Study transient response of RLC circuits.<br>
	<i>SQR1</i> is used to provide the transient, and the midpoint of L and C is monitored via <i>CH1</i>'
	'''
}

class AppWindow(QtGui.QMainWindow, template_transient.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot1=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot1.setLabel('left','Voltage -->', units='V',**labelStyle)
		self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)

		self.plot1.setYRange(-8.5,8.5)
		self.I.set_gain('CH1',1)
		self.I.configure_trigger(0,'CH1',0)
		self.tg=1
		self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')
		self.x=[]

		self.looptimer=QtCore.QTimer()
		self.curveCH1 = self.addCurve(self.plot1,'CH1')
		self.CH1Fit = self.addCurve(self.plot1,'CH1 Fit')
		self.region = pg.LinearRegionItem([self.tg*50,self.tg*800])
		self.region.setZValue(-10)
		self.plot1.addItem(self.region)		
		self.lognum=0
		self.state=0
		self.I.set_state(SQR1=0)
		self.msg.setText("Fitting fn :\noff+amp*exp(-damp*x)*sin(x*freq+ph)")
		self.Params=[]

	def saveData(self):
		self.saveDataWindow([self.curveCH1,self.CH1Fit])
		
	def ZeroToFive(self):
		self.I.set_state(SQR1 = 0); time.sleep(0.2) #DisCharge Circuit
		self.I.__capture_fullspeed__('CH1',5000,self.tg,'SET_HIGH')
		self.tg = self.I.timebase
		self.CH1Fit.setData([],[])
		self.loop=self.delayedTask(5000*self.I.timebase*1e-3+10,self.plotData)

	def FiveToZero(self):
		self.I.set_state(SQR1 = 1); time.sleep(0.2) #Charge Circuit
		self.I.__capture_fullspeed_hr__('CH1',5000,self.tg,'SET_LOW')
		self.CH1Fit.setData([],[])
		self.loop=self.delayedTask(5000*self.I.timebase*1e-3+10,self.plotData)


	def plotData(self):	
		self.x,self.VMID=self.I.__retrieveBufferData__('CH1',self.I.samples,self.I.timebase)#self.I.fetch_trace(1)
		self.VMID = self.I.analogInputSources['CH1'].calPoly12(self.VMID)
		self.curveCH1.setData(self.x,self.VMID)


	def setTimebase(self,T):
		self.tgs = [1,2,4,6,8,10,25,50,80,100]
		self.tg = self.tgs[T]
		self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')

	def fit(self):
		if(not len(self.x)):return
		start,end=self.region.getRegion()
		if(start>0):start = int(round(start/self.I.timebase))
		else: start=0
		if(end>0):end = int(round(end/self.I.timebase))
		else:end=0
		guess = self.CC.getGuessValues(self.x[start:end]-self.x[start],self.VMID[start:end],func='damped sine')
		Csuccess,Cparams,chisq = self.CC.arbitFit(self.x[start:end]-self.x[start],self.VMID[start:end],self.CC.dampedSine,guess=guess)

		if Csuccess:
			self.CLabel.setText("CH1:\nA:%.2f V\tF:%.1f Hz\tDamp:%.3e"%(Cparams[0],1e6*abs(Cparams[1])/(2*np.pi),Cparams[4]))
			self.CH1Fit.setData(self.x[start:end],self.CC.dampedSine(self.x[start:end]-self.x[start],*Cparams))
			self.CParams=Cparams
		else:
			self.CLabel.setText("CH1:\nFit Failed. Change selected region.")
			self.CH1Fit.clear()


	def showData(self):
		self.lognum+=1
		b=self.CParams
		res =  'FIT:\nAmp:%.1fV\tFreq:%.1fHz\tPhase:%.1f\nOffset:%.2fV\tDamping:%.2e'%(b[0],1e6*abs(b[1])/(2*np.pi),b[2]*180/np.pi,b[3],b[4])
		self.displayDialog(res)
		


if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

