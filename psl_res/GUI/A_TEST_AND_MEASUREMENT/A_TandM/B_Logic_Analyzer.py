#!/usr/bin/python
'''
oscilloscope for the PSLab. \n

Also Includes XY plotting mode, and fitting against standard Sine/Square functions\n
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

from PyQt5 import QtCore, QtGui
import time,sys
from .templates import ui_digitalScopeNoTrig as digitalScopeNoTrig
from PSL.commands_proto import applySIPrefix

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
from PSL.commands_proto import *
from PSL_Apps.utilitiesClass import utilitiesClass
params = {
'image' : 'ico_la.png',
'name':'Logic\nAnalyzer',
'hint':'4-Channel Logic analyzer that uses inputs ID1 through ID4. Capable of detecting various level changes in the input signal, and recording timestamps'
}

class AppWindow(QtGui.QMainWindow, digitalScopeNoTrig.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		
		for a in [self.C1_chan,self.edge1chan,self.edge2chan,self.C2_ID1,self.C2_ID2]: #,self.C1_trig,self.C2_trig,self.C3_trig]:
			a.addItems(self.I.digital_channel_names)
		self.C2_ID2.setCurrentIndex(1)

		#cross hair
		self.vLine = pg.InfiniteLine(angle=90, movable=True)
		#self.vLine.setPen(color=(135,44,64,150), width=3)
		self.plot.addItem(self.vLine, ignoreBounds=False)


		self.proxy = pg.SignalProxy(self.vLine.scene().sigMouseMoved, rateLimit=60, slot=self.readCursor)
		
		self.fps=0
		self.active_dchannels=1
		self.channel_states=np.array([1,0,0,0])
		self.channels_in_buffer=1
		self.dtrig=0
		self.dchan_modes=[1,1,1,1]
		self.dtime=0.001
		self.maxT=0


		self.max_samples_per_channel=[0,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4]
		self.samples=self.I.MAX_SAMPLES/4#self.sample_slider.value()
		self.lastTime=time.time()
		self.trace_colors=[(0,255,20),(255,255,0),(255,10,100),(10,255,255)]
		self.plot.setLabel('bottom', 'Time -->>', units='S')
		self.LlabelStyle = {'color': 'rgb%s'%(str(self.trace_colors[0])), 'font-size': '11pt'}
		self.plot.setLabel('left','CH1', units='V',**self.LlabelStyle)
		#self.plot.addLegend(offset=(-10,30))
		self.plot.getPlotItem().setMouseEnabled(True,False)
		self.plot.setLimits(yMax=10,yMin=0,xMin=0)
		ydict = {2:'Chan 1', 4:'Chan 2', 6:'Chan 3', 8:'Chan 4'}
		self.plot.getAxis('left').setTicks([ydict.items()])




		self.curve1 = self.addCurve(self.plot,name='1'); #self.curve1.setPen(color=self.trace_colors[0], width=1)
		self.curve2 = self.addCurve(self.plot,name='2'); #self.curve2.setPen(color=self.trace_colors[1], width=1)
		self.curve3 = self.addCurve(self.plot,name='3'); #self.curve3.setPen(color=self.trace_colors[2], width=1)
		self.curve4 = self.addCurve(self.plot,name='4'); #self.curve4.setPen(color=self.trace_colors[3], width=1)
		#self.I.sqr4_continuous(1000,.5,0.1,.5,0.3,.3,0.5,.1)

		self.region = pg.LinearRegionItem([0,0])
		self.region.setZValue(10)
		self.plot.addItem(self.region)		

		for x in range(4):
				item = QtGui.QTableWidgetItem();self.timingResults.setItem(x, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
				item = QtGui.QTableWidgetItem();self.timingResults.setItem(x, 1, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)

		self.showgrid()
		self.set_digital_scope_time(0)
		self.timer = self.newTimer()
		self.finished=False
		self.timer.timeout.connect(self.update)
		self.timer.start(100)
		

	def updateViews(self):
			self.plot2.setGeometry(self.plot.getViewBox().sceneBoundingRect())
			self.plot2.linkedViewChanged(self.plot.plotItem.vb, self.plot2.XAxis)
		
	def showgrid(self):
		return

	def capture(self):
		self.curve1.clear()
		self.curve2.clear()
		self.curve3.clear()
		self.curve4.clear()
		
		if self.channelSelection.currentIndex()==0:  #1 channel mode
			self.active_dchannels = 1
			aqchan = self.C1_chan.currentText()
			aqmode = self.C1_chanmode.currentIndex()
			trchan = aqchan#self.C1_trig.currentText()
			trmode = 2# self.C1_trigmode.currentIndex()
			if(trmode):
				self.I.start_one_channel_LA(channel=aqchan,channel_mode=aqmode,trigger_channel=trchan,trigger_mode=trmode+1)
			#else : self.I.start_one_channel_LA(channel=aqchan,channel_mode=aqmode,trigger_mode=0)

		elif self.channelSelection.currentIndex()==1:  #2 channel mode
			self.active_dchannels = 2
			self.dchan_modes = []
			for a in [self.C2_M1,self.C2_M2]: self.dchan_modes.append(a.currentIndex())
			TT='rising'#['','falling','rising'][self.C2_trigmode.currentIndex()]
			#trigger = self.C2_trigmode.currentIndex()
			self.I.start_two_channel_LA(modes = self.dchan_modes,chans = [self.C2_ID1.currentText(),self.C2_ID2.currentText()], trigger = True,\
			trig_type = TT,trig_chan = self.C2_ID1.currentText() ) #self.C2_trig.currentText())

		elif self.channelSelection.currentIndex()==2:  #3 channel mode
			self.active_dchannels = 3
			trchan = 'ID1' # self.C3_trig.currentText()
			trmode = 2#self.C3_trigmode.currentIndex()
			self.dchan_modes = []
			for a in [self.C3_M1,self.C3_M2,self.C3_M3]: self.dchan_modes.append(a.currentIndex())
			if(trmode):
				trmode+=1
				self.I.start_three_channel_LA(modes=self.dchan_modes,trigger_channel=trchan,trigger_mode=trmode)
			#else : self.I.start_three_channel_LA(modes=self.dchan_modes,trigger_channel=trchan,trigger_mode=0)

		elif self.channelSelection.currentIndex()==3:  #4 channel mode
			self.active_dchannels = 4
			self.dchan_modes = []
			for a in [self.C4_M1,self.C4_M2,self.C4_M3,self.C4_M4]: self.dchan_modes.append(a.currentIndex())
			self.I.start_four_channel_LA(1,self.dtime,self.dchan_modes,edge='rising',trigger_ID1=True)#self.FourChanTrig.isChecked())



	def showData(self):
		from PSL_Apps.utilityApps import spreadsheet
		self.info = spreadsheet.AppWindow(self)
		start,end=self.region.getRegion()
		start*=1e6;end*=1e6 # Convert back to uS
		colnum=0;labels=[]
		for a in range(self.active_dchannels):
			startIndex = np.argmin(abs(self.I.dchans[a].timestamps-start));	endIndex = np.argmin(abs(self.I.dchans[a].timestamps-end))
			data =  self.I.dchans[a].timestamps[startIndex:endIndex]
			self.info.setColumn(colnum,data);colnum+=1
			self.info.setColumn(colnum,np.diff(data));colnum+=1
			labels.append('Time[%d] uS'%(1+a));labels.append('Difference[%d]'%(1+a));

		self.info.table.setHorizontalHeaderLabels(labels)
		self.info.show()

	def plotData(self):
		n=0
		self.timer.stop()
		self.I.fetch_LA_channels()
		self.timer.start(100)
		#print(len(self.I.dchans[0].timestamps))
		if len(self.I.dchans[0].timestamps)>2:
			offset = self.I.dchans[0].timestamps[0]
			txt = 'CH1: Offset:\t%.3euS\ttimestamps(uS):\t'%(offset/64.)
			txt += string.join(['%.2e'%(a/64.) for a in (self.I.dchans[0].timestamps[1:4]-offset)],'\t')
			self.message_label.setText(txt+'...')
		else:
			self.message_label.setText('CH1: too few points to display')

		self.curve1.clear()
		self.curve2.clear()
		self.curve3.clear()
		self.curve4.clear()
		self.maxT=0
		#print ( self.I.dchans[0].get_xaxis(), self.I.dchans[0].timestamps )
		self.curve1.setData(self.I.dchans[0].get_xaxis()*1e-6,self.I.dchans[0].get_yaxis()+2 )

		if self.maxT < self.I.dchans[0].maxT*1e-6:
			self.maxT = self.I.dchans[0].maxT*1e-6

		if self.I.dchans[0].plot_length==1: #No level changes were detected
			x=self.I.dchans[0].xaxis[0]*1e-6;y=self.I.dchans[0].yaxis[0]+2
			self.curve1.setData([x,x+self.maxT],[y,y])
		if(self.active_dchannels>1):
			self.curve2.setData(self.I.dchans[1].get_xaxis()*1e-6,self.I.dchans[1].get_yaxis()+4 )
			if self.maxT < self.I.dchans[1].maxT*1e-6: self.maxT = self.I.dchans[1].maxT *1e-6
			if self.I.dchans[1].plot_length==1: #No level changes were detected
				x=self.I.dchans[1].xaxis[0]*1e-6;y=self.I.dchans[1].yaxis[0]+4
				self.curve2.setData([x,x+self.maxT],[y,y])
		else:	self.curve2.clear()		

		if(self.active_dchannels>2):
			self.curve3.setData(self.I.dchans[2].get_xaxis()*1e-6,self.I.dchans[2].get_yaxis()+6)
			if self.maxT < self.I.dchans[2].maxT*1e-6: self.maxT = self.I.dchans[2].maxT*1e-6 
			if self.I.dchans[2].plot_length==1: #No level changes were detected
				x=self.I.dchans[2].xaxis[0]*1e-6;y=self.I.dchans[2].yaxis[0]+6
				self.curve3.setData([x,x+self.dtime*1e6],[y,y])
		else:
			self.curve3.clear()
		
		if(self.active_dchannels>3):
			self.curve4.setData(self.I.dchans[3].get_xaxis()*1e-6,self.I.dchans[3].get_yaxis() +8)
			if self.maxT < self.I.dchans[3].maxT*1e-6: self.maxT = self.I.dchans[3].maxT *1e-6
			if self.I.dchans[3].plot_length==1: #No level changes were detected
				x=self.I.dchans[3].xaxis[0]*1e-6;y=self.I.dchans[3].yaxis[0]+8
				self.curve4.setData([x,x+self.maxT],[y,y])
		else:	self.curve4.clear()

		self.autodRange()
		self.plot.setRange(QtCore.QRectF(0, -2, self.maxT, 16)) 
		self.region.setBounds([0,self.maxT])
		self.region.setRegion([0,self.maxT/4])
		self.readCursor()		


	def update(self):
		if self.finished:
			self.timer.stop()
		states = self.I.get_LA_initial_states()
		a,b,c,d,e=states
		#print (a,b,c,d)
		self.progressBar.setValue(a)

	def readCursor(self):
		pos=self.vLine.getPos()
		index = int(pos[0]*1e6)/self.I.timebase
		if index > 0 and index < self.I.samples:
			coords="<span style='color: white'>%0.1f uS</span>: "%(self.I.achans[0].xaxis[index])
			for a in range(4):
				if self.channel_states[a]:
					c=self.trace_colors[a]
					coords+="<span style='color: rgb%s'>%0.3fV</span>," %(c, self.I.achans[a].yaxis[index])
			self.coord_label.setText(coords)
		else:
			self.coord_label.setText("")


	def autodRange(self):
		self.plot.setRange(QtCore.QRectF(0, -2, self.maxT, 16)) 

	def set_digital_scope_time(self,val):
		self.autodRange()

	def autoSetSamples(self):
		self.samples = self.max_samples_per_channel[self.active_channels]

	def measure_dcycle(self):
		inp = self.timing_input.currentText()
		v=self.I.DutyCycle(inp)
		if(v[0]!=-1):p=100*v[1]
		else: p=0
		self.timing_results.setText('Duty Cycle: %f %%'%(p))

	def measure_interval(self):
		for a in range(4):
			i=self.timingResults.item(a,0);	i.setText('')
			i=self.timingResults.item(a,1);	i.setText('')
		i=self.timingResults.item(0,0);	i.setText('Timeout')

		t1,t2 = self.I.MeasureMultipleDigitalEdges(self.edge1chan.currentText(),self.edge2chan.currentText(),self.edge1edge.currentText(),self.edge2edge.currentText(),self.edge1Count.currentIndex()+1,self.edge2Count.currentIndex()+1,self.timeoutBox.value()/1000.)
		pos=0
		if t1!=None:
			for a in t1:
				i=self.timingResults.item(pos,0);	i.setText(applySIPrefix(a,'S'));		pos+=1
		pos=0
		if t2!=None:
			for a in t2:
				i=self.timingResults.item(pos,1);i.setText(applySIPrefix(a,'S'));	pos+=1
		
	def saveData(self):
		self.saveDataWindow([self.curve1,self.curve2,self.curve3,self.curve4],self.plot)

	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		self.finished=True
		print('bye')

		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

