#!/usr/bin/python
'''
Stream data acquired from supported I2C sensors.

Currently Supports:\n

refer to SENSORS.supported

'''
from __future__ import print_function

from PSL_Apps.utilitiesClass import utilitiesClass
from templates import ui_hackYourOwn as hackYourOwn


import pyqtgraph as pg
from pyqtgraph.flowchart import Flowchart, Node
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.flowchart.library.common import CtrlNode

import time,random,functools,sys
import numpy as np


from PyQt5 import QtCore, QtGui

params = {
'image' : 'sensors.png',
'name':'Make a\nFlow Chart',
'hint':'''
	Hack your own code by dragging and dropping graphical code blocks for rapid prototyping.<br> severely in beta testing mode.
	'''
}

## At this point, we need some custom Node classes since those provided in the library
## are not sufficient. Each node will define a set of input/output terminals, a 
## processing function, and optionally a control widget (to be displayed in the 
## flowchart control panel)

class PlotViewNode(Node):
	"""Node that displays plot data in an Plotwidget"""
	nodeName = 'PlotView'
	
	def __init__(self, name):
		self.view = None
		## Initialize node with only a single input terminal
		Node.__init__(self, name, terminals={'data': {'io':'in'}})
		
	def setView(self, view):  ## setView must be called by the program
		self.view = view
		
	def process(self, data, display=True):
		## if process is called with display=False, then the flowchart is being operated
		## in batch processing mode, so we should skip displaying to improve performance.
		if display and self.view is not None:
			## the 'data' argument is the value given to the 'data' terminal
			if data is None:
				self.view.setData([])
			else:
				self.view.setData(*data)

class CaptureNode(CtrlNode):
	nodeName = 'Capture'
	uiTemplate = [
		('channel',  'combo', {'values':['CH1','CH2','CH3']}),
        ('samples', 'spin', {'value': 100, 'dec': False, 'step': 10, 'minStep': 1, 'range': [0, 10000]}),
        ('timegap', 'spin', {'value': 1, 'dec': False, 'step': 10, 'minStep': 1, 'range': [0, 100]}),
	]

	def __init__(self, name):
		terminals = {'dataIn': dict(io='in'),'dataOut': dict(io='out')	}                              
		CtrlNode.__init__(self, name, terminals=terminals)

	def setI(self,I):
		self.I = I
		
	def process(self, dataIn, display=False):
		# CtrlNode has created self.ctrls, which is a dict containing {ctrlName: widget}
		output = self.I.capture1(self.ctrls['channel'].currentText(),self.ctrls['samples'].value(),self.ctrls['timegap'].value())
		return {'dataOut': output}




class AppWindow(QtGui.QMainWindow, hackYourOwn.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		self.setWindowTitle('pyqtgraph example: FlowchartCustomNode')

		## Create an empty flowchart with a single input and output
		self.fc = Flowchart(terminals={
			'dataIn': {'io': 'in'},
			
		})
		self.w = self.fc.widget()
		self.WidgetLayout.addWidget(self.fc.widget())

		self.plot1 = self.add2DPlot(self.ExperimentLayout)
		self.plot2 = self.add2DPlot(self.ExperimentLayout)
		self.curve1 = self.addCurve(self.plot1)
		self.curve2 = self.addCurve(self.plot2)
		self.curve1.setData([1,2,3],[5,6,7])

		self.library = fclib.LIBRARY.copy() # start with the default node set
		self.library.addNodeType(PlotViewNode, [('Display',)])
		self.library.addNodeType(CaptureNode, [('Acquire',)])
		self.fc.setLibrary(self.library)


		## Now we will programmatically add nodes to define the function of the flowchart.
		## Normally, the user will do this manually or by loading a pre-generated
		## flowchart file.

		self.cap = self.fc.createNode('Capture', pos=(0, 0))
		self.cap.setI(self.I)

		self.v1Node = self.fc.createNode('PlotView', pos=(0, -150))
		self.v1Node.setView(self.curve1)

		self.v2Node = self.fc.createNode('PlotView', pos=(150, -150))
		self.v2Node.setView(self.curve2)

		self.fc.connectTerminals(self.fc['dataIn'], self.cap['dataIn'])
		self.fc.connectTerminals(self.cap['dataOut'], self.v1Node['data'])
		#self.fc.connectTerminals(self.fc['dataIn'], self.v2Node['data'])

		self.fc.setInput(dataIn=True)


	def run(self):
		self.fc.setInput(dataIn=True)

	def __del__(self):
		#self.looptimer.stop()
		print ('bye')

	def closeEvent(self, event):
		self.finished=True
		
if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
