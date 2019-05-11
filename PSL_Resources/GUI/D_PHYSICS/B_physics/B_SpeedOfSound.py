#!/usr/bin/python

"""

::

    This experiment is used to study non-inverting amplifiers

"""

from __future__ import print_function

import sys

from PyQt5 import QtGui, QtCore

from PSL_Apps.templates import auto_template_graph_nofft
from PSL_Apps.utilitiesClass import utilitiesClass

params = {
    'image': 'halfwave.png',
    'name': 'Speed of\nSound',
    'hint': '''
	Measure speed of sound using a 40KHz transmit piezo and receiver.<br>
	'''

}


class AppWindow(QtGui.QMainWindow, ui_template_graph_nofft.Ui_MainWindow, utilitiesClass):
    def __init__(self, parent=None, **kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I = kwargs.get('I', None)

        self.setWindowTitle(self.I.H.version_string + ' : ' + params.get('name', '').replace('\n', ' '))

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
        self.max_samples = 10000
        self.samples = self.max_samples
        self.timer = QtCore.QTimer()

        self.legend = self.plot.addLegend(offset=(-10, 30))
        self.curveCH1 = self.addCurve(self.plot, 'RAMP In(CH1)')
        self.autoRange()

        self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.ControlsLayout.setAlignment(QtCore.Qt.AlignRight)

        a1 = {'TITLE': 'Acquire Data', 'FUNC': self.run,
              'TOOLTIP': 'Sets SQR1 to HIGH, and immediately records the ramp'}
        self.ampGain = self.buttonIcon(**a1)
        self.WidgetLayout.addWidget(self.ampGain)

        self.WidgetLayout.addWidget(self.addSQR1(self.I))

        # Control widgets
        a1 = {'TITLE': 'TIMEBASE', 'MIN': 0, 'MAX': 9, 'FUNC': self.set_timebase, 'UNITS': 'S',
              'TOOLTIP': 'Set Timebase of the oscilloscope'}
        self.ControlsLayout.addWidget(self.dialIcon(**a1))

        G = self.gainIcon(FUNC=self.I.set_gain, LINK=self.gainChanged)
        self.ControlsLayout.addWidget(G)
        G.g1.setCurrentIndex(1);
        G.g2.setEnabled(False)

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
            x, y = self.I.capture_fullspeed('CH3', self.samples, self.tg, 'FIRE_PULSES', interval=50)
            self.curveCH1.setData(x * 1e-6, y)
            # self.displayCrossHairData(self.plot,False,self.samples,self.I.timebase,[y],[(0,255,0)])
            self.I.set_state(SQR1=False)  # Set SQR1 to 0
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
