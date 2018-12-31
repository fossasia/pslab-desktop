#!/usr/bin/python
'''
Output Peripheral control for FOSSASIA PSLab - version 1.0.0.
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt5 import QtCore, QtGui
import time,sys
from PSL_Apps.templates import ui_controlWidgets as controlWidgets
from PSL_Apps.templates.widgets import dial,button,selectAndButton
from PSL_Apps.utilitiesClass import utilitiesClass

import sys,os,string,functools
import time
import sys


params = {
'image' : 'dials.png',
'name' :u'Measurement\n& Control'
}

class AppWindow(QtGui.QMainWindow, controlWidgets.Ui_MainWindow,utilitiesClass):
    def __init__(self, parent=None,**kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I=kwargs.get('I',None)

        row=0;col=0;colLimit=3
        self.funcs=[]
        self.WidgetLayout.setAlignment(QtCore.Qt.AlignTop)

        self.supplySection = self.supplyWidget(self.I)
        self.advancedControlsLayout.addWidget(self.supplySection)
        self.sineSection = self.sineWidget(self.I)
        self.advancedControlsLayout.addWidget(self.sineSection)
        self.pwmSection = self.pwmWidget(self.I)
        self.advancedControlsLayout.addWidget(self.pwmSection)


        autogenControls=[]
        if self.I:
            if self.I.connected:
                autogenControls.append({'TITLE':'Wave 1','MIN':1,'MAX':5000,'FUNC':self.I.set_sine1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1','LINK':self.updateWAVE1_FREQ})
                autogenControls.append({'TITLE':'Wave 2','MIN':1,'MAX':5000,'FUNC':self.I.set_sine2,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #2','LINK':self.updateWAVE2_FREQ})
                autogenControls.append({'TITLE':'square 1','MIN':10,'MAX':50000,'FUNC':self.I.sqr1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of square wave generator #1'})

                tmpfunc = functools.partial(self.I.DAC.__setRawVoltage__,'PV1')
                autogenControls.append({'TITLE':'PV1','MIN':0,'MAX':4095,'FUNC':tmpfunc,'TYPE':'dial','UNITS':'V','TOOLTIP':'Programmable Voltage Source ','LINK':self.updatePV1_LABEL})

                tmpfunc = functools.partial(self.I.DAC.__setRawVoltage__,'PV2')
                autogenControls.append({'TITLE':'PV2','MIN':0,'MAX':4095,'FUNC':tmpfunc,'TYPE':'dial','UNITS':'V','TOOLTIP':'Programmable Voltage Source ','LINK':self.updatePV2_LABEL})

                tmpfunc = functools.partial(self.I.DAC.__setRawVoltage__,'PV3')
                autogenControls.append({'TITLE':'PV3','MIN':0,'MAX':4095,'FUNC':tmpfunc,'TYPE':'dial','UNITS':'V','TOOLTIP':'Programmable Voltage Source ','LINK':self.updatePV3_LABEL})

                tmpfunc = lambda x: self.I.DAC.__setRawVoltage__('PCS',4095-x)
                autogenControls.append({'TITLE':'PCS','MIN':0,'MAX':4095,'FUNC':tmpfunc,'TYPE':'dial','UNITS':'mA','TOOLTIP':'Programmable Current Source ','SCALE_FACTOR' : 1e3,'LINK':self.updatePCS_LABEL})

                autogenControls.append({'TITLE':'CAPACITANCE','FUNC':self.I.get_capacitance,'TYPE':'button','UNITS':'F','TOOLTIP':'Read Capacitance connected to CAP input '})

                tmpfunc = functools.partial(self.I.get_average_voltage,samples=100)
                autogenControls.append({'TITLE':'VOLTMETER','FUNC':tmpfunc,'TYPE':'selectButton','UNITS':'V','TOOLTIP':'Voltmeter','OPTIONS':self.I.allAnalogChannels})
                autogenControls.append({'TITLE':'Low Frequency','FUNC':self.I.get_freq,'TYPE':'selectButton','UNITS':'Hz','TOOLTIP':'Measure Frequency. Minimum 40Hz','OPTIONS':self.I.allDigitalChannels})
                autogenControls.append({'TITLE':'High Frequency','FUNC':self.I.get_high_freq,'TYPE':'selectButton','UNITS':'Hz','TOOLTIP':'Measure Frequencies over 1MHz with 10Hz resolution','OPTIONS':self.I.allDigitalChannels})

                autogenControls.append({'TITLE':'SR-04 Distance','FUNC':self.I.estimateDistance,'TYPE':'button','UNITS':'m','TOOLTIP':'Measure Distance using an HCSR04 sensor. TRIG-SQR1  , ECHO-ID1'})

                self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8"))

                for C in autogenControls:
                    if C['TYPE']=='dial':
                        self.funcs.append(C.get('FUNC',None))
                        self.WidgetLayout.addWidget(self.dialIcon(**C),row,col)
                    elif C['TYPE']=='button':
                        self.funcs.append(C.get('FUNC',None))
                        self.WidgetLayout.addWidget(self.buttonIcon(**C),row,col)
                    elif C['TYPE']=='selectButton':
                        self.funcs.append(C.get('FUNC',None))
                        self.WidgetLayout.addWidget(self.selectAndButtonIcon(**C),row,col)

                    col+=1
                    if(col==colLimit):
                        col=0;row+=1

                self.WidgetLayout.addWidget(self.setStateIcon(I=self.I),row,col)

            else:
                self.setWindowTitle(self.I.generic_name + ' : Not Connected')
        else:
            self.setWindowTitle('Not Connected!')


        self.setWindowTitle('vLabtool output Peripherals : '+self.I.H.version_string.decode("utf-8"))




    def measure_dcycle(self):
        inp = self.timing_input.currentText()
        v=self.I.DutyCycle(inp)
        if(v[0]!=-1):p=100*v[1]
        else: p=0
        self.timing_results.setText('Duty Cycle: %f %%'%(p))

    def measure_interval(self):
        t = self.I.MeasureInterval(self.edge1chan.currentText(),self.edge2chan.currentText(),self.edge1edge.currentText(),self.edge2edge.currentText())
        self.time_interval_label.setText('time: %.2e S'%(t))

    def updateWAVE1_FREQ(self,value,units=''):
        self.sineSection.WAVE1_FREQ.setText('%.3f %s '%(value,units))
    def updateWAVE2_FREQ(self,value,units=''):
        self.sineSection.WAVE2_FREQ.setText('%.3f %s '%(value,units))
    def updatePV1_LABEL(self,value,units=''):
        self.supplySection.PV1_LABEL.setText('%.3f %s '%(value,units))
    def updatePV2_LABEL(self,value,units=''):
        self.supplySection.PV2_LABEL.setText('%.3f %s '%(value,units))
    def updatePV3_LABEL(self,value,units=''):
        self.supplySection.PV3_LABEL.setText('%.3f %s '%(value,units))
    def updatePCS_LABEL(self,value,units=''):
        self.supplySection.PCS_LABEL.setText('%.3f %s '%(value,units))


    def loadSineTable(self):
        if self.I:
            from PSL.utilityApps import loadSineTable
            inst = loadSineTable.AppWindow(self,I=self.I)
            inst.show()
        else:
            print (self.setWindowTitle('Device Not Connected!'))

    def __del__(self):
        print ('bye')
                
if __name__ == "__main__":
    from PSL import sciencelab
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())
