#!/usr/bin/env bash
pyuic5 -x ADS1115calibrator.ui -o auto_ADS1115calibrator.py
pyuic5 -x arbitStream.ui -o auto_arbitStream.py
pyuic5 -x calibration_loader.ui -o auto_calibration_loader.py
pyuic5 -x calibrator.ui -o auto_calibrator.py
pyuic5 -x hackYourOwn.ui -o auto_hackYourOwn.py
pyuic5 -x remote.ui -o auto_remote.py