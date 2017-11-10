# PSLab-apps
GUI Experiments for PSLab from FOSSASIA 

[![Build Status](https://travis-ci.org/fossasia/pslab-desktop-apps.svg?branch=development)](https://travis-ci.org/fossasia/pslab-desktop-apps)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8259e5c2220f484e95a88cf4aaed1a96)](https://www.codacy.com/app/mb/pslab-apps?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/pslab-apps&amp;utm_campaign=Badge_Grade)

This repository is for Qt based applications for PSLab - GUI programs, widgets and templates for various experiments.
This is also installable on linux machine. 

The goal of PSLab is to create an Open Source hardware device (open on all layers) that can be used for experiments by teachers, students and citizen scientists. Our tiny pocket lab provides an array of sensors for doing science and engineering experiments. It provides functions of numerous measurement devices including an oscilloscope, a waveform generator, a frequency counter, a programmable voltage, current source and as a data logger.

We are developing the experiments starting on the hardware to libraries and user interfaces for desktop PCs and Android apps for smartphones. The PSLab project is inspired by the work of the Open Science Hardware community and the ExpEYES project. Our website is at: http://pslab.fossasia.org

### Communication

Please join us on the following channels:
* [Pocket Science Channel](https://gitter.im/fossasia/pslab)
* [Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia)

### Installation

#### Installing the manual way

To install PSLab on Debian based Gnu/Linux system, the following dependencies must be installed.

#### Dependencies

* PyQt 4.7+, PySide, or PyQt5
* python 2.6, 2.7, or 3.x
* NumPy, Scipy            &nbsp;   **Analytical tools and array manipulations**
* pyqt4-dev-tools         &nbsp;   **Contains Pyuic4 which compiles xml layout files into python template files**
* Pyqtgraph               &nbsp;   **Primary Plotting library**
* pyopengl and qt-opengl  &nbsp;   **For 3D graphics support in pyqtgraph**
* iPython-qtconsole       &nbsp;   **optional**


##### Now clone both the repositories [pslab-apps](https://github.com/fossasia/pslab-apps)  and [pslab](https://github.com/fossasia/pslab).


##### Libraries must be installed in following order :

1. pslab **(Python Communication Library)**
2. pslab-apps **(GUI for performing experiments)**

**Note**
*If user is only interested in using PSLab as an acquisition device without a display/GUI, only one repository  [pslab](https://github.com/fossasia/pslab) needs to be installed*


##### To install, cd into the directories

    $ cd <SOURCE_DIR>

and run the following (for both the repos)

    $ sudo make clean

    $ sudo make

    $ sudo make install

Now you are ready with the PSLab software on your machine :)

#### Install using the `installer.sh` script

Installation of PSLab desktop app is made easier using the `installer.sh` script. First you have to make the file an executable. Go to the directory where the `installer.sh` file is downloaded and then execute the following command.

```
sudo chmod +x installer.sh
```

This will ask for your password to proceed. Once it is completed, run the intaller by the following command;

```
sudo ./installer.sh
```

This will install the PSLab desktop application in the /opt/ directory. Once the installation is completed it will prompt to open the application. Press `Y` to launch PSLab desktop application for the first time or press `N` to exit the installer. 

-----------------------
For the main GUI (Control panel), you can run the Experiments app from the terminal.

    $ Experiments
If the device was not detected , the following splash screen error will be displayed on launch:
![](https://i1.wp.com/blog.fossasia.org/wp-content/uploads/2016/07/SplashNotConnected.png?w=625)

Under normal circumstances, the splash screen will be followed by the application's main window
![](https://i2.wp.com/blog.fossasia.org/wp-content/uploads/2016/07/SplashScreen.png?w=613)
![](https://i0.wp.com/blog.fossasia.org/wp-content/uploads/2016/07/controlpanel.png?w=455)


-----------------------

#### Development Environment

To set up the development environment, install the packages mentioned in dependencies. For building GUI's Qt Designer is used.

## Communicating with Pocket Science Lab via USB and understanding the various read/write functions

Design of PSLab combines the flexibility of Python programming language and the real-time measurement capability of micro-controllers.

PSLab, with its simple and open architecture allows users to use the tool for various measurements and to develop new experiments with simple functions written in python.

It is interfaced and powered by USB port of the computer. For connecting external signals it has several input/output terminals as shown in the following figure.
![](https://i2.wp.com/blog.fossasia.org/wp-content/uploads/2016/07/pslabdesign.png?resize=276%2C296)

### Interfacing with the real world. One small Python script at a time

### Example1.py : Connecting to the device , and read a voltage value from one of the analog inputs
```
>>> from PSL import sciencelab
>>> I = sciencelab.connect()     #Returns None if device isn't found
# An example function that measures voltage present at the specified analog input
>>> print I.get_average_voltage('CH1')
```

The module [sciencelab.py](https://github.com/fossasia/pslab/blob/master/PSL/sciencelab.py) contains all the functions required for communicating with PSLab hardware. It also contains some utility functions. The class `ScienceLab()` contains methods that can be used to interact with the PSLab. The `connect()` function returns an instance of this class if PSLab hardware is detected.
The ScienceLab class does the following crucial jobs during the creation of an instance.
+ Scan for ttyACM devices, and attempt to read device version if the vendor and product IDs match, and the device appears to be unopened by any other instance.
+ Load calibration constants, polynomials, and tables
+ Create a socket to indicate ownership of the device being used

Once the device has been succesfully opened, the instance of ScienceLab.py can be used to access its various features.
Here's an example script to read values from a magnetometer connected to the I2C port of the PSLab
```
>>> from PSL import sciencelab
>>> I = sciencelab.connect()     #Returns None if device isn't found
>>> from PSL.SENSORS import HMC5883L #A 3-axis magnetometer
>>> M = HMC5883L.connect(I.I2C)    #Specify that the I2C bridge is to be used
>>> Gx,Gy,Gz = M.getRaw()           #Returns three decimal numbers that indicate magnetic fields along orthogonal axes
```

### Example 3 : Capturing a sine wave, and plotting it using matplotlib

The function call that is used for acquisition 
`capture1(channel name,number of samples,time gap (uS) between samples, *optional keyword arguments)`
+ Channel name : Any one of the analog inputs available : 'CH1','CH2','CH3','MIC','SEN','CAP','AN8'
+ Number of samples : total voltage samples to read (Maximum 10000 samples)
+ time gap : The time delay between successive samples

```
>>> from PSL import sciencelab   #These first two lines are always used to create the instance, 
>>> I = sciencelab.connect()     #and will not be repeated in further examples.
>>> I.set_gain('CH1', 3) # set input CH1 to +/-4V range
>>> I.set_sine1(1000) # generate 1kHz sine wave on the waveform generator W1
>>> #USE A WIRE TO CONNECT W1 to CH1.
>>> x,y = I.capture1('CH1', 1000, 10) # measure the voltage at CH1 1000 times, with 10uS interval between successive samples
>>> from pylab import *    #Import the plotting library
>>> plot(x,y)                   #Plot the time axis against the voltage data
>>> show()                  #display the plot
```
The following image displays the plot output

![](https://i0.wp.com/blog.fossasia.org/wp-content/uploads/2016/08/sine1.png?resize=750%2C565)

### Example 4 : Capturing two sine waves, and plotting them
The function call that is used for acquisition 
`capture2(number of samples,time gap (uS) between samples, TraceOneRemap)`
+ Number of samples : total voltage samples to read (Maximum 5000 samples)
+ time gap : The time delay between successive samples
+ TraceOneRemap(optional) : This function returns data from CH1 and CH2 by default, but CH1 can be replaced by any one of the analog inputs available : 'CH1','CH2','CH3','MIC','SEN','CAP','AN8' . Channel 2 is always CH2

```
# -*- coding: utf-8 -*-

from pylab import *
from PSL import sciencelab
I=sciencelab.connect()
I.set_gain('CH1', 2) # set input CH1 to +/-4V range
I.set_gain('CH2', 3) # set input CH2 to +/-4V range
I.set_sine1(1000) # generate 1kHz sine wave on output W1
I.set_sine2(1000) # generate 1kHz sine wave on output W2
#Connect W1 to CH1, and W2 to CH2. W1 can be attenuated using the manual amplitude knob on the PSlab
x,y1,y2 = I.capture2(1600,1.75,'CH1') 
plot(x,y1) #Plot of analog input CH1
plot(x,y2) #plot of analog input CH2
show()
```

Resultant plot :

![](https://i0.wp.com/blog.fossasia.org/wp-content/uploads/2016/08/sine2.png?resize=750%2C565)


### Example 5 : Capturing four oscilloscope traces simultaneously from various analog inputs
The function call that is used for acquisition 
`capture4(number of samples,time gap (uS) between samples, TraceOneRemap)`
+ Number of samples : total voltage samples to read (Maximum 2500 samples)
+ time gap : The time delay between successive samples. Minimum 2uS, Maximum 8000
+ TraceOneRemap(optional) : This function returns data from CH1,CH2,CH3,MIC by default, but CH1 can be replaced by any one of the analog inputs available : 'CH1','CH2','CH3','MIC','SEN','CAP','AN8' . the other three channels are fixed

```
# -*- coding: utf-8 -*-

from pylab import *
from PSL import sciencelab
I=sciencelab.connect()
I.set_gain('CH1', 2) # set input CH1 to +/-4V range
I.set_gain('CH2', 3) # set input CH2 to +/-4V range
I.set_sine1(1000) # generate 1kHz sine wave on output W1
I.set_sine2(1000) # generate 1kHz sine wave on output W2
I.sqr1(2000,duty_cycle=50) # generate 1kHz square wave on output SQR1
#Connect SQR1 to CH1
#Connect W1 to CH2, and W2 to CH3. W1 can be attenuated using the manual amplitude knob on the PSlab
x,y1,y2,y3,y4 = I.capture4(1600,1.75,'CH1')
plot(x,y1) #Plot of analog input CH1
plot(x,y2) #plot of analog input CH2
plot(x,y3) #plot of analog input CH3
plot(x,y4) #plot of analog input CH4 : MIC
show()
```

Resultant plot :

![](https://i2.wp.com/blog.fossasia.org/wp-content/uploads/2016/08/waves.png?resize=750%2C565)


### You can help
```
Please report a bug/install errors here 
Your suggestions to improve PSLab are welcome :)
```

### Blog posts related to PSLab on FOSSASIA blog 
* [Installation of PSLab](http://blog.fossasia.org/pslab-code-repository-and-installation/)
* [Communicating with PSLab](http://blog.fossasia.org/communicating-with-pocket-science-lab-via-usb-and-capturing-and-plotting-sine-waves/)
* [New Tools and Sensors for Fossasia PSLab and ExpEYES](http://blog.fossasia.org/new-tools-and-sensors-fossasia-pslab-and-expeyes/) 
