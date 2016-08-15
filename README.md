# PSLab-apps
GUI Experiments for PSLab from FOSSASIA 

[![Build Status](https://travis-ci.org/fossasia/pslab-apps.svg?branch=development)](https://travis-ci.org/fossasia/pslab-apps)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8259e5c2220f484e95a88cf4aaed1a96)](https://www.codacy.com/app/mb/pslab-apps?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/pslab-apps&amp;utm_campaign=Badge_Grade)

This repository is for Qt based applications for PSLab - GUI programs, widgets and templates for various experiments.
This is also installable on linux machine. 

* The project is inspired from ExpEYES  http://expeyes.in
* FOSSASIA is supporting development and promotion of ExpEYES project since 2014 mainly through Google Summer of Code
* The current work is a part of my GSoC-16 project

##Communication
Chat: [Pocket Science Slack Channel](http://fossasia.slack.com/messages/pocketscience/) | [Get an Invite](http://fossasia-slack.herokuapp.com/)

----------------

Installation
------------

To install PSLab on Debian based Gnu/Linux system, the following dependencies must be installed.

####Dependencies

* PyQt 4.7+, PySide, or PyQt5
* python 2.6, 2.7, or 3.x
* NumPy, Scipy
* pyqt4-dev-tools         &nbsp;   #for pyuic4
* Pyqtgraph               &nbsp;  #Plotting library
* pyopengl and qt-opengl  &nbsp;   #for 3D graphics
* iPython-qtconsole       &nbsp;   #optional


#####Now clone both the repositories [pslab-apps](https://github.com/fossasia/pslab-apps)  and [pslab](https://github.com/fossasia/pslab).


#####Libraries must be installed in ~~the following order~~  any order

1. pslab-apps
2. pslab

**Note**
*If user is only interested in using PSLab as an acquisition device without a display/GUI, only [pslab](https://github.com/fossasia/pslab) needs to be installed*


#####To install, cd into the directories

`$ cd <SOURCE_DIR>`

and run the following (for both the repos)

`$ sudo make clean`

`$ sudo make` 

`$ sudo make install`

Now you are ready with the PSLab software on your machine :)

For the main GUI (Control panel), you can run Experiments from the terminal.

`$ Experiments`

-----------------------

####Development Environment

To set up the development environment, install the packages mentioned in dependencies. For building GUI's Qt Designer is used.

