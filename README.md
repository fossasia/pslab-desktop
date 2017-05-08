# PSLab-apps
GUI Experiments for PSLab from FOSSASIA 

[![Build Status](https://travis-ci.org/fossasia/pslab-desktop-apps.svg?branch=development)](https://travis-ci.org/fossasia/pslab-desktop-apps)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8259e5c2220f484e95a88cf4aaed1a96)](https://www.codacy.com/app/mb/pslab-apps?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/pslab-apps&amp;utm_campaign=Badge_Grade)

This repository is for Qt based applications for PSLab - GUI programs, widgets and templates for various experiments.
This is also installable on linux machine. 

* The project is inspired from ExpEYES  http://expeyes.in
* FOSSASIA is supporting development and promotion of ExpEYES project since 2014 mainly through Google Summer of Code
* The current work is a part of my GSoC-16 project

### Communication

Please join us on the following channels:
* [Pocket Science Channel](https://gitter.im/fossasia/pslab)
* [Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia)

Our website is at: http://pslab.fossasia.org

### Installation

To install PSLab on Debian based Gnu/Linux system, the following dependencies must be installed.

#### Dependencies

* PyQt 4.7+, PySide, or PyQt5
* python 2.6, 2.7, or 3.x
* NumPy, Scipy
* pyqt4-dev-tools         &nbsp;   **For pyuic4**
* Pyqtgraph               &nbsp;  **For Plotting library**
* pyopengl and qt-opengl  &nbsp;   **For 3D graphics**
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

For the main GUI (Control panel), you can run Experiments from the terminal.

    $ Experiments

-----------------------

#### Development Environment

To set up the development environment, install the packages mentioned in dependencies. For building GUI's Qt Designer is used.

### Blog posts related to PSLab on FOSSASIA blog 
* [Installation of PSLab](http://blog.fossasia.org/pslab-code-repository-and-installation/)
* [Communicating with PSLab](http://blog.fossasia.org/communicating-with-pocket-science-lab-via-usb-and-capturing-and-plotting-sine-waves/)
* [New Tools and Sensors for Fossasia PSLab and ExpEYES](http://blog.fossasia.org/new-tools-and-sensors-fossasia-pslab-and-expeyes/) 
