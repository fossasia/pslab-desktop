#!/usr/bin/python

"""

::

    This experiment is used to study phase shift oscillators


"""

from __future__ import print_function
from PSL_Apps.utilitiesClass import utilitiesClass

from PSL_Apps.templates import ui_widget_layout as widget_layout

import numpy as np
from PyQt5 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'cap.png',
'name':"Capacitance\nMeasurement",
'hint':'''
	Make a parallel plate capacitor and measure it<br>
	Study capacitors in series and parallel. Cross check with theory<br>
	'''
}


class AppWindow(QtGui.QMainWindow, widget_layout.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.capmeter = self.wideButtonIcon(TITLE = 'Capacitance (CAP)',UNITS='F',FUNC=self.I.get_capacitance,TOOLTIP='Displays the value of a capacitor connected between CAP and GND')
		self.WidgetLayout.addWidget(self.capmeter)

	def closeEvent(self, event):
		pass

	def __del__(self):
		pass

if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

