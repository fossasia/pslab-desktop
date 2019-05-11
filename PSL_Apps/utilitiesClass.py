import functools
import importlib
import numbers
import os
import random
import sys

import pkg_resources

import numpy as np
import pyqtgraph as pg
import PyQt5.sip as sip
from PSL_Apps import saveProfile
from PSL_Apps.templates.widgets import auto_button as button
from PSL_Apps.templates.widgets import auto_dial as dial
from PSL_Apps.templates.widgets import auto_dialAndDoubleSpin as dialAndDoubleSpin
from PSL_Apps.templates.widgets import auto_displayWidget as displayWidget
from PSL_Apps.templates.widgets import auto_doubleSpinBox as doubleSpinBox
from PSL_Apps.templates.widgets import auto_dualButton as dualButton
from PSL_Apps.templates.widgets import auto_gainWidget as gainWidget
from PSL_Apps.templates.widgets import auto_gainWidgetCombined as gainWidgetCombined
from PSL_Apps.templates.widgets import auto_pulseCounter as pulseCounter
from PSL_Apps.templates.widgets import auto_pwmWidget as pwmWidget
from PSL_Apps.templates.widgets import auto_selectAndButton as selectAndButton
from PSL_Apps.templates.widgets import auto_sensorWidget as sensorWidget
from PSL_Apps.templates.widgets import auto_setStateList as setStateList
from PSL_Apps.templates.widgets import auto_simpleButton as simpleButton
from PSL_Apps.templates.widgets import auto_sineWidget as sineWidget
from PSL_Apps.templates.widgets import auto_spinBox as spinBox
from PSL_Apps.templates.widgets import auto_supplyWidget as supplyWidget
from PSL_Apps.templates.widgets import auto_voltWidget as voltWidget
from PSL_Apps.templates.widgets import auto_widebutton as widebutton
from PyQt5 import QtCore, QtGui

os.environ['QT_API'] = 'pyqt'
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

unicode = str  # Python 3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class utilitiesClass():
    """
    This class contains methods that simplify setting up and running
    an experiment.

    feature list :

    * 2D Plots

      - Embed a PyQtgraph PlotWidget into a specified Qt Layout
      - Add curves into a supplied PlotWidget, and maintain a list.
      - Add crosshairs

    """
    timers = []
    viewBoxes = []
    plots3D = {}
    plots2D = {}
    total_plot_areas = 0
    funcList = []
    interactivePlots = []
    gl = None
    black_trace_colors = [(0, 255, 20), (255, 0, 0), (255, 255, 100), (10, 255, 255)]
    white_trace_colors = [(0, 255, 20), (255, 0, 0), (255, 255, 100), (10, 255, 255)]
    black_trace_colors += [QtGui.QColor(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for a
                           in range(50)]
    white_trace_colors += [QtGui.QColor(random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)) for a
                           in range(50)]

    studioPlots = {}
    studioWidgets = {}
    properties = {'colorScheme': 'black'}
    outputs = {
        'W1': {'min': 1, 'max': 5000, 'tooltip': 'Set the frequency of Wavegen 1(W1)'},
        'W2': {'min': 1, 'max': 5000, 'tooltip': 'Set the frequency of Wavegen 2(W2)'},
        'SQR1': {'min': 10, 'max': 100000, 'tooltip': 'Set the frequency of a Square Wave(SQR1)'},
        'PV1': {'min': -5, 'max': 5, 'tooltip': 'Set the voltage of Programmable Voltage #1(PV1)'},
        'PV2': {'min': -3.3, 'max': 3.3, 'tooltip': 'Set the voltage of Programmable Voltage #2(PV2)'},
        'PV3': {'min': 0, 'max': 3.3, 'tooltip': 'Set the voltage of Programmable Voltage #3(PV3)'},
        'PCS': {'min': 0, 'max': 2,
                'tooltip': 'Set the current of Programmable Current source(PCS)\nSubject to load resistance!'},
    }

    def __init__(self):
        sys.path.append('/usr/share/pslab')

    def enableShortcuts(self):
        """
        Enable the following shortcuts :

        * CTRL-S : Opens the saveData window for saving trace data . It will load the coordinate data from all curves created using :func:`addCurve`

        """

        self.saveSignal = QtGui.QShortcut(
            QtGui.QKeySequence(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+S", None)), self)
        self.saveSignal.activated.connect(self.saveData)

    def applySIPrefix(self, value, unit='', precision=2):
        """
        Convert a given value into scientific notation

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        value            The number to convert into a human readable form
        unit             SI units to suffix. Leave blank if not needed
        precision        Decimal precision digits
        ===============  ============================================================================================

        .. code-block:: python

            applySIPrefix(1010,'Hz')
            >>> 1.01kHz

        """

        neg = False
        if value < 0.:
            value *= -1
            neg = True
        elif value == 0.:
            return '0 '  # mantissa & exponnt both 0
        exponent = int(np.log10(value))
        if exponent > 0:
            exponent = (exponent // 3) * 3
        else:
            exponent = (-1 * exponent + 3) // 3 * (-3)

        value *= (10 ** (-exponent))
        if value >= 1000.:
            value /= 1000.0
            exponent += 3
        if neg:
            value *= -1
        exponent = int(exponent)
        PREFIXES = "yzafpnum kMGTPEZY"
        prefix_levels = (len(PREFIXES) - 1) // 2
        si_level = exponent // 3
        if abs(si_level) > prefix_levels:
            raise ValueError("Exponent out range of available prefixes.")
        return '%.*f %s%s' % (precision, value, PREFIXES[si_level + prefix_levels], unit)

    class utils:
        def __init__(self):
            pass

        def applySIPrefix(self, value, unit='', precision=2):
            neg = False
            if value < 0.:
                value *= -1
                neg = True
            elif value == 0.:
                return '0 '  # mantissa & exponnt both 0
            exponent = int(np.log10(value))
            if exponent > 0:
                exponent = (exponent // 3) * 3
            else:
                exponent = (-1 * exponent + 3) // 3 * (-3)

            value *= (10 ** (-exponent))
            if value >= 1000.:
                value /= 1000.0
                exponent += 3
            if neg:
                value *= -1
            exponent = int(exponent)
            PREFIXES = "yzafpnum kMGTPEZY"
            prefix_levels = (len(PREFIXES) - 1) // 2
            si_level = exponent // 3
            if abs(si_level) > prefix_levels:
                raise ValueError("Exponent out range of available prefixes.")
            return '%.*f %s%s' % (precision, value, PREFIXES[si_level + prefix_levels], unit)

    def __importGL__(self):
        print('importing opengl')
        import pyqtgraph.opengl as gl
        self.gl = gl

    def updateViews(self, plot):
        for a in plot.viewBoxes:
            a.setGeometry(plot.getViewBox().sceneBoundingRect())
            a.linkedViewChanged(plot.plotItem.vb, a.XAxis)

    def setColorSchemeWhite(self):
        """
        Set the plot background to white . This will also automatically change trace colours.
        """
        self.properties['colorScheme'] = 'white'
        for plot in self.plots2D:
            try:
                plot.setBackground((252, 252, 245, 255))
            except:
                pass

            for a in ['left', 'bottom', 'right']:
                try:
                    axis = plot.getAxis(a)
                    axis.setPen('k')
                except:
                    pass

            n = 0
            if isinstance(plot, pg.widgets.PlotWidget.PlotWidget):  # Only consider curves part of the main left axis
                for c in self.plots2D[plot]:  # Change curve colors to match white background
                    c.setPen(color=self.white_trace_colors[n], width=3)
                    n += 1
                    if (n == 54): break

                try:
                    for d in self.plots2D[plot].viewBoxes:  # Go through the additional axes too
                        for f in self.plots2D[d]:
                            f.setPen(color=self.white_trace_colors[n], width=3)
                            n += 1
                            if (n == 54): break
                except:
                    pass

                try:
                    for d in plot.axisItems:  # Go through any additional axes, and set colors there too
                        d.setPen('k')
                except Exception as ex:
                    print('error while changing scheme', ex)

    def rightClickToZoomOut(self, plot):
        """
        Enables zooming out when the user presses the right mouse button on the plot

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             The plot to activate this feature on
        ===============  ============================================================================================
        """

        clickEvent = functools.partial(self.autoRangePlot, plot)
        return pg.SignalProxy(plot.scene().sigMouseClicked, rateLimit=60, slot=clickEvent)

    def autoRangePlot(self, plot, evt):
        pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
        if plot.sceneBoundingRect().contains(pos) and evt[0].button() == QtCore.Qt.RightButton:
            plot.enableAutoRange(True, True)

    def enableCrossHairs(self, plot, curves=[]):
        """
        Enables crosshairs on the specified plot

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             The plot to activate this feature on
        ===============  ============================================================================================
        """

        plot.setTitle('')
        vLine = pg.InfiniteLine(angle=90, movable=False, pen=[100, 100, 200, 200])
        plot.addItem(vLine, ignoreBounds=True)
        hLine = pg.InfiniteLine(angle=0, movable=False, pen=[100, 100, 200, 200])
        plot.addItem(hLine, ignoreBounds=True)
        plot.hLine = hLine
        plot.vLine = vLine
        crossHairPartial = functools.partial(self.crossHairEvent, plot)
        proxy = pg.SignalProxy(plot.scene().sigMouseClicked, rateLimit=60, slot=crossHairPartial)
        plot.proxy = proxy
        plot.mousePoint = None

    def crossHairEvent(self, plot, evt):
        pos = evt[0].scenePos()  ## using signal proxy turns original arguments into a tuple
        if plot.sceneBoundingRect().contains(pos):
            plot.mousePoint = plot.getPlotItem().vb.mapSceneToView(pos)
            plot.vLine.setPos(plot.mousePoint.x())
            plot.hLine.setPos(plot.mousePoint.y())

    def displayCrossHairData(self, plot, fmode, ns, tg, axes, cols):
        """
        .. warning:: beta function to extract specific coordinate data from curves , and show them as the plot title

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             The plot to activate this feature on
        fmode            Set to True if fourier transform mode is active
        ns               Number of samples
        tg               time gap
        axes             axes
        cols             list of trace colours
        ===============  ============================================================================================
        """

        if plot.mousePoint:
            if fmode:
                index = int(ns * plot.mousePoint.x() * tg / 1e6)
            else:
                index = int(plot.mousePoint.x() * 1e6 / tg)

            maxIndex = ns
            if index > 0 and index < maxIndex:
                coords = "<span style='color: rgb(255,255,255)'>%s</span>," % self.applySIPrefix(index * tg / 1e6, 'S')
                for col, a in zip(cols, axes):
                    try:
                        coords += "<span style='color: rgb%s'>%0.3fV</span>," % (col, a[index])
                    except:
                        pass
                # self.coord_label.setText(coords)
                plot.plotItem.titleLabel.setText(coords)
            else:
                plot.plotItem.titleLabel.setText('')
                plot.vLine.setPos(-1)
                plot.hLine.setPos(-1)

    def setColorSchemeBlack(self):
        """
        Changes plot background to black. Also changes plot colours
        """

        self.properties['colorScheme'] = 'black'
        for plot in self.plots2D:
            try:
                plot.setBackground((0, 0, 0, 255))
            except:
                pass
            for a in ['left', 'bottom', 'right']:
                try:
                    axis = plot.getAxis(a)
                    axis.setPen('w')
                except:
                    pass

            n = 0
            if isinstance(plot, pg.widgets.PlotWidget.PlotWidget):  # Only consider curves part of the main left axis
                for c in self.plots2D[plot]:  # Change curve colors to match black background
                    c.setPen(color=self.black_trace_colors[n], width=2)
                    n += 1
                    if (n == 54): break

                try:
                    for d in self.plots2D[plot].viewBoxes:  # Go through the additional axes too
                        for f in self.plots2D[d]:
                            f.setPen(color=self.black_trace_colors[n], width=2)
                            n += 1
                            if (n == 54): break
                except:
                    pass

                try:
                    for d in plot.axisItems:  # Go through any additional axes, and set colors there too
                        d.setPen('w')
                except Exception as ex:
                    print('error while changing scheme', ex)

                for c in self.plots2D[plot]:  # Change curve colors to match black background
                    c.setPen(color=self.black_trace_colors[n], width=3)
                    n += 1
                    if (n == 54): break

    def random_color(self):
        """
        Generate a random colour

        :return: QtGui.QColor object
        """

        c = QtGui.QColor(random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        if np.average(c.getRgb()) < 150:
            c = self.random_color()
        return c

    def add2DPlot(self, plot_area, **args):
        """
        Add a 2D plot to a specified Qt Layout

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot_area        QtGui.<some layout> to add a 2D plot to
        ===============  ============================================================================================

        :return: pyqtgraph.PlotWidget
        """

        plot = pg.PlotWidget(**args)
        plot.setMinimumHeight(250)
        plot_area.addWidget(plot)

        plot.getAxis('left').setGrid(170)
        plot.getAxis('bottom').setGrid(170)

        plot.viewBoxes = []
        plot.axisItems = []
        self.plots2D[plot] = []
        if self.properties['colorScheme'] == 'white':
            self.setColorSchemeWhite()
        return plot

    def add3DPlot(self, plot_area):
        """
        Add a 3D plot to a specified Qt Layout

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot_area        QtGui.<some layout> to add a 3D plot to
        ===============  ============================================================================================

        :return: pyqtgraph.gl.GLViewWidget
        """
        if not self.gl: self.__importGL__()
        plot3d = self.gl.GLViewWidget()
        # gx = self.gl.GLGridItem();gx.rotate(90, 0, 1, 0);gx.translate(-10, 0, 0);self.plot.addItem(gx)
        # gy = self.gl.GLGridItem();gy.rotate(90, 1, 0, 0);gy.translate(0, -10, 0);self.plot.addItem(gy)
        gz = self.gl.GLGridItem();  # gz.translate(0, 0, -10);
        plot3d.addItem(gz);
        plot3d.opts['distance'] = 40
        plot3d.opts['elevation'] = 5
        plot3d.opts['azimuth'] = 20
        plot3d.setMinimumHeight(250)
        plot_area.addWidget(plot3d)
        self.plots3D[plot3d] = []
        plot3d.plotLines3D = []
        return plot3d

    def addCurve(self, plot, name='', **kwargs):
        """
        Add a new curve to a 2D plot

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             QPlotWidget created using :func:`add2DPlot`
        name             something to call this trace. Shown in the legend too
        ===============  ============================================================================================

        :return: pyqtgraph.PlotDataItem
        """
        # if(len(name)):curve = pg.PlotDataItem(name=name)
        curve = pg.PlotCurveItem(name=name, **kwargs)
        plot.addItem(curve)
        if self.properties['colorScheme'] == 'white':
            curve.setPen(kwargs.get('pen', {'color': self.white_trace_colors[len(self.plots2D[plot])], 'width': 1}))
        elif self.properties['colorScheme'] == 'black':
            curve.setPen(kwargs.get('pen', {'color': self.black_trace_colors[len(self.plots2D[plot])], 'width': 1}))
        # print (self.black_trace_colors[len(self.plots2D[plot])] , len(self.plots2D[plot]) )
        self.plots2D[plot].append(curve)
        return curve

    def removeCurve(self, plot, curve):
        """
        Remove a curve from a plot

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             pyqtgraph.PlotWidget created using :func:`add2DPlot`
        name             pyqtgraph.PlotDataItem created for the specified plot using :func:`addCurve`
        ===============  ============================================================================================

        """
        plot.removeItem(curve)
        try:
            self.plots2D[plot].pop(self.plots2D[plot].index(curve))
        except:
            pass

    def rebuildLegend(self, plot):
        return plot.addLegend(offset=(-10, 30))

    def renameLegendItem(self, legend, oldName, newName):
        """
        Renames one item from the legend.

        ==============  ========================================================
        **Arguments:**
        legend          legendItem
        name			name of the entry
        ==============  ========================================================
        """
        for sample, label in legend.items:
            if label.text == oldName:  # hit
                label.setText(newName)
                legend.updateSize()  # redraw box
                return

    def fetchColumns(self, qtablewidget, *args):
        """
        Fetch columns from a QTableWidget

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        qtablewidget     Widget in question
        *args            columns numbers
        ===============  ============================================================================================

        :return: 2D array of requested elements [[col1R0,col1,R1,col1,R3...col1Rn],[col2R0,col2,R1,col2,R3...col2Rn], ...]
        """
        data = [[] for a in range(len(args))]
        pos = 0
        for col in args:
            for row in range(50):
                item = qtablewidget.item(row, col)
                if item:
                    try:
                        data[pos].append(float(item.text()))
                    except:
                        break
                else:
                    break
            pos += 1
        return data

    def fetchSelectedItemsFromColumns(self, qtablewidget, *args):
        data = [[] for a in range(len(args))]
        pos = 0
        for col in args:
            for row in range(50):
                item = qtablewidget.item(row, col)
                if item:
                    if item.isSelected():
                        try:
                            data[pos].append(float(item.text()))
                        except:
                            break
                else:
                    break
            pos += 1
        return data

    def newPlot(self, x, y, **args):
        self.plot_ext = pg.GraphicsWindow(title=args.get('title', ''))
        self.curve_ext = self.plot_ext.addPlot(title=args.get('title', ''), x=x, y=y, connect='finite')
        self.curve_ext.setLabel('bottom', args.get('xLabel', ''))
        self.curve_ext.setLabel('left', args.get('yLabel', ''))

    def addAxis(self, plot, **args):
        """
        Add an axis on the right side

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        plot             pyqtgraph.PlotWidget
        *args
        1. label         Label of the new axis
        ===============  ============================================================================================

        :return: pg.ViewBox
        """
        p3 = pg.ViewBox()
        ax3 = pg.AxisItem('right')
        plot.plotItem.layout.addItem(ax3, 2, 3 + len(plot.axisItems))
        plot.plotItem.scene().addItem(p3)
        ax3.linkToView(p3)
        p3.setXLink(plot.plotItem)
        ax3.setZValue(-10000)
        if args.get('label', False):
            ax3.setLabel(args.get('label', False), color=args.get('color', '#ffffff'))

        p3.setGeometry(plot.plotItem.vb.sceneBoundingRect())
        p3.linkedViewChanged(plot.plotItem.vb, p3.XAxis)
        ## Handle view resizing
        Callback = functools.partial(self.updateViews, plot)
        plot.getViewBox().sigStateChanged.connect(Callback)
        plot.viewBoxes.append(p3)
        plot.axisItems.append(ax3)
        self.plots2D[
            p3] = []  # TODO do not consider a new axis as a plot. simply make it a part of the axisItems array of the main plot
        return p3

    def enableRightAxis(self, plot):
        p = pg.ViewBox()
        plot.showAxis('right')
        plot.setMenuEnabled(False)
        plot.scene().addItem(p)
        plot.getAxis('right').linkToView(p)
        p.setXLink(plot)
        plot.viewBoxes.append(p)
        Callback = functools.partial(self.updateViews, plot)
        plot.getViewBox().sigStateChanged.connect(Callback)
        if self.properties['colorScheme'] == 'white':
            self.setColorSchemeWhite()
        self.plots2D[p] = []
        return p

    def updateViews(self, plot):
        for a in plot.viewBoxes:
            a.setGeometry(plot.getViewBox().sceneBoundingRect())
            a.linkedViewChanged(plot.plotItem.vb, a.XAxis)

    def loopTask(self, interval, func, *args):
        """
        Execute a function every 'interval' milliseconds

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        interval         Time delay between consecutive executions
        func             function to be run
        *args            arguments for that function. in order.
        ===============  ============================================================================================

        :return: the timer . You should store this if you will need to stop this event loop at some point

        .. code-block:: python

            tmr = loopTask(100,np.sin,np.pi/2)  #calculate sin(pi/2) every 100mS = 0.1 seconds
            #equivalent to :
            while True:
                np.sin(np.pi/2)
                time.sleep(0.1)

        """
        timer = QtCore.QTimer()
        timerCallback = functools.partial(func, *args)
        timer.timeout.connect(timerCallback)
        timer.start(interval)
        self.timers.append(timer)
        return timer

    def delayedTask(self, interval, func, *args):
        """
        Execute a function after 'interval' milliseconds

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        interval         Time delay before execution
        func             function to be run
        *args            arguments for that function. in order.
        ===============  ============================================================================================

        :return: the timer .

        .. code-block:: python

            tmr = delayedTask(5000,np.sin,np.pi/2)  #calculate sin(pi/2) after 5 seconds
            #equivalent to :
            time.sleep(5)
            np.sin(np.pi/2)

        """
        timer = QtCore.QTimer()
        timerCallback = functools.partial(func, *args)
        timer.singleShot(interval, timerCallback)
        self.timers.append(timer)

    def killAllTimers(self):
        """
        Stop all timers created using either :func:`delayedTask` or :func:`loopTask`
        """
        for a in self.timers:
            try:
                a.stop()
                self.timers.remove(a)
            except:
                pass

    def newTimer(self):
        """
        Create a QtCore.QTimer object and return it.
        A reference is also stored in order to keep track of it
        """

        timer = QtCore.QTimer()
        self.timers.append(timer)
        return timer

    def displayDialog(self, txt=''):
        """
        Show a pop up dialog with a message
        """

        QtGui.QMessageBox.about(self, 'Message', txt)

    class spinIcon(QtGui.QFrame, spinBox.Ui_Form, utils):
        """
        Create a widget with a number entry field, and an associated function that is called when the value of the field changes

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the value of the widget changes
        UNITS			 SI units of the entry field
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        LINK             Another function to which the return value of FUNC is passed when an event occurs
        MIN              minimum limit for the number entry
        MAX              maximum limit for the number entry
        ===============  ============================================================================================

        :return: the spin widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.spinIcon, self).__init__()
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))
            self.linkFunc = args.get('LINK', None)

            self.scale = args.get('SCALE_FACTOR', 1)

            self.spinBox.setMinimum(args.get('MIN', 0))
            self.spinBox.setMaximum(args.get('MAX', 100))

        def setValue(self, val):
            retval = self.func(val)
            # self.value.setText('%.3f %s '%(retval*self.scale,self.units))
            if isinstance(retval, numbers.Number):
                self.value.setText('%s' % (self.applySIPrefix(retval * self.scale, self.units)))
            else:
                self.value.setText(str(retval))
            if self.linkFunc:
                self.linkFunc(retval * self.scale, self.units)

    class doubleSpinIcon(QtGui.QFrame, doubleSpinBox.Ui_Form, utils):
        """
        Create a widget with a number entry field with decimal support, and an associated function that is called when the value of the field changes

        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the value of the widget changes
        UNITS			 SI units of the entry field
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        LINK             Another function to which the return value of FUNC is passed when an event occurs
        MIN              minimum limit for the number entry
        MAX              maximum limit for the number entry
        ===============  ============================================================================================

        :return: the double spin widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.doubleSpinIcon, self).__init__()
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))
            self.linkFunc = args.get('LINK', None)

            self.scale = args.get('SCALE_FACTOR', 1)

            self.doubleSpinBox.setMinimum(args.get('MIN', 0))
            self.doubleSpinBox.setMaximum(args.get('MAX', 100))

        def setValue(self, val):
            retval = self.func(val)
            if isinstance(retval, numbers.Number):
                self.value.setText('%s' % (self.applySIPrefix(retval * self.scale, self.units)))
            else:
                self.value.setText(str(retval))
            # self.value.setText('%.3f %s '%(retval*self.scale,self.units))
            if self.linkFunc:
                self.linkFunc(retval * self.scale, self.units)

    class dialIcon(QtGui.QFrame, dial.Ui_Form, utils):
        """
        Create a widget with a knob, and an associated function that is called when the knob is turned by the user

        .. figure:: images/dialIcon.png
            :align: left
            :figclass: align-center


        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the knob is turned
        UNITS			 SI units of the entry field
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        LINK             Another function to which the return value of FUNC is passed when an event occurs
        MIN              minimum limit for the knob
        MAX              maximum limit for the knob
        ===============  ============================================================================================

        :return: the spin widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.dialIcon, self).__init__()
            self.setupUi(self)
            self.linkFunc = args.get('LINK', None)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

            self.scale = args.get('SCALE_FACTOR', 1)

            self.dial.setMinimum(args.get('MIN', 0))
            self.dial.setMaximum(args.get('MAX', 100))

        def setValue(self, val):
            try:
                retval = self.func(val)
            except Exception as err:
                retval = 'err'

            if isinstance(retval, numbers.Number):
                self.value.setText('%s' % (self.applySIPrefix(retval * self.scale, self.units)))
                if self.linkFunc:
                    self.linkFunc(retval * self.scale, self.units)
            # self.linkObj.setText('%.3f %s '%(retval*self.scale,self.units))
            else:
                self.value.setText(str(retval))

    class dialAndDoubleSpinIcon(QtGui.QFrame, dialAndDoubleSpin.Ui_Form, utils):
        """
        Create a widget with a knob, and an associated function that is called when the knob is turned by the user.
        It also contains a number entry field connected to the knob if the user wishes to manually enter a value

        .. figure:: images/dialAndDoubleSpinIcon.png
            :align: left
            :figclass: align-center


        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the knob is turned
        UNITS			 SI units of the entry field
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        LINK             Another function to which the return value of FUNC is passed when an event occurs
        MIN              minimum limit for the knob
        MAX              maximum limit for the knob
        ===============  ============================================================================================

        :return: the widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.dialAndDoubleSpinIcon, self).__init__()
            self.linkFunc = args.get('LINK', None)
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            self.value.setSuffix(' ' + self.units)
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))
            self.dial.setMinimum(args.get('MIN', 0))
            self.dial.setMaximum(args.get('MAX', 100))
            self.value.setMinimum(args.get('MIN', 0))
            self.value.setMaximum(args.get('MAX', 100))

        def setValue(self, val):
            retval = self.func(val)
            self.value.setValue(retval)
            if self.linkFunc:
                self.linkFunc(retval, self.units)

        def setDoubleValue(self):
            try:
                retval = self.func(self.value.value())
                self.value.setValue(int(retval))
                self.dial.setValue(int(retval))
                if self.linkFunc:
                    self.linkFunc(retval, self.units)
            except:
                pass

    class buttonIcon(QtGui.QFrame, button.Ui_Form, utils):
        """
        Create a widget with a button, and an associated function that is called when the button is clicked.
        The return value of the function is shown in a label on the same widget

        .. figure:: images/buttonIcon.png
            :align: left
            :figclass: align-center


        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the button is clicked
        UNITS			 SI units used when the user clicks the button, and the results are displayed in the label
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        ===============  ============================================================================================

        :return: the widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.buttonIcon, self).__init__()
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def read(self):
            retval = self.func()
            if isinstance(retval, numbers.Number) and retval != np.Inf:
                self.value.setText('%s' % (self.applySIPrefix(retval, self.units)))
            else:
                self.value.setText(str(retval))

    class simpleButtonIcon(QtGui.QFrame, simpleButton.Ui_Form):
        def __init__(self, **args):
            super(utilitiesClass.simpleButtonIcon, self).__init__()
            self.setupUi(self)
            self.button.setText(args.get('TITLE', 'CLICK'))
            self.func = args.get('FUNC', None)
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def clicked(self):
            retval = self.func()
            self.value.setText(str(retval))

    class dualButtonIcon(QtGui.QFrame, dualButton.Ui_Form):
        """
        Create a widget with two buttons, and associated functions that are called when the buttons are clicked.
        The return values of the functions are not shown


        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        A                Text shown on button A
        B                Text shown on button B
        FUNCA            function to be run when the first button is clicked
        FUNCB            function to be run when the second button is clicked
        UNITS			 SI units used when the user clicks the button, and the results are displayed in the label
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        ===============  ============================================================================================

        :return: the widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.dualButtonIcon, self).__init__()
            self.setupUi(self)
            self.title.setText(args.get('TITLE', 'select'))
            self.funcA = args.get('FUNCA', None)
            self.funcB = args.get('FUNCB', None)
            self.buttonA.setText(args.get('A', 'A'))
            self.buttonB.setText(args.get('B', 'B'))
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def clickedA(self):
            retval = self.funcA()

        def clickedB(self):
            retval = self.funcB()

    class wideButtonIcon(QtGui.QFrame, widebutton.Ui_Form, utils):
        """
        Create a widget with a wide button, and an associated function that is called when the button is clicked.
        The return value of the function is shown in a giant label on the same widget

        .. figure:: images/wideButtonIcon.png
            :align: left
            :figclass: align-center


        .. tabularcolumns:: |p{3cm}|p{11cm}|

        ===============  ============================================================================================
        **Arguments**
        ===============  ============================================================================================
        *\*\kwargs
        TITLE            Text shown on the top section of the widget
        FUNC             function to be run when the button is clicked
        UNITS			 SI units used when the user clicks the button, and the results are displayed in the label
        TOOLTIP          text to be displayed when the mouse hovers over the widget
        ===============  ============================================================================================

        :return: the widget . You may add this to any layout


        """

        def __init__(self, **args):
            super(utilitiesClass.wideButtonIcon, self).__init__()
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def read(self):
            retval = self.func()
            try:
                if isinstance(retval, numbers.Number) and retval != np.Inf:
                    self.value.setText('%s' % (self.applySIPrefix(retval, self.units)))
                else:
                    self.value.setText(retval)
            except:
                self.value.setText(str(retval))

    class displayIcon(QtGui.QFrame, displayWidget.Ui_Form, utils):
        def __init__(self, **args):
            super(utilitiesClass.displayIcon, self).__init__()
            self.setupUi(self)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.units = args.get('UNITS', '')
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def setValue(self, retval):
            try:
                if isinstance(retval, numbers.Number):
                    self.value.setText('%s' % (self.applySIPrefix(retval, self.units)))
                else:
                    self.value.setText(retval)
            except:
                self.value.setText(str(retval))

    class selectAndButtonIcon(QtGui.QFrame, selectAndButton.Ui_Form, utils):
        def __init__(self, **args):
            super(utilitiesClass.selectAndButtonIcon, self).__init__()
            self.setupUi(self)
            self.linkFunc = args.get('LINK', None)
            self.name = args.get('TITLE', '')
            self.title.setText(self.name)
            self.func = args.get('FUNC', None)
            self.units = args.get('UNITS', '')
            self.button.setText(args.get('LABEL', 'Read'))
            self.optionBox.addItems(args.get('OPTIONS', []))
            if 'TOOLTIP' in args: self.widgetFrameOuter.setToolTip(args.get('TOOLTIP', ''))

        def read(self):
            retval = self.func(self.optionBox.currentText())
            # if abs(retval)<1e4 and abs(retval)>.01:self.value.setText('%.3f %s '%(retval,self.units))
            # else: self.value.setText('%.3e %s '%(retval,self.units))
            if isinstance(retval, numbers.Number) and retval != np.Inf:
                self.value.setText('%s' % (self.applySIPrefix(retval, self.units)))
            else:
                self.value.setText(str(retval))
            if self.linkFunc:
                self.linkFunc(retval)

    class gainIcon(QtGui.QFrame, gainWidget.Ui_Form, utils):
        def __init__(self, **args):
            super(utilitiesClass.gainIcon, self).__init__()
            self.setupUi(self)
            self.func = args.get('FUNC', None)
            self.linkFunc = args.get('LINK', None)
            self.msg = QtGui.QMessageBox()
            self.msg.setIcon(QtGui.QMessageBox.Information)
            self.msg.setWindowTitle("Set Input Attenuation")
            self.msg.setText("Note :");
            self.msg.setInformativeText("Please connect a 10MOhm resistor in series with this input")
            self.msg.setDetailedText(
                "Connecting a 10MOhm resistor in series with the channel causes an 11x attenuation.\nThe software automatically compensates for this, and assumes a +/-160V range \n")

        def setGainCH1(self, g):
            if (g == 8):
                self.msg.exec_()
            retval = self.func('CH1', g)
            if self.linkFunc:
                self.linkFunc(retval)

        def setGainCH2(self, g):
            if (g == 8):
                self.msg.exec_()
            retval = self.func('CH2', g)
            if self.linkFunc:
                self.linkFunc(retval)

    class gainIconCombined(QtGui.QFrame, gainWidgetCombined.Ui_Form, utils):
        def __init__(self, **args):
            super(utilitiesClass.gainIconCombined, self).__init__()
            self.setupUi(self)
            self.func = args.get('FUNC', None)
            self.linkFunc = args.get('LINK', None)

        def setGains(self, g):
            if (g == 8):
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setWindowTitle("Set Input Attenuation")
                msg.setText("Note :");
                msg.setInformativeText("Please connect a 10MOhm resistor in series on both inputs")
                msg.setDetailedText(
                    "Connecting a 10MOhm resistor in series with the channel causes an 11x attenuation.\nThe software automatically compensates for this, and assumes a +/-160V range \n")
                msg.exec_()
            self.func('CH1', g)
            retval = self.func('CH2', g)
            if self.linkFunc:
                self.linkFunc(retval)

    class pulseCounterIcon(QtGui.QFrame, pulseCounter.Ui_Form):
        def __init__(self, I):
            super(utilitiesClass.pulseCounterIcon, self).__init__()
            self.setupUi(self)
            self.readfn = I.readPulseCount
            self.resetfn = I.countPulses
            self.channelBox.addItems(I.allDigitalChannels)

        def read(self):
            retval = self.readfn()
            self.value.setText('%d' % (retval))

        def reset(self):
            chan = self.channelBox.currentText()
            if len(chan): self.resetfn(chan)

    class experimentIcon(QtGui.QPushButton):
        mouseHover = QtCore.pyqtSignal(str)

        def __init__(self, basepackage, name, launchfunc, *args):
            super(utilitiesClass.experimentIcon, self).__init__()
            self.setMouseTracking(True)
            self.name = name
            tmp = importlib.import_module(basepackage + '.' + name)
            genName = tmp.params.get('name', name)
            self.setText(genName)
            self.hintText = tmp.params.get('hint', 'No summary available')
            try:
                if 'local' in args:
                    imgloc = pkg_resources.resource_filename(basepackage + '.icons',
                                                             _fromUtf8(tmp.params.get('image', '')))
                else:
                    imgloc = pkg_resources.resource_filename('PSL_Resources.ICONS', _fromUtf8(tmp.params.get('image', '')))
            except:
                imgloc = ''
            self.hintText = '''
			<img src="%s" align="left" width="150" style="margin: 0 20"/><strong>%s</strong><br>%s
			''' % (imgloc, genName.replace('\n', ' '), self.hintText)
            self.func = launchfunc
            self.clicked.connect(self.func)
            self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred))
            self.setMaximumWidth(170)
            # self.setStyleSheet("border-image: url(%s) 0 0 0 0 stretch stretch;color:white;"%(pkg_resources.resource_filename('PSL_Apps.icons', _fromUtf8(tmp.params.get('image','') ))))
            self.setStyleSheet(
                "color:black;background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #bbb);")
            self.setMinimumHeight(50)  # 70)

        def enterEvent(self, event):
            self.mouseHover.emit(self.hintText)

        def leaveEvent(self, event):
            self.mouseHover.emit('')

    class experimentListItem(QtGui.QPushButton):
        mouseHover = QtCore.pyqtSignal(str)

        def __init__(self, basepackage, name, launchfunc):
            super(utilitiesClass.experimentListItem, self).__init__()
            self.setMouseTracking(True)
            self.name = name
            tmp = importlib.import_module(basepackage + '.' + name)
            genName = tmp.params.get('name', name)
            self.setText(genName)
            self.hintText = tmp.params.get('hint', 'No summary available')
            self.hintText = '''
			<p><strong>%s</strong>.</p>
			%s
			''' % (genName.replace('\n', ' '), self.hintText)
            self.func = launchfunc
            self.clicked.connect(self.func)
            self.setMinimumHeight(30)

        # self.setMaximumWidth(170)
        # self.setStyleSheet("border-image: url(%s) 0 0 0 0 stretch stretch;color:white;"%(pkg_resources.resource_filename(basepackage, _fromUtf8(tmp.params.get('image','') ))))

        def enterEvent(self, event):
            self.mouseHover.emit(self.hintText)

        def leaveEvent(self, event):
            self.mouseHover.emit('')

    class sineWidget(QtGui.QWidget, sineWidget.Ui_Form):
        def __init__(self, I):
            super(utilitiesClass.sineWidget, self).__init__()
            self.setupUi(self)
            self.I = I
            self.commandLinkButton.setVisible(False)  # TODO :
            self.modes = ['sine', 'tria']

        def loadSineTable(self):
            if self.I:
                from PSL_Apps.utilityApps import loadSineTable
                inst = loadSineTable.AppWindow(self, I=self.I)
                inst.show()
            else:
                print(self.setWindowTitle('Device Not Connected!'))

        def setSINE1(self, val):
            f = self.I.set_w1(val)
            self.WAVE1_FREQ.setText('%.2f' % (f))

        def setSINE2(self, val):
            f = self.I.set_w2(val)
            self.WAVE2_FREQ.setText('%.2f' % (f))

        def setSinePhase(self):
            freq1 = self.SINE1BOX.value()
            freq2 = self.SINE2BOX.value()
            phase = self.SINEPHASE.value()
            f = self.I.set_waves(freq1, phase, freq2)
            self.WAVE1_FREQ.setText('%.2f' % (f))
            self.WAVE2_FREQ.setText('%.2f' % (f))

        def setW1Type(self, val):
            self.I.load_equation('W1', self.modes[val])

        def setW2Type(self, val):
            self.I.load_equation('W2', self.modes[val])

    class sensorIcon(QtGui.QFrame, sensorWidget.Ui_Form):
        def __init__(self, cls, **kwargs):
            super(utilitiesClass.sensorIcon, self).__init__()
            self.cls = cls
            self.setupUi(self)
            self.hintLabel.setText(kwargs.get('hint', ''))
            self.func = cls.getRaw
            self.plotnames = cls.PLOTNAMES
            self.menu = self.PermanentMenu()
            self.menu.setMinimumHeight(25)
            self.sub_menu = QtGui.QMenu('%s:%s' % (hex(cls.ADDRESS), cls.name[:15]))
            for i in cls.params:
                mini = self.sub_menu.addMenu(i)
                for a in cls.params[i]:
                    Callback = functools.partial(getattr(cls, i), a)
                    mini.addAction(str(a), Callback)
            self.menu.addMenu(self.sub_menu)
            self.formLayout.insertWidget(0, self.menu)

        class PermanentMenu(QtGui.QMenu):
            def hideEvent(self, event):
                self.show()

        def read(self):
            retval = self.func()
            if not retval:
                self.resultLabel.setText('err')
                return
            res = ''
            for a in range(len(retval)):
                res += self.plotnames[a] + '\t%.3e\n' % (retval[a])
            self.resultLabel.setText(res)

    class pwmWidget(QtGui.QWidget, pwmWidget.Ui_Form):
        def __init__(self, I):
            super(utilitiesClass.pwmWidget, self).__init__()
            self.setupUi(self)
            self.I = I

        def setSQRS(self):
            P2 = self.SQR2P.value() / 360.
            P3 = self.SQR3P.value() / 360.
            P4 = self.SQR4P.value() / 360.
            D1 = self.SQR1DC.value()
            D2 = self.SQR2DC.value()
            D3 = self.SQR3DC.value()
            D4 = self.SQR4DC.value()

            retval = self.I.sqrPWM(self.SQRSF.value(), D1, P2, D2, P3, D3, P4, D4)
            try:
                self.SQRSF.setValue(retval)
            except Exception as e:
                print(e.message)

        def fireSQR1(self):
            if self.I:
                from PSL_Apps.utilityApps import firePulses
                inst = firePulses.AppWindow(self, I=self.I)
                inst.show()
            else:
                print(self.setWindowTitle('Device Not Connected!'))

    class voltWidget(QtGui.QWidget, voltWidget.Ui_Form, utils):
        def __init__(self, I):
            super(utilitiesClass.voltWidget, self).__init__()
            self.setupUi(self)

            self.I = I
            self.col1 = ['CH1', 'CH2', 'CH3']
            self.col2 = ['CAP', 'SEN', 'AN8']
            pos = 0
            for a, b in zip(self.col1, self.col2):
                item = QtGui.QTableWidgetItem();
                self.table.setItem(pos, 0, item);
                item.setText('%s' % a)
                item = QtGui.QTableWidgetItem();
                self.table.setItem(pos, 2, item);
                item.setText('%s' % b)

                item = QtGui.QTableWidgetItem();
                self.table.setItem(pos, 1, item);
                item.setText('')
                item = QtGui.QTableWidgetItem();
                self.table.setItem(pos, 3, item);
                item.setText('')

                pos += 1

        def read(self):
            pos = 0
            for a, b in zip(self.col1, self.col2):
                self.table.item(pos, 1).setText(self.applySIPrefix(self.I.get_average_voltage(a), 'V'))
                self.table.item(pos, 3).setText(self.applySIPrefix(self.I.get_average_voltage(b), 'V'))
                pos += 1

    class supplyWidget(QtGui.QWidget, supplyWidget.Ui_Form, utils):
        def __init__(self, I):
            super(utilitiesClass.supplyWidget, self).__init__()
            self.setupUi(self)
            self.I = I

        def setPV1(self, val):
            val = self.I.DAC.setVoltage('PV1', val)
            self.PV1_LABEL.setText(self.applySIPrefix(val, 'V'))

        def setPV2(self, val):
            val = self.I.DAC.setVoltage('PV2', val)
            self.PV2_LABEL.setText(self.applySIPrefix(val, 'V'))

        def setPV3(self, val):
            val = self.I.DAC.setVoltage('PV3', val)
            self.PV3_LABEL.setText(self.applySIPrefix(val, 'V'))

        def setPCS(self, val):
            val = self.I.DAC.setVoltage('PCS', val / 1.e3)
            self.PCS_LABEL.setText(self.applySIPrefix(val, 'A'))

    class setStateIcon(QtGui.QFrame, setStateList.Ui_Form):
        def __init__(self, **args):
            super(utilitiesClass.setStateIcon, self).__init__()
            self.setupUi(self)
            self.I = args.get('I', None)

        def toggle1(self, state):
            self.I.set_state(SQR1=state)

        def toggle2(self, state):
            self.I.set_state(SQR2=state)

        def toggle3(self, state):
            self.I.set_state(SQR3=state)

        def toggle4(self, state):
            self.I.set_state(SQR4=state)

    def addPV1(self, I, link=None):
        tmpfunc = functools.partial(I.DAC.__setRawVoltage__, 'PV1')
        a1 = {'TITLE': 'PV1', 'MIN': 0, 'MAX': 4095, 'FUNC': tmpfunc, 'UNITS': 'V',
              'TOOLTIP': 'Programmable Voltage Source 1'}
        if link: a['LINK'] = link
        return self.dialIcon(**a1)

    def addPV2(self, I, link=None):
        tmpfunc = functools.partial(I.DAC.__setRawVoltage__, 'PV2')
        a = {'TITLE': 'PV2', 'MIN': 0, 'MAX': 4095, 'FUNC': tmpfunc, 'UNITS': 'V',
             'TOOLTIP': 'Programmable Voltage Source 2'}
        if link: a['LINK'] = link
        return self.dialIcon(**a)

    def addPV3(self, I, link=None):
        tmpfunc = functools.partial(I.DAC.__setRawVoltage__, 'PV3')
        a = {'TITLE': 'PV3', 'MIN': 0, 'MAX': 4095, 'FUNC': tmpfunc, 'UNITS': 'V',
             'TOOLTIP': 'Programmable Voltage Source 3'}
        if link: a['LINK'] = link
        return self.dialIcon(**a)

    def addPCS(self, I, link=None):
        tmpfunc = functools.partial(I.DAC.__setRawVoltage__, 'PCS')
        a = {'TITLE': 'PCS', 'MIN': 0, 'MAX': 4095, 'FUNC': tmpfunc, 'UNITS': 'A',
             'TOOLTIP': 'Programmable Current Source'}
        if link: a['LINK'] = link
        return self.dialIcon(**a)

    def addVoltmeter(self, I, link=None):
        tmpfunc = functools.partial(I.get_voltage, samples=10)
        a = {'TITLE': 'VOLTMETER', 'FUNC': tmpfunc, 'UNITS': 'V', 'TOOLTIP': 'Voltmeter',
             'OPTIONS': I.allAnalogChannels}
        if link: a['LINK'] = link
        return self.selectAndButtonIcon(**a)

    def addW1(self, I, link=None):
        a = {'TITLE': 'Wave 1', 'MIN': 1, 'MAX': 5000, 'FUNC': I.set_w1, 'UNITS': 'Hz',
             'TOOLTIP': 'Frequency of waveform generator #1'}
        if link: a['LINK'] = link
        return self.dialAndDoubleSpinIcon(**a)

    def addW2(self, I, link=None):
        a = {'TITLE': 'Wave 2', 'MIN': 1, 'MAX': 5000, 'FUNC': I.set_w2, 'UNITS': 'Hz',
             'TOOLTIP': 'Frequency of waveform generator #2'}
        if link: a['LINK'] = link
        return self.dialAndDoubleSpinIcon(**a)

    def addSQR1(self, I, link=None):
        a = {'TITLE': 'SQR 1', 'MIN': 1, 'MAX': 100000, 'FUNC': I.sqr1, 'UNITS': 'Hz', 'TOOLTIP': 'Frequency of SQR1'}
        if link: a['LINK'] = link
        return self.dialAndDoubleSpinIcon(**a)

    def addTimebase(self, I, func):
        a = {'TITLE': 'TIMEBASE', 'MIN': 0, 'MAX': 9, 'FUNC': func, 'UNITS': 'S',
             'TOOLTIP': 'Set Timebase of the oscilloscope'}
        T2 = self.dialIcon(**a)
        T2.dial.setPageStep(1)
        T2.dial.setValue(0)
        return T2

    def addRes(self, I, wide=None):
        a = {'TITLE': 'RESISTANCE', 'FUNC': I.get_resistance, 'UNITS': u"\u03A9",
             'TOOLTIP': 'Read Resistance connected to SEN input '}
        if wide:
            T2 = self.wideButtonIcon(**a)
        else:
            T2 = self.buttonIcon(**a)
        return T2

    def addPauseButton(self, layout, func):
        freezeButton = QtGui.QCheckBox(self)
        freezeButton.setObjectName(_fromUtf8("freezeButton"))
        freezeButton.setText("Pause")
        layout.addWidget(freezeButton)
        QtCore.QObject.connect(freezeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), func)
        return freezeButton

    def addRegularButton(self, layout, func, name):
        Button = QtGui.QPushButton(self)
        Button.setObjectName(_fromUtf8("button"))
        Button.setText(name)
        layout.addWidget(Button)
        QtCore.QObject.connect(Button, QtCore.SIGNAL(_fromUtf8("clicked()")), func)
        return Button

    def addHelpImageToLayout(self, layout, filename):
        imgurl = pkg_resources.resource_filename('PSL_Resources.HTML.images', filename)
        return self.addPixMapToLayout(layout, QtGui.QPixmap(imgurl))

    def addPixMapToLayout(self, layout, pixmap):
        pic = QtGui.QLabel(self)
        pic.setGeometry(10, 10, 250, 120)
        self.setPixMapOnLabel(pic, pixmap)
        layout.addWidget(pic)
        return pic

    def setPixMapOnLabel(self, pic, pixmap):
        pic.setPixmap(pixmap.scaled(pic.size(), QtCore.Qt.KeepAspectRatio))

    def saveToCSV(self, table):
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '~/', 'CSV(*.csv)')
        sections = path.split('.')
        if (sections[-1] != 'csv'): path += '.csv'
        if path:
            import csv
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream)
                for row in range(table.rowCount()):
                    rowdata = []
                    for column in range(table.columnCount()):
                        item = table.item(row, column)
                        if item is not None:
                            rowdata.append(
                                unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)

    def saveDataWindow(self, curveList, plot=None):
        from utilityApps import plotSaveWindow
        info = plotSaveWindow.AppWindow(self, curveList, plot)
        info.show()

    def savePro(self):
        from os.path import expanduser
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save Profile', expanduser("./"), 'INI(*.ini)')
        if path:
            sections = path.split('.')
            if (sections[-1] != 'ini'): path += '.ini'
            saveProfile.guisave(self, QtCore.QSettings(path, QtCore.QSettings.IniFormat))

    def saveSelectedPro(self, parent):
        from os.path import expanduser
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save Profile', expanduser("./"), 'INI(*.ini)')
        sections = path.split('.')
        if (sections[-1] != 'ini'): path += '.ini'
        print('custom save', path)
        if path: saveProfile.guisave(parent, QtCore.QSettings(path, QtCore.QSettings.IniFormat))

    def loadPro(self):
        from os.path import expanduser
        filename = QtGui.QFileDialog.getOpenFileName(self, "Load a Profile", expanduser("."), 'INI(*.ini)')
        if filename:
            saveProfile.guirestore(self, QtCore.QSettings(filename, QtCore.QSettings.IniFormat))

    def getFile(self, filetype=None):
        from os.path import expanduser
        if filetype:
            filename = QtGui.QFileDialog.getOpenFileName(self, "Select File", expanduser("."))
        else:
            filename = QtGui.QFileDialog.getOpenFileName(self, "Select File", expanduser("."), filetype)
        return filename

    ######################### high level functions ##################################

    def addWG(self, I, widget, layout):
        studioCMDS = {'W1': self.addW1, 'W2': self.addW2, 'PV1': self.addPV1, 'PV2': self.addPV2, 'PV3': self.addPV3,
                      'PCS': self.addPCS, 'SQR1': self.addSQR1, 'VOLTMETER': self.addVoltmeter, 'OHMMETER': self.addRes}
        name = widget.get('name', None)
        TP = widget.get('type', None)
        if not TP or not name: return

        if TP in studioCMDS.keys():
            LINK = widget.get('LINK', None)
            if LINK:
                WG = studioCMDS[TP](I, LINK)
            else:
                WG = studioCMDS[TP](I)
            layout.addWidget(WG)
            self.studioWidgets[name] = WG
            return WG
        return None
