#!/usr/bin/python
'''
Output Peripheral control for PSLab.
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt5 import QtCore, QtGui
import time,sys
from .templates import ui_ipy as ipy

import sys,os,string
import time

params = {
'image' : 'ipython.jpg',
'name' :'IPython Console'
}

class AppWindow(QtGui.QMainWindow, ipy.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle('iPython Console : '+self.I.H.version_string.decode("utf-8"))
		self.msg = QtGui.QLabel()
		self.statusbar.addWidget(self.msg)
		self.msg.setText('Hi!')
		self.timer = QtCore.QTimer()

		self.showSplash();self.updateSplash(10,'Importing iPython Widgets...')
		try:
			from PSL_Apps.iPythonEmbed import QIPythonWidget
			self.updateSplash(10,'Creating Dock Widget...')
		except:
			self.splash.finish(self);
			errbox = QtGui.QMessageBox()
			errbox.setStyleSheet('background:#fff;')
			print (errbox.styleSheet())
			errbox.about(self, "Error", "iPython-qtconsole not found.\n Please Install the module")
			return
			
		self.updateSplash(10,'Embedding IPython Widget...')

		#--------instantiate the iPython class-------
		self.ipyConsole = QIPythonWidget(customBanner="An interactive Python Console!\n");self.updateSplash(10)
		self.layout.addWidget(self.ipyConsole);self.updateSplash(10,'Preparing default command dictionary...')        
		
		from PSL.analyticsClass import analyticsClass
		self.analytics = analyticsClass()
		cmdDict = {"analytics":self.analytics}
		#if self.graphContainer1_enabled:cmdDict["graph"]=self.graph
		if self.I :
			cmdDict["I"]=self.I
			self.ipyConsole.printText("Access hardware using the Instance 'I'.  e.g.  I.get_average_voltage('CH1')")
		self.ipyConsole.pushVariables(cmdDict);self.updateSplash(10,'Winding up...')
		self.console_enabled=True
		self.splash.finish(self);self.updateSplash(10)



	def importNumpy(self):
		self.ipyConsole.executeCommand('import numpy as np',True)
		self.message('imported Numpy as np')

	def importScipy(self):
		self.ipyConsole.executeCommand('import scipy',True)
		self.message('imported scipy')

	def importPylab(self):
		self.msg.setText('importing Pylab...')
		self.ipyConsole.executeCommand('from pylab import *',True)
		self.message('from pylab import * .  You can use plot() and show() commands now.')


	def message(self,txt):
		self.msg.setText(txt)
		self.timer.stop()
		self.timer.singleShot(4000,self.msg.clear)


	def updateSplash(self,x,txt=''):
		self.progressBar.setValue(self.progressBar.value()+x)
		if(len(txt)):self.splashMsg.setText('  '+txt)
		self.splash.repaint()

	def showSplash(self):
		import pkg_resources
		splash_pix = QtGui.QPixmap(pkg_resources.resource_filename('PSL_Apps.stylesheets', "ipy_splash.png"))
		self.splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
		# adding progress bar
		self.progressBar = QtGui.QProgressBar(self.splash)
		self.progressBar.resize(self.splash.width(),20)
		css = pkg_resources.resource_string('PSL_Apps', "stylesheets/splash.css").decode("utf-8")
		if css:
			self.splash.setStyleSheet(css)
		self.splashMsg = QtGui.QLabel(self.splash);self.splashMsg.setStyleSheet("font-weight:bold;color:purple")
		self.splash.setMask(splash_pix.mask())
		self.splashMsg.setText('Loading....');self.splashMsg.resize(self.progressBar.width(),20)
		self.splash.show()
		self.splash.repaint()

	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True

	def __del__(self):
		print ('bye')
        		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
