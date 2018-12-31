#!/usr/bin/python

"""

::

    This experiment is used to study Half wave rectifiers

"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from .templates import ui_template_xl as template_xl

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'LCRsteady.png',
'helpfile': 'http://www.electronics-tutorials.ws/capacitor/cap_8.html',
'name':'LCR Steady State',
'hint':'''
	Study the phase shifts in an LCR circuit, and also note that the sum of VL and VC goes to zero at resonance.
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
		self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)
		self.p1legend = self.plot1.addLegend(offset=(-1,1))
		self.p2=self.enableRightAxis(self.plot1)

		self.plot1.getAxis('left').setLabel('Vc -->>', color='#ffffff')
		self.plot1.getAxis('right').setLabel('I -->>', units='A', color='#00ffff')

		self.I.set_gain('CH1',1)
		self.I.set_gain('CH2',1)
		self.plot1.setYRange(-8.5,8.5)
		self.p2.setYRange(-3.3/self.resistance.value(),3.3/self.resistance.value())


		from PSL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		self.I.configure_trigger(0,'CH1',0)
		self.tg=20
		self.samples = 2000
		self.max_samples = 2000
		self.prescaler = 0
		self.timer = QtCore.QTimer()

		self.curveVL = self.addCurve(self.plot1,'VL(CH1-CH2)')
		self.curveVC = self.addCurve(self.plot1,'VC(CH2-CH3)')
		self.curveVLC = self.addCurve(self.plot1,'VLC(VL + VC)')
		self.curveVR = self.addCurve(self.plot1,'VR(CH3)')
		self.curveI = self.addCurve(self.p2,'Current')
		self.p1legend.addItem(self.curveI,'current')


		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		self.fdial = self.addW1(self.I);
		self.WidgetLayout.addWidget(self.fdial)
		self.fdial.dial.setValue(100)

		self.WidgetLayout.addWidget(self.addTimebase(self.I,self.set_timebase))


		self.timer.singleShot(100,self.run)
		self.resultsTable.setRowCount(50)
		self.resultsTable.setColumnCount(4)
		self.resultsTable.setHorizontalHeaderLabels(['F','Vc','I (mA)','Xc = Vc/I'])
		self.acquireParams = False
		self.currentRow=0
		self.running=True
		
		self.plotAButton.setText('F vs Xc')
		self.plotBButton.setText('F vs 1/Xc')
		self.splitter.setSizes([10,1000])

	def set_timebase(self,g):
		timebases = [1.5,2,4,8,16,32,128,256,512,1024]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
		self.tg=timebases[g]
		self.samples = int(self.max_samples*samplescaling[g])
		self.plot1.setXRange(0,self.samples*self.tg*1e-6)
		self.plot1.setLimits(yMax=8,yMin=-8,xMin=0,xMax=self.samples*self.tg*1e-6)
		self.p2.setLimits(yMax=8/self.resistance.value(),yMin=-8/self.resistance.value(),xMin=0,xMax=self.samples*self.tg*1e-6)
		return self.samples*self.tg*1e-6


	def fit(self):
		print ("Adding...")
		self.acquireParams = True
		
	def run(self):
		if not self.running:return
		if self.I.sine1freq < 150: self.prescaler = 3
		else: self.prescaler = 0
		self.I.configure_trigger(0,'CH1',0,resolution=10,prescaler=self.prescaler)
		self.I.capture_traces(3,self.samples,self.tg)
		if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+50,self.plotData)

	def plotData(self): 
		while(not self.I.oscilloscope_progress()[0]):
			time.sleep(0.1);n=0
			print (self.I.timebase,'correction required',n)
			n+=1
			if n>10:
				self.timer.singleShot(100,self.run)
				return
		self.I.__fetch_channel__(1)
		self.I.__fetch_channel__(2)
		self.I.__fetch_channel__(3)
		T = self.I.achans[0].get_xaxis()*1e-6
		VCH1 = self.I.achans[0].get_yaxis()
		VCH2 = self.I.achans[1].get_yaxis()
		VCH3 = self.I.achans[2].get_yaxis()
		I = VCH3/self.resistance.value()   
		VR = VCH3
		VL = VCH1-VCH2 - (VR*self.resistanceInductor.value()/self.resistance.value())
		VC = VCH2-VCH3
		self.curveVL.setData(T,VL,connect='finite')
		self.curveVC.setData(T,VC,connect='finite')
		self.curveVR.setData(T,VR,connect='finite')
		self.curveVLC.setData(T,VL+VC,connect='finite')

		self.curveI.setData(T,I,connect='finite')
		if self.acquireParams:
			pars1 = self.CC.sineFit(T,VC)
			pars2 = self.CC.sineFit(T,I)#,freq=self.frq)
			if pars1 and pars2:
				a1,f1,o1,p1 = pars1
				a2,f2,o2,p2 = pars2
				f1=f1*1e-6
				f2=f2*1e-6
				if (a2 and a1) and (abs(f2-self.I.sine1freq)<10) and (abs(f1-self.I.sine1freq)<10):
					#self.msg.setText("Set F:%.1f\tFitted F:%.1f"%(frq,f1))
					p2=(p2)
					p1=(p1)
					dp=(p2-p1)-360
					if dp<-360:dp+=360
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(self.I.sine1freq));self.resultsTable.setItem(self.currentRow, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1));self.resultsTable.setItem(self.currentRow, 1, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a2*1e3));self.resultsTable.setItem(self.currentRow, 2, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1/a2));self.resultsTable.setItem(self.currentRow, 3, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					self.currentRow+=1
					print ('F: %.2f,%.2f\tA: %.2f,%.2f\tP: %.1f,%.1f'%(f1,f2,a1,a2,p1,p2))
					print ('Xc*F %.3f'%(f2*a1/a2))
				else:
					self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			else:
				self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			self.acquireParams = False
		if self.running:self.timer.singleShot(100,self.run)

	   
	def plotA(self):
		F,XC = self.fetchColumns(self.resultsTable,0,3)
		self.newPlot(F,XC,title = "F vs XC: ",xLabel = 'F',yLabel='XC')

	def plotB(self):
		F,XC = self.fetchColumns(self.resultsTable,0,3)
		self.newPlot(F,1./np.array(XC),title = "F vs 1/XC: ",xLabel = 'F',yLabel='1/XC')        

	def saveFile(self):
		self.saveToCSV(self.resultsTable)

	def savePlot(self):
		self.saveDataWindow([self.curveVL,self.curveVC,self.curveVLC,self.curveVR])


	def setTimebase(self,T):
		self.tgs = [0.5,1,2,4,6,8,10,25,50,100]
		self.tg = self.tgs[T]
		self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')
		
	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True
		self.running = False
		

	def __del__(self):
		self.timer.stop()
		print ('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

