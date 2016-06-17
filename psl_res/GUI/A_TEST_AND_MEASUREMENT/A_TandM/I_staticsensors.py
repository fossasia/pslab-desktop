#!/usr/bin/python
'''
Stream data acquired from supported I2C sensors.

Currently Supports:\n

refer to SENSORS.supported

'''
from __future__ import print_function

from PSL_Apps.utilitiesClass import utilitiesClass
from .templates import sensorGrid


import pyqtgraph as pg
import time,random,functools,sys
import numpy as np


from PyQt4 import QtCore, QtGui

params = {
'image' : 'sensors.png',
'name':'Sensor\nQuickView',
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
			self.I.I2C.init()
			self.I.I2C.config(400e3)
		self.setWindowTitle('FOSSASIA PSLab : '+params.get('name','').replace('\n',' ') )

		from SEEL.SENSORS.supported import supported
		self.supported = supported
		#from SEEL.sensorlist import sensors as sensorHints
		#self.hints = sensorHints

		self.foundSensors=[]
		
		self.looptimer = QtCore.QTimer()
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
		lst = self.I.I2C.scan()
		for a in self.sensorWidgets:
			a.setParent(None)
		self.sensorWidgets=[]
		print (lst)
		
		row=0;col=0;colLimit=3
		self.ExperimentLayout.setAlignment(QtCore.Qt.AlignTop)
		for a in lst:
			cls=False
			cls_module = self.supported.get(a,None)
			if cls_module:
				cls = cls_module.connect(self.I.I2C)
				if cls:
					if col==colLimit:
						col=0;row+=1
					newSensor=self.sensorIcon(cls)
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
