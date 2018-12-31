#!/usr/bin/python

"""

::

    This experiment is used to ...study resistors in parallel and in series


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_widget_layout as widget_layout

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'res.png',
'name':"Resistance\nMeasurement",
'hint':'''
	Study resistors in series and parallel. Cross check with theory<br>
	'''
}


class AppWindow(QtGui.QMainWindow, widget_layout.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.resmeter = self.displayIcon(TITLE = 'Resistance (SEN)',UNITS=u"\u03A9",TOOLTIP='Displays the value of a resistor connected between SEN and GND')
		self.WidgetLayout.addWidget(self.resmeter)

		self.running=True
		self.timer=self.newTimer()
		self.timer.timeout.connect(self.run)
		self.timer.start(100)

	def run(self):
		if not self.running: return
		R = self.I.get_resistance()
		self.resmeter.setValue(R)
		
	def saveData(self):
		pass

		
	def closeEvent(self, event):
		self.running=False
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

