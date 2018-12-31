#!/usr/bin/python
'''
Stream data acquired from supported I2C sensors.

Currently Supports:\n

refer to SENSORS.supported

'''
from __future__ import print_function

from PSL_Apps.utilitiesClass import utilitiesClass
from .templates import ui_sensorGrid as sensorGrid


import pyqtgraph as pg
import time,random,functools,sys
import numpy as np


from PyQt5 import QtCore, QtGui

params = {
'image' : 'ico_sensor_w.png',
'name':'Wireless Sensor\nQuickView',
'hint':'''
	Display values returned by sensors connected to the I2C input.</br>
	Supported sensors include MPU6050(3-axis Accel/gyro), TSL2561(luminosity),<br>
	HMC5883L(3-axis magnetometer), SHT21(humidity), BMP180(Pressure,Altitude),
	MLX90614(PAssive IR based thermometer) etc,
	'''
}

class AppWindow(QtGui.QMainWindow, sensorGrid.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		if self.I:
			self.I.NRF.start_token_manager()
			print (self.I.readLog()	)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		from PSL.SENSORS.supported import supported
		self.supported = supported
		#from PSL.sensorlist import sensors as sensorHints
		#self.hints = sensorHints

		self.foundSensors=[]
		
		self.looptimer = self.newTimer()
		self.looptimer.timeout.connect(self.updateData)
		self.looptimer.start(20)
		self.deviceMenus=[]
		self.sensorWidgets=[]
		self.Running =True

	def updateData(self):
		for a in self.sensorWidgets:
			if a.autoRefresh.isChecked():
				a.read()

	def autoScan(self):
		self.scan()

	def scan(self):
		lst = self.I.NRF.get_nodelist()
		x=self.I.readLog()
		print (lst,x)		
		for a in self.sensorWidgets:
			a.setParent(None)
		self.sensorWidgets=[]
		row=0;col=0;colLimit=3
		self.ExperimentLayout.setAlignment(QtCore.Qt.AlignTop)
		for a in lst:
			for b in lst[a]:
				cls_module = self.supported.get(b,None)
				if cls_module:
					new = self.I.newRadioLink(address=a)
					cls = cls_module.connect(new)
					if cls:
						if col==colLimit:
							col=0;row+=1
						newSensor=self.sensorIcon(cls,hint='Node: '+hex(a))
						self.ExperimentLayout.addWidget(newSensor,row,col)
						self.sensorWidgets.append(newSensor)
						col+=1
			
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
