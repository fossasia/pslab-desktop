#!/usr/bin/env bash
pyuic5 -x analogScope.ui -o auto_analogScope.py
pyuic5 -x arbitStream.ui -o auto_arbitStream.py
pyuic5 -x digitalScope.ui -o auto_digitalScope.py
pyuic5 -x digitalScopeNoTrig.ui -o auto_digitalScopeNoTrig.py
pyuic5 -x sensorGrid.ui -o auto_sensorGrid.py
pyuic5 -x sensorTemplate.ui -o auto_sensorTemplate.py
pyuic5 -x wirelessTemplate.ui -o auto_wirelessTemplate.py

