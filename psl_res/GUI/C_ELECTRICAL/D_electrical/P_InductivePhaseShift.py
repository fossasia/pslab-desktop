#!/usr/bin/python

"""

::

    This experiment is used to study inductive reactance XL


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from templates import ui_template_xl as template_xl

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'XLi.png',
'helpfile': 'http://www.electronics-tutorials.ws/inductor/ac-inductors.html',
'name':'LR Phase Shift',
'hint':'''
	Study the phase shift caused by inductors, and also the ratio of input and output amplitudes and their dependence on frequency
	'''
}

class AppWindow(QtGui.QMainWindow, template_xl.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot1=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot1.setLabel('bottom','Time', units='S',**labelStyle)

		self.p2=self.enableRightAxis(self.plot1)

		self.plot1.getAxis('left').setLabel('VL', units='V', color='#ffffff')
		self.plot1.getAxis('right').setLabel('VR', units='V', color='#00ffff')
		self.p1legend = self.plot1.addLegend(offset=(-1,1))

		self.I.set_gain('CH1',3)
		self.I.set_gain('CH2',1)
		self.plot1.setYRange(-8.5,8.5)

		self.p2.setYRange(-8.5,8.5)

		self.curveCH1 = self.addCurve(self.plot1,'VC(CH1-CH2)')
		self.curveCH2 = self.addCurve(self.p2,'VR(CH2)',pen=(0,255,255))
		self.p1legend.addItem(self.curveCH2,'VR(CH2)')

		#setting up plot 2
		self.plot2=self.add2DPlot(self.plot_area)
		self.plot2.getAxis('left').setLabel('VR', units='V', color='#00ffff')
		self.plot2.getAxis('bottom').setLabel('VL', units='V', color='#ffffff')
		self.plot2.setYRange(-8.5,8.5)
		self.plot2.setXRange(-8.5,8.5)
		self.plot2.addLegend()
		self.curveXY = self.addCurve(self.plot2,'Vl vs Vr',pen=[0,255,255])


		from PSL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		self.I.configure_trigger(0,'CH1',0)
		self.tg=2
		self.samples = 2000
		self.max_samples = 2000

		self.prescaler = 0
		self.timer = QtCore.QTimer()

		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		self.fdial = self.addW1(self.I);
		self.WidgetLayout.addWidget(self.fdial)
		self.fdial.dial.setValue(100)

		self.TB = self.addTimebase(self.I,self.set_timebase)
		self.WidgetLayout.addWidget(self.TB)

		self.timer.singleShot(100,self.run)
		self.resultsTable.setRowCount(50)
		self.resultsTable.setColumnCount(4)
		self.resultsTable.setHorizontalHeaderLabels(['F','Vl','Vr','dP = P(Vl)-P(Vr)'])
		self.acquireParams = False
		self.currentRow=0
		self.running=True
		
		self.plotAButton.setText('F vs dP')
		self.plotBButton.setParent(None)
		self.splitter.setSizes([10,1000])

	def savePlot(self):
		self.saveDataWindow([self.curveCH1,self.curveCH2,self.curveXY])

        
	def set_timebase(self,g):
		timebases = [1.5,2,4,8,16,32,128,256,512,1024]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
		self.tg=timebases[g]
		self.samples = int(self.max_samples*samplescaling[g])
		self.autoRange()
		return self.samples*self.tg*1e-6

	def autoRange(self):
		xlen = self.tg*self.samples*1e-6
		chan = self.I.analogInputSources['CH1']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.plot1.setLimits(yMax=max(R),yMin=min(R),xMin=0,xMax=xlen)
		self.plot1.setYRange(min(R),max(R))	
		self.plot1.setXRange(0,xlen)
		self.plot2.setXRange(min(R),max(R))	
		
		chan = self.I.analogInputSources['CH2']
		R = [chan.calPoly10(0),chan.calPoly10(1023)]
		R[0]=R[0]*.9;R[1]=R[1]*.9
		self.p2.setYRange(min(R),max(R))
		self.plot2.setYRange(min(R),max(R))
		return self.samples*self.tg*1e-6


	def fit(self):
		self.acquireParams = True
		
	def run(self):
		if not self.running:return
		if self.I.sine1freq < 150: self.prescaler = 3
		else: self.prescaler = 0
		self.I.configure_trigger(0,'CH1',0,resolution=10,prescaler=self.prescaler)
		self.I.capture_traces(2,self.samples,self.tg)
		if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+50,self.plotData)

	def plotData(self): 
		while(not self.I.oscilloscope_progress()[0]):
			time.sleep(0.1);n=0
			print (self.I.timebase,'correction required',n)
			n+=1
			if n>10:
				if self.running:self.timer.singleShot(100,self.run)
				return
		self.I.__fetch_channel__(1)
		self.I.__fetch_channel__(2)
		T = self.I.achans[0].get_xaxis()*1e-6
		VCH1 = self.I.achans[0].get_yaxis()
		self.I.__autoSelectRange__('CH1',max(abs(VCH1)));
		VCH2 = self.I.achans[1].get_yaxis()
		self.I.__autoSelectRange__('CH2',max(abs(VCH2))); self.autoRange()
		VR = VCH2
		VL = VCH1-VCH2 - (VR*self.resistanceInductor.value()/self.resistance.value())
		self.curveCH1.setData(T,VL,connect='finite')
		self.curveCH2.setData(T,VR,connect='finite')
		self.curveXY.setData(VL,VR,connect='finite')
		if self.acquireParams:
			pars1 = self.CC.sineFit(T,VL)
			pars2 = self.CC.sineFit(T,VR)#,freq=self.frq)
			if pars1 and pars2:
				a1,f1,o1,p1 = pars1
				a2,f2,o2,p2 = pars2
				f1=f1*1e-6
				f2=f2*1e-6
				if (a2 and a1) and (abs(f2-self.I.sine1freq)<10) and (abs(f1-self.I.sine1freq)<10):
					#self.msg.setText("Set F:%.1f\tFitted F:%.1f"%(frq,f1))
					p2=(p2)
					p1=(p1)
					dp=(p2-p1)
					if dp<0:dp+=360
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(self.I.sine1freq));self.resultsTable.setItem(self.currentRow, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1));self.resultsTable.setItem(self.currentRow, 1, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a2));self.resultsTable.setItem(self.currentRow, 2, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(dp));self.resultsTable.setItem(self.currentRow, 3, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					self.currentRow+=1
					print ('F: %.2f,%.2f\tA: %.2f,%.2f\tP: %.1f,%.1f'%(f1,f2,a1,a2,p1,p2))
					print ('Xc*F %.3f'%(f2*a1/a2))
				else:
					self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			else:
				self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			self.acquireParams = False
		if self.running:self.timer.singleShot(100,self.run)
		#print (self.resultsTable.selectedRanges()[0].leftColumn(),self.resultsTable.selectedRanges()[0].rightColumn())


		
	def plotA(self):
		F,XC = self.fetchColumns(self.resultsTable,0,3)
		self.newPlot(F,XC,title = "F vs dP: ",xLabel = 'F',yLabel='dP')

	def plotB(self):
		pass
		#F,XC = self.fetchColumns(self.resultsTable,0,3)
		#self.newPlot(F,1./np.array(XC),title = "F vs 1/XL: ",xLabel = 'F',yLabel='1/XL')        

	def saveFile(self):
		self.saveToCSV(self.resultsTable)

	def setTimebase(self,T):
		self.tgs = [0.5,1,2,4,6,8,10,25,50,100]
		self.tg = self.tgs[T]
		self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')
		
	def closeEvent(self, event):
		self.running=False
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print ('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

