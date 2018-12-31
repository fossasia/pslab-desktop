#!/usr/bin/python
'''
Stream data acquired from supported I2C sensors.

Currently Supports:\n

	MPU6050 - 3-Axis Accelerometer. 3-Axis Gyro  . Temperature sensor.\n
	HMC5883L - 3-Axis Magnetometer \n
	BMP180 - Temperature, Pressure, Altitude \n
	MLX90614 - Passive IR base temperature sensor (Thermopile) \n
	SHT21 - Temperature. humidity. \n



'''
from __future__ import print_function

from PSL_Apps.templates.widgets.clicking import Ui_Form as Ui_Clicking
from .templates import ui_sensorTemplate as sensorTemplate

from PSL.SENSORS.supported import supported
from PSL.sensorlist import sensors as sensorHints


from PSL_Apps.utilitiesClass import utilitiesClass
import pyqtgraph as pg
import time,random,functools
import numpy as np


from PyQt5 import QtCore, QtGui

params = {
'image' : 'sensors.png',
'name':'Sensor\ntmp Logger',
'hint':'''
	Temporary application to monitor MPU6050 and other I2C sensors
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
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		print (self.I.readLog()	)
		self.plot=self.add2DPlot(self.plot_area)
		self.plotLegend=self.plot.addLegend(offset=(-1,1))

		self.axisItems=[]

		self.plot.setLabel('bottom', 'Datapoints -->>')
		self.plot.setYRange(-35000,35000)
		self.curves=[]
		self.acquireList=[]
		self.actions=[]
		
		self.POINTS=1000
		self.xdata=range(self.POINTS)
		self.fps=0;self.lastTime=time.time();self.updatepos=0
		self.active_device_counter=0
		self.right_axes=[]

		self.looptimer = QtCore.QTimer()
		self.looptimer.timeout.connect(self.updatePlots)
		self.looptimer.start(2)

		self.updatepos=0



		self.deviceMenus=[]
		self.sensorWidgets=[]
		self.availableClasses=[0x68,0x1E,0x5A,0x77,0x39,0x40]

	class plotItem:
		def __init__(self,handle,ydata,curves):
			self.handle = handle
			self.ydata = ydata
			self.curves=curves

	def addPlot(self,param):
		cls=False
		cls_module = supported.get(param,None)
		if cls_module:
			cls = cls_module.connect(self.I.I2C)
		else:
			cls=None

		if cls:
			if hasattr(cls,'name'):	label = cls.name
			else: label =''
			cols=[self.random_color() for a in cls.PLOTNAMES]
			if cls.ADDRESS==0x68: #accelerometer, gyro. split plots
				curvesA=[self.addCurve(self.plot,'%s[%s]'%(label[:10],cls.PLOTNAMES[a])) for a in range(4)]
				newplt = self.addAxis(self.plot)
				self.right_axes.append(newplt)
				curvesB=[self.addCurve(newplt ,'%s[%s]'%(label[:10],cls.PLOTNAMES[a])) for a in range(4,7)]
				curves = curvesA+curvesB
			else:
				if not self.active_device_counter:
					if len(label):self.plot.setLabel('left', label)
					curves=[self.addCurve(self.plot,'%s[%s]'%(label[:10],cls.PLOTNAMES[a])) for a in range(cls.NUMPLOTS)]
				else:
					if label:
						colStr = lambda col: hex(col[0])[2:]+hex(col[1])[2:]+hex(col[2])[2:]
						newplt = self.addAxis(self.plot,label=label,color='#'+colStr(cols[0].getRgb()))
					else: newplt = self.addAxis(self.plot)
					self.right_axes.append(newplt)
					curves=[self.addCurve(newplt ,'%s[%s]'%(label[:10],cls.PLOTNAMES[a])) for a in range(cls.NUMPLOTS)]
					for a in range(cls.NUMPLOTS):
						self.plotLegend.addItem(curves[a],'%s[%s]'%(label[:10],cls.PLOTNAMES[a]))
			
			self.createMenu(cls,param)
			for a in range(cls.NUMPLOTS):
				curves[a].checked=True
				Callback = functools.partial(self.setTraceVisibility,curves[a])		
				action=QtGui.QCheckBox('%s'%(cls.PLOTNAMES[a])) #self.curveMenu.addAction('%s[%d]'%(label[:12],a)) 
				action.toggled[bool].connect(Callback)
				action.setChecked(True)
				action.setStyleSheet("background-color:rgb%s;"%(str(cols[a].getRgb())))
				self.paramMenus.insertWidget(1,action)
				self.actions.append(action)
			self.acquireList.append(self.plotItem(cls,np.zeros((cls.NUMPLOTS,self.POINTS)), curves)) 
			self.active_device_counter+=1


	def setTraceVisibility(self,curve,status):
		curve.clear()
		curve.setEnabled(status)
		curve.checked=status

	class PermanentMenu(QtGui.QMenu):
		def hideEvent(self, event):
			self.show()
        
	def createMenu(self,cls,addr):
		menu = self.PermanentMenu()
		menu.setMinimumHeight(25)
		sub_menu = QtGui.QMenu('%s:%s'%(hex(addr),cls.name[:15]))
		for i in cls.params: 
			mini=sub_menu.addMenu(i) 
			for a in cls.params[i]:
				Callback = functools.partial(getattr(cls,i),a)		
				mini.addAction(str(a),Callback) 
		menu.addMenu(sub_menu)
		self.paramMenus.insertWidget(0,menu)
		self.deviceMenus.append(menu)
		self.deviceMenus.append(sub_menu)
	

	class senHandler(QtGui.QFrame,Ui_Clicking):
		def __init__(self,addr,evaluator):
			super(AppWindow.senHandler, self).__init__()
			self.setupUi(self)
			self.label.setText(hex(addr)+':'+str(sensorHints.get(addr,['Unknown'])[0]+'?'))
			self.label.setToolTip(str(sensorHints.get(addr,'Unknown')))
			self.addr=addr
			self.cmd = evaluator
			self.button.setText('GO!')

		def clicked(self):
			self.cmd(self.addr)



	def scan(self):
		lst = self.I.I2C.scan()
		for a in self.sensorWidgets:
			a.setParent(None)
		self.sensorWidgets=[]
		for a in lst:
			if a in self.availableClasses:
				newSensor=self.senHandler(a,self.addPlot)
				self.nodeArea.insertWidget(0,newSensor)
				self.sensorWidgets.append(newSensor)

	def updatePlots(self):			
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
