#!/usr/bin/python
'''
Stream data acquired from supported I2C sensors.

Currently Supports:\n

	MPU6050 - 3-Axis Accelerometer. 3-Axis Gyro  . Temperature sensor.\n
	HMC5883L - 3-Axis Magnetometer \n
	BMP180 - Temperature, Pressure, Altitude \n
	MLX90614 - Passive IR base temperature sensor (Thermopile) \n
	SHT21 - Temperature. humidity. \n
	please refer to SENSORS.supported for more...



'''
from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass
from PSL.SENSORS.supported import supported
from PSL.sensorlist import sensors as sensorHints

from templates import ui_sensorTemplate as sensorTemplate
from PSL_Apps.templates.widgets.ui_clicking import Ui_Form as Ui_Clicking

import pyqtgraph as pg
import time,random,functools
import numpy as np


from PyQt5 import QtCore, QtGui

params = {
'image' : 'ico_sensor.png',
'name':'Sensor\nData Logger',
'hint':'''
	Plot values returned by sensors connected to the I2C input.</br>
	Support sensors include MPU6050(3-axis Accel/gyro), TSL2561(luminosity),<br>
	HMC5883L(3-axis magnetometer), SHT21(humidity), BMP180(Pressure,Altitude) etc.
	'''
}

class AppWindow(QtGui.QMainWindow, sensorTemplate.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		if self.I:
			self.I.I2C.init()
			self.I.I2C.config(400e3)

		print (self.I.readLog()	)
		self.plot=self.add2DPlot(self.plot_area)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.axisItems=[]

		self.plot.setLabel('bottom', 'Datapoints -->>')
		self.plot.setYRange(-35000,35000)
		self.plot.setLimits(xMin=0,xMax=1000)		
		self.curves=[]
		self.acquireList=[]
		self.actions=[]
		
		self.POINTS=1000
		self.xdata=range(self.POINTS)
		self.fps=0;self.lastTime=time.time();self.updatepos=0
		self.active_device_counter=0
		self.right_axes=[]

		self.looptimer = self.newTimer()
		self.looptimer.timeout.connect(self.updatePlots)
		self.looptimer.start(2)

		self.updatepos=0


		self.Running =True
		self.deviceMenus=[]
		self.sensorWidgets=[]

	class plotItem:
		def __init__(self,handle,ydata,curves):
			self.handle = handle
			self.ydata = ydata
			self.curves=curves

	def addPlot(self,cls,addr):
		bridge = cls.connect(self.I.I2C,address = addr)
		if bridge:
			self.createMenu(bridge)
			if bridge.NUMPLOTS:
				if hasattr(bridge,'name'):	label = bridge.name
				else: label =''
				if not self.active_device_counter:
					if len(label):self.plot.setLabel('left', label)
					curves=[self.addCurve(self.plot,'%s[%s]'%(label[:10],bridge.PLOTNAMES[a])) for a in range(bridge.NUMPLOTS)]
				else:
					if label:
						colStr = lambda col: hex(col[0])[2:]+hex(col[1])[2:]+hex(col[2])[2:]
						newplt = self.addAxis(self.plot,label=label)#,color='#'+colStr(cols[0].getRgb()))
					else: newplt = self.addAxis(self.plot)
					self.right_axes.append(newplt)
					curves=[self.addCurve(newplt ,'%s[%s]'%(label[:10],bridge.PLOTNAMES[a])) for a in range(bridge.NUMPLOTS)]
					#for a in range(bridge.NUMPLOTS):
					#	self.plotLegend.addItem(curves[a],'%s[%s]'%(label[:10],bridge.PLOTNAMES[a]))
				
				for a in range(bridge.NUMPLOTS):
					curves[a].checked=True
					Callback = functools.partial(self.setTraceVisibility,curves[a])		
					action=QtGui.QCheckBox('%s'%(bridge.PLOTNAMES[a])) #self.curveMenu.addAction('%s[%d]'%(label[:12],a)) 
					action.toggled[bool].connect(Callback)
					action.setChecked(True)
					action.setStyleSheet("background-color:rgb%s;"%(str(curves[a].opts['pen'].color().getRgb())))
					self.paramMenus.insertWidget(1,action)
					self.actions.append(action)
				self.acquireList.append(self.plotItem(bridge,np.zeros((bridge.NUMPLOTS,self.POINTS)), curves)) 
				self.active_device_counter+=1


	def setTraceVisibility(self,curve,status):
		curve.clear()
		curve.setEnabled(status)
		curve.checked=status

	class PermanentMenu(QtGui.QMenu):
		def hideEvent(self, event):
			self.show()
        
	def createMenu(self,bridge):
		menu = self.PermanentMenu()
		menu.setMinimumHeight(25)
		sub_menu = QtGui.QMenu('%s:%s'%(hex(bridge.ADDRESS),bridge.name[:15]))
		for i in bridge.params: 
			if bridge.params[i] is None:  #A function with no arguments.
				sub_menu.addAction(str(i),getattr(bridge,i))
			elif type(bridge.params[i]) == list:  #Function with pre-defined arguments  
				mini=sub_menu.addMenu(i)
				for a in bridge.params[i]:
					Callback = functools.partial(getattr(bridge,i),a)
					mini.addAction(str(a),Callback)
			elif type(bridge.params[i]) == dict:  #Function with user defined variable input
				mini=sub_menu.addMenu(i)
				options =  bridge.params[i]
				
				#Data type: Default is integer.
				# double : Create QDoubleSpinBox
				# Integer : Create QSpinBox
				# String : QLineEdit
				dataType = options.get('dataType','integer')
				if dataType in ['double','integer']:
					if dataType == 'double':
						Btn=QtGui.QDoubleSpinBox()
					elif dataType == 'integer':
						Btn=QtGui.QDoubleSpinBox()

					def executeCallback():
						getattr(bridge,i)(Btn.value())

					Btn.setRange(options.get('min',0),options.get('max',100))
					Btn.setPrefix(options.get('prefix',''))
					Btn.setValue(options.get('value',0))
					BtnAction = QtGui.QWidgetAction(mini)
					BtnAction.setDefaultWidget(Btn)
					mini.addAction(BtnAction)

					#Btn.editingFinished.connect(executeCallback)  #Uncomment after discussion. Is this necessary, or should we just stick with the 'Apply' button?
					mini.addAction('Apply' , executeCallback)

		menu.addMenu(sub_menu)
		self.paramMenus.insertWidget(0,menu)
		self.deviceMenus.append(menu)
		self.deviceMenus.append(sub_menu)
	

	class senHandler(QtGui.QFrame,Ui_Clicking):
		def __init__(self,cls,addr,evaluator):
			super(AppWindow.senHandler, self).__init__()
			self.setupUi(self)
			self.label.setText(hex(addr)+':'+str(sensorHints.get(addr,['Unknown'])[0]+'?'))
			self.label.setToolTip(str(sensorHints.get(addr,'Unknown')))
			#self.label.setText(hex(cls.BRIDGE.ADDRESS)+':'+cls.BRIDGE.name)
			#self.label.setToolTip(hex(cls.BRIDGE.ADDRESS)+':'+cls.BRIDGE.name)
			self.addr=addr
			self.cls = cls
			self.evaluator = evaluator
			self.button.setText('GO!')

		def clicked(self):
			self.evaluator(self.cls,self.addr)
			

	def scan(self):
		lst = self.I.I2C.scan()
		for a in self.sensorWidgets:
			a.setParent(None)
		self.sensorWidgets=[]
		for a in lst:
			if a in supported:
				newSensor=self.senHandler(supported[a],a,self.addPlot)
				self.nodeArea.insertWidget(0,newSensor)
				self.sensorWidgets.append(newSensor)

	def updatePlots(self):			
		if self.pauseBox.isChecked():return
		for item in self.acquireList:
			need_data=False
			for a in item.curves:
				if a.checked:need_data=True
			if need_data:			
				vals=item.handle.getRaw()
				if not vals:continue
				for X in range(len(item.curves)):
					item.ydata[X][self.updatepos] = vals[X]
				if self.updatepos%20==0:
					for a in range(len(item.curves)):
						if item.curves[a].checked:item.curves[a].setData(self.xdata,item.ydata[a])
		#N2.readADC(10)
		if len(self.acquireList):
			self.updatepos+=1
			if self.updatepos>=self.POINTS:self.updatepos=0
		
			now = time.time()
			dt = now - self.lastTime
			self.lastTime = now
			if self.fps is None:
				self.fps = 1.0/dt
			else:
				s = np.clip(dt*3., 0, 1)
				self.fps = self.fps * (1-s) + (1.0/dt) * s
			self.plot.setTitle('%0.2f fps' % (self.fps) )

	def saveData(self):
		self.pauseBox.setChecked(True)
		curvelist = []
		for item in self.acquireList:
			for a in item.curves:
				if a.checked:curvelist.append(a)
		self.saveDataWindow(curvelist,self.plot)


			
	def __del__(self):
		self.looptimer.stop()
		print ('bye')

	def closeEvent(self, event):
		self.looptimer.stop()
		self.finished=True
		

if __name__ == "__main__":
	from PSL import sciencelab
	import sys
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
