#!/usr/bin/python

"""

::

    An Op-Amp based linear ramp generator that integrates a step signal issued via SQR1 to make a smooth ramp output.

"""

from __future__ import print_function

import sys
import time

from PyQt5 import QtGui, QtCore

from PSL_Apps.templates import ui_template_graph_nofft as template_graph_nofft
from PSL_Apps.utilitiesClass import utilitiesClass

params = {
    'image': 'monostable.png',
    'name': 'Monostable\nMultivibrator',
    'hint': '''
	A transistor based monostable multivibrator 
	'''

}


class AppWindow(QtGui.QMainWindow, template_graph_nofft.Ui_MainWindow, utilitiesClass):
    def __init__(self, parent=None, **kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I = kwargs.get('I', None)

        self.setWindowTitle(self.I.H.version_string + ' : ' + params.get('name', '').replace('\n', ' '))
        self.I.set_state(SQR1=0)

        from PSL.analyticsClass import analyticsClass
        self.math = analyticsClass()
        self.prescalerValue = 0

        self.plot = self.add2DPlot(self.plot_area, enableMenu=False)
        # self.enableCrossHairs(self.plot,[])
        labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
        self.plot.setLabel('left', 'V (CH1)', units='V', **labelStyle)
        self.plot.setLabel('bottom', 'Time', units='S', **labelStyle)
        self.plot.setYRange(-8.5, 8.5)

        self.tg = 0.5
        self.max_samples = 2000
        self.samples = self.max_samples
        self.timer = self.newTimer()

        self.legend = self.plot.addLegend(offset=(-10, 30))
        self.curveCH1 = self.addCurve(self.plot, 'Pulse output(CH2)')
        self.curveCH2 = self.addCurve(self.plot, 'Trigger Pulse(CH1)')
        self.autoRange()

        self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ControlsLayout.setAlignment(QtCore.Qt.AlignRight)

        a1 = {'TITLE': 'Acquire Data', 'FUNC': self.run,
              'TOOLTIP': 'Sets SQR1 to HIGH, and immediately records the ramp'}
        self.ampGain = self.buttonIcon(**a1)
        self.WidgetLayout.addWidget(self.ampGain)

        # Control widgets
        a1 = {'TITLE': 'TIMEBASE', 'MIN': 0, 'MAX': 9, 'FUNC': self.set_timebase, 'UNITS': 'S',
              'TOOLTIP': 'Set Timebase of the oscilloscope'}
        self.ControlsLayout.addWidget(self.dialIcon(**a1))

        G = self.gainIconCombined(FUNC=self.I.set_gain, LINK=self.gainChanged)
        self.ControlsLayout.addWidget(G)
        G.g1.setCurrentIndex(1)

        self.running = True
        self.fit = False

    def gainChanged(self, g):
        self.autoRange()

    def set_timebase(self, g):
        timebases = [0.5, 1, 2, 4, 8, 32, 128, 256, 512, 1024]
        self.prescalerValue = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3][g]
        samplescaling = [1, 1, 1, 1, 1, 0.5, 0.4, 0.3, 0.2, 0.2, 0.1]
        self.tg = timebases[g]
        self.samples = int(self.max_samples * samplescaling[g])
        return self.autoRange()

    def autoRange(self):
        xlen = self.tg * self.samples * 1e-6
        self.plot.autoRange();
        chan = self.I.analogInputSources['CH1']
        R = [chan.calPoly10(0), chan.calPoly10(1023)]
        R[0] = R[0] * .9;
        R[1] = R[1] * .9
        self.plot.setLimits(yMax=max(R), yMin=min(R), xMin=0, xMax=xlen)
        self.plot.setYRange(min(R), max(R))
        self.plot.setXRange(0, xlen)

        return self.samples * self.tg * 1e-6

    def run(self):
        try:
            self.ampGain.value.setText('reading...')
            self.I.capture_traces(2, self.samples, self.tg, trigger=False)
            self.I.set_state(SQR1=1)
            time.sleep(0.001)
            self.I.set_state(SQR1=0)
            # self.I.__write_data_address__(0x902,0)
            # self.I.sqrPWM(10000,.1,0,.1,0,.1,0,.1,pulse=True)

            time.sleep(1e-6 * self.samples * self.I.timebase + .01)
            self.I.__fetch_channel__(1)
            self.I.__fetch_channel__(2)

            x = self.I.achans[0].get_xaxis()

            self.curveCH1.setData(x * 1e-6, self.I.achans[0].get_yaxis())
            self.curveCH2.setData(x * 1e-6, self.I.achans[1].get_yaxis())
            # self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[y],[(0,255,0)])
            return 'Done'
        except Exception as e:
            print(e)
            return 'Error'

    def saveData(self):
        self.saveDataWindow([self.curveCH1], self.plot)

    def closeEvent(self, event):
        self.running = False
        self.timer.stop()
        self.finished = True

    def __del__(self):
        self.timer.stop()
        print('bye')


if __name__ == "__main__":
    from PSL import sciencelab

    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=sciencelab.connect())
    myapp.show()
    sys.exit(app.exec_())
