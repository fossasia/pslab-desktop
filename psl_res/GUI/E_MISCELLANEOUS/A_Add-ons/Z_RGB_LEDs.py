# -*- coding: utf-8 -*-
"""
Simple example demonstrating controlling servo motors with sliders
"""

from __future__ import print_function
import sys,time
from PyQt5 import QtGui, QtCore
import pyqtgraph as pg

params = {
'image' : 'rgbled.png',
'helpfile': 'servos.html',
'name':'RGB LED\nWS2812B',
'hint':'''
	Control WS2812B RGB LED chains using CS1/CS2/SQR1
	This utility allows setting the shades via a color widget
	'''
}

class AppWindow(QtGui.QMainWindow):
	def __init__(self,parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.I=kwargs.get('I',None)
		a=self.I.WS2812B([[0xAA,0x00,0xFF]],'SQR1')
		TOTAL_PIXELS=3
		self.Frame=QtGui.QFrame()
		self.Holder=QtGui.QVBoxLayout()
		self.Frame.setLayout(self.Holder)
		self.setCentralWidget(self.Frame)
		self.setWindowTitle('Set color of WS2812B RGB LEDs')

		self.btns = [pg.ColorButton() for a in range(TOTAL_PIXELS)]
		for sld in self.btns:
			self.Holder.addWidget(sld)

		self.COLS=[[1,0,1]]*len(self.btns)
		for btn in self.btns: btn.sigColorChanging.connect(self.change)


	def change(self,btn):
		self.COLS[ self.btns.index(btn) ]=list(btn.color().getRgb())
		a=self.I.WS2812B(self.COLS,'SQR1')


if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

