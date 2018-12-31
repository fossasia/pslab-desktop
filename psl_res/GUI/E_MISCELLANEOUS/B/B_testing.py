#!/usr/bin/python

"""

::

	This program loads calibration data from a directory, processes it, and loads it into a connected device
	Not for regular users!
	Maybe dont include this in the main package

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass
from PSL_Apps.utilityApps.templates import ui_testing as testing

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,os,random,struct,time,string

params = {
'image' : '',
'name':'Device\nTesting',
'hint':"A utility to test the device's features.\n These include digital I/O, analog I/O, capacitance measurement, Resistance, W1,W2 and I2C port."

}



class AppWindow(QtGui.QMainWindow, testing.Ui_MainWindow,utilitiesClass):
	RESISTANCE_ERROR = 10
	CAPACITANCE_ERROR = 20e-12 #20pF
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.I.set_wave('W1',1e3) #1KHz test
		self.I.set_wave('W2',1e3) #1KHz test
		cap_and_pcs=self.I.read_bulk_flash(self.I.CAP_AND_PCS,8*4+5)  #READY+calibration_string
		if cap_and_pcs[:5]=='READY':
			self.scalers = list(struct.unpack('8f',cap_and_pcs[5:]))
		else:
			self.displayDialog('Cap and PCS calibration invalid')
			self.scalers = [self.I.SOCKET_CAPACITANCE,1,0,1,1,1,1,1]
		
		
		from PSL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.hexid = hex(self.I.device_id())
		self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8")+' : '+self.hexid)
		for a in range(50):
			for b in range(3):
				item = QtGui.QTableWidgetItem();self.tbl.setItem(a,b,item);	item.setText('')
		self.tests = [
		['I2C scan',[96],self.I2CScan],
		['SQR-ID',1e6,self.SQRID],
		['CAP_SOCK',0,self.CAP_SOCK],
		['PV1-CH1','graph',self.PV1CH1],
		['PV2-CH2','graph',self.PV2CH2],
		['PV3-CH3','graph',self.PV3CH3],
		#group 2 begins
		['SEN',1e3,self.SEN],
		['CAP',329.5e-12,self.CAP],
		['W1-CH1',1e3,self.W1CH1],
		['W2-CH2',1e3,self.W2CH2],
		['PCS-CH3',1e3,self.PCSCH3],
		]
		self.group1size = 6
		self.tbl.setVerticalHeaderLabels([row[0] for row in self.tests])
		self.tbl.setHorizontalHeaderLabels(['Expected','read',''])
		self.tbl.setColumnWidth(0, 80)
		self.tbl.setColumnWidth(1, 150)
		
		#Nominal values for calibration constants
		self.PCS_SLOPE=1
		self.PCS_OFFSET=0
		self.socket_cap = 0
		self.RESISTANCE_SCALING=1
		self.CR0=1;self.CR1=1;self.CR2=1;self.CR3=1
		
		self.G1Tests = {}
		self.G2Tests = {}
		for n in range(len(self.tests)) :
			self.tbl.item(n,0).setText(str(self.tests[n][1]))
			################# make readback buttons ##############
			fn = functools.partial(self.tests[n][2],n)
			if n<self.group1size: self.G1Tests[self.tests[n][0]]=(fn)
			else: self.G2Tests[self.tests[n][0]]=(fn)
			item = QtGui.QPushButton();item.setText('test'); item.clicked.connect(fn)
			self.tbl.setCellWidget(n, 2, item)



		self.DACPLOT = self.add2DPlot(self.plot_area)
		self.WPLOT = self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.DACPLOT.setLabel('left','Error -->', units='V',**labelStyle)
		self.DACPLOT.setLabel('bottom','Actual Voltage -->', units='V',**labelStyle)
		self.DACPLOT.setYRange(-.02,.02)
		self.WPLOT.setLabel('left','Voltage -->', units='V',**labelStyle)
		self.WPLOT.setLabel('bottom','time -->', units='V',**labelStyle)
		self.WPLOT.setYRange(-3.3,3.3)
		self.DacCurves={}
		self.rebuildLegend(self.DACPLOT)
		for a in self.I.DAC.CHANS:
			self.DacCurves[a] = self.addCurve(self.DACPLOT,a)

		self.WCurves={}
		self.rebuildLegend(self.WPLOT)
		for a in ['W1','W2']:
			self.WCurves[a] = self.addCurve(self.WPLOT,a)



	def setSuccess(self,item,val):
		if val : item.setBackground(QtCore.Qt.green);
		else:item.setBackground(QtCore.Qt.red);

	def I2CScan(self,row):
		res = self.I.I2C.scan()
		item = self.tbl.item(row,1)
		item.setText(str(res))
		if 96 in res : self.setSuccess(item,1) #DAC found
		else :
			self.setSuccess(item,0) #dac not detected
			item.setText('DAC missing')

	def SQRID(self,row):
		self.I.map_reference_clock(7,'SQR1','SQR2','SQR3','SQR4')
		res = [self.I.get_freq(a) for a in ['ID1','ID2','ID3','ID4','CNTR'] ]
		self.I.set_state(SQR1=0,SQR2=0,SQR3=0,SQR4=0)	
		item = self.tbl.item(row,1)
		try:
			avg = np.average(res)
			item.setText('%.3e'%avg)
			if abs(avg-float(self.tbl.item(row,0).text() ))<20:	 self.setSuccess(item,1)
			else:	 self.setSuccess(item,1)				
		except Exception as e:
			print (e)
			item.setText('failed'); self.setSuccess(item,0)
		self.I.set_waves(1e3,0) #1KHz test

	def eval1(self):
		for a in self.G1Tests: self.G1Tests[a]()

	def eval2(self):
		for a in self.G2Tests: self.G2Tests[a]()

	def SEN(self,row):
		res = self.I.get_resistance()
		item = self.tbl.item(row,1)
		if res!=np.inf:
			item.setText(self.applySIPrefix(res, "\u03A9"))
			actual = float(self.tbl.item(row,0).text() )
			if abs(res-actual)<self.RESISTANCE_ERROR :
				self.setSuccess(item,1) #resistance within error margins
				self.RESISTANCE_SCALING = actual/res
			else :
				self.setSuccess(item,0) 
		else:
			item.setText('Open')
			self.setSuccess(item,0) 

	def CAP_SOCK(self,row):
		cap = self.I.get_capacitance()
		item = self.tbl.item(row,1)
		item.setText(self.applySIPrefix(cap,'F'))
		if abs(cap-float(self.tbl.item(row,0).text() ))<self.CAPACITANCE_ERROR :
			self.setSuccess(item,1) #capacitance within error margins
			self.socket_cap = cap
		else :	self.setSuccess(item,0) 

	def CAP(self,row):
		res = self.I.get_capacitance()
		print (res)
		item = self.tbl.item(row,1)
		item.setText(self.applySIPrefix(res,'F'))
		if abs(res-float(self.tbl.item(row,0).text() ))<self.CAPACITANCE_ERROR : self.setSuccess(item,1) #capacitance within error margins
		else :	self.setSuccess(item,0) 

	def __PVCH__(self,DAC,ADC,row,rng):
		actuals=[];read=[]
		for a in np.linspace(*rng):
			actuals.append( self.I.DAC.setVoltage(DAC,a) )
			time.sleep(0.001)
			read.append (self.I.get_voltage(ADC,samples=5) )
		read = np.array(read)
		actuals = np.array(actuals)
		self.DacCurves[DAC].setData(actuals,read-actuals)
		self.tbl.item(row,0).setText(string.join(['%.3f'%a for a in actuals],' '))
		self.tbl.item(row,1).setText(string.join(['%.3f'%a for a in read-actuals],' '))
		if np.any(abs(read-actuals)>10e-3):self.setSuccess(self.tbl.item(row,1),0)
		else: self.setSuccess(self.tbl.item(row,1),1)
		
	def PV1CH1(self,row):
		self.__PVCH__('PV1','CH1',row,[-4,4,10])
	def PV2CH2(self,row):
		self.__PVCH__('PV2','CH2',row,[-2.5,2.5,10])
	def PV3CH3(self,row):
		self.__PVCH__('PV3','CH3',row,[0.2,2.8,10])

	def PCSCH3(self,row):
		actuals=[];read=[]
		resistance = float(self.tbl.item(row,0).text())
		for a in np.linspace(.2e-3,1.5e-3,20):
			actuals.append( self.I.DAC.setCurrent(a) )
			time.sleep(0.001)
			read.append (self.I.get_voltage('CH3',samples=5))
		read = np.array(read)/resistance 
		actuals = np.array(actuals)
		sread = read*1e3
		sactuals = actuals*1e3
		self.DacCurves['PCS'].setData(sactuals,sread-sactuals)
		self.tbl.item(row,1).setText(string.join(['%.3f'%a for a in sread-sactuals],' '))
		if np.any(abs(read-actuals)>10e-6):self.setSuccess(self.tbl.item(row,1),0)
		else: self.setSuccess(self.tbl.item(row,1),1)

		fitvals = np.polyfit(self.I.DAC.CHANS['PCS'].VToCode(read),self.I.DAC.CHANS['PCS'].VToCode(actuals),1)
		print (fitvals)
		if list(fitvals):
			self.PCS_SLOPE = fitvals[0] #slope
			self.PCS_OFFSET = fitvals[1]	#offset

	def __WCH__(self,WG,ADC,row):
		self.I.set_wave(WG,1e3) #1KHz test
		self.I.select_range(ADC,4)
		x,y = self.I.capture1(ADC,1000,5)#get about five cycles
		self.WCurves[WG].setData(x,y)
		self.tbl.item(row,0).setText('1 KHz')
		try:
			amp,frq,ph,off = self.math.sineFit(x,y)
			self.tbl.item(row,1).setText(self.applySIPrefix(frq,'Hz')+','+self.applySIPrefix(amp,'V'))
			if abs(frq-1e3)>2:self.setSuccess(self.tbl.item(row,1),0)
			else: self.setSuccess(self.tbl.item(row,1),1)
		except:
			self.tbl.item(row,1).setText('Check Connections')
			self.setSuccess(self.tbl.item(row,1),0)
	def W1CH1(self,row):
		self.__WCH__('W1','CH1',row)
	def W2CH2(self,row):
		self.__WCH__('W2','CH2',row)


	def correct(self):
		self.scalers[0] += self.socket_cap
		self.scalers[1] = self.scalers[1]*self.PCS_SLOPE  #slope
		self.scalers[2] = self.scalers[2]*self.PCS_SLOPE+self.PCS_OFFSET  #offset
		self.scalers[3] = self.scalers[3]*self.RESISTANCE_SCALING
		self.scalers[4]*=self.CR0;self.scalers[5]*=self.CR1;self.scalers[6]*=self.CR2;self.scalers[7]*=self.CR3;
		
		self.displayDialog('loading %s\n%s\n%s'%(self.scalers,self.PCS_SLOPE,self.PCS_OFFSET))
		cap_and_pcs=self.I.write_bulk_flash(self.I.CAP_AND_PCS,self.I.__stoa__('READY'+struct.pack('8f',*self.scalers)))  #READY+calibration_string
		self.I.SOCKET_CAPACITANCE = self.scalers[0]
		self.I.__calibrate_ctmu__(self.scalers[3:])
		self.I.DAC.CHANS['PCS'].load_calibration_twopoint(self.scalers[1],self.scalers[2]) #Slope and offset for current source
		self.I.resistanceScaling = self.scalers[3]
		self.G2Tests['SEN']()
		self.G2Tests['PCS-CH3']()


	def __del__(self):
		print ('bye')
	def closeEvent(self,e):
		self.save()

	def save(self):
		p = QtGui.QPixmap.grabWindow(self.tab1.winId())
		from os.path import expanduser
		home = expanduser("~")
		path = os.path.join(home,'test '+self.I.hexid+'.png')
		p.save(path)		
		self.displayDialog('saved to '+path)


if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect(verbose=True))
    myapp.show()
    sys.exit(app.exec_())

