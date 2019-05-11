#!/usr/bin/env bash
# UIs in template directory
pyuic5 -x controlWidgets.ui -o auto_controlWidgets.py
pyuic5 -x designer.ui -o auto_designer.py
pyuic5 -x graph_and_sheet.ui -o auto_graph_and_sheet.py
pyuic5 -x icon.ui -o auto_icon.py
pyuic5 -x nodeList.ui -o auto_nodeList.py
pyuic5 -x rectifier.ui -o auto_rectifier.py
pyuic5 -x scope.ui -o auto_scope.py
pyuic5 -x sensors.ui -o auto_sensors.py
pyuic5 -x simplePendulum.ui -o auto_simplePendulum.py
pyuic5 -x simpleTemplate.ui -o auto_simpleTemplate.py
pyuic5 -x single_col_exp.ui -o auto_single_col_exp.py
pyuic5 -x stepper.ui -o auto_stepper.py
pyuic5 -x template_bandpass.ui -o auto_template_bandpass.py
pyuic5 -x template_experiments.ui -o auto_template_experiments.py
pyuic5 -x template_graph_nofft.ui -o auto_template_graph_nofft.py
pyuic5 -x template_graph.ui -o auto_template_graph.py
pyuic5 -x twit.ui -o auto_twit.py
pyuic5 -x widget_layout.ui -o auto_widget_layout.py

# UIs in widget directory
cd widgets/
pyuic5 -x spinBox.ui -o auto_spinBox.py
pyuic5 -x dial.ui -o auto_dial.py
pyuic5 -x widebutton.ui -o auto_widebutton.py
pyuic5 -x dialAndDoubleSpin.ui -o auto_dialAndDoubleSpin.py
pyuic5 -x customFunc.ui -o auto_customFunc.py
pyuic5 -x pwmWidget.ui -o auto_pwmWidget.py
pyuic5 -x sineWidget.ui -o auto_sineWidget.py
pyuic5 -x sweepTitle.ui -o auto_sweepTitle.py
pyuic5 -x dualButton.ui -o auto_dualButton.py
pyuic5 -x sweep.ui -o auto_sweep.py
pyuic5 -x gainWidgetCombined.ui -o auto_gainWidgetCombined.py
pyuic5 -x clicking.ui -o auto_clicking.py
pyuic5 -x sensorWidget.ui -o auto_sensorWidget.py
pyuic5 -x displayWidget.ui -o auto_displayWidget.py
pyuic5 -x customSweep.ui -o auto_customSweep.py
pyuic5 -x gainWidget.ui -o auto_gainWidget.py
pyuic5 -x selectAndButton.ui -o auto_selectAndButton.py
pyuic5 -x pulseCounter.ui -o auto_pulseCounter.py
pyuic5 -x button.ui -o auto_button.py
pyuic5 -x simpleButton.ui -o auto_simpleButton.py
pyuic5 -x setStateList.ui -o auto_setStateList.py
pyuic5 -x customSensor.ui -o auto_customSensor.py
pyuic5 -x interactivePlot.ui -o auto_interactivePlot.py
pyuic5 -x nodeList.ui -o auto_nodeList.py
pyuic5 -x doubleSpinBox.ui -o auto_doubleSpinBox.py
pyuic5 -x supplyWidget.ui -o auto_supplyWidget.py
pyuic5 -x voltWidget.ui -o auto_voltWidget.py

cd ..
