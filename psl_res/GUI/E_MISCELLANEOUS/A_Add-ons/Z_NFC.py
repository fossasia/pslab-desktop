#!/usr/bin/python
'''
Use the MF522 RFID Reader via the SPI port.
uses chip select 1
'''

from __future__ import print_function

from PyQt5 import QtCore, QtGui
from .templates import ui_NFC as NFC
import sys


params = {
'image' : 'mf522.png',
'helpfile': 'diodeIV.html',
'name':'RFID Reader\nMF522'
}

class AppWindow(QtGui.QMainWindow, NFC.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from PSL.SENSORS import MF522
		self.MF = MF522.connect(self.I,'CS1')
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		if not self.MF.connected:
			QtGui.QMessageBox.about(self, 'Error', 'Card reader not detected')
			print ("No")
		else:
			self.MF.getStatus()
			self.UID = False
			self.present =False
			self.key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
			self.looptimer = QtCore.QTimer()
			self.looptimer.timeout.connect(self.autoscan)
			self.looptimer.start(500)


	def read(self):
		self.detect.setText( "Searching ..." )
		(status,TagType) = self.MF.MFRC522_Request(self.MF.PICC_CMD_REQA)
		if status == self.MF.MI_OK:
			print ("Found",TagType)
			self.detect.setText( "Card detected" )
			(status,uid) = self.MF.MFRC522_Anticoll()
			if status == self.MF.MI_OK:
				self.detect.setText("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
				print ("UID Read.")
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				self.MF.MFRC522_SelectTag(uid)
				status = self.MF.MFRC522_Auth(self.MF.PICC_AUTHENT1A, 8, key, uid)
				if status == self.MF.MI_OK:
					print ("Data read.")
					data = self.MF.MFRC522_Read(self.sectorEdit.value())
					self.MF.MFRC522_StopCrypto1()
					self.dataLabel.setText(str(data))
					txt = ''
					for a in data:
						txt+=chr(a)
					self.dataEdit.setText(txt)
				else:
					self.dataLabel.setText( "Sector read failed. Auth Err." )

				self.MF.MFRC522_StopCrypto1()

			else:
				self.detect.setText( "UID read failed." )

		else:
			print ("Card not found")
			self.detect.setText( "Card not detected" )
	
	def write(self):
		print ("searching...")
		self.detect.setText( "Searching ..." )
		(status,TagType) = self.MF.MFRC522_Request(self.MF.PICC_CMD_REQA)
		if status == self.MF.MI_OK:
			print ("Found")
			self.detect.setText( "Card detected" )
			(status,uid) = self.MF.MFRC522_Anticoll()
			if status == self.MF.MI_OK:
				self.detect.setText("Card write UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
				print ("UID Read.")
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				self.MF.MFRC522_SelectTag(uid)
				status = self.MF.MFRC522_Auth(self.MF.PICC_AUTHENT1A, 8, key, uid)
				if status == self.MF.MI_OK:
					print ("Data read.")
					self.dataLabel.setText(str(self.MF.MFRC522_Read(self.sectorEdit.value() )))
					print ("Data writing...")
					data = [46 for a in range(16)]
					txt = str(self.dataEdit.text())
					for a in range(len(txt)):data[a] = ord(txt[a])
					print (data)
					self.MF.MFRC522_Write(self.sectorEdit.value(), data)
					self.MF.MFRC522_StopCrypto1()
				else:
					self.dataLabel.setText( "Sector read failed. Auth Err." )

			else:
				self.detect.setText( "UID read failed." )

		else:
			print ("Card not found")
			self.detect.setText( "Card not detected" )

	def autoscan(self):
		if not self.autoBox.isChecked():
			return
		(status,TagType) = self.MF.MFRC522_Request(self.MF.PICC_CMD_REQA)
		txt = ''
		if status == self.MF.MI_OK:
			(status,uid) = self.MF.MFRC522_Anticoll()
			if status == self.MF.MI_OK:
				txt+="UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+'\n'
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				self.MF.MFRC522_SelectTag(uid)
				status = self.MF.MFRC522_Auth(self.MF.PICC_AUTHENT1A, 8, key, uid)
				if status == self.MF.MI_OK:
					data = self.MF.MFRC522_Read(self.sectorEdit.value())
					self.MF.MFRC522_StopCrypto1()
					txt+=str(data)+'\n'
					for a in data:
						txt+=chr(a)
				else:
					txt+= "Sector read failed. Auth Err."

				self.MF.MFRC522_StopCrypto1()

			else:
				txt+= "UID read failed."
		else:
			txt = "Searching ..."
		
		self.autoLabel.setText(txt)



	def __del__(self):
		self.looptimer.stop()
		print ('bye')

	def closeEvent(self, event):
		self.looptimer.stop()
		self.finished=True


if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())

