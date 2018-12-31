#!/usr/bin/python
'''
oscilloscope for the PsLab version 1.0.0

Also Includes XY plotting mode, and fitting against standard Sine/Square functions\n
'''
#TODO : Fix scaling issues in fourier transform mode. The user should be able to pan and zoom fourier plots within limits

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PyQt5 import QtCore, QtGui
import time,sys
from .templates import ui_ampMod as ampMod

import sys,os,string
import time
import sys

import pyqtgraph as pg

import numpy as np
import scipy.optimize as optimize
import scipy.fftpack as fftpack


err_count=0
trial = 0
start_time = time.time()
fps = None
dacval=0
from PSL.commands_proto import *

params = {
'image' : 'ampmod.png',
'name':'Amplitude\nModulation',
'hint':'Study amplitude modulation using the AD633 analog multiplier IC . W1 is the carrier, and W2 is the modulator waveform'
}



class AppWindow(QtGui.QMainWindow, ampMod.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
		self.plot.setDownsampling(mode='peak')
		self.plot.setClipToView(True)
	
		self.trace_colors=[(0,255,20),(255,0,0),(255,255,100)]
		labelStyle = {'color': 'rgb%s'%(str(self.trace_colors[1])), 'font-size': '13pt'}
		self.plot2 = self.addAxis(self.plot,label='CH2',**labelStyle)
		labelStyle = {'color': 'rgb%s'%(str(self.trace_colors[2])), 'font-size': '13pt'}
		
		self.plotF=self.add2DPlot(self.plot_area,enableMenu=False)
		self.plotF.setLabel('bottom', 'Frequency', units='Hz')
		self.FT=50
		xlen = 1.e6/self.FT/2
		self.plotF.autoRange();self.plotF.setXRange(0,min(10e3,xlen))
		self.plotF.setLimits(xMin=0,xMax=min(10e3,xlen))
		self.plot2.setMouseEnabled(True,True)
		self.ftzoomout = self.rightClickToZoomOut(self.plotF)


		self.plot.getPlotItem().setMouseEnabled(True,False)

		#self.plot.getViewBox().setMouseMode(pg.ViewBox.RectMode)
		self.plot.hideButtons();#self.plotF.hideButtons()

		self.fps=0
		self.MAX_SAMPLES=5000
		self.max_samples_per_channel=[0,self.MAX_SAMPLES,self.MAX_SAMPLES/2]
		self.samples=self.max_samples_per_channel[1]
		self.active_channels=1
		self.channel_states=np.array([1,0])
		self.channels_in_buffer=1
		g=1.75
		self.timebase = g
		self.lastTime=time.time()
		self.highresMode = False


		self.plot.setLabel('bottom', 'Time', units='S')
		self.LlabelStyle = {'color': 'rgb%s'%(str(self.trace_colors[0])), 'font-size': '11pt'}
		self.plot.setLabel('left','CH1', units='V',**self.LlabelStyle)

		

		self.plot2.setGeometry(self.plot.plotItem.vb.sceneBoundingRect())
		#self.plot2.linkedViewChanged(self.plot.plotItem.vb, self.plot2.XAxis)
		## Handle view resizing 
		self.plot.getViewBox().sigStateChanged.connect(self.updateViews)

		self.curve1 = self.addCurve(self.plot,name='CH1'); self.curve1.setPen(color=self.trace_colors[0], width=1)
		self.curve2 = self.addCurve(self.plot2,name='CH2(Carrier/Mod)');self.curve2.setPen(color=self.trace_colors[1], width=1)

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.legend.addItem(self.curve1,'CH1');self.legend.addItem(self.curve2,'CH2');
		
		#self.I.load_equation('W2','sine',amp=0.7)
		
		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
		a1={'TITLE':'W2(Carrier)','MIN':10,'MAX':5000,'FUNC':self.I.set_w2,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #2.\nUsed as the Carrier Wave'}
		self.w1 = self.dialAndDoubleSpinIcon(**a1);self.WidgetLayout.addWidget(self.w1);self.w1.dial.setValue(5000)
		a1={'TITLE':'W1(Mod)','MIN':10,'MAX':500,'FUNC':self.I.set_w1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1.\nUsed as the Modulation input'}
		self.w2 = self.dialAndDoubleSpinIcon(**a1);self.WidgetLayout.addWidget(self.w2);self.w2.dial.setValue(400)


		#cross hair

		self.vLine = pg.InfiniteLine(angle=90, movable=False,pen=[100,100,200,200])
		self.plot.addItem(self.vLine, ignoreBounds=True)
		self.hLine = pg.InfiniteLine(angle=0, movable=False,pen=[100,100,200,200])
		self.plot.addItem(self.hLine, ignoreBounds=True)
		self.vb = self.plot.getPlotItem().vb
		self.proxy = pg.SignalProxy(self.plot.scene().sigMouseClicked, rateLimit=60, slot=self.mouseClicked)
		self.mousePoint=None

		#add FFT curve
		self.curveFft= self.addCurve(self.plotF,name='CH1 FFT')
		self.curveFft.setPen(color=self.trace_colors[0], width=1)

		#Add fit overlay curves
		self.curveFL= self.addCurve(self.plot)
		self.curveFL.setPen(color=(255,255,255,100), width=3)
		self.curveFR = self.addCurve(self.plot2)#pg.PlotDataItem()
		self.curveFR.setPen(color=(255,255,255,100), width=3)


		self.CH1_ENABLE.setStyleSheet('background-color:rgba'+str(self.trace_colors[0])[:-1]+',3);color:(0,0,0);')
		self.CH2_ENABLE.setStyleSheet('background-color:rgba'+str(self.trace_colors[1])[:-1]+',3);color:(0,0,0);')

		for a in range(2):
			self.trigger_select_box.setItemData(a, QtGui.QColor(*self.trace_colors[a]), QtCore.Qt.BackgroundRole);

		self.triggerChannelName='CH1'
		self.arrow = pg.ArrowItem(pos=(0, 0), angle=0)
		self.plot.addItem(self.arrow)
		#markings every 5 Volts
		self.voltsperdiv = ['5V/div','3V/div','2V/div','1V/div','500mV/div','400mV/div','300mV/div','100mV/div']
		self.trigger_channel=0
		self.trigger_level = 0
		self.trigtext = pg.TextItem(html=self.trigger_text('CH1'), anchor=(1.2,0.5), border='w', fill=(0, 0, 255, 100),angle=0)
		self.plot.addItem(self.trigtext)
		#self.plot_area.addWidget(self.plot)
		#self.plot_area.addWidget(self.plot)
		self.showgrid()
		self.trigtext.setParentItem(self.arrow)
		self.prescalerValue=0
		self.I.configure_trigger(self.trigger_channel,self.triggerChannelName,0,prescaler = self.prescalerValue)
		
		self.autoRange()
		self.timer = self.newTimer()
		self.finished=False
		self.timer.singleShot(500,self.start_captureNORMAL)
		self.enableShortcuts()


	def mouseClicked(self,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		self.plot.setTitle('')
		if self.plot.sceneBoundingRect().contains(pos):
			self.mousePoint = self.vb.mapSceneToView(pos)
			self.vLine.setPos(self.mousePoint.x())
			self.hLine.setPos(self.mousePoint.y())

		
	def updateViews(self,*args):
		self.plot2.setGeometry(self.plot.getViewBox().sceneBoundingRect())
		self.plot2.linkedViewChanged(self.plot.plotItem.vb, self.plot2.XAxis)
		
	def trigger_text(self,c):
		return '<div style="text-align: center"><span style="color: #FFF; font-size: 8pt;">'+c+'</span></div>'		

	def showgrid(self):
		self.plot.getAxis('left').setGrid(170)
		self.plot.getAxis('bottom').setGrid(170)
		#self.plot.showGrid(True,True,0.7)
		#self.plot2.showGrid(True,False,0.7)
		return
				
	def start_captureNORMAL(self):
		if self.finished:
			return
		if(self.freezeButton.isChecked()):
			self.timer.singleShot(200,self.start_captureNORMAL)
			return

		try:
			self.channels_in_buffer=self.active_channels

			a = self.CH1_ENABLE.isChecked()
			b = self.CH2_ENABLE.isChecked()
			if b:
				self.active_channels=2
			elif a:
				self.active_channels=1
			else:
				self.active_channels=0

			self.channels_in_buffer=self.active_channels
			self.channel_states[0]=a
			self.channel_states[1]=b
			
			if self.active_channels:
				self.I.configure_trigger(self.trigger_channel,self.triggerChannelName,self.trigger_level,resolution=10,prescaler=self.prescalerValue)
				self.I.capture_traces(self.active_channels,self.samples,self.timebase,'CH1',0,trigger=self.triggerBox.isChecked())
		except:
			print ('error')
			self.close()

		self.timer.singleShot(self.samples*self.I.timebase*1e-3+10+self.prescalerValue*20,self.updateNORMAL)

	def updateNORMAL(self):
		n=0
		try:
			while(not self.I.oscilloscope_progress()[0]):
				time.sleep(0.1)
				print (self.timebase,'correction required',n)
				n+=1
				if n>10:
					self.timer.singleShot(100,self.start_captureNORMAL)
					return
			for a in range(min(self.channels_in_buffer,3)): self.I.__fetch_channel__(a+1)
		except:
			print ('communication error')
			self.close()

		self.curve1.clear()
		self.curve2.clear()
		self.curveFR.clear()
		self.curveFL.clear()

		msg='';pos=0;phaseA=0
		for fitsel in [self.fit_select_box,self.fit_select_box_2]:
			if fitsel.currentIndex()<2:
				if len(msg)>0:msg+='\n'
				if self.channel_states[fitsel.currentIndex()]:
					if fitsel.currentText()=='CH2':
						ed = self.fitData(self.I.achans[fitsel.currentIndex()].get_xaxis(),	self.I.achans[fitsel.currentIndex()].get_yaxis(),self.curveFR)
					else:
						ed = self.fitData(self.I.achans[fitsel.currentIndex()].get_xaxis(),self.I.achans[fitsel.currentIndex()].get_yaxis(),self.curveFL)

					if len(ed)==4:
						dp=''
						if not len(msg): phaseA = ed[3]
						else:dp = '(%.3f)'%(ed[3]-phaseA)
							
						msg+='Fit %c:Amp = %0.3fV \tFreq=%0.2fHz \tOffset=%0.3fV \tPhase=%0.1f%c'%(pos+65,ed[0],ed[1],ed[2],ed[3],176)
						msg+=dp
					else:
						msg+='Fit Failed'

				else:
					msg+='FIT '+chr(pos+65)+': Channel Unavailable'

		if len(msg):
			self.message_label.setText(msg)
		
		
		#UPDATE THE PLOTS
		pos=0
		for a in [self.curve1,self.curve2]:
			if self.channel_states[pos]:
				a.setData(self.I.achans[pos].get_xaxis()*1e-6,self.I.achans[pos].get_yaxis())
				#self.curve3.setData(self.I.achans[pos].get_xaxis()*1e-6,self.I.achans[pos].get_yaxis(),connect='finite')
			pos+=1



		now = time.time()
		dt = now - self.lastTime
		self.lastTime = now
		if self.fps is None:
			self.fps = 1.0/dt
		else:
			s = np.clip(dt*3., 0, 1)
			self.fps = self.fps * (1-s) + (1.0/dt) * s
		
		if self.mousePoint:
			1.e6/self.timebase/2
			
			index = int(self.mousePoint.x()*1e6/self.I.timebase)
			maxIndex = self.I.samples
			
			#print (self.mousePoint.x(),1.e6/self.timebase/2,index,max(self.curve1.getData()[0]),min(self.curve1.getData()[0]),len(self.curve1.getData()[0]))
			if index > 0 and index < maxIndex:
				coords="%.1f FPS, <span style='color: white'>%0.1f uS</span>: "%(self.fps,self.I.achans[0].xaxis[index])
				for a in range(2):
					if self.channel_states[a]:
						c=self.trace_colors[a]
						coords+="<span style='color: rgb%s'>%0.3fV</span>," %(c, self.I.achans[a].yaxis[index])
				#self.coord_label.setText(coords)
				self.plot.plotItem.titleLabel.setText(coords)
			else:
				self.plot.plotItem.titleLabel.setText('')
				self.vLine.setPos(-1)
				self.hLine.setPos(-1)


		self.timer.singleShot(100,self.start_captureFFT)



	def start_captureFFT(self):
		if self.finished:
			return
		if(self.freezeButton.isChecked()):
			self.timer.singleShot(200,self.start_captureFFT)
			return

		try:
			self.channels_in_buffer=1
			self.I.capture_traces(1,10000,self.FT,'CH1',0,trigger=False)
		except:
			print ('error')
			self.close()

		self.timer.singleShot(10000*self.FT*1e-3+10,self.updateFFT)





	def updateFFT(self):
		n=0
		try:
			while(not self.I.oscilloscope_progress()[0]):
				time.sleep(0.1)
				print (self.timebase,'correction required',n)
				n+=1
				if n>10:
					self.timer.singleShot(100,self.start_captureNORMAL)
					return
			self.I.__fetch_channel__(1)
		except:
			self.message_label.setText ('communication error')
			self.timer.singleShot(100,self.start_captureNORMAL)

		self.curveFft.clear()
		#UPDATE THE FOURIER TRANSFORMS
		x,y = self.math.fft(self.I.achans[0].get_yaxis(),self.I.timebase*1e-6)
		self.curveFft.setData(x,y,connect='finite')

		self.timer.singleShot(100,self.start_captureNORMAL)



	def fitData(self,xReal,yReal,curve):
		if self.fit_type_box.currentIndex()==0: #sine wave
			fitres = self.math.sineFit(xReal,yReal)
			if fitres:
				amp=fitres[0]
				freq=fitres[1]
				offset=fitres[2]
				ph=fitres[3]

				frequency = freq/1e6
				period = 1./frequency/1e6
				#Collapse waveforms on top of each other.
				'''
				if(self.collapseButton.isChecked()):
					self.collapseButton.setChecked(False)
					self.collapse_win = pg.GraphicsWindow(title="Collapsing plot")
					xNew=[]
					yNew=[]
					for a in range(len(xReal)):
						x=((xReal[a]*1e-6)%(period*2))
						xNew.append(x)
						yNew.append(yReal[a])
					xNew=np.array(xNew)
					yNew=np.array(yNew)
					s=np.argsort(xNew)
					self.p1 = self.collapse_win.addPlot(title="Collapsing plot: %.1f waveforms collapsed on top of each other"%(xReal[-1]/period), x=xNew[s],y=yNew[s])
					if(self.collapse_win.windowState() & QtCore.Qt.WindowActive):
						print ('opened')
				'''
				#------------------------------------------------------
				
				##Overlay fit curve
				if(self.overlay_fit_button.isChecked()):
					x=np.linspace(0,xReal[-1],50000)
					curve.setData(x*1e-6,self.math.sineFunc(x,amp,frequency,ph*np.pi/180,offset))
				return [amp, freq, offset,ph]
			else:
				return []

		elif self.fit_type_box.currentIndex()==1: #square
			fitres = self.math.squareFit(xReal,yReal)
			if fitres:
				amp=fitres[0]
				freq=fitres[1]
				phase=fitres[2]
				dc=fitres[3]
				offset=fitres[4]

				frequency = freq/1e6
				period = 1./freq/1e6
				'''
				if(self.collapseButton.isChecked()):
					self.collapseButton.setChecked(False)
					self.collapse_win = pg.GraphicsWindow(title="Collapsing plot")
					xNew=[]
					yNew=[]
				
					for a in range(len(xReal)):
						x=(xReal[a]%(period*2))*1e-6
						xNew.append(x)
						yNew.append(yReal[a])
					xNew=np.array(xNew)
					yNew=np.array(yNew)
					s=np.argsort(xNew)
					self.p1 = self.collapse_win.addPlot(title="Collapsing plot: %.1f waveforms collapsed on top of each other"%(xReal[-1]/period), x=xNew[s],y=yNew[s])
					if(self.collapse_win.windowState() & QtCore.Qt.WindowActive):
						print ('opened')
				'''
				#------------------------------------------------------
			
				if(self.overlay_fit_button.isChecked()):
					x=np.linspace(0,xReal[-1],50000)
					curve.setData(x*1e-6,self.math.squareFunc(x,amp,frequency,phase,dc,offset))
				return 'Amp = %0.3fV \tFreq=%0.2fHz \tDC=%0.3fV \tOffset=%0.3fV'%(amp, freq,dc,offset)
			else:
				return 'fit failed'
		else:
				return 'fit failed'


	def setGainCH1(self,g):
		self.I.set_gain('CH1',g)
		
		chan = self.I.analogInputSources['CH1']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot.setYRange(min(R),max(R))
		self.plot.setLimits(yMax=max(R),yMin=min(R))			
		#RHalf = min(abs(R[0]),abs(R[1]))*0.9   #Make vertical axes symmetric. Post calibration voltage ranges are not symmetric usually.
		#self.plot.setYRange(-1*RHalf,RHalf)    #Not sure how to handle unipolar channels . TODO
		
	def setGainCH2(self,g):
		self.I.set_gain('CH2',g)

		chan = self.I.analogInputSources['CH2']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot2.setYRange(min(R),max(R))
		self.plot2.setLimits(yMax=max(R),yMin=min(R))		
		
		#RHalf = min(abs(R[0]),abs(R[1]))*0.9  #Make vertical axes symmetric. Post calibration voltage ranges are not symmetric usually.
		#self.plot.setYRange(-1*RHalf,RHalf)


	def setTimeBase(self,g):
		timebases = [1.75,2,4,8,16,32,128,256,512,1024,2048]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.9,0.7,0.5,0.3,0.2,0.1]
		self.timebase=timebases[g]
		'''
		if(self.active_channels==1 and self.timebase<1.0):
			self.timebase=1.0
		elif(self.active_channels==2 and self.timebase<1.25):
			self.timebase=1.25
		elif((self.active_channels==3 or self.active_channels==4) and self.timebase<1.75):
			self.timebase=1.75
		'''
		self.autoSetSamples()
		self.samples = int(self.samples*samplescaling[g])
		self.autoRange()
		self.showgrid()

	def autoSetSamples(self):
		self.samples = self.max_samples_per_channel[self.active_channels]

	def setTriggerLevel(self,val):
		if self.trigger_channel==0:self.triggerChannelName='CH1'
		else:self.triggerChannelName='CH2'
		
		chan = self.I.analogInputSources[self.triggerChannelName]
		if chan.inverted:val=1000-val
		levelInVolts=chan.calPoly10(val*1023/1000.)
		
		self.trigger_level=levelInVolts
		self.arrow.setPos(0,levelInVolts) #TODO
		self.trigger_level_label.setText('Level : %.3f V'%levelInVolts)

	def setTriggerChannel(self,val):
		self.trigtext.setHtml(self.trigger_text(self.I.achans[val].name))
		self.triggerChannel=val
		self.trigger_channel = val
		c=self.trace_colors[val]
		s='QFrame{background-color:rgba'+str(c)[:-1]+',50);}'
		#self.sender().parentWidget().setStyleSheet(s)
		self.trigger_frame.setStyleSheet(s)
		self.arrow.setParentItem(None)
		if val==0:
			self.plot.addItem(self.arrow)
		elif val==1:
			self.plot2.addItem(self.arrow)

	def setActiveChannels(self,val):
		self.active_channels = int(val)
		self.autoSetSamples()

		
	def autoRange(self):
		chan = self.I.analogInputSources['CH1']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		chan = self.I.analogInputSources['CH2']
		R2 = [chan.calPoly10(0),chan.calPoly10(1023)]
		R2[0]=R2[0]*.9;R2[1]=R2[1]*.9
		self.plot.setYRange(min(R),max(R))
		self.plot2.setYRange(min(R2),max(R2))
		
		xlen = (self.timebase*self.samples*1e-6)
		#print (self.timebase,self.samples,xlen)
		
		self.plot.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
		self.plot2.setLimits(yMax=max(R2),yMin=min(R2))		
		self.plot.setXRange(0,xlen)





	def saveData(self):
		self.saveDataWindow([self.curve1,self.curve2],self.plot)

	def saveFft(self):
		self.saveDataWindow([self.curveFft],self.plotF)


	def closeEvent(self, event):
		self.timer.stop()
		self.running =False
		self.finished=True

		

	def __del__(self):
		self.running =False
		self.finished=True
		self.timer.stop()
		print ('bye')

		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	app.exec_()
