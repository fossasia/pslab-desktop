import time,random,functools,pkgutil,importlib,functools,pkg_resources

import os,numbers
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from PSL_Apps.templates.widgets import dial,button,selectAndButton,sineWidget,pwmWidget,supplyWidget,setStateList,sensorWidget
from PSL_Apps.templates.widgets import spinBox,doubleSpinBox,dialAndDoubleSpin,pulseCounter,voltWidget,gainWidget,gainWidgetCombined
from PSL_Apps import saveProfile
from PSL.commands_proto import applySIPrefix
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class utilitiesClass():
	"""
	This class contains methods that simplify setting up and running
	an experiment.
	
	"""
	timers=[]
	viewBoxes=[]
	plots3D={}
	plots2D={}
	total_plot_areas=0
	funcList=[]
	gl=None
	black_trace_colors=[(0,255,20),(255,0,0),(255,255,100),(10,255,255)]
	white_trace_colors=[(0,255,20),(255,0,0),(255,255,100),(10,255,255)]
	black_trace_colors+=[QtGui.QColor(random.randint(50,255),random.randint(50,255),random.randint(50,255)) for a in range(50)]
	white_trace_colors+=[QtGui.QColor(random.randint(50,200),random.randint(50,200),random.randint(50,200)) for a in range(50)]
	
	properties={'colorScheme':'black'}
	def __init__(self):
		sys.path.append('/usr/share/pslab')
		pass

	def enableShortcuts(self):
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(dial._translate("MainWindow", "Ctrl+S", None)), self), QtCore.SIGNAL('activated()'), self.saveData)


	def applySIPrefix(self,value, unit='',precision=2 ):
			neg = False
			if value < 0.:
				value *= -1; neg = True
			elif value == 0.:  return '0 '  # mantissa & exponnt both 0
			exponent = int(np.log10(value))
			if exponent > 0:
				exponent = (exponent // 3) * 3
			else:
				exponent = (-1*exponent + 3) // 3 * (-3)

			value *= (10 ** (-exponent) )
			if value >= 1000.:
				value /= 1000.0
				exponent += 3
			if neg:
				value *= -1
			exponent = int(exponent)
			PREFIXES = "yzafpnum kMGTPEZY"
			prefix_levels = (len(PREFIXES) - 1) // 2
			si_level = exponent // 3
			if abs(si_level) > prefix_levels:
				raise ValueError("Exponent out range of available prefixes.")
			return '%.*f %s%s' % (precision, value,PREFIXES[si_level + prefix_levels],unit)


	class utils:
		def __init__(self):
			pass

		def applySIPrefix(self,value, unit='',precision=2 ):
				neg = False
				if value < 0.:
					value *= -1; neg = True
				elif value == 0.:  return '0 '  # mantissa & exponnt both 0
				exponent = int(np.log10(value))
				if exponent > 0:
					exponent = (exponent // 3) * 3
				else:
					exponent = (-1*exponent + 3) // 3 * (-3)

				value *= (10 ** (-exponent) )
				if value >= 1000.:
					value /= 1000.0
					exponent += 3
				if neg:
					value *= -1
				exponent = int(exponent)
				PREFIXES = "yzafpnum kMGTPEZY"
				prefix_levels = (len(PREFIXES) - 1) // 2
				si_level = exponent // 3
				if abs(si_level) > prefix_levels:
					raise ValueError("Exponent out range of available prefixes.")
				return '%.*f %s%s' % (precision, value,PREFIXES[si_level + prefix_levels],unit)

	def __importGL__(self):
		print ('importing opengl')
		import pyqtgraph.opengl as gl
		self.gl = gl

	def updateViews(self,plot):
		for a in plot.viewBoxes:
			a.setGeometry(plot.getViewBox().sceneBoundingRect())
			a.linkedViewChanged(plot.plotItem.vb, a.XAxis)

	def setColorSchemeWhite(self):
		self.properties['colorScheme']='white'
		for plot in self.plots2D:
			try:
				plot.setBackground((252,252,245, 255))
			except:
				pass

			for a in ['left','bottom','right']:
				try:
					axis = plot.getAxis(a)
					axis.setPen('k')
				except:
					pass
			
			n=0
			if isinstance(plot, pg.widgets.PlotWidget.PlotWidget):  #Only consider curves part of the main left axis
				for c in self.plots2D[plot]: #Change curve colors to match white background
					c.setPen(color=self.white_trace_colors[n], width=3)
					n+=1
					if(n==54):break

				try:
					for d in self.plots2D[plot].viewBoxes:  #Go through the additional axes too
						for f in self.plots2D[d]:
							f.setPen(color=self.white_trace_colors[n], width=3)
							n+=1
							if(n==54):break
				except: pass

				try:
					for d in plot.axisItems:  #Go through any additional axes, and set colors there too
						d.setPen('k')
				except Exception as ex: print ('error while changing scheme',ex)


	def rightClickToZoomOut(self,plot):
		clickEvent = functools.partial(self.autoRangePlot,plot)
		return pg.SignalProxy(plot.scene().sigMouseClicked, rateLimit=60, slot=clickEvent)


	def autoRangePlot(self,plot,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		if plot.sceneBoundingRect().contains(pos) and evt[0].button() == QtCore.Qt.RightButton:
			plot.enableAutoRange(True,True)

	def enableCrossHairs(self,plot,curves):
		plot.setTitle('')
		vLine = pg.InfiniteLine(angle=90, movable=False,pen=[100,100,200,200])
		plot.addItem(vLine, ignoreBounds=True)
		hLine = pg.InfiniteLine(angle=0, movable=False,pen=[100,100,200,200])
		plot.addItem(hLine, ignoreBounds=True)
		plot.hLine = hLine; plot.vLine = vLine
		crossHairPartial = functools.partial(self.crossHairEvent,plot)
		proxy = pg.SignalProxy(plot.scene().sigMouseClicked, rateLimit=60, slot=crossHairPartial)
		plot.proxy = proxy
		plot.mousePoint=None

	def crossHairEvent(self,plot,evt):
		pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
		if plot.sceneBoundingRect().contains(pos):
			plot.mousePoint = plot.getPlotItem().vb.mapSceneToView(pos)
			plot.vLine.setPos(plot.mousePoint.x())
			plot.hLine.setPos(plot.mousePoint.y())

	def displayCrossHairData(self,plot,fmode,ns,tg,axes,cols):
		if plot.mousePoint:
			if fmode:
				index = int(ns*plot.mousePoint.x()*tg/1e6)
			else:
				index = int(plot.mousePoint.x()*1e6/tg)

			maxIndex = ns			
			if index > 0 and index < maxIndex:
				coords=''' '''
				for col,a in zip(cols,axes):
						try: coords+="<span style='color: rgb%s'>%0.3fV</span>," %(col, a[index])
						except: pass
				#self.coord_label.setText(coords)
				plot.plotItem.titleLabel.setText(coords)
			else:
				plot.plotItem.titleLabel.setText('')
				plot.vLine.setPos(-1)
				plot.hLine.setPos(-1)



	def setColorSchemeBlack(self):
		self.properties['colorScheme']='black'
		for plot in self.plots2D:
			try:
				plot.setBackground((0,0,0,255))
			except:
				pass
			for a in ['left','bottom','right']:
				try:
					axis = plot.getAxis(a)
					axis.setPen('w')
				except:
					pass

			n=0
			if isinstance(plot, pg.widgets.PlotWidget.PlotWidget):  #Only consider curves part of the main left axis
				for c in self.plots2D[plot]: #Change curve colors to match black background
					c.setPen(color=self.black_trace_colors[n], width=2)
					n+=1
					if(n==54):break

				try:
					for d in self.plots2D[plot].viewBoxes:  #Go through the additional axes too
						for f in self.plots2D[d]:
							f.setPen(color=self.black_trace_colors[n], width=2)
							n+=1
							if(n==54):break
				except: pass

				try:
					for d in plot.axisItems:  #Go through any additional axes, and set colors there too
						d.setPen('w')
				except Exception,ex: print ('error while changing scheme',ex)




				for c in self.plots2D[plot]: #Change curve colors to match black background
					c.setPen(color=self.black_trace_colors[n], width=3)
					n+=1
					if(n==54):break


		
	def random_color(self):
		c=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
		if np.average(c.getRgb())<150:
			c=self.random_color()
		return c

	def add2DPlot(self,plot_area,**args):
		plot=pg.PlotWidget(**args)
		plot.setMinimumHeight(250)
		plot_area.addWidget(plot)
		
		plot.getAxis('left').setGrid(170)
		plot.getAxis('bottom').setGrid(170)

		plot.viewBoxes=[]
		plot.axisItems=[]
		self.plots2D[plot]=[]
		if self.properties['colorScheme']=='white':
			self.setColorSchemeWhite()
		return plot


	def add3DPlot(self,plot_area):
		if not self.gl : self.__importGL__()
		plot3d = self.gl.GLViewWidget()
		#gx = self.gl.GLGridItem();gx.rotate(90, 0, 1, 0);gx.translate(-10, 0, 0);self.plot.addItem(gx)
		#gy = self.gl.GLGridItem();gy.rotate(90, 1, 0, 0);gy.translate(0, -10, 0);self.plot.addItem(gy)
		gz = self.gl.GLGridItem();#gz.translate(0, 0, -10);
		plot3d.addItem(gz);
		plot3d.opts['distance'] = 40
		plot3d.opts['elevation'] = 5
		plot3d.opts['azimuth'] = 20
		plot3d.setMinimumHeight(250)
		plot_area.addWidget(plot3d)
		self.plots3D[plot3d]=[]
		plot3d.plotLines3D=[]
		return plot3d


	def addCurve(self,plot,name='',**kwargs):
		if(len(name)):curve = pg.PlotDataItem(name=name)
		else:curve = pg.PlotCurveItem(**kwargs)
		plot.addItem(curve)
		if self.properties['colorScheme']=='white':
			curve.setPen(kwargs.get('pen',{'color':self.white_trace_colors[len(self.plots2D[plot])],'width':1}))
		elif self.properties['colorScheme']=='black':
			curve.setPen(kwargs.get('pen',{'color':self.black_trace_colors[len(self.plots2D[plot])],'width':1}))
		#print (self.black_trace_colors[len(self.plots2D[plot])] , len(self.plots2D[plot]) )
		self.plots2D[plot].append(curve)
		return curve

	def removeCurve(self,plot,curve):
		plot.removeItem(curve)
		try:
			self.plots2D[plot].pop(self.plots2D[plot].index(curve))
		except:
			pass


	def rebuildLegend(self,plot):
		return plot.addLegend(offset=(-10,30))


	def fetchColumns(self,qtablewidget,*args):
		data = [[] for a in range(len(args))]
		pos=0
		for col in args:
			for row in range(50):
				item = qtablewidget.item(row,col)
				if item:
					try:
						data[pos].append(float(item.text()))
					except:
						break
				else:
					break
			pos+=1
		return data

	def fetchSelectedItemsFromColumns(self,qtablewidget,*args):
		data = [[] for a in range(len(args))]
		pos=0
		for col in args:
			for row in range(50):
				item = qtablewidget.item(row,col)
				if item:
					if item.isSelected():
						try:
							data[pos].append(float(item.text()))
						except:
							break
				else:
					break
			pos+=1
		return data


	def newPlot(self,x,y,**args):
		self.plot_ext = pg.GraphicsWindow(title=args.get('title',''))
		self.curve_ext = self.plot_ext.addPlot(title=args.get('title',''), x=x,y=y,connect='finite')
		self.curve_ext.setLabel('bottom',args.get('xLabel',''))
		self.curve_ext.setLabel('left',args.get('yLabel',''))

	def addAxis(self,plot,**args):
		p3 = pg.ViewBox()
		ax3 = pg.AxisItem('right')
		plot.plotItem.layout.addItem(ax3, 2, 3+len(plot.axisItems))
		plot.plotItem.scene().addItem(p3)
		ax3.linkToView(p3)
		p3.setXLink(plot.plotItem)
		ax3.setZValue(-10000)
		if args.get('label',False):
			ax3.setLabel(args.get('label',False), color=args.get('color','#ffffff'))

		p3.setGeometry(plot.plotItem.vb.sceneBoundingRect())
		p3.linkedViewChanged(plot.plotItem.vb, p3.XAxis)
		## Handle view resizing 
		Callback = functools.partial(self.updateViews,plot)		
		plot.getViewBox().sigStateChanged.connect(Callback)
		plot.viewBoxes.append(p3)
		plot.axisItems.append(ax3)
		self.plots2D[p3]=[]  # TODO do not consider a new axis as a plot. simply make it a part of the axisItems array of the main plot
		return p3

	def enableRightAxis(self,plot):
		p = pg.ViewBox()
		plot.showAxis('right')
		plot.setMenuEnabled(False)
		plot.scene().addItem(p)
		plot.getAxis('right').linkToView(p)
		p.setXLink(plot)
		plot.viewBoxes.append(p)
		Callback = functools.partial(self.updateViews,plot)		
		plot.getViewBox().sigStateChanged.connect(Callback)
		if self.properties['colorScheme']=='white':
			self.setColorSchemeWhite()
		self.plots2D[p]=[]
		return p


	def updateViews(self,plot):
		for a in plot.viewBoxes:
			a.setGeometry(plot.getViewBox().sceneBoundingRect())
			a.linkedViewChanged(plot.plotItem.vb, a.XAxis)



	def loopTask(self,interval,func,*args):
			timer = QtCore.QTimer()
			timerCallback = functools.partial(func,*args)
			timer.timeout.connect(timerCallback)
			timer.start(interval)
			self.timers.append(timer)
			return timer
		
	def delayedTask(self,interval,func,*args):
			timer = QtCore.QTimer()
			timerCallback = functools.partial(func,*args)
			timer.singleShot(interval,timerCallback)
			self.timers.append(timer)





	def displayDialog(self,txt=''):
			QtGui.QMessageBox.about(self, 'Message',  txt)


	class spinIcon(QtGui.QFrame,spinBox.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.spinIcon, self).__init__()
			self.setupUi(self)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))
			self.linkFunc = args.get('LINK',None)

			self.scale = args.get('SCALE_FACTOR',1)

			self.spinBox.setMinimum(args.get('MIN',0))
			self.spinBox.setMaximum(args.get('MAX',100))

		def setValue(self,val):
			retval = self.func(val)
			#self.value.setText('%.3f %s '%(retval*self.scale,self.units))
			if isinstance(retval,numbers.Number):
				self.value.setText('%s'%(self.applySIPrefix(retval*self.scale,self.units) ))
			else: self.value.setText(str(retval))
			if self.linkFunc:
				self.linkFunc(retval*self.scale,self.units)
				#self.linkObj.setText('%.3f %s '%(retval*self.scale,self.units))

	class doubleSpinIcon(QtGui.QFrame,doubleSpinBox.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.doubleSpinIcon, self).__init__()
			self.setupUi(self)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))
			self.linkFunc = args.get('LINK',None)

			self.scale = args.get('SCALE_FACTOR',1)

			self.doubleSpinBox.setMinimum(args.get('MIN',0))
			self.doubleSpinBox.setMaximum(args.get('MAX',100))

		def setValue(self,val):
			retval = self.func(val)
			if isinstance(retval,numbers.Number): self.value.setText('%s'%(self.applySIPrefix(retval*self.scale,self.units) ))
			else: self.value.setText(str(retval))
			#self.value.setText('%.3f %s '%(retval*self.scale,self.units))
			if self.linkFunc:
				self.linkFunc(retval*self.scale,self.units)
				#self.linkObj.setText('%.3f %s '%(retval*self.scale,self.units))


	class dialIcon(QtGui.QFrame,dial.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.dialIcon, self).__init__()
			self.setupUi(self)
			self.linkFunc = args.get('LINK',None)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))

			self.scale = args.get('SCALE_FACTOR',1)

			self.dial.setMinimum(args.get('MIN',0))
			self.dial.setMaximum(args.get('MAX',100))

		def setValue(self,val):
			try:
				retval = self.func(val)
			except Exception,err:
				retval = 'err'

			if isinstance(retval,numbers.Number):
				self.value.setText('%s'%(self.applySIPrefix(retval*self.scale,self.units) ))
				if self.linkFunc:
					self.linkFunc(retval*self.scale,self.units)
					#self.linkObj.setText('%.3f %s '%(retval*self.scale,self.units))
			else: self.value.setText(str(retval))
			#self.value.setText('%.2f %s '%(retval*self.scale,self.units))



	class dialAndDoubleSpinIcon(QtGui.QFrame,dialAndDoubleSpin.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.dialAndDoubleSpinIcon, self).__init__()
			self.linkFunc = args.get('LINK',None)
			self.setupUi(self)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			self.value.setSuffix(' '+self.units)
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))
			self.dial.setMinimum(args.get('MIN',0))
			self.dial.setMaximum(args.get('MAX',100))
			self.value.setMinimum(args.get('MIN',0))
			self.value.setMaximum(args.get('MAX',100))

		def setValue(self,val):
			retval = self.func(val)
			self.value.setValue(retval)
			if self.linkFunc:
				self.linkFunc(retval,self.units)

		def setDoubleValue(self):
			try:
				retval = self.func(self.value.value())
				self.value.setValue(int(retval))
				self.dial.setValue(int(retval))
				if self.linkFunc:
					self.linkFunc(retval,self.units)
			except:
				pass


	class buttonIcon(QtGui.QFrame,button.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.buttonIcon, self).__init__()
			self.setupUi(self)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))


		def read(self):
			retval = self.func()
			#if abs(retval)<1e4 and abs(retval)>.01:self.value.setText('%.3f %s '%(retval,self.units))
			#else: self.value.setText('%.3e %s '%(retval,self.units))
			if isinstance(retval,numbers.Number):self.value.setText('%s'%(self.applySIPrefix(retval,self.units) ))
			else: self.value.setText(str(retval))

	class selectAndButtonIcon(QtGui.QFrame,selectAndButton.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.selectAndButtonIcon, self).__init__()
			self.setupUi(self)
			self.linkFunc = args.get('LINK',None)
			self.name = args.get('TITLE','')
			self.title.setText(self.name)
			self.func = args.get('FUNC',None)
			self.units = args.get('UNITS','')
			self.button.setText(args.get('LABEL','Read'))
			self.optionBox.addItems(args.get('OPTIONS',[]))
			if 'TOOLTIP' in args:self.widgetFrameOuter.setToolTip(args.get('TOOLTIP',''))

		def read(self):
			retval = self.func(self.optionBox.currentText())
			#if abs(retval)<1e4 and abs(retval)>.01:self.value.setText('%.3f %s '%(retval,self.units))
			#else: self.value.setText('%.3e %s '%(retval,self.units))
			if isinstance(retval,numbers.Number):self.value.setText('%s'%(self.applySIPrefix(retval,self.units) ))
			else: self.value.setText(str(retval))
			if self.linkFunc:
				self.linkFunc(retval)

	class gainIcon(QtGui.QFrame,gainWidget.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.gainIcon, self).__init__()
			self.setupUi(self)
			self.func = args.get('FUNC',None)
			self.linkFunc = args.get('LINK',None)
			self.msg = QtGui.QMessageBox()
			self.msg.setIcon(QtGui.QMessageBox.Information)
			self.msg.setWindowTitle("Set Input Attenuation")
			self.msg.setText("Note :");
			self.msg.setInformativeText("Please connect a 10MOhm resistor in series with this input")
			self.msg.setDetailedText("Connecting a 10MOhm resistor in series with the channel causes an 11x attenuation.\nThe software automatically compensates for this, and assumes a +/-160V range \n")

		def setGainCH1(self,g):
			if (g==8):
				self.msg.exec_()
			retval= self.func('CH1',g)
			if self.linkFunc:
				self.linkFunc(retval)
		def setGainCH2(self,g):
			if (g==8):
				self.msg.exec_()
			retval= self.func('CH2',g)
			if self.linkFunc:
				self.linkFunc(retval)

	class gainIconCombined(QtGui.QFrame,gainWidgetCombined.Ui_Form,utils):
		def __init__(self,**args):
			super(utilitiesClass.gainIconCombined, self).__init__()
			self.setupUi(self)
			self.func = args.get('FUNC',None)
			self.linkFunc = args.get('LINK',None)

		def setGains(self,g):
			if (g==8):
				msg = QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Information)
				msg.setWindowTitle("Set Input Attenuation")
				msg.setText("Note :");
				msg.setInformativeText("Please connect a 10MOhm resistor in series on both inputs")
				msg.setDetailedText("Connecting a 10MOhm resistor in series with the channel causes an 11x attenuation.\nThe software automatically compensates for this, and assumes a +/-160V range \n")
				msg.exec_()
			self.func('CH1',g)
			retval=self.func('CH2',g)
			if self.linkFunc:
				self.linkFunc(retval)



	class pulseCounterIcon(QtGui.QFrame,pulseCounter.Ui_Form):
		def __init__(self,I):
			super(utilitiesClass.pulseCounterIcon, self).__init__()
			self.setupUi(self)
			self.readfn = I.readPulseCount
			self.resetfn = I.countPulses
			self.channelBox.addItems(I.allDigitalChannels)

		def read(self):
			retval = self.readfn()
			self.value.setText('%d'%(retval))

		def reset(self):
			chan = self.channelBox.currentText()
			if len(chan):self.resetfn(chan)



	class experimentIcon(QtGui.QPushButton):
		mouseHover = QtCore.pyqtSignal(str)
		def __init__(self,basepackage,name,launchfunc,*args):
			super(utilitiesClass.experimentIcon, self).__init__()
			self.setMouseTracking(True)
			self.name = name
			tmp = importlib.import_module(basepackage+'.'+name)
			genName = tmp.params.get('name',name)
			self.setText(genName)
			self.hintText = tmp.params.get('hint','No summary available')
			try:
				if 'local' in args: imgloc = pkg_resources.resource_filename(basepackage+'.icons', _fromUtf8(tmp.params.get('image','') )) 
				else: imgloc = pkg_resources.resource_filename('psl_res.ICONS', _fromUtf8(tmp.params.get('image','') )) 
			except:
				imgloc = ''
			self.hintText = '''
			<img src="%s" align="left" width="120" style="margin: 0 20"/><strong>%s</strong><br>%s
			'''%(imgloc,genName.replace('\n',' '),self.hintText)
			self.func = launchfunc			
			self.clicked.connect(self.func)
			self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred))
			self.setMaximumWidth(170)
			#self.setStyleSheet("border-image: url(%s) 0 0 0 0 stretch stretch;color:white;"%(pkg_resources.resource_filename('PSL_Apps.icons', _fromUtf8(tmp.params.get('image','') ))))
			self.setStyleSheet("color:black;background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #bbb);")
			self.setMinimumHeight(50)#70)

		def enterEvent(self, event):
			self.mouseHover.emit(self.hintText)

		def leaveEvent(self, event):
			self.mouseHover.emit('')



	class experimentListItem(QtGui.QPushButton):
		mouseHover = QtCore.pyqtSignal(str)
		def __init__(self,basepackage,name,launchfunc):
			super(utilitiesClass.experimentListItem, self).__init__()
			self.setMouseTracking(True)
			self.name = name
			tmp = importlib.import_module(basepackage+'.'+name)
			genName = tmp.params.get('name',name)
			self.setText(genName)
			self.hintText = tmp.params.get('hint','No summary available')
			self.hintText = '''
			<p><strong>%s</strong>.</p>
			%s
			'''%(genName.replace('\n',' '), self.hintText)
			self.func = launchfunc			
			self.clicked.connect(self.func)
			self.setMinimumHeight(30)
			#self.setMaximumWidth(170)
			#self.setStyleSheet("border-image: url(%s) 0 0 0 0 stretch stretch;color:white;"%(pkg_resources.resource_filename(basepackage, _fromUtf8(tmp.params.get('image','') ))))

		def enterEvent(self, event):
			self.mouseHover.emit(self.hintText)

		def leaveEvent(self, event):
			self.mouseHover.emit('')



	class sineWidget(QtGui.QWidget,sineWidget.Ui_Form):
		def __init__(self,I):
			super(utilitiesClass.sineWidget, self).__init__()
			self.setupUi(self)
			self.I = I
			self.commandLinkButton.setVisible(False)  #TODO : 
			self.modes = ['sine','tria']


		def loadSineTable(self):
			if self.I:
				from PSL_Apps.utilityApps import loadSineTable
				inst = loadSineTable.AppWindow(self,I=self.I)
				inst.show()
			else:
				print (self.setWindowTitle('Device Not Connected!'))

		def setSINE1(self,val):
			f=self.I.set_w1(val)
			self.WAVE1_FREQ.setText('%.2f'%(f))

		def setSINE2(self,val):
			f=self.I.set_w2(val)
			self.WAVE2_FREQ.setText('%.2f'%(f))

		def setSinePhase(self):
			freq1 = self.SINE1BOX.value()
			freq2 = self.SINE2BOX.value()
			phase = self.SINEPHASE.value()
			f=self.I.set_waves(freq1,phase,freq2)
			self.WAVE1_FREQ.setText('%.2f'%(f))
			self.WAVE2_FREQ.setText('%.2f'%(f))

		def setW1Type(self,val):
			self.I.load_equation('W1',self.modes[val])
		def setW2Type(self,val):
			self.I.load_equation('W2',self.modes[val])


	class sensorIcon(QtGui.QFrame,sensorWidget.Ui_Form):
		def __init__(self,cls,**kwargs):
			super(utilitiesClass.sensorIcon, self).__init__()
			self.cls = cls
			self.setupUi(self)
			self.hintLabel.setText(kwargs.get('hint',''))
			self.func = cls.getRaw
			self.plotnames = cls.PLOTNAMES
			self.menu = self.PermanentMenu()
			self.menu.setMinimumHeight(25)
			self.sub_menu = QtGui.QMenu('%s:%s'%(hex(cls.ADDRESS),cls.name[:15]))
			for i in cls.params: 
				mini=self.sub_menu.addMenu(i) 
				for a in cls.params[i]:
					Callback = functools.partial(getattr(cls,i),a)		
					mini.addAction(str(a),Callback)
			self.menu.addMenu(self.sub_menu)
			self.formLayout.insertWidget(0,self.menu)

		class PermanentMenu(QtGui.QMenu):
			def hideEvent(self, event):
				self.show()


		def read(self):
			retval = self.func()
			if not retval:
				self.resultLabel.setText('err')
				return
			res = ''
			for a in range(len(retval)):
				res+=self.plotnames[a]+'\t%.3e\n'%(retval[a])
			self.resultLabel.setText(res)



	class pwmWidget(QtGui.QWidget,pwmWidget.Ui_Form):
		def __init__(self,I):
			super(utilitiesClass.pwmWidget, self).__init__()
			self.setupUi(self)
			self.I = I

		def setSQRS(self):
			P2=self.SQR2P.value()/360.
			P3=self.SQR3P.value()/360.
			P4=self.SQR4P.value()/360.
			D1=self.SQR1DC.value()
			D2=self.SQR2DC.value()
			D3=self.SQR3DC.value()
			D4=self.SQR4DC.value()
			
			retval = self.I.sqrPWM(self.SQRSF.value(),D1,P2,D2,P3,D3,P4,D4)
			try:
				self.SQRSF.setValue(retval)
			except Exception,e:
				print (e.message)

		def fireSQR1(self):
			if self.I:
				from PSL_Apps.utilityApps import firePulses
				inst = firePulses.AppWindow(self,I=self.I)
				inst.show()
			else:
				print (self.setWindowTitle('Device Not Connected!'))



	class voltWidget(QtGui.QWidget,voltWidget.Ui_Form,utils):
		def __init__(self,I):
			super(utilitiesClass.voltWidget, self).__init__()
			self.setupUi(self)

			self.I = I
			self.col1=['CH1','CH2','CH3']
			self.col2=['CAP','SEN','AN8']
			pos=0
			for a,b in zip(self.col1,self.col2):
				item = QtGui.QTableWidgetItem();self.table.setItem(pos,0,item);	item.setText('%s'%a)
				item = QtGui.QTableWidgetItem();self.table.setItem(pos,2,item); item.setText('%s'%b)

				item = QtGui.QTableWidgetItem();self.table.setItem(pos,1,item);	item.setText('')
				item = QtGui.QTableWidgetItem();self.table.setItem(pos,3,item); item.setText('')

				pos+=1


		def read(self):
			pos =0 
			for a,b in zip(self.col1,self.col2):
				self.table.item(pos,1).setText(self.applySIPrefix(self.I.get_average_voltage(a),'V'))
				self.table.item(pos,3).setText(self.applySIPrefix(self.I.get_average_voltage(b),'V'))
				pos+=1



	class supplyWidget(QtGui.QWidget,supplyWidget.Ui_Form,utils):
		def __init__(self,I):
			super(utilitiesClass.supplyWidget, self).__init__()
			self.setupUi(self)
			self.I = I

		def setPV1(self,val):
			val=self.I.DAC.setVoltage('PV1',val)
			self.PV1_LABEL.setText(self.applySIPrefix(val,'V'))

		def setPV2(self,val):
			val=self.I.DAC.setVoltage('PV2',val)
			self.PV2_LABEL.setText(self.applySIPrefix(val,'V'))

		def setPV3(self,val):
			val=self.I.DAC.setVoltage('PV3',val)
			self.PV3_LABEL.setText(self.applySIPrefix(val,'V'))

		def setPCS(self,val):
			val=self.I.DAC.setVoltage('PCS',val/1.e3)
			self.PCS_LABEL.setText(self.applySIPrefix(val,'A'))




	class setStateIcon(QtGui.QFrame,setStateList.Ui_Form):
		def __init__(self,**args):
			super(utilitiesClass.setStateIcon, self).__init__()
			self.setupUi(self)
			self.I = args.get('I',None)
		def toggle1(self,state):
			self.I.set_state(SQR1 = state)
		def toggle2(self,state):
			self.I.set_state(SQR2 = state)
		def toggle3(self,state):
			self.I.set_state(SQR3 = state)
		def toggle4(self,state):
			self.I.set_state(SQR4 = state)



	def addPV1(self,I,link=None):
		tmpfunc = functools.partial(I.DAC.__setRawVoltage__,'PV1')
		a1={'TITLE':'PV1','MIN':0,'MAX':4095,'FUNC':tmpfunc,'UNITS':'V','TOOLTIP':'Programmable Voltage Source 1'}
		if link: a['LINK'] = link
		return self.dialIcon(**a1)

	def addPV2(self,I,link=None):
		tmpfunc = functools.partial(I.DAC.__setRawVoltage__,'PV2')
		a={'TITLE':'PV2','MIN':0,'MAX':4095,'FUNC':tmpfunc,'UNITS':'V','TOOLTIP':'Programmable Voltage Source 2'}
		if link: a['LINK'] = link
		return self.dialIcon(**a)


	def addPV3(self,I,link=None):
		tmpfunc = functools.partial(I.DAC.__setRawVoltage__,'PV3')
		a={'TITLE':'PV3','MIN':0,'MAX':4095,'FUNC':tmpfunc,'UNITS':'V','TOOLTIP':'Programmable Voltage Source 3'}
		if link: a['LINK'] = link
		return self.dialIcon(**a)

	def addPCS(self,I,link=None):
		tmpfunc = functools.partial(I.DAC.__setRawVoltage__,'PCS')
		a={'TITLE':'PCS','MIN':0,'MAX':4095,'FUNC':tmpfunc,'UNITS':'A','TOOLTIP':'Programmable Current Source'}
		if link: a['LINK'] = link
		return self.dialIcon(**a)

	def addVoltmeter(self,I,link=None):
		tmpfunc = functools.partial(I.get_voltage,samples=10)
		a={'TITLE':'VOLTMETER','FUNC':tmpfunc,'UNITS':'V','TOOLTIP':'Voltmeter','OPTIONS':I.allAnalogChannels}
		if link: a['LINK'] = link
		return self.selectAndButtonIcon(**a)


	def addW1(self,I,link=None):
		a={'TITLE':'Wave 1','MIN':1,'MAX':5000,'FUNC':self.I.set_w1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1'}
		if link: a['LINK'] = link
		return self.dialAndDoubleSpinIcon(**a)


	def addW2(self,I,link=None):
		a={'TITLE':'Wave 2','MIN':1,'MAX':5000,'FUNC':self.I.set_w2,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #2'}
		if link: a['LINK'] = link
		return self.dialAndDoubleSpinIcon(**a)

	def addSQR1(self,I,link=None):
		a={'TITLE':'SQR 1','MIN':1,'MAX':100000,'FUNC':self.I.sqr1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of SQR1'}
		if link: a['LINK'] = link
		return self.dialAndDoubleSpinIcon(**a)

	def addTimebase(self,I,func):
		a={'TITLE':'TIMEBASE','MIN':0,'MAX':9,'FUNC':func,'TYPE':'dial','UNITS':'S','TOOLTIP':'Set Timebase of the oscilloscope'}
		T2 = self.dialIcon(**a)
		T2.dial.setPageStep(1)
		return T2



	def saveToCSV(self,table):
		path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '~/', 'CSV(*.csv)')
		sections = path.split('.')
		if(sections[-1]!='csv'):path+='.csv'
		if path:
			import csv
			with open(unicode(path), 'wb') as stream:
				writer = csv.writer(stream)
				for row in range(table.rowCount()):
					rowdata = []
					for column in range(table.columnCount()):
						item = table.item(row, column)
						if item is not None:
							rowdata.append(
								unicode(item.text()).encode('utf8'))
						else:
							rowdata.append('')
					writer.writerow(rowdata)

	'''
	def saveDataWindow(self,curveList,plot=None):
		from utilityApps import spreadsheet
		info = spreadsheet.AppWindow(self)
		colnum=0;labels=[]
		for a in curveList:
			x,y = a.getData()
			name = a.name()
			if x!=None and y!=None:
				info.setColumn(colnum,x);colnum+=1
				info.setColumn(colnum,y);colnum+=1
				labels.append('%s(X)'%(name));labels.append('%s(Y)'%(name));
		info.table.setHorizontalHeaderLabels(labels)
		info.show()
	'''
	
	def saveDataWindow(self,curveList,plot=None):
		from utilityApps import plotSaveWindow
		info = plotSaveWindow.AppWindow(self,curveList,plot)
		info.show()


	def savePro(self):
		from os.path import expanduser
		path = QtGui.QFileDialog.getSaveFileName(self, 'Save Profile',  expanduser("./"), 'INI(*.ini)')
		if path:
			sections = path.split('.')
			if(sections[-1]!='ini'):path+='.ini'
			saveProfile.guisave(self, QtCore.QSettings(path, QtCore.QSettings.IniFormat))

	def saveSelectedPro(self,parent):
		from os.path import expanduser
		path = QtGui.QFileDialog.getSaveFileName(self, 'Save Profile',  expanduser("./"), 'INI(*.ini)')
		sections = path.split('.')
		if(sections[-1]!='ini'):path+='.ini'
		print ('custom save',path)
		if path: saveProfile.guisave(parent, QtCore.QSettings(path, QtCore.QSettings.IniFormat))

	def loadPro(self):
		from os.path import expanduser
		filename = QtGui.QFileDialog.getOpenFileName(self,  "Load a Profile", expanduser("."), 'INI(*.ini)')
		if filename :
			saveProfile.guirestore(self, QtCore.QSettings(filename, QtCore.QSettings.IniFormat))


