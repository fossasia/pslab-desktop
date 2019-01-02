#!/usr/bin/python

"""

::

    This experiment is used to study Half wave rectifiers


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft

from PyQt5 import QtGui,QtCore
import sys,time

params = {
'image' : 'clipping.png',
'name':"Summing Junction",
'hint':'''
	Study summing junctions using op-amps
	
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
		self.plot.setLabel('left','Voltage -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Time -->', units='S',**labelStyle)
		self.plot.setYRange(-8.5,8.5)
		self.I.set_gain('CH1',1)
		self.I.set_gain('CH2',1)
		self.I.set_pv2(0);self.I.set_pv3(0)
		self.plot.setLimits(yMax=8,yMin=-8,xMin=0,xMax=4e-3)

		self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
		self.tg=2
		self.max_samples=2000
		self.samples = self.max_samples
		self.timer = QtCore.QTimer()

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.curve1 = self.addCurve(self.plot,'INPUT 1(CH2)')
		self.curve2 = self.addCurve(self.plot,'INPUT 2(CH3)')
		self.curve3 = self.addCurve(self.plot,'OUTPUT (CH1)')

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		#Utility widgets
		#Widgets related to power supplies PV1,PVS2,PV3,PCS
		self.supplySection = self.supplyWidget(self.I);		self.WidgetLayout.addWidget(self.supplySection)

		#Widgets related to Analog Waveform generators
		self.sineSection = self.sineWidget(self.I); self.WidgetLayout.addWidget(self.sineSection)



		#Control widgets
		a1={'TITLE':'TIMEBASE','MIN':0,'MAX':9,'FUNC':self.set_timebase,'UNITS':'S','TOOLTIP':'Set Timebase of the oscilloscope'}
		self.ControlsLayout.addWidget(self.dialIcon(**a1))

		self.ControlsLayout.addWidget(self.gainIconCombined(FUNC=self.I.set_gain,LINK=self.gainChanged))

		self.running=True
		self.timer.singleShot(100,self.run)
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
		return self.samples*self.tg*1e-6
	def run(self):
		if not self.running: return
		try:
			self.I.configure_trigger(0,'CH1',0,prescaler = self.prescalerValue)
			self.I.capture_traces(3,self.samples,self.tg)
			if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+10,self.plotData)
		except Exception as e:
			print (e)

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
			self.I.__fetch_channel__(3)
			self.curve1.setData(self.I.achans[1].get_xaxis()*1e-6,self.I.achans[1].get_yaxis(),connect='finite')
			self.curve2.setData(self.I.achans[2].get_xaxis()*1e-6,self.I.achans[2].get_yaxis(),connect='finite')
			self.curve3.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
			
			self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[self.I.achans[1].get_yaxis(),self.I.achans[2].get_yaxis(),self.I.achans[0].get_yaxis()],[(0,255,0),(255,0,0),(255,255,0)])
			
			if self.running:self.timer.singleShot(100,self.run)
		except Exception as e:
			print (e)
	def saveData(self):
		self.saveDataWindow([self.curve1,self.curve2,self.curve3],self.plot)

		
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

