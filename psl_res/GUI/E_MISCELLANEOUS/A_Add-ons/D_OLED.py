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
'image' : 'oled.png',
'name':"OLED\nDISPLAY",
'hint':'''
	Load An image onto an SSD1306 128*64 OLED display connected to the I2C port<br>
	'''
}


class AppWindow(QtGui.QMainWindow, widget_layout.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.SENSORS import SSD1306
		self.OLED = SSD1306.SSD1306(self.I.I2C)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		
		from PIL import Image
		
		self.IMAGE = Image
		self.img=None;self.bw=None
		
		self.WidgetLayout.addWidget(self.simpleButtonIcon(TITLE = 'Clear OLED',FUNC=self.clear,TOOLTIP='Clear the display'))
		self.WidgetLayout.addWidget(self.simpleButtonIcon(TITLE = 'Test OLED',FUNC=self.test,TOOLTIP='Load the CSpark Logo'))

		self.selectfile = self.simpleButtonIcon(TITLE = 'Open File',FUNC=self.open_file,TOOLTIP='Open an image file')
		self.WidgetLayout.addWidget(self.selectfile)

		self.imgFrame = self.addHelpImageToLayout(self.WidgetLayout,'')
		self.WidgetLayout.addWidget(self.dialIcon(TITLE = 'Threshold',FUNC=self.setThreshold,MIN=1,MAX=254,TOOLTIP='Set the threshold for making a monochrome image'))
		self.WidgetLayout.addWidget(self.simpleButtonIcon(TITLE = 'Load It!',FUNC=self.load,TOOLTIP='Load the image'))



	def clear(self):
		from PSL.SENSORS import SSD1306
		self.OLED = SSD1306.SSD1306(self.I.I2C)
		self.OLED.clearDisplay()
		self.OLED.displayOLED()
		return 'Done'

	def test(self):
		self.clear()
		self.OLED.load('logo')
		self.OLED.displayOLED()
		return 'Done'

	def open_file(self):
		fname = self.getFile()
		if fname:
			size=128,64
			col = self.IMAGE.open(fname)
			col.thumbnail(size, self.IMAGE.ANTIALIAS)
			gray = col.convert('L')
			self.img = gray
			self.setThreshold(128)
			return 'loaded'
		else:
			return 'nothing'

	def setThreshold(self,val):
		if self.img:
			bw = self.img.point(lambda x: 0 if x<val else 255, '1')			
			image = QtGui.QImage(bw.convert("RGBA").tostring("raw", "RGBA"), bw.size[0], bw.size[1], QtGui.QImage.Format_ARGB32)
			pix = QtGui.QPixmap.fromImage(image)
			self.setPixMapOnLabel(self.imgFrame,pix)	
			self.bw = bw

		return val

	def load(self):
		if self.bw:
			self.clear()
			x,y = self.bw.size
			for a in range(x):
				for b in range(y):
					if(self.bw.getpixel((a,b)) ):self.OLED.drawPixel(a,b,1)
			self.OLED.displayOLED()
			return 'Done'
		else:
			return 'Load File'

	def closeEvent(self, event):
		pass

	def __del__(self):
		pass

if __name__ == "__main__":
	sys.path.append('/usr/share/seelablet')
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())

