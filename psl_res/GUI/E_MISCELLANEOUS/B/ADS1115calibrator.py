#!/usr/bin/python

#from __future__ import print_function
'''
Description

The ADS1115 is a 16-bit, 4-channel ADC, and will be used to calibrate the device

The priamry objective is to reduce the time taken to calibrate and test each PSLab device.

Features :
- The Analog outputs (PV1...PV3) will be configured to output a set of voltage values that are simultaneously monitored
  by the Analog inputs(CH1.. CH3) and 2 degree fitting polynomial coefficients will be extracted and stored in flash memory .
- A unique timestamp in human readable format will be stored along with the calibration data, and raw data will be locally
  stored in a folder with the same name as the timestamp
- All floating points are converted to strings using the struct module . e.g. struct.pack('3f',*fitvals) , where fitvals = [f1,f2,f3]


'''


import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

import templates.ui_ADS1115calibrator as ADS1115calibrator

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,random,struct,time


params = {
'image' : 'calib.png',
'name':'ADS1115 based\nCalibrator',
'hint':'''Calibrate your device using a plugged in ADS1115 16-bit ADC and save values to a directory. Use the calibration loader utility to process the results and write to flash. Not for beginners!
'''
}


def addCurve(plot,**kwargs):
	C=pg.PlotCurveItem(**kwargs)
	plot.addItem(C)
	return C

def stoa(s):
	return [ord(a) for a in s]
def atos(a):
	return ''.join(chr(e) for e in a)



class acquirer():
	def __init__(self,parent):
		self.I=parent.I
		self.CHANA=0
		self.CHANB=1
		self.parent = parent
		self.INPUTS = parent.INPUTS
		self.paused = False
		if self.I and len(sys.argv)==1: self.I.__ignoreCalibration__()  #provide any argument to skip calibration erase
		self.DAC_CHAN = None
		self.SECOND_DAC = None

		self.DAC_VALS = []
		self.DAC_VALS2 = []
		self.ADC_DIRECT=[]
		self.ADC_DIRECT2=[]

		self.ADC_VALUES={}
		self.ADC_ACTUALS={}
		for a in self.INPUTS:
			self.ADC_VALUES[a]={}
			self.ADC_ACTUALS[a]={}
			for b in range(8):
				self.ADC_VALUES[a][b]=[]
				self.ADC_ACTUALS[a][b]=[]

		self.Running = False
	def setADC(self,adc):
		self.ADC = adc
		self.ADC.setGain('GAIN_ONE') #unity gain
		self.ADC.setChannel('UNI_0') #single ended 0
		self.ADC.setDataRate(32)
	def setDAC(self,dac,dac2=None):
		self.DAC_CHAN = dac
		self.SECOND_DAC = dac2
	def getAnotherPoint(self):
		if self.vv>=3.2: #We're all done here.
			self.Running = False
			self.timer.stop()
			self.parent.progressBar.setValue(100)
			self.parent.setWindowTitle(" We're all finished here")
			self.parent.askBeforeQuit()
			return
		if(self.paused):return

		#STEP 1 : Set the DAC output , and save the expected value.
		dacval = self.I.DAC.setVoltage(self.DAC_CHAN,self.vv)
		self.DAC_VALS.append(dacval)
		if self.SECOND_DAC:
			val2 = self.I.DAC.setVoltage(self.SECOND_DAC,self.vv)
			self.DAC_VALS2.append(val2)
		time.sleep(0.01)

		ADC_ACTUAL = self.ADC.readADC_SingleEnded(self.CHANA)*1e-3 #convert to volts
		self.ADC_DIRECT.append(ADC_ACTUAL)

		self.ADC_DIRECT2.append(self.ADC.readADC_SingleEnded(self.CHANB)*1e-3) #for second DAC channel

		#step 3 : readd all ADC inputs : CH1,CH2 (all gain settings) ,CH3 , and save them
		for a in self.INPUTS:
			if self.I.analogInputSources[a].gainEnabled:
				averages = 10
				for b in range(8):
					if b==7:averages = 50
					self.I.set_gain(a,b)
					rawval = self.I.__get_raw_average_voltage__(a)
					#if self.I.analogInputSources[a].__conservativeInRange__(ADC_ACTUAL):
					if self.I.analogInputSources[a].__conservativeInRangeRaw__(rawval,100):
						v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(averages) ]))
						self.ADC_VALUES[a][b].append(v)
						self.ADC_ACTUALS[a][b].append(ADC_ACTUAL)
			else:
				if self.I.analogInputSources[a].__conservativeInRange__(ADC_ACTUAL):
					v=self.I.analogInputSources[a].calPoly12(np.average([self.I.__get_raw_average_voltage__(a) for x in range(10) ]))
					self.ADC_VALUES[a][0].append(v)
					self.ADC_ACTUALS[a][0].append(ADC_ACTUAL)

		#DAC, CAP , CH1, CH2, CH3
		try:
			self.parent.valueTable.item(0,0).setText('%.3f'%self.DAC_VALS[-1])
			self.parent.valueTable.item(0,1).setText('%.3f'%self.ADC_DIRECT[-1])
			self.parent.valueTable.item(0,2).setText('%.3f'%self.ADC_VALUES['CH1'][0][-1])
			self.parent.valueTable.item(0,3).setText('%.3f'%self.ADC_VALUES['CH2'][0][-1])
			self.parent.valueTable.item(0,4).setText('%.3f'%self.ADC_VALUES['CH3'][0][-1])

		except Exception as e:
			print (e)
		self.numpoints+=1
		#########################----UPDATE PLOTS AND TABLE----######################
		self.parent.curves['DAC'].setData(self.ADC_DIRECT,np.array(self.DAC_VALS)-np.array(self.ADC_DIRECT))
		self.parent.curves['DAC2'].setData(self.ADC_DIRECT2,np.array(self.DAC_VALS2)-np.array(self.ADC_DIRECT2))

		for a in self.INPUTS:
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
						X = np.array(self.ADC_ACTUALS[a][b])
						if len(X)>3:
							Y = np.array(self.ADC_VALUES[a][b])
							self.parent.curves[a][b].setData(X,Y-X)
			else:
						X = np.array(self.ADC_ACTUALS[a][0])
						if len(X)>3:
							Y = np.array(self.ADC_VALUES[a][0])
							self.parent.curves[a][0].setData(X,Y-X)

		#-------------------------------------------------------
		self.parent.progressBar.setValue(self.vv*100/3.3)
		self.vv += self.dv
		self.dv+=0.005
		return True

	def startCalibration(self):
		self.Running = True
		self.vv = 0.1
		self.dv = 0.005
		self.I.DAC.setVoltage(self.DAC_CHAN,self.vv)
		time.sleep(0.5)
		self.DAC_VALS=[]
		self.DAC_VALS2=[]
		self.ADC_DIRECT = []
		self.ADC_DIRECT2 = []

		self.ADC_VALUES={}
		self.ADC_ACTUALS={}
		for a in self.INPUTS:
			self.ADC_VALUES[a]={}
			self.ADC_ACTUALS[a]={}
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
					self.ADC_VALUES[a][b]=[]
					self.ADC_ACTUALS[a][b]=[]
			else:
					self.ADC_VALUES[a][0]=[]
					self.ADC_ACTUALS[a][0]=[]

		self.numpoints=0
		print('started')
		self.timer=QtCore.QTimer()
		self.timer.timeout.connect(self.getAnotherPoint)
		self.timer.start(20)





class AppWindow(QtGui.QMainWindow, ADS1115calibrator.Ui_MainWindow):

	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.INPUTS=['CH1','CH2','CH3','CAP']
		self.calibrateOnlyADC = True #DACs will have to calibrated against the ADCs later
		self.type1text = 'invalid'
		self.type2text = 'PV1->(CH1,CH2,CH3, CAP)'
		self.timers=[]
		self.setType(0)
		self.A = acquirer(self)
		from PSL.SENSORS import ADS1115
		self.A.setADC(ADS1115.connect(self.I.I2C))
		self.DAC_CHAN = 'PV1';self.DAC_CHAN2 = 'PV2';
		self.A.setDAC(self.DAC_CHAN,'PV2')
		self.I.DAC.setVoltage(self.DAC_CHAN,0) #0+

		self.savedir = os.path.join('.',time.ctime())

		self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8")+' : '+time.ctime())

		for a in range(8):
			item = QtGui.QTableWidgetItem()
			self.valueTable.setItem(0,a,item)
			item.setText('.')

		self.plot=pg.PlotWidget()
		self.plot_area.addWidget(self.plot)

		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot.setLabel('left','Read Voltages -->', units='V',**labelStyle)
		self.plot.setLabel('bottom','Actual Voltage -->', units='V',**labelStyle)
		#self.plot.setYRange(-.1,.1)
		self.curves={}

		self.curves['DAC']=pg.PlotCurveItem(pen=pg.mkPen([255,255,255], width=2),name='DAC')
		self.plot.addItem(self.curves['DAC'])

		#item = self.addLabel('DAC',[255,255,255]); self.curves['DAC'].setClickable(True);	self.curves['DAC'].sigClicked.connect(functools.partial(self.selectItem,item))

		self.curves['DAC2']=pg.PlotCurveItem(pen=pg.mkPen([255,0,255], width=2),name='DAC2')
		self.plot.addItem(self.curves['DAC2'])
		#item = self.addLabel('DAC2',[255,255,255]); self.curves['DAC2'].setClickable(True);	self.curves['DAC2'].sigClicked.connect(functools.partial(self.selectItem,item))
		for a in self.INPUTS:
			self.curves[a]={}
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
					col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
					name = '%s:%dx'%(a,self.I.gain_values[b])
					self.curves[a][b]=addCurve(self.plot,pen=pg.mkPen(col, width=1),name=name)
					item = self.addLabel(name,col);	self.curves[a][b].setClickable(True);	self.curves[a][b].sigClicked.connect(functools.partial(self.selectItem,item))
			else:
				col=QtGui.QColor(random.randint(20,255),random.randint(20,255),random.randint(20,255))
				name = '%s:1x'%(a)
				self.curves[a][0]=addCurve(self.plot,pen=pg.mkPen(col, width=1),name='%s:1x'%(a))
				item = self.addLabel(name,col);	self.curves[a][0].setClickable(True);	self.curves[a][0].sigClicked.connect(functools.partial(self.selectItem,item))

		self.shortlist=[]
		self.menu_entries=[]
		self.menu_group=None
		self.A.startCalibration()

	def newTimer(self):
		"""
		Create a QtCore.QTimer object and return it.
		A reference is also stored in order to keep track of it
		"""

		timer = QtCore.QTimer()
		self.timers.append(timer)
		return timer

		
	def setType(self,v):
		print ('only option is to calibrate only ADCs. TODO')
		self.calibrateOnlyADC = True
		self.dirnameLabel.setText(self.type2text)
		self.valueTable.setHorizontalHeaderLabels(['DAC', 'CAP' , 'CH1', 'CH2', 'CH3'])

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
			tmpdir = os.path.join(dirname,time.ctime)
			print(tmpdir)

			try:
				os.mkdir(tmpdir)
				self.dirnameLabel.setText(tmpdir)
				self.savedir = tmpdir
			except Exception as e:
				print('directory exists. overwrite?',e.message)
				reply = QtGui.QMessageBox.question(self, 'Message', 'directory exists. overwrite?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if reply:
					self.dirnameLabel.setText(tmpdir)
					self.savedir = tmpdir



		self.A.paused = False

	def startCalibration(self):
		self.A.startCalibration()

	def closeEvent(self, evnt):
		evnt.ignore()
		try:self.timer.stop()
		except Exception as e: print (e)
		try:self.A.timer.stop()
		except Exception as e: print (e)
		self.askBeforeQuit()
	
	def askBeforeQuit(self):
		global app
		reply = QtGui.QMessageBox.question(self, 'Warning', 'save and quit?', QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			self.running =False
			self.finished=True
			self.upload()
			self.saveData()
			app.quit()
		else:
			self.running =False
			self.finished=True
			print ('Did not save/upload calibration')
			app.quit()



	def __del__(self):
		self.running =False
		self.finished=True
		try:self.timer.stop()
		except Exception as e: print(e)
		try:self.A.timer.stop()
		except Exception as e: print (e)


	def saveData(self):
		try:
			os.mkdir(self.savedir)
		except Exception as e:
			print('directory exists. overwriting',e.message)
		print ('saving to ',self.savedir)

		DY = self.A.DAC_VALS
		DX = self.A.ADC_DIRECT
		np.savetxt(os.path.join(self.savedir,'%s_ERR.csv'%self.DAC_CHAN),np.column_stack([DX,DY ]))
		if self.A.SECOND_DAC:
			DY2 = self.A.DAC_VALS2
			DX2 = self.A.ADC_DIRECT2
			np.savetxt(os.path.join(self.savedir,'%s_ERR.csv'%self.DAC_CHAN2),np.column_stack([DX2,DY2 ]))

		for a in self.INPUTS:
			if self.I.analogInputSources[a].gainEnabled:
				for b in range(8):
					measured=self.A.ADC_VALUES[a][b]
					actual = self.A.ADC_ACTUALS[a][b]
					np.savetxt(os.path.join(self.savedir,'CALIB_%s_%dx.csv'%(a,self.I.gain_values[b])),np.column_stack([actual,measured]))
			else:
				measured=self.A.ADC_VALUES[a][0]
				actual = self.A.ADC_ACTUALS[a][0]
				np.savetxt(os.path.join(self.savedir,'CALIB_%s_%dx.csv'%(a,1)),np.column_stack([actual,measured]))

		
	def upload(self):
		final_fitstr=stoa('PSLab SLOPES and OFFSETS``%s\n'%(time.ctime()))
		for a in self.A.ADC_VALUES:
			keys=np.sort(self.A.ADC_VALUES[a].keys())
			final_fitstr+=stoa('>|'+a+'|<')
			print (keys,self.A.ADC_ACTUALS[a])
			source = self.I.analogInputSources[a]
			for b in keys:
				source.__setGain__(int(b)) #b=gain [0-7]
				fitvals = np.polyfit(  source.voltToCode12(self.A.ADC_VALUES[a][b][1:]),self.A.ADC_ACTUALS[a][b][1:],2) #measured, actual, 2 degree.
				fitstr=struct.pack('3f',*fitvals)
				print (a,b,self.A.ADC_VALUES[a][b],len(fitstr),fitstr)
				final_fitstr+=stoa(fitstr)

		final_fitstr+=stoa('STOP')

		#DAC CALIBRATION
		final_fitstr+=stoa('>|%s|<'%self.DAC_CHAN) #len(DAC_CHAN)==3 . mandatory
		VToCode = self.I.DAC.CHANS[self.DAC_CHAN].VToCode
		fitvals = np.polyfit(VToCode(np.array(self.A.ADC_DIRECT)),VToCode(np.array(self.A.DAC_VALS)),2 )
		fitstr = struct.pack('3f',*fitvals)
		final_fitstr+=stoa(fitstr)

		if self.A.SECOND_DAC:
			final_fitstr+=stoa('>|%s|<'%self.DAC_CHAN2) #len(DAC_CHAN)==3 . mandatory
			VToCode = self.I.DAC.CHANS[self.DAC_CHAN2].VToCode
			fitvals = np.polyfit(VToCode(np.array(self.A.ADC_DIRECT2)),VToCode(np.array(self.A.DAC_VALS2)),2 )
			fitstr = struct.pack('3f',*fitvals)
			final_fitstr+=stoa(fitstr)


		final_fitstr+=stoa('STOP')

		print('Writing adc slopes and offsets to Flash.....'+str(len(final_fitstr)))
		print (final_fitstr)
		self.I.write_bulk_flash(self.I.ADC_POLYNOMIALS_LOCATION,final_fitstr)



if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)

    app.setStyleSheet(" *{outline:none;} QMainWindow{background:#aabbcc;} QTabWidget#tabwidget{margin:0px; padding:0px; border:none;} QTabBar{font:20px;} QTabBar::tab{background: #3F51B5; padding:15px 50px; color:#C5CAE9;} QTabBar::tab:selected,QTabBar::tab:hover{color:white; background:#303F9F} QWidget#cont1{background:#E0E0E0; max-width:250px;}  QLabel{color:#424242; margin:10px 0px;} QLabel#intvalue,QLabel#smoothvalue{border:1px dotted #424242; padding: 8px;} QLabel#intvalue{min-width: 70px;} QLabel#smoothvalue{max-width: 70px;} .CustomSlider{outline:none; border:none;}  QSlider::groove:horizontal {margin:0px; padding:0px; border:none; background:#3F51B5; color:#FF4081; height: 3px;} QSlider::handle:horizontal {width:18px; height:18px; border-image:url(handle.png) 0 0 0 0 stretch stretch; border-width:0px; margin:-7px 0px;} QComboBox#plottype::drop-down{min-width:35px; background:#E0E0E0; border-left:1px;border-style: solid;} QComboBox#plottype::drop-down:hover{background:#3F51B5;} QComboBox#plottype::down-arrow{border-image:url(downarrow.png) 0 0 0 0 stretch stretch;margin:-3px;border:0px;} QComboBox#plottype:!editable {background:#E0E0E0; border:1px solid #424242;} QComboBox#plottype:!editable{background:#3F51B5; border-color:#303F9F;color:white; padding-left:5px;} QComboBox#plottype QAbstractItemView {background:#E0E0E0; border:1px solid #9E9E9E} QAbstractItemView::item {min-height: 35px;} QComboBox#plottype QListView::item:selected { color:white; background-color: #3F51B5;}  QPushButton:hover{background:#BDBDBD;} QToolTip{background:#FBE9E7;color:#757575; padding:4px; border:0px; margin:0px;} QPushButton{min-height: 24px;min-width:30px; border:1px solid #424242; padding:3px;color:#424242; background:#998897;}  ")

    myapp = AppWindow(I=sciencelab.connect(verbose = True))
    myapp.show()
    sys.exit(app.exec_())

