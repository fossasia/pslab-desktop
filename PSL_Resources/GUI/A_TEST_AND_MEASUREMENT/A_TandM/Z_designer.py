#!/usr/bin/python
'''
design experiments

'''
from __future__ import print_function

import functools
import numbers
import time

import numpy as np
import pyqtgraph as pg
from PSL.SENSORS.supported import nameMap as I2CSensorsNameMap
from PSL.SENSORS.supported import supported as I2CSensors
from PSL_Apps.templates.widgets.auto_customFunc import Ui_Form as ui_custom
from PSL_Apps.templates.widgets.auto_customSensor import Ui_Form as ui_customSensor
from PSL_Apps.templates.widgets.auto_customSweep import Ui_Form as ui_customSweep
from PSL_Apps.templates.widgets.auto_sweep import Ui_Form as ui_sweep
from PSL_Apps.templates.widgets.auto_sweepTitle import Ui_Form as ui_sweepTitle
from PyQt5 import QtCore, QtGui
from pkg_resources import resource_filename, resource_listdir

from PSL_Apps.templates import auto_designer as designer
from PSL_Apps.utilitiesClass import utilitiesClass

xrange = range  # Python 3

params = {
    'image': 'sensors.png',
    'name': 'Experiment\nDesigner',
    'hint': '''
	Design your own experiment layout by choosing channels to sweep/monitor/plot.
	'''
}


class AppWindow(QtGui.QMainWindow, designer.Ui_MainWindow, utilitiesClass):
    helpLoader = QtCore.pyqtSignal(str, name='helpChanged')

    def __init__(self, parent=None, **kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I = kwargs.get('I', None)
        self.setWindowTitle(self.I.H.version_string + ' : ' + params.get('name', '').replace('\n', ' '))

        self.statics = {}
        self.sweeps = {}
        self.monitors = {}
        self.staticMap = {'W1': self.addW1, 'W2': self.addW2, 'PV1': self.addPV1, 'PV2': self.addPV2,
                          'PV3': self.addPV3, 'PCS': self.addPCS,
                          'SQR1': self.addSQR1}  # ,'VOLTMETER':self.addVoltmeter,'OHMMETER':self.addRes}
        self.widgets = {}
        self.customWidgetCount = 0
        self.evalGlobals = {}
        self.evalGlobals = {k: getattr(self.I, k) for k in dir(self.I)}
        try:
            if self.parent: self.helpLoader.connect(self.parent().setHelpUrl)
        except:
            print('standalone')

        ###################################READ AND LIST PROFILE FILES(.CONF)####################
        self.confTable.setHorizontalHeaderLabels(['File name', 'Path'])
        sys.path.append('/usr/share/pslab')
        RESMODULE = 'PSL_Resources.CONF'
        apps = [(n.split('.conf')[0], resource_filename(RESMODULE, n)) for n in resource_listdir(RESMODULE, '') if
                n != '__init__.py']
        self.populateResources(apps)

        ###################################POPULATE MONITORS LIST################################
        mons = self.I.allAnalogChannels[:]  # Shallow copy, since we will be removing elements
        mons.remove('MIC')
        mons += self.I.DAC.CHANS  # Add all the DAC channels for optional monitoring
        mons += ['W1', 'W2', 'SQR1', 'SQR2', 'SQR3', 'SQR4']  # add the waveforms for frequency monitoring
        self.totalReadBacks = 0
        self.monitorLayout.setAlignment(QtCore.Qt.AlignTop)
        for a in mons:
            self.addReadBackWidget(a)
        self.addParamButton = QtGui.QPushButton();
        self.addParamButton.setText('Add a Derived Channel');
        self.monitorLayout.addWidget(self.addParamButton)
        self.addParamButton.clicked.connect(self.addCustomMonitor)

        self.columnFuncs = []  # A collection of tuples on how to evaluate each column
        self.maxrows = 0
        self.maxcols = 0
        self.evaluatorLocation = None
        self.timer = self.newTimer()
        # self.timer.timeout.connect(self.evaluator)

        ###################################POPULATE STATIC OUTPUTS LIST##########################
        self.outputs['PV1']['func'] = self.I.set_pv1
        self.outputs['PV2']['func'] = self.I.set_pv2
        self.outputs['PV3']['func'] = self.I.set_pv3
        self.outputs['PCS']['func'] = self.I.set_pcs
        self.outputs['W1']['func'] = self.I.set_w1
        self.outputs['W2']['func'] = self.I.set_w2
        self.outputs['SQR1']['func'] = self.I.sqr1
        self.outputs['STEPS'] = {'min': 0, 'max': 10000,
                                 'tooltip': 'Generate a sequence of numbers.\nUseful if you want to simply record data in\na table without setting any parameter',
                                 'func': lambda x: x}

        for a in self.outputs.keys():
            box = QtGui.QCheckBox('%s' % a)
            box.setChecked(False)
            # action.setStyleSheet("background-color:rgb%s;"%(str(curves[a].opts['pen'].color().getRgb())))
            self.staticLayout.addWidget(box)
            self.statics[a] = box

        ###################################POPULATE SWEEP LIST##################################
        self.sweepLayout.addWidget(self.sweepTitle())
        for a in self.outputs:
            out = self.outputs[a]
            box = self.sweepHandler(title=a, **out)
            self.sweepLayout.addWidget(box)
            self.sweeps[a] = box
        self.addParamButton2 = QtGui.QPushButton();
        self.addParamButton2.setText('Add Custom Sweep Output');
        self.sweepLayout.addWidget(self.addParamButton2)
        self.addParamButton2.clicked.connect(self.addCustomSweep)

        ###################################CREATE PLOT#########################################
        self.plot = self.add2DPlot(self.plot_area)
        self.plot.getAxis('left').setLabel('Time', units='S')
        self.plot.getAxis('left').setLabel('Voltage', units='V')
        self.curves = [];
        self.curveLabels = []

        ###################################   LOAD A PRESET LIST  #########################
        preset = kwargs.get('preset', [])
        for p in preset:
            cstm = self.addCustomMonitor()
            if cstm:
                cstm.cmd.setText(p['cmd'])
                cstm.name.setText(p['name'])
                cstm.enable.setChecked(True)

    def populateResources(self, confList):
        num = 0
        for a in confList:
            name, path = a
            item = QtGui.QPushButton();
            item.setText(name);
            item.clicked.connect(functools.partial(self.loadProfileFile, path))
            self.confTable.setCellWidget(num, 0, item)
            item = QtGui.QTableWidgetItem();
            item.setText(path);
            self.confTable.setItem(num, 1, item)
            num += 1

    class customMonitorHandler(QtGui.QFrame, ui_custom):
        def __init__(self, **kwargs):
            super(AppWindow.customMonitorHandler, self).__init__()
            self.setupUi(self)
            self.I = kwargs.get('I', None)
            self.evalGlobals = kwargs.get('evalGlobals', None)

        def remove(self):
            self.enable.setChecked(False)
            self.setParent(None)

        def getFunc(self):
            tx = self.cmd.text()
            if len(tx) == 0:
                return None

            def fn():
                return eval(tx, globals(), self.evalGlobals)

            return fn

        def isChecked(self):
            return self.enable.isChecked()

        def text(self):
            return self.name.text()

    class customSensorMonitorHandler(QtGui.QFrame, ui_customSensor):
        def __init__(self, **kwargs):
            super(AppWindow.customSensorMonitorHandler, self).__init__()
            self.setupUi(self)
            self.SEN = kwargs.get('sen', None)
            if not hasattr(self.SEN, 'getRaw'):
                raise Exception  # QtGui.QMessageBox.about(self, 'Error',  'This Sensor does not have a read option')

            self.evalGlobals = kwargs.get('evalGlobals', None)
            self.title.setText('%s|%s' % (hex(self.SEN.ADDRESS), self.SEN.name))
            self.dataOptions.addItems(self.SEN.PLOTNAMES)

        def remove(self):
            self.enable.setChecked(False)
            self.setParent(None)

        def getFunc(self):
            try:
                method = getattr(self.SEN, 'getRaw')
                return lambda: method()[self.dataOptions.currentIndex()]
            except:
                return None

        def isChecked(self):
            return self.enable.isChecked()

        def text(self):
            return self.dataOptions.currentText() + ' : ' + hex(self.SEN.ADDRESS)

    def addCustomMonitor(self):  # Final wrapper that interacts with the user
        mons = ['generic expression', 'I2C sensor']
        item, ok = QtGui.QInputDialog.getItem(self, "Read Backs", "select the type of data you would like to record",
                                              mons, 0, False)
        if ok:
            if item == 'generic expression':
                return self.addCustomMonitorGeneric()
            elif item == 'I2C sensor':
                import inspect
                mons = {}
                names = []
                for a in I2CSensors:
                    m = inspect.getmembers(I2CSensors[a], inspect.isclass)
                    for b in m:
                        if hasattr(b[1], 'name'):
                            mons[b[1].name + ' | ' + b[0]] = (I2CSensors[a])
                            break
                item, ok = QtGui.QInputDialog.getItem(self, "Sensors", "select the type of sensor", mons.keys(), 0,
                                                      False)
                if ok:
                    try:
                        cstm = self.customSensorMonitorHandler(sen=mons[item].connect(self.I.I2C))
                        if cstm.SEN.ADDRESS not in self.I.I2C.scan():  # Sensor not connected
                            reply = QtGui.QMessageBox.question(self, 'Warning', 'Sensor Not detected. Use anyway?',
                                                               QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
                            if reply == QtGui.QMessageBox.No:
                                return None
                        self.monitorLayout.addWidget(cstm)
                        self.monitors['CSTM' + str(self.customWidgetCount)] = cstm
                        self.customWidgetCount += 1
                        return cstm
                    except Exception as e:
                        print(e)

    def addCustomMonitorGeneric(self):
        cstm = self.customMonitorHandler(I=self.I, evalGlobals=self.evalGlobals)
        self.monitorLayout.addWidget(cstm)
        self.monitors['CSTM' + str(self.customWidgetCount)] = cstm
        self.customWidgetCount += 1
        return cstm

    def addCustomMonitorSensor(self, classname):
        if classname in I2CSensorsNameMap:
            cstm = self.customSensorMonitorHandler(sen=I2CSensorsNameMap[classname].connect(self.I.I2C))
            self.monitorLayout.addWidget(cstm)
            self.monitors['CSTM' + str(self.customWidgetCount)] = cstm
            self.customWidgetCount += 1
            return cstm
        else:
            print('invalid sensor', classname)
            return None

    class monitorHandler(QtGui.QCheckBox):
        def __init__(self, **kwargs):
            super(AppWindow.monitorHandler, self).__init__()
            self.I = kwargs.get('I', None)
            self.chanName = kwargs.get('chan', None)
            self.setText(self.chanName)
            if self.chanName in self.I.allAnalogChannels:
                self.func = functools.partial(self.I.get_voltage, self.chanName)
            elif self.chanName in self.I.DAC.CHANS:
                self.func = functools.partial(self.I.DAC.getVoltage, self.chanName)
            elif self.chanName in ['W1', 'W2', 'SQR1', 'SQR2', 'SQR3', 'SQR4']:
                self.func = functools.partial(self.I.readbackWaveform, self.chanName)

        def getFunc(self):
            return self.func

    def addReadBackWidget(self, a):
        box = self.monitorHandler(chan=a, I=self.I)
        box.setChecked(False)
        self.sampleReadbacks.addWidget(box, self.totalReadBacks % 4, self.totalReadBacks / 4)
        self.monitors[a] = box
        self.evalGlobals[a] = box.getFunc()
        self.totalReadBacks += 1
        return box

    class sweepHandler(QtGui.QFrame, ui_sweep):
        def __init__(self, **kwargs):
            super(AppWindow.sweepHandler, self).__init__()
            self.setupUi(self)
            self.func = kwargs.get('func', None)
            self.enable.setText(kwargs.get('title', 'Not Set'))
            self.startBox.setMinimum(kwargs.get('min', 0));
            self.startBox.setMaximum(kwargs.get('max', 1));
            self.startBox.setValue(kwargs.get('min', 0))
            self.stopBox.setMinimum(kwargs.get('min', 0));
            self.stopBox.setMaximum(kwargs.get('max', 1));
            self.stopBox.setValue(kwargs.get('max', 0))
            self.setToolTip(kwargs.get('tooltip', ''))

        def getFunc(self):
            return self.func

        def text(self):
            return self.enable.text()

    class sweepTitle(QtGui.QFrame, ui_sweepTitle):
        def __init__(self, **kwargs):
            super(AppWindow.sweepTitle, self).__init__()
            self.setupUi(self)

    class customSweepHandler(QtGui.QFrame, ui_customSweep):
        def __init__(self, **kwargs):
            super(AppWindow.customSweepHandler, self).__init__()
            self.setupUi(self)
            self.I = kwargs.get('I', None)
            self.func = kwargs.get('func', None)
            self.name.setText(kwargs.get('title', ''))
            self.cmd.setText('set_pv1')
            self.setToolTip(kwargs.get('tooltip', ''))

        def remove(self):
            self.enable.setChecked(False)
            self.setParent(None)

        def getFunc(self):
            tx = self.cmd.text()
            try:
                method = getattr(self.I, tx)
                return method
            except:
                return None

        def isChecked(self):
            return self.enable.isChecked()

        def text(self):
            return self.name.text()

    def addCustomSweep(self):
        cstm = self.customSweepHandler(I=self.I)
        self.sweepLayout.addWidget(cstm)
        self.sweeps['CSTM' + str(self.customWidgetCount)] = cstm
        self.customWidgetCount += 1
        return cstm

    def prepare(self):
        self.eTabs.setCurrentIndex(2)  # Switch to experiment tab
        self.columnFuncs = []  # Reset the collection of tuples on how to evaluate each column

        for a in range(self.maxcols + 1):  ## clear the table
            for b in range(self.maxrows):
                self.tbl.setItem(b, a, None)
                self.tbl.setCellWidget(b, a, None)
        self.maxcols = 0
        self.maxrows = 0

        for a in self.widgets:
            self.widgets[a].setParent(None)
        self.widgets = {}

        ##########################################  PREPARATION  #########################################################
        tblheaders = []
        # Sweep inputs
        for a in self.sweeps:
            widget = self.sweeps[a]
            if widget.enable.isChecked():
                func = widget.getFunc()
                if func == None:
                    self.displayDialog('Invalid function : ' + str(widget.text()))
                tblheaders.append(str(widget.text()))
                self.columnFuncs.append([1, func])  # 1= output , function to use

        #############    prepare monitor readback commands    ################
        for a in self.monitors:
            widget = self.monitors[a]
            if widget.isChecked():
                func = widget.getFunc()
                if func == None:
                    self.displayDialog('Invalid function : ' + str(widget.text()))
                tblheaders.append(str(widget.text()))
                self.columnFuncs.append([0, func])  # 0= input , function to use
        tblheaders.append('Evaluate')
        self.tbl.setColumnCount(len(tblheaders))  # Last column will have push buttons for each row
        self.tbl.setHorizontalHeaderLabels(tblheaders)
        ###################################################################################################################

        ##############    populate sweep columns    #############
        for a in self.sweeps:
            widget = self.sweeps[a]
            if widget.enable.isChecked():
                vals = np.linspace(widget.startBox.value(), widget.stopBox.value(), widget.numBox.value())
                self.maxrows = max(len(vals), self.maxrows)
                self.tbl.setRowCount(self.maxrows)
                for num in range(len(vals)):
                    item = QtGui.QTableWidgetItem();
                    item.setText('%.3e' % (vals[num]));
                    self.tbl.setItem(num, self.maxcols,
                                     item)  # ;item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                self.maxcols += 1

        if self.maxcols == 0:  # No sweeps were selected
            reply = QtGui.QMessageBox.question(self, 'Connection',
                                               'No sweep channels were selected!\nReturn to editor?',
                                               QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.eTabs.setCurrentIndex(1)  # Go back to editing
                return
        ##############   populate monitor columns    #############
        for a in self.monitors:
            widget = self.monitors[a]
            if widget.isChecked():
                for b in range(self.maxrows):
                    item = QtGui.QTableWidgetItem();
                    item.setText('');
                    self.tbl.setItem(b, self.maxcols,
                                     item)  # ;item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                self.maxcols += 1

        ################# make readback buttons ##############
        for a in range(self.maxrows):
            item = QtGui.QPushButton();
            item.setText('Calc');
            item.clicked.connect(functools.partial(self.evaluateRow, a))
            self.tbl.setCellWidget(a, self.maxcols,
                                   item)  # ;item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)

        ###################  Make the static widgets  ######################
        row = 0;
        col = 0
        for a in self.statics:
            widget = self.statics[a]
            if widget.isChecked():
                newWidget = self.staticMap[str(widget.text())](self.I)
                self.controlsLayout.addWidget(newWidget, row, col)
                self.widgets[str(widget.text())] = newWidget
                col += 1
                if col == 3:
                    col = 0;
                    row += 1

    def solveRowOutputs(self, row):
        for a in range(self.maxcols):
            tp = self.columnFuncs[a]
            if tp[0]:  # Set all outputs
                try:
                    item = self.tbl.item(row, a)
                    item.setText('%.3e' % tp[1](float(item.text())))
                except:
                    pass

    def solveRowInputs(self, row):
        for a in range(self.maxcols):
            tp = self.columnFuncs[a]
            if not tp[0]:  # Read all inputs
                try:
                    val = tp[1]()
                    item = self.tbl.item(row, a);
                    if isinstance(val, numbers.Number):
                        item.setText('%.3e' % val)
                    else:
                        item.setText(val)
                except:
                    pass

    def evaluateRow(self, row):
        self.solveRowOutputs(row)
        time.sleep(self.delayBox.value() * 1e-3)  # allow settling time
        self.solveRowInputs(row)

    def clearColumn(self):
        pass

    def runAll(self):
        self.evaluatorLocation = 0
        self.timer.singleShot(0, self.evaluator)

    def evaluator(self):
        self.tbl.selectRow(self.evaluatorLocation)
        # self.evaluateRow(self.evaluatorLocation)
        if self.evaluatorLocation: self.solveRowInputs(
            self.evaluatorLocation - 1)  # Evaluate the inputs for the previous row
        self.solveRowOutputs(
            self.evaluatorLocation)  # Evaluate the outputs for the current row, and evaluate the next row after a settling delay
        self.evaluatorLocation += 1
        if self.evaluatorLocation == self.maxrows:
            time.sleep(1e-3 * self.delayBox.value())
            self.solveRowInputs(
                self.evaluatorLocation - 1)  # Solve the last row's inputs after allowing a settling delay
            print('stopping')
            self.evaluatorLocation = None
            self.timer.stop()
            return
        self.timer.singleShot(self.delayBox.value(), self.evaluator)

    # Just a little something to enable copying data from the table
    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            if e.key() == QtCore.Qt.Key_C:  # copy
                self.copyTable()

    def copyTable(self):
        selected = self.tbl.selectedRanges()
        s = '\t' + "\t".join([str(self.tbl.horizontalHeaderItem(i).text()) for i in
                              xrange(selected[0].leftColumn(), selected[0].rightColumn() + 1)])
        s = s + '\n'

        for r in xrange(selected[0].topRow(), selected[0].bottomRow() + 1):
            # Add vertical headers
            try:
                s += self.tbl.verticalHeaderItem(r).text() + '\t'
            except:
                s += str(r) + '\t'

            for c in xrange(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    s += str(self.tbl.item(r, c).text()) + "\t"
                except AttributeError:
                    s += "\t"
            s = s[:-1] + "\n"  # eliminate last '\t'
        self.clip = QtGui.QApplication.clipboard()
        self.clip.setText(s)

    def plotColumns(self):
        selected = self.tbl.selectedRanges()
        x = []
        y = []
        xname = '';
        yname = ''
        if len(selected) == 0:
            self.displayDialog('Please Select at least two columns')
            return

        if len(selected) == 1:
            if selected[0].leftColumn() == selected[0].rightColumn():
                self.displayDialog('Please Select at least two columns')
                return
            for a in xrange(selected[0].topRow(), selected[0].bottomRow() + 1): x.append(
                float(self.tbl.item(a, selected[0].leftColumn()).text()))
            for a in xrange(selected[0].topRow(), selected[0].bottomRow() + 1): y.append(
                float(self.tbl.item(a, selected[0].leftColumn() + 1).text()))
            xname = str(self.tbl.horizontalHeaderItem(selected[0].leftColumn()).text())
            yname = str(self.tbl.horizontalHeaderItem(selected[0].leftColumn() + 1).text())
        elif len(selected) == 2:
            for a in xrange(selected[0].topRow(), selected[0].bottomRow() + 1): x.append(
                float(self.tbl.item(a, selected[0].leftColumn()).text()))
            for a in xrange(selected[1].topRow(), selected[1].bottomRow() + 1): y.append(
                float(self.tbl.item(a, selected[1].leftColumn()).text()))
            xname = str(self.tbl.horizontalHeaderItem(selected[0].leftColumn()).text())
            yname = str(self.tbl.horizontalHeaderItem(selected[1].leftColumn()).text())

        msgBox = QtGui.QMessageBox()
        msgBox.setText("Plotting \nxaxis : %s\nyaxis : %s" % (xname, yname))
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel)
        noRev = msgBox.addButton(self.tr("Plot"), QtGui.QMessageBox.ActionRole)
        rev = msgBox.addButton(self.tr("Swap Axes and plot"), QtGui.QMessageBox.ActionRole)

        ret = msgBox.exec_()
        if msgBox.clickedButton() == rev:
            tmp = y;
            y = x;
            x = tmp
            tmp = yname;
            yname = xname;
            xname = tmp
        elif ret == QtGui.QMessageBox.Cancel:
            return

        AllItems = [self.plotList.itemText(i) for i in range(self.plotList.count())]
        num = 1
        self.plot.getAxis('bottom').setLabel(xname)
        self.plot.getAxis('left').setLabel(yname)
        name = xname + ' vs ' + yname
        while name + ' #' + str(num) in AllItems:
            num += 1
        name = name + ' #' + str(num)
        self.eTabs.setCurrentIndex(3)  # Switch to plot tab
        curve = self.addCurve(self.plot, name)
        curve.setData(x, y)
        txt = '<div style="text-align: center"><span style="color: #FFF;font-size:8pt;">%s</span></div>' % (name)
        text = pg.TextItem(html=txt, anchor=(0, 0), border='w', fill=(0, 0, 255, 100))
        self.plot.addItem(text)
        text.setPos(x[-1], y[-1])
        self.plotList.addItem(name)
        self.curveLabels.append(text)
        self.curves.append(curve)
        self.plot.autoRange()
        self.plot.setXRange(min(x), max(x) * 1.3)
        self.plot.setYRange(min(y), max(y) * 1.3)

    def deleteCurve(self):
        c = self.plotList.currentIndex()
        if c > -1:
            self.plotList.removeItem(c)
            self.removeCurve(self.plot, self.curves[c]);
            self.plot.removeItem(self.curveLabels[c]);
            self.curves.pop(c);
            self.curveLabels.pop(c);
            if len(self.curves) == 0:  # reset counter for plot numbers
                self.plotnum = 0

    def saveData(self):
        self.saveDataWindow(self.curves, self.plot)

    def clearCustomWidgets(self):
        for box in self.monitors:
            try:
                if box[:4] == 'CSTM': self.monitors[box].remove()
            except:
                print(box)
        for box in self.sweeps:
            try:
                if box[:4] == 'CSTM': self.sweeps[box].remove()
            except:
                print(box)
        self.totalReadBacks = 0

    def loadProfile(self):
        from os.path import expanduser
        filename = QtGui.QFileDialog.getOpenFileName(self, "Load a Profile", expanduser("."), 'CONF(*.conf)')
        if filename:
            self.loadProfileFile(filename)

    def loadProfileFile(self, filename):
        from itertools import takewhile
        self.clearCustomWidgets()
        is_tab = '\t'.__eq__
        inFile = open(filename)
        source = inFile.read()
        lines = iter(source.split('\n'))
        stack = []
        for line in lines:
            indent = len(list(takewhile(is_tab, line)))
            stack[indent:] = [line.lstrip()]
            self.loadPresets(stack)
        self.eTabs.setCurrentIndex(1)  # Switch to design tab

    def loadPresets(self, P):
        if len(P) != 3:
            if len(P) == 2:
                P[0].strip();
                P[1].strip()
                if P[0] == 'HELPFILE': self.helpLoader.emit(P[1])
            return
        P[0].strip();
        P[1].strip();
        P[2].strip()
        if P[0] == 'STATIC':  # P = ['STATIC','SOMETHING','PV1'] . creates knobs
            if P[2] in self.statics:
                self.statics[P[2]].setChecked(True)
        elif P[
            0] == 'MONITOR':  # P  = ['MONITOR','STANDARD','NAME CHANNEL'] or ['MONITOR','SENSOR','MAG HMC5883L 1'] etc
            if P[1] == 'STANDARD':
                chan = P[2].strip()
                if chan in self.monitors:
                    self.monitors[chan].setChecked(True)
                else:
                    box = self.addReadBackWidget(chan)
                    box.setChecked(True)
            elif P[1] == 'CUSTOM':
                name, cmd = P[2].strip().split(' ')
                box = self.addCustomMonitorGeneric()
                box.enable.setChecked(True)
                box.name.setText(name)
                box.cmd.setText(cmd)
            elif P[1] == 'SENSOR':
                sensor, plotnum = P[2].strip().split(' ')
                box = self.addCustomMonitorSensor(sensor)
                box.enable.setChecked(True)
                box.dataOptions.setCurrentIndex(int(plotnum))

        elif P[0] == 'SWEEP':  # P = ['SWEEP', 'STANDARD', 'PV2 1 2 10']
            if P[1] == 'STANDARD':
                name, st, en, pt = P[2].strip().split(' ')
                if name in self.sweeps:
                    self.sweeps[name].enable.setChecked(True)
                    self.sweeps[name].startBox.setValue(float(st))
                    self.sweeps[name].stopBox.setValue(float(en))
                    self.sweeps[name].numBox.setValue(float(pt))
            elif P[1] == 'CUSTOM':
                name, cmd, st, en, pt = P[2].strip().split(' ')
                box = self.addCustomSweep()
                box.enable.setChecked(True)
                box.name.setText(name)
                box.cmd.setText(cmd)
                box.startBox.setValue(float(st))
                box.stopBox.setValue(float(en))
                box.numBox.setValue(float(pt))

    def saveProfile(self):
        from os.path import expanduser
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save Profile', expanduser("./"), 'CONF(*.conf)')
        # path = '/home/jithin/pro.conf'
        if path:
            sections = path.split('.')
            if (sections[-1] != 'conf'): path += '.conf'
            FL = open(path, 'wt')
            FL.write('SWEEP\n')
            for a in self.sweeps:
                w = self.sweeps[a]
                if w.enable.isChecked():
                    if isinstance(w, self.sweepHandler):
                        FL.write('\tSTANDARD\n')
                        FL.write('\t\t%s %f %f %d\n' % (
                        w.enable.text(), float(w.startBox.value()), float(w.stopBox.value()), int(w.numBox.value())))
                    if isinstance(w, self.customSweepHandler):
                        FL.write('\tCUSTOM\n')
                        FL.write('\t\t%s %s %f %f %d\n' % (
                        w.name.text(), w.cmd.text(), float(w.startBox.value()), float(w.stopBox.value()),
                        int(w.numBox.value())))
            FL.write('MONITOR\n')
            for a in self.monitors:
                w = self.monitors[a]
                if isinstance(w, self.monitorHandler):
                    if w.isChecked():
                        FL.write('\tSTANDARD\n')
                        FL.write('\t\t%s\n' % (w.text()))
                if isinstance(w, self.customMonitorHandler):
                    if w.enable.isChecked():
                        FL.write('\tCUSTOM\n')
                        FL.write('\t\t%s %s\n' % (w.name.text(), w.cmd.text()))
                if isinstance(w, self.customSensorMonitorHandler):
                    if w.enable.isChecked():
                        FL.write('\tSENSOR\n')
                        FL.write('\t\t%s %d\n' % (w.SEN.__module__.split('.')[-1], w.dataOptions.currentIndex()))

            FL.write('STATIC\n')
            for a in self.statics:
                w = self.statics[a]
                if w.isChecked():
                    FL.write('\tSTANDARD\n')
                    FL.write('\t\t%s\n' % (w.text()))

            FL.close()

    def __del__(self):
        self.timer.stop()
        print('bye')

    def closeEvent(self, event):
        self.timer.stop()
        self.finished = True


if __name__ == "__main__":
    from PSL import sciencelab
    import sys

    app = QtGui.QApplication(sys.argv)
    # P=[{'name':'res','cmd':'CH1'}]  #An array of dictionaries defining custom functions
    myapp = AppWindow(I=sciencelab.connect())  # ,preset = P)
    myapp.show()
    sys.exit(app.exec_())
