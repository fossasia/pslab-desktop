#!/usr/bin/python

"""

::

    This experiment is used to study resistance of a body


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
'name':"Human Body's\nResistance",
'hint':'''
	Observe that your skin has non zero electrical resistance. 
	'''
}

class AppWindow(QtGui.QMainWindow, widget_layout.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.resmeter = self.displayIcon(TITLE = "Body's Resistance (PV3 <-> CH3)",UNITS=u"\u03A9",TOOLTIP='Displays the value of a resistor connected between PV3 and CH3\nThe known input impedance (1MOhm) of CH3, and measured voltage is used.')
		self.WidgetLayout.addWidget(self.resmeter)
		self.I.set_pv3(3.0)
		self.running=True
		self.timer=self.newTimer()
		self.timer.timeout.connect(self.run)
		self.timer.start(100)

	def run(self):
		V=self.I.get_average_voltage('CH3',samples=100)
		if V<0:
			self.resmeter.setValue('Disconnected')
			return
		R = 'Voltage(CH3)\t%s\nCurrent Flow\t%s\nResistance\t%s'%(self.applySIPrefix(V,'V'),self.applySIPrefix(V/1e6,'A'),self.applySIPrefix(1e6*(3.0-V)/V,u"\u03A9"))
		self.resmeter.setValue(R)
		

	def closeEvent(self, event):
		pass

	def __del__(self):
		self.timer.stop()
		print('bye')

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

