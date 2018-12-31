#!/usr/bin/python
'''
oscilloscope application for PSLab. \n

Also Includes XY plotting mode, and fitting against standard Sine/Square functions, and FFT\n
'''
#TODO : Fix scaling issues in fourier transform mode. The user should be able to pan and zoom fourier plots within limits

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PyQt5 import QtCore, QtGui
import time,sys
from .templates import ui_analogScope as analogScope

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
'image' : 'scope.png',
'name':'Oscilloscope',
'hint':'4-Channel oscilloscope with basic configuration options such as vertical and horizontal scales, trigger selection, and XY mode.\n Also includes curve fitting routines for data analysis'
}



class AppWindow(QtGui.QMainWindow, analogScope.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		self.trace_colors=[(0,255,20),(255,0,0),(255,255,100),(10,255,255)]
		self.plot=self.add2DPlot(self.plot_area,enableMenu=False)
	
		labelStyle = {'color': 'rgb%s'%(str(self.trace_colors[1])), 'font-size': '13pt'}
		self.plot2 = self.addAxis(self.plot,label='CH2',**labelStyle)

		self.plot.getPlotItem().setMouseEnabled(True,False)
		self.plot2.setMouseEnabled(True,False)

		#self.plot.getViewBox().setMouseMode(pg.ViewBox.RectMode)
		self.plot.hideButtons()

		self.fps=0
		self.MAX_SAMPLES=2000
		self.max_samples_per_channel=[0,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4]
		self.liss_win=None
		self.liss_ready=False
		self.liss_animate_arrow1=None
		self.liss_animate_arrow2=None
		self.liss_animate_arrow3=None
		self.liss_anim1=None
		self.liss_anim2=None
		self.liss_anim3=None
		self.samples=self.max_samples_per_channel[1]
		self.active_channels=1
		self.channel_states=np.array([1,0,0,0])
		self.channels_in_buffer=1
		self.chan1remap='CH1'
		self.ch123sa = 0
		g=1.75
		self.timebase = g
		self.lastTime=time.time()
		self.highresMode = False


		self.plot.setLabel('bottom', 'Time', units='S')
		self.LlabelStyle = {'color': 'rgb%s'%(str(self.trace_colors[0])), 'font-size': '11pt'}
		self.plot.setLabel('left','CH1', units='V',**self.LlabelStyle)

		
		labelStyle = {'color': 'rgb%s'%(str(self.trace_colors[1])), 'font-size': '13pt'}
		self.plot.getAxis('right').setLabel('CH2', units='V', **labelStyle)

		self.plot2.setGeometry(self.plot.plotItem.vb.sceneBoundingRect())
		self.plot2.linkedViewChanged(self.plot.plotItem.vb, self.plot2.XAxis)
		## Handle view resizing 
		self.plot.getViewBox().sigStateChanged.connect(self.updateViews)

		self.curve1 = self.addCurve(self.plot,name='CH1'); self.curve1.setPen(color=self.trace_colors[0], width=2)
		self.curve2 = self.addCurve(self.plot2,name='CH2');self.curve2.setPen(color=self.trace_colors[1], width=2)
		self.curve3 = self.addCurve(self.plot,name='CH3'); self.curve3.setPen(color=self.trace_colors[2], width=2)
		self.curve4 = self.addCurve(self.plot,name='CH4'); self.curve4.setPen(color=self.trace_colors[3], width=2)
		self.curve_lis = self.addCurve(self.plot,name='XY'); self.curve_lis.setPen(color=(255,255,255), width=2)

		self.legend = self.plot.addLegend(offset=(-10,30))
		self.legend.addItem(self.curve1,'Chan 1');self.legend.addItem(self.curve2,'Chan 2');self.legend.addItem(self.curve3,'CH3');self.legend.addItem(self.curve4,'MIC')
		
		#cross hair

		self.vLine = pg.InfiniteLine(angle=90, movable=False,pen=[100,100,200,200])
		self.plot.addItem(self.vLine, ignoreBounds=True)
		self.hLine = pg.InfiniteLine(angle=0, movable=False,pen=[100,100,200,200])
		self.plot.addItem(self.hLine, ignoreBounds=True)
		self.vb = self.plot.getPlotItem().vb
		self.proxy = pg.SignalProxy(self.plot.scene().sigMouseClicked, rateLimit=60, slot=self.mouseClicked)
		self.mousePoint=None

		self.fourierMode = False
		self.plot.setTitle('')

		self.curveF=[]
		for a in range(2):
			self.curveF.append( self.addCurve(self.plot));
			self.curveF[-1].setPen(color=(255,255,255), width=2)

		self.curveFR = self.addCurve(self.plot2)#pg.PlotDataItem()
		#self.plot2.addItem(self.curveFR)
		self.curveFR.setPen(color=(255,255,255), width=1)

		self.CH1_ENABLE.setStyleSheet('background-color:rgba'+str(self.trace_colors[0])[:-1]+',3);color:(0,0,0);')
		self.CH2_ENABLE.setStyleSheet('background-color:rgba'+str(self.trace_colors[1])[:-1]+',3);color:(0,0,0);')

		for a in range(4):
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
		self.plot_area.addWidget(self.plot)
		self.CH1_REMAPS.addItems(self.I.allAnalogChannels)
		self.showgrid()
		self.trigtext.setParentItem(self.arrow)
		self.prescalerValue=0
		self.setGainCH1(0)
		self.setGainCH2(0)
		self.I.configure_trigger(self.trigger_channel,self.triggerChannelName,0,prescaler = self.prescalerValue)
		
		self.autoRange()
		self.timer = self.newTimer()
		self.finished=False
		self.timer.singleShot(500,self.start_capture)
		self.enableShortcuts()


	def mouseClicked(self,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
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

	def setFourier(self,val):
		if val:
			self.fourierMode=True
			for a in [self.curve1,self.curve2,self.curve3,self.curve4]:
				a.setFftMode(True)
			#self.curve4.setFftMode(True)
			self.plot.setLabel('bottom', 'Frequency', units='Hz')
			self.MAX_SAMPLES=10000
		else:
			self.fourierMode=False
			for a in [self.curve1,self.curve2,self.curve3,self.curve4]:#,self.curveFR]+self.curveF:
				a.setFftMode(False)
			self.MAX_SAMPLES=2000
			self.plot.setLabel('bottom', 'Time', units='S')

		self.max_samples_per_channel=[0,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4,self.MAX_SAMPLES/4]
		self.autoSetSamples()
		self.autoRange()
				
	def start_capture(self):
		if self.finished:
			return
		if(self.freezeButton.isChecked()):
			self.timer.singleShot(200,self.start_capture)
			return

		try:
			#self.plot.setTitle('%0.2f fps, 	%0.1f ^C' % (self.fps,self.I.get_temperature() ) )
			self.channels_in_buffer=self.active_channels

			a = self.CH1_ENABLE.isChecked()
			b = self.CH2_ENABLE.isChecked()
			c = self.CH3_ENABLE.isChecked()
			d = self.MIC_ENABLE.isChecked()
			if c or d:
				self.active_channels=4
			elif b:
				self.active_channels=2
			elif a:
				self.active_channels=1
			else:
				self.active_channels=0

			self.channels_in_buffer=self.active_channels
			self.channel_states[0]=a
			self.channel_states[1]=b
			self.channel_states[2]=c
			self.channel_states[3]=d
			
			if self.active_channels:
				#if self.highresMode and self.active_channels == 1:
				#	self.I.configure_trigger(self.trigger_channel,self.triggerChannelName,self.trigger_level,resolution=12,prescaler=self.prescalerValue)
				#	self.I.capture_highres_traces(self.chan1remap,self.samples,self.timebase,trigger=self.triggerBox.isChecked())
				#else:
				self.I.configure_trigger(self.trigger_channel,self.triggerChannelName,self.trigger_level,resolution=10,prescaler=self.prescalerValue)
				self.I.capture_traces(self.active_channels,self.samples,self.timebase,self.chan1remap,self.ch123sa,trigger=self.triggerBox.isChecked())
		except:
			print ('communication error')
			self.close()

		self.timer.singleShot(self.samples*self.I.timebase*1e-3+10+self.prescalerValue*20,self.update)

	def update(self):
		n=0
		try:
			while(not self.I.oscilloscope_progress()[0]):
				time.sleep(0.1)
				print (self.timebase,'correction required',n)
				n+=1
				if n>10:
					self.timer.singleShot(100,self.start_capture)
					return
			for a in range(self.channels_in_buffer): self.I.__fetch_channel__(a+1)
		except:
			print ('communication error')
			self.close()

		self.curve1.clear()
		self.curve2.clear()
		self.curve3.clear()
		self.curve4.clear()
		self.curveF[0].clear()
		self.curveF[1].clear()
		self.curveFR.clear()

		msg='';pos=0;phaseA=0
		for fitsel in [self.fit_select_box,self.fit_select_box_2]:
			if fitsel.currentIndex()<4:
				if len(msg)>0:msg+='\n'
				if self.channel_states[fitsel.currentIndex()]:
					if fitsel.currentText()=='CH2':
						ed = self.fitData(self.I.achans[fitsel.currentIndex()].get_xaxis(),	self.I.achans[fitsel.currentIndex()].get_yaxis(),self.curveFR)
					else:
						ed = self.fitData(self.I.achans[fitsel.currentIndex()].get_xaxis(),self.I.achans[fitsel.currentIndex()].get_yaxis(),self.curveF[pos])

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

			pos+=1
		if len(msg):
			self.message_label.setText(msg)
		pos=0

		if self.Liss_show.isChecked():
			chans = ['CH1','CH2','CH3','CH4']
			lissx = self.Liss_x.currentText()
			lissy = self.Liss_y.currentText()
			self.liss_x = self.Liss_x.currentIndex()
			self.liss_y = self.Liss_y.currentIndex()
			la=self.I.achans[self.liss_x].get_yaxis()
			lb=self.I.achans[self.liss_y].get_yaxis()
			if(self.liss_x<self.active_channels and self.liss_y<self.active_channels and len(la)==len(lb)):
				self.curve_lis.setData(self.I.achans[self.liss_x].get_yaxis(),self.I.achans[self.liss_y].get_yaxis())
				self.liss_ready=True
			else:
				self.curve_lis.clear()
				self.liss_ready=False
				self.message_label.setText('Channels for XY display not selected')
				#print (self.fps,'not available',self.active_channels,self.liss_x,self.liss_y)

		else:
			self.curve_lis.clear()
			for a in [self.curve1,self.curve2,self.curve3,self.curve4]:
				if self.channel_states[pos]: a.setData(self.I.achans[pos].get_xaxis()*1e-6,self.I.achans[pos].get_yaxis(),connect='finite')
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
			if self.fourierMode:
				index = int(self.I.samples*self.mousePoint.x()*self.I.timebase/1e6)
				maxIndex = len(self.curve1.getData()[0])
			else:
				index = int(self.mousePoint.x()*1e6/self.I.timebase)
				maxIndex = self.I.samples
			
			#print (self.mousePoint.x(),1.e6/self.timebase/2,index,max(self.curve1.getData()[0]),min(self.curve1.getData()[0]),len(self.curve1.getData()[0]))
			if index > 0 and index < maxIndex:
				if self.fourierMode : coords="%.1f FPS, <span style='color: white'>%s</span>: "%(self.fps,applySIPrefix(self.curve1.getData()[0][index],'Hz'))
				else : coords="%.1f FPS, <span style='color: white'>%0.1f uS</span>: "%(self.fps,self.I.achans[0].xaxis[index])
				for a in range(4):
					if self.channel_states[a]:
						c=self.trace_colors[a]
						coords+="<span style='color: rgb%s'>%0.3fV</span>," %(c, self.I.achans[a].yaxis[index])
				#self.coord_label.setText(coords)
				self.plot.plotItem.titleLabel.setText(coords)
			else:
				self.plot.plotItem.titleLabel.setText('')
				self.vLine.setPos(-1)
				self.hLine.setPos(-1)


		self.timer.singleShot(100,self.start_capture)



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
		self.I.set_gain(self.chan1remap,g)
		
		if not self.Liss_show.isChecked():
			chan = self.I.analogInputSources[self.chan1remap]
			R = [chan.calPoly10(0),chan.calPoly10(1023)]
			R[0]=R[0]*.9;R[1]=R[1]*.9
			self.plot.setYRange(min(R),max(R))
			self.plot.setLimits(yMax=max(R),yMin=min(R))			
			#RHalf = min(abs(R[0]),abs(R[1]))*0.9   #Make vertical axes symmetric. Post calibration voltage ranges are not symmetric usually.
			#self.plot.setYRange(-1*RHalf,RHalf)    #Not sure how to handle unipolar channels . TODO
		if g==8:  # attenuator mode. Remind the user
			self.displayDialog('Connect a 10MOhm resistor in series with CH1')
			self.plot.getPlotItem().setMouseEnabled(True,True)
		else:self.plot.getPlotItem().setMouseEnabled(True,False)
		
	def setGainCH2(self,g):
		self.I.set_gain('CH2',g)

		if not self.Liss_show.isChecked():
			chan = self.I.analogInputSources['CH2']
			R = [chan.calPoly10(0),chan.calPoly10(1023)]
			R[0]=R[0]*.9;R[1]=R[1]*.9
			self.plot2.setYRange(min(R),max(R))
			self.plot2.setLimits(yMax=max(R),yMin=min(R))		
			
			#RHalf = min(abs(R[0]),abs(R[1]))*0.9  #Make vertical axes symmetric. Post calibration voltage ranges are not symmetric usually.
			#self.plot.setYRange(-1*RHalf,RHalf)
		if g==8:  # attenuator mode. Remind the user
			self.displayDialog('Connect a 10MOhm resistor in series with CH2')
			self.plot2.setMouseEnabled(True,True)
		else:self.plot2.setMouseEnabled(True,False)


	def setTimeBase(self,g):
		timebases = [1.75,2,4,8,16,32,128,256,512,1024,2048]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
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
		if self.trigger_channel==0:self.triggerChannelName=self.chan1remap
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

	def remap_CH0(self,val):
		val = str(val)
		self.plot.setLabel('left',val, units='V',**self.LlabelStyle)
		self.chosa = self.I.__calcCHOSA__(val)
		self.chan1remap=val
		chan = self.I.analogInputSources[self.chan1remap]
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		self.plot.setYRange(min(R),max(R))
		if val!='CH1':self.CH1GainBox.setEnabled(False)   # remapped. gain does not apply
		else :self.CH1GainBox.setEnabled(True)
		
	def autoRange(self):
		if self.Liss_show.isChecked():
			X = self.I.analogInputSources[self.chan1remap]
			R1 = [X.calPoly10(0),X.calPoly10(1023)]
			R1[0]=R1[0]*.9;R1[1]=R1[1]*.9
			
			Y = self.I.analogInputSources['CH2']
			R2 = [Y.calPoly10(0),Y.calPoly10(1023)]
			R2[0]=R2[0]*.9;R2[1]=R2[1]*.9

			self.plot.setLimits(yMax=max(R2),yMin=min(R2),xMin=min(R1),xMax=max(R1))		
			self.plot.setXRange(min(R1),max(R1))
			self.plot.setYRange(min(R2),max(R2))

		else:
			chan = self.I.analogInputSources[self.chan1remap]
			R = [chan.calPoly10(0),chan.calPoly10(1023)]
			R[0]=R[0]*.9;R[1]=R[1]*.9
			chan = self.I.analogInputSources['CH2']
			R2 = [chan.calPoly10(0),chan.calPoly10(1023)]
			R2[0]=R2[0]*.9;R2[1]=R2[1]*.9
			self.plot.setYRange(min(R),max(R))
			self.plot2.setYRange(min(R2),max(R2))
			if not self.fourierMode:
				xlen = (self.timebase*self.samples*1e-6)
			else:
				xlen = 1.e6/self.timebase/2
				self.plot.autoRange();self.plot2.autoRange()
				print (xlen)

			self.plot.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
			self.plot2.setLimits(yMax=max(R2),yMin=min(R2))		
			if self.fourierMode:
				self.time_label.setText(applySIPrefix(xlen, unit='Hz',precision=2 ))
			else:
				self.time_label.setText(applySIPrefix(xlen, unit='S',precision=2 ))
			self.plot.setXRange(0,xlen)

	def enableXY(self,state):
		self.autoRange()



	def plot_liss(self):
		lissx = self.Liss_x.currentText()
		lissy = self.Liss_y.currentText()
		self.liss_x = self.Liss_x.currentIndex()
		self.liss_y = self.Liss_y.currentIndex()
		if not (self.channel_states[self.liss_x] and self.channel_states[self.liss_y]):
			QtGui.QMessageBox.about(self, 'Error : Insufficient Data',  'Please enable the selected channels in the oscilloscope')
			return

		self.liss_win = pg.GraphicsWindow(title="Basic plotting examples")
		self.liss_win.setWindowTitle('pyqtgraph example: Plotting')
		self.p1 = self.liss_win.addPlot(title="Lissajous: x : %s vs y : %s"%(lissx,lissy),x=self.I.achans[self.liss_x].get_yaxis(),y=self.I.achans[self.liss_y].get_yaxis())
		self.p1.setLabel('left',lissy);self.p1.setLabel('bottom',lissx)
		self.p1.getAxis('left').setGrid(170)
		self.p1.getAxis('bottom').setGrid(170)

		self.lissvLine = pg.InfiniteLine(angle=90, movable=False,pen=[100,100,200,200])
		self.p1.addItem(self.lissvLine, ignoreBounds=True)
		self.lisshLine = pg.InfiniteLine(angle=0, movable=False,pen=[100,100,200,200])
		self.p1.addItem(self.lisshLine, ignoreBounds=True)
		self.vb = self.p1.vb
		self.lissproxy = pg.SignalProxy(self.p1.scene().sigMouseClicked, rateLimit=60, slot=self.lissMouseClicked)

	def lissMouseClicked(self,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		if self.p1.sceneBoundingRect().contains(pos):
			mousePoint = self.vb.mapSceneToView(pos)
			self.lissvLine.setPos(mousePoint.x())
			self.lisshLine.setPos(mousePoint.y())

	def saveData(self):
		self.saveDataWindow([self.curve1,self.curve2,self.curve3,self.curve4,self.curve_lis],self.plot)



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
