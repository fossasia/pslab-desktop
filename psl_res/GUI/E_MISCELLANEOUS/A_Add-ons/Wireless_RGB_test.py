# -*- coding: utf-8 -*-
"""
Check the range of your RF Nodes by counting dropped packets.


"""

import sys,time,functools
from PyQt5 import QtGui, QtCore
import numpy as np
params = {
'image' : 'rgbled.png',
'helpfile': '',
'name':'Wireless\nRGB lights',
'hint':'''
	Displays alternating shades on the onboard colored LEDs of selected wireless nodes.<br>
	Also shows the signal quality based on dropped packet count.
	'''
}

class AppWindow(QtGui.QMainWindow):
	def __init__(self,parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.I=kwargs.get('I',None)

		self.I.NRF.write_register(self.I.NRF.SETUP_RETR,0x45)
		self.pos=0
		x = np.linspace(0,np.pi*2,500)
		self.t1 = 50+50*np.sin(x*2)
		self.t2 = 50+50*np.sin(x*4)
		self.t3 = 50+50*np.sin(x)


		self.resize(400, 120)
		self.Frame=QtGui.QFrame()
		self.Holder=QtGui.QVBoxLayout()
		self.Frame.setLayout(self.Holder)
		self.setCentralWidget(self.Frame)
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )
		self.lbl = QtGui.QLabel('Signal Strength meter:')
		self.Holder.addWidget(self.lbl)

		self.addressBox = QtGui.QLineEdit()
		self.addressBox.setText('0x010101')
		self.addressBox.returnPressed.connect(self.addAddress)
		self.addrLabel = QtGui.QLabel('address')
		self.Holder.addWidget(self.addrLabel)
		self.Holder.addWidget(self.addressBox)

		self.chanBox = QtGui.QSpinBox()
		self.chanBox.setMinimum(1); self.chanBox.setMaximum(127);self.chanBox.setValue(10);self.chanBox.valueChanged.connect(self.switchChannel)
		self.chanLabel = QtGui.QLabel('channel[0-127]: ')
		self.Holder.addWidget(self.chanLabel)
		self.Holder.addWidget(self.chanBox)


		self.slds = {}
		self.wids=[]
		self.last_chan = 100

		self.setWindowTitle('Control RGB LEDs on Wireless Nodes')
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(1)
		
	def switchChannel(self):
		self.timer.stop()
		chan = self.chanBox.value()
		for a in self.slds:
			for b in range(10):
				res = self.slds[a][1].write_register(self.I.NRF.RF_CH,chan)
				
		self.I.NRF.write_register(self.I.NRF.RF_CH,chan)
		self.last_chan = chan
		self.chanLabel.setText('Channel[0-127]: '+str(chan))
		self.timer.start(1)
		

	def addAddress(self):
		addr = int(str(self.addressBox.text()),16)
		if addr in self.slds:
			print('Already added')
			return

		Frame=QtGui.QFrame()
		Holder=QtGui.QHBoxLayout()
		Frame.setLayout(Holder)
		Holder.setMargin(0)
		self.Holder.addWidget(Frame)
		sld = QtGui.QProgressBar()
		btn = QtGui.QPushButton('X');btn.setMaximumWidth(20);btn.setStyleSheet("color:'red';")
		lbl = QtGui.QLabel(hex(addr))

		Holder.addWidget(sld)
		Holder.addWidget(lbl)
		Holder.addWidget(btn)
		btn.clicked.connect(functools.partial(self.pop,addr))
		sld.setRange(0,100)

		newlink = self.I.newRadioLink(address = addr)
		self.slds[addr]=[sld,newlink ,Frame]

		self.timer.stop()
		self.I.NRF.write_register(self.I.NRF.SETUP_RETR,0x21)
		for a in range(0,127):  #Sweep all channels and set the node channel to the one in use
			self.I.NRF.write_register(self.I.NRF.RF_CH,a)
			res = newlink.write_register(self.I.NRF.RF_CH,self.last_chan)
		self.I.NRF.write_register(self.I.NRF.RF_CH,self.last_chan)
		self.I.NRF.write_register(self.I.NRF.SETUP_RETR,0x25)
		self.timer.start(1)
		

		self.addrLabel.setText('Last Added: '+hex(addr))
		
	def pop(self,addr):
		a=self.slds.pop(addr)
		a[2].setParent(None)

	def update(self):
		self.pos+=1
		if(self.pos==500):self.pos=0
		for a in self.slds: self.slds[a][1].WS2812B([[int(self.t1[self.pos]),int(self.t2[self.pos]),int(self.t3[self.pos])]])
		if self.pos%50==0:
			for a in self.slds:
				wid = self.slds[a]
				wid[0].setValue(round(100*self.I.NRF.sigs[a]))

	def __del__(self):
		self.timer.stop()

	def closeEvent(self, event):
		self.timer.stop()


if __name__ == "__main__":
	from PSL import sciencelab
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=sciencelab.connect())
	myapp.show()
	sys.exit(app.exec_())
