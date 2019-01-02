#!/usr/bin/python

"""
::

	This program calibrates the device using a plugged in AD7718 24-bit ADC and saves the results to a directory.
	Use the calibration loader utility to process the results and write to flash.
	Not for regular users!
	Maybe dont include this in the main package

The AD7718 has already been calibrated against a KEITHLEY 2100 multimeter

PV3 - AIN7AINCOM
Connected to AN8 , AIN7

PV2 - AIN6AINCOM
Connected to AIN6, CH1,CH2,CH3

PV1
Connected to AIN5

"""
#from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass
from templates import ui_calibrator as calibrator

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,os,random,struct,time,serial.tools.list_ports


params = {
'image' : 'calib.png',
'name':'Device\nCalibrator',
'hint':'''Calibrate your device using a plugged in AD7718 24-bit ADC and save values to a directory. Use the calibration loader utility to process the results and write to flash. Not for regular users!
	AIN7AINCOM: Connected to AN8 , PV3 
	AIN6AINCOM: Connected to CH1,CH2,CH3,PV2
	AIN5AINCOM: Connected to PV1
'''

}


class acquirer():
	def __init__(self,parent):
		self.I=parent.I
		self.parent = parent
		self.INPUTS = parent.INPUTS
		self.INL_CHANNEL = 'AN8'
		self.paused = False
		if self.I : self.I.__ignoreCalibration__()

		self.DAC_VALS={'PV1':[],'PV2':[],'PV3':[]}
		self.ADC24={'AIN5':[],'AIN6':[],'AIN7':[]}
		self.ADCPIC_INL=[]

		self.ADC_VALUES={}
		self.ADC_ACTUALS={}
		for a in self.INPUTS:
			self.ADC_VALUES[a]={}
			self.ADC_ACTUALS[a]={}
			for b in range(8):
				self.ADC_VALUES[a][b]=[]
				self.ADC_ACTUALS[a][b]=[]

		self.calibs={  #TODO : load custom constants from file
		'AIN6AINCOM':[6.993123e-07,-1.563294e-06,9.994211e-01,-4.596018e-03], 
		'AIN7AINCOM':[3.911521e-07,-1.706405e-06,1.002294e+00,-1.286302e-02], 
		'AIN3AINCOM':[-3.455831e-06,2.861689e-05,1.000195e+00,3.802349e-04], 
		'AIN1AINCOM':[8.220199e-05,-4.587100e-04,1.001015e+00,-1.684517e-04], 
		'AIN5AINCOM':[-1.250787e-07,-9.203838e-07,1.000299e+00,-1.262684e-03], 
		'AIN2AINCOM':[5.459186e-06,-1.749624e-05,1.000268e+00,1.907896e-04], 
		'AIN9AINCOM':[7.652808e+00,1.479229e+00,2.832601e-01,4.495232e-02], 
		'AIN8AINCOM':[8.290843e-07,-7.129532e-07,9.993159e-01,3.307947e-03], 
		'AIN4AINCOM':[4.135213e-06,-1.973478e-05,1.000277e+00,2.115374e-04], }

		self.setADC(self.I)
		self.Running = False
		
			
	def setADC(self,I):
		from PSL.SENSORS.AD7718_class import AD7718
		self.ADC=AD7718(I,self.calibs)
		print (self.ADC.printstat())
		if self.ADC.readRegister(self.ADC.STATUS)&1==0: #PLL not locked
			print ('PLL not locked!!!!!!!!!!!!') 
		self.ADC.writeRegister(self.ADC.FILTER,20)

	def setINL_CHANNEL(self,chan):
		self.INL_CHANNEL = chan

	def getAnotherPoint(self):
		if self.vv==4096: #We're all done here.
			self.parent.typeSelectBox.setEnabled(True)
			self.parent.INLBox.setEnabled(True)
			self.Running = False
			self.timer.stop()
			self.parent.setWindowTitle(" We're all finished here")
			return
		if(self.paused):return

		
		#PV3 and ADC input AN8
		val3 = self.I.DAC.__setRawVoltage__('PV3',self.vv)
		self.DAC_VALS['PV3'].append(val3)
		time.sleep(0.001)

		self.ADC.__startRead__('AIN7AINCOM')
		ADC_INL_RAW = np.average([self.I.__get_raw_average_voltage__(self.INL_CHANNEL) for x in range(70) ])
		ADC_INL_CONVERTED = self.I.analogInputSources[self.INL_CHANNEL].calPoly12(ADC_INL_RAW)
		self.ADCPIC_INL.append(ADC_INL_CONVERTED)
		AIN7 = self.ADC.__fetchData__('AIN7AINCOM')
		self.ADC24['AIN7'].append(AIN7)

		if self.parent.calibrateOnlyADC:
				######################----Get points every 30 steps for slope & intercept calculation----######################
				if self.vv%30==0:
					val1 = self.I.DAC.__setRawVoltage__('PV1',self.vv)
					time.sleep(0.001)

					self.ADC.__startRead__('AIN6AINCOM')
					for a in self.INPUTS:
						if self.I.analogInputSources[a].gainEnabled:
							for b in range(8):
								self.I.set_gain(a,b)
								if self.I.analogInputSources[a].__conservativeInRange__(val1):
									v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(20) ]))
									self.ADC_VALUES[a][b].append(v)
									self.ADC_ACTUALS[a][b].append(self.numpoints)
						else:
							if self.I.analogInputSources[a].__conservativeInRange__(val1):
								v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(20) ]))
								self.ADC_VALUES[a][0].append(v)
								self.ADC_ACTUALS[a][0].append(self.numpoints)
					#---------------------------------------------------------------------------------------


					AIN6 = self.ADC.__fetchData__('AIN6AINCOM')
					self.ADC24['AIN6'].append(AIN6)
					#'PV1','AIN6','AIN7','PV3','INL'
					self.parent.valueTable.item(0,0).setText('%.3f'%val1)
					self.parent.valueTable.item(0,1).setText('%.3f'%AIN6)
					
					self.parent.valueTable.item(0,2).setText('%.3f'%AIN7)

					self.parent.valueTable.item(0,3).setText('%.3f'%val3)
					self.parent.valueTable.item(0,4).setText('%.3f'%ADC_INL_CONVERTED)
					self.numpoints+=1

		else:
				#PV1
				val1 = self.I.DAC.__setRawVoltage__('PV1',self.vv)
				self.DAC_VALS['PV1'].append(val1)
				time.sleep(0.001)

				self.ADC.__startRead__('AIN5AINCOM')
				time.sleep(0.1)

				AIN5 =  self.ADC.__fetchData__('AIN5AINCOM') 
				self.ADC24['AIN5'].append(AIN5)

				#PV2 and ADC inputs CH1,CH2
				val2 = self.I.DAC.__setRawVoltage__('PV2',self.vv)
				self.DAC_VALS['PV2'].append(val2)
				time.sleep(0.001)

				self.ADC.__startRead__('AIN6AINCOM')
				time.sleep(0.1)

				######################----Get points every 30 steps for slope & intercept calculation----######################
				if self.vv%30==0:
					for a in self.INPUTS:
						if self.I.analogInputSources[a].gainEnabled:
							for b in range(8):
								self.I.set_gain(a,b)
								if self.I.analogInputSources[a].__conservativeInRange__(val2):
									v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(100) ]))
									self.ADC_VALUES[a][b].append(v)
									self.ADC_ACTUALS[a][b].append(self.vv)
						else:
							if self.I.analogInputSources[a].__conservativeInRange__(val2):
								v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(100) ]))
								self.ADC_VALUES[a][0].append(v)
								self.ADC_ACTUALS[a][0].append(self.vv)
				#---------------------------------------------------------------------------------------


				AIN6 = self.ADC.__fetchData__('AIN6AINCOM')
				self.ADC24['AIN6'].append(AIN6)

				self.parent.valueTable.item(0,0).setText('%.3f'%AIN5)
				self.parent.valueTable.item(0,1).setText('%.3f'%val1)

				self.parent.valueTable.item(0,2).setText('%.3f'%AIN6)
				self.parent.valueTable.item(0,3).setText('%.3f'%val2)

				self.parent.valueTable.item(0,4).setText('%.3f'%AIN7)
				self.parent.valueTable.item(0,5).setText('%.3f'%val3)
				self.parent.valueTable.item(0,6).setText('%.3f'%ADC_INL_CONVERTED)

		#########################----UPDATE PLOTS AND TABLE----######################
		if self.vv%50==0:  
			self.parent.curves['PV3'].setData(self.ADC24['AIN7'],np.array(self.DAC_VALS['PV3'])-np.array(self.ADC24['AIN7']))
			self.parent.curves['INL'].setData(self.ADC24['AIN7'],np.array(self.ADCPIC_INL)-np.array(self.ADC24['AIN7']))
			for a in self.INPUTS:
				if self.I.analogInputSources[a].gainEnabled:
					for b in range(8):
							X = np.array(self.ADC24['AIN6'])[self.ADC_ACTUALS[a][b]]
							if len(X)>3:
								Y = np.array(self.ADC_VALUES[a][b])
								#fitvals = np.polyfit(X,Y,2)
								#fitfn = np.poly1d(fitvals)
								self.parent.curves[a][b].setData(X,Y-X)#fitfn(X) )
				else:
							X = np.array(self.ADC24['AIN6'])[self.ADC_ACTUALS[a][0]]
							if len(X)>3:
								Y = np.array(self.ADC_VALUES[a][0])
								#fitvals = np.polyfit(X,Y,2)
								#fitfn = np.poly1d(fitvals)
								self.parent.curves[a][0].setData(X,Y-X)#fitfn(X) )


		#-------------------------------------------------------
		self.parent.progressBar.setValue(self.vv*100/4095.)
		self.vv += 1;
		return True

	def startCalibration(self):
		self.Running = True
		self.I.DAC.__setRawVoltage__('PV1',0)
		self.I.DAC.__setRawVoltage__('PV2',0)
		self.I.DAC.__setRawVoltage__('PV3',0)
		time.sleep(0.1)
		self.DAC_VALS={'PV1':[],'PV2':[],'PV3':[]}
		self.ADC24={'AIN5':[],'AIN6':[],'AIN7':[]}
		self.ADCPIC_INL=[]

		self.ADC_VALUES={}
		self.ADC_ACTUALS={}
		for a in self.INPUTS:
			self.ADC_VALUES[a]={}
			self.ADC_ACTUALS[a]={}
			for b in range(8):
				self.ADC_VALUES[a][b]=[]
				self.ADC_ACTUALS[a][b]=[]

		self.vv = 0
		self.numpoints=0
		print('started')
		self.timer=QtCore.QTimer()
		self.timer.timeout.connect(self.getAnotherPoint)
		self.timer.start(5)





class AppWindow(QtGui.QMainWindow, calibrator.Ui_MainWindow,utilitiesClass):

	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.INPUTS=['CH1','CH2','CH3']
		self.calibrateOnlyADC = True #DACs will have to calibrated against the ADCs later
		self.type1text = 'PV3->(AN8 or CAP, AIN7), PV2->CH1,2,3,AIN6 , PV1->AIN5'
		self.type2text = 'PV3->(AN8 or CAP, AIN7), PV1->(AIN6, CH1,CH2,CH3), '
		
		self.setType(0)
		self.A = acquirer(self)
		self.INLBox.setCurrentIndex(1)
		self.typeSelectBox.setCurrentIndex(1)
		self.hexid = hex(self.I.device_id())
		self.savedir = os.path.join('.',self.hexid)

		self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8")+' : '+self.hexid)

		for a in range(8):
			item = QtGui.QTableWidgetItem()
			self.valueTable.setItem(0,a,item)
			item.setText('.')

		self.plot=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Read Voltages -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Actual Voltage -->', units='V',**labelStyle)
		#self.plot.setYRange(-.1,.1)
		self.curves={}

		self.curves['INL']=self.addCurve(self.plot,pen=pg.mkPen([255,255,255], width=1),name='INL')
		item = self.addLabel('INL',[255,255,255]);	self.curves['INL'].curve.setClickable(True);	self.curves['INL'].sigClicked.connect(functools.partial(self.selectItem,item))

		self.curves['PV3']=self.addCurve(self.plot,pen=pg.mkPen([255,255,255], width=1),name='PV3')
		item = self.addLabel('PV3',[255,255,255]); self.curves['PV3'].curve.setClickable(True);	self.curves['PV3'].sigClicked.connect(functools.partial(self.selectItem,item))

		
		for a in self.INPUTS:
			self.curves[a]={}
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
					col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
					name = '%s:%dx'%(a,self.I.gain_values[b])
					self.curves[a][b]=self.addCurve(self.plot,pen=pg.mkPen(col, width=1),name=name)
					item = self.addLabel(name,col);	self.curves[a][b].curve.setClickable(True);	self.curves[a][b].sigClicked.connect(functools.partial(self.selectItem,item))
			else:
				col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
				name = '%s:1x'%(a)
				self.curves[a][0]=self.addCurve(self.plot,pen=pg.mkPen(col, width=1),name='%s:1x'%(a))
				item = self.addLabel(name,col);	self.curves[a][0].curve.setClickable(True);	self.curves[a][0].sigClicked.connect(functools.partial(self.selectItem,item))

		self.shortlist=[]
		self.menu_entries=[]
		self.menu_group=None
		self.timer = self.newTimer()
		self.timer.timeout.connect(self.locateDevices)
		self.timer.start(500)

	def setType(self,v):
		if v :
			self.calibrateOnlyADC = False
			self.dirnameLabel.setText(self.type1text)
			self.valueTable.setHorizontalHeaderLabels(['AIN5','PV1','AIN6','PV2','AIN7','PV3','INL'])
		else:
			self.calibrateOnlyADC = True
			self.dirnameLabel.setText(self.type2text)
			self.valueTable.setHorizontalHeaderLabels(['PV1','AIN6','AIN7','PV3','INL','',''])


	def addLabel(self,name,color=None):
		item = QtGui.QListWidgetItem()
		if color:
			brush = QtGui.QBrush(color)
			brush.setStyle(QtCore.Qt.SolidPattern)
			item.setBackground(brush)
			brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
			brush.setStyle(QtCore.Qt.SolidPattern)
			item.setForeground(brush)
		item.setText(name)
		self.listWidget.addItem(item)
		return item

	def selected(self,item):
		c=self.curves.get(str(item),None)
		if c and r:
			for a in self.cleanCurves:
				self.curves[a].curve.opts['shadowPen'] = None
			c.setShadowPen(color=[255,255,255], width=3)
	
	def selectItem(self,item):
		self.listWidget.setCurrentItem(item)


	def selectDir(self):
		self.A.paused = True
		from os.path import expanduser
		dirname = QtGui.QFileDialog.getExistingDirectory(self,  "Select a folder for dumping the calibration data.",  expanduser("./"),  QtGui.QFileDialog.ShowDirsOnly)
		if dirname:
			tmpdir = os.path.join(dirname,self.hexid)
			print(tmpdir)

			try:
				os.mkdir(tmpdir)
				self.dirnameLabel.setText(tmpdir)
				self.savedir = tmpdir
			except:
				print('directory exists. overwrite?')
				reply = QtGui.QMessageBox.question(self, 'Message', 'directory exists. overwrite?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if reply:
					self.dirnameLabel.setText(tmpdir)
					self.savedir = tmpdir



		self.A.paused = False

	def startCalibration(self):
		self.INLBox.setEnabled(False)
		self.typeSelectBox.setEnabled(False)
		self.A.startCalibration()



	def closeEvent(self, event):
		self.running =False
		self.finished=True
		try:self.timer.stop()
		except: pass
		try:self.A.timer.stop()
		except: pass

	def __del__(self):
		self.running =False
		self.finished=True
		try:self.timer.stop()
		except: pass
		try:self.A.timer.stop()
		except: pass

	def saveData(self):
		try:
			os.mkdir(self.savedir)
		except:
			print('directory exists. overwriting')
		print ('saving to ',self.savedir)

		if self.calibrateOnlyADC: # create ideal dataset for PV1, PV2
			np.savetxt(os.path.join(self.savedir,'PV1_ERR.csv'),np.column_stack([np.linspace(-5,5,4096),np.linspace(-5,5,4096) ]))
			np.savetxt(os.path.join(self.savedir,'PV2_ERR.csv'),np.column_stack([np.linspace(-3.3,3.3,4096),np.linspace(-3.3,3.3,4096) ]))
		else:
			np.savetxt(os.path.join(self.savedir,'PV1_ERR.csv'),np.column_stack([self.A.ADC24['AIN5'],self.A.DAC_VALS['PV1'] ]))
			np.savetxt(os.path.join(self.savedir,'PV2_ERR.csv'),np.column_stack([self.A.ADC24['AIN6'],self.A.DAC_VALS['PV2'] ]))

		np.savetxt(os.path.join(self.savedir,'PV3_ERR.csv'),np.column_stack([self.A.ADC24['AIN7'],self.A.DAC_VALS['PV3'] ]))


		np.savetxt(os.path.join(self.savedir,'CALIB_INL.csv'),np.column_stack([self.A.ADC24['AIN7'],self.A.ADCPIC_INL]))
		for a in self.INPUTS:
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
					raw=self.A.ADC_VALUES[a][b]
					np.savetxt(os.path.join(self.savedir,'CALIB_%s_%dx.csv'%(a,self.I.gain_values[b])),np.column_stack([np.array(self.A.ADC24['AIN6'])[self.A.ADC_ACTUALS[a][b]],raw]))
			else:
				np.savetxt(os.path.join(self.savedir,'CALIB_%s_%dx.csv'%(a,1)),np.column_stack([np.array(self.A.ADC24['AIN6'])[self.A.ADC_ACTUALS[a][0]],self.A.ADC_VALUES[a][0]]))

	def locateDevices(self):
		L = serial.tools.list_ports.comports()
		shortlist=[]
		for a in L:
			if ('ACM' in a[1]) and ('04d8:00df' in a[2]) and a[0]!=self.I.H.portname:
				shortlist.append(a)
		total = len(shortlist)
		if shortlist != self.shortlist:
			self.shortlist=shortlist
			for a in self.menu_entries:
				self.deviceBox.removeItem(0)
			self.menu_entries=[]
			for a in shortlist:
				self.deviceBox.addItem(a[0])
				self.menu_entries.append(a[0])


	def setDifferentAD7718(self):
		sel = self.deviceBox.currentText()
		if ( not ('ACM' in sel  or 'USB' in sel)):
			self.displayDialog('No devices Found')
			return
		from PSL import sciencelab
		self.ISPI = sciencelab.connect(port = sel,load_calibration=False)
		self.A.setADC(self.ISPI)
		self.displayDialog('Connected'+self.I.H.version_string.decode("utf-8"))
			
	def setINL_CHANNEL(self,chan):
		chan = str(chan)
		print ('inl changed to ',chan)
		self.A.setINL_CHANNEL(chan)


if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

