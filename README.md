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

To install PSLab on Debian based Gnu/Linux system, the following dependencies must be installed.

#### Dependencies

* PyQt 4.7+, PySide, or PyQt5
* python 2.6, 2.7, or 3.x
* NumPy, Scipy            &nbsp;   ** Analytical tools and array manipulations**
* pyqt4-dev-tools         &nbsp;   **Contains Pyuic4 which compiles xml layout files into python template files**
* Pyqtgraph               &nbsp;  **Primary Plotting library**
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

### You can help
```
Please report a bug/install errors here 
Your suggestions to improve PSLab are welcome :)
```

### Blog posts related to PSLab on FOSSASIA blog 
* [Installation of PSLab](http://blog.fossasia.org/pslab-code-repository-and-installation/)
* [Communicating with PSLab](http://blog.fossasia.org/communicating-with-pocket-science-lab-via-usb-and-capturing-and-plotting-sine-waves/)
* [New Tools and Sensors for Fossasia PSLab and ExpEYES](http://blog.fossasia.org/new-tools-and-sensors-fossasia-pslab-and-expeyes/) 
