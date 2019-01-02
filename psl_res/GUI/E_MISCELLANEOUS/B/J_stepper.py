#!/usr/bin/python
'''
Output Peripheral control for the vLabtool - version 0.
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt5 import QtCore, QtGui
import time,sys
from PSL_Apps.templates import ui_stepper as stepper

import sys,os,string
import time
import sys


params = {
'image' : 'servo.jpg',
'name' : 'Stepper\nMotors',
'hint':'''
	Control 4-wire stepper motors via SQR1-4.<br>
	Do not connect high loads to SQR outputs. Use a push pull driver IC such as L293B with an external power supply.
	'''

}

class AppWindow(QtGui.QMainWindow, stepper.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )


	def takeSteps(self):
		steps = self.steps.value()
		if steps>0:
			self.I.stepForward(steps,self.delay.value())
		else:
			self.I.stepBackward(-1*steps,self.delay.value())

	def stepForward(self):
		self.I.stepForward(1,self.delay.value())
	
	def stepBackward(self):
		self.I.stepBackward(1,self.delay.value())

        		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	# Create and display the splash screen
	#splash_pix = QtGui.QPixmap('cat.png')
	#splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
	#progressBar = QtGui.QProgressBar(splash)
	#progressBar.setStyleSheet("""QProgressBar::chunk { width:100%;background: #112255; }""")
	#splash.setMask(splash_pix.mask())
	#splash.show()
	#for i in range(0, 100):
	#	progressBar.setValue(i)
	#	t = time.time()
	#	while time.time() < t + 0.001:
	#		app.processEvents()
	
	myapp = MyMainWindow()
	myapp.show()
	app.processEvents()
	#splash.finish(myapp)
	sys.exit(app.exec_())
