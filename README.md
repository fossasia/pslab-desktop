# PSLab Desktop :gemini:

Electron desktop application for an awesome open-hardware platform. Made with love :purple_heart:

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/pslab)

[![Build Status](https://travis-ci.org/fossasia/pslab-desktop.svg?branch=v2)](https://travis-ci.org/fossasia/pslab-desktop)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8259e5c2220f484e95a88cf4aaed1a96)](https://www.codacy.com/app/mb/pslab-desktop?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/pslab-desktop&amp;utm_campaign=Badge_Grade)
[![Mailing List](https://img.shields.io/badge/Mailing%20List-FOSSASIA-blue.svg)](https://groups.google.com/forum/#!forum/pslab-fossasia)
[![Twitter Follow](https://img.shields.io/twitter/follow/pslabio.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/pslabio)
[![pslab](https://snapcraft.io/pslab/badge.svg)](https://snapcraft.io/pslab)

<a href="https://pslab.io/" rel="some text">![PSLab Banner](./docs/project_banner.png)</a>  
This project is a reimplementation of the PSLab Desktop orginally developed using the python stack. As of now, we are working on replicating features of the android app one by one.

The goal of PSLab is to create an Open Source hardware device (open on all layers) that can be used for experiments by teachers, students and citizen scientists. Our tiny pocket lab provides an array of sensors for doing science and engineering experiments. It provides functions of numerous measurement devices including an oscilloscope, a waveform generator, a frequency counter, a programmable voltage, current source and as a data logger.

We are developing the experiments starting on the hardware to libraries and user interfaces for desktop PCs and Android apps for smartphones. The PSLab project is inspired by the work of the Open Science Hardware community and the ExpEYES project. Our website is at: https://pslab.io

### Communication

Please join us on the following channels:
* [Pocket Science Channel](https://gitter.im/fossasia/pslab)
* [Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia)

***

# How to contribute
In order to contribute, we would recommend you to first read the [community guidelines](https://blog.fossasia.org/open-source-developer-guide-and-best-practices-at-fossasia/) as stated by FOSSASIA.

## Setup  :metal:
1. Fork the project to get a copy of the repository in your github profile.
2. Clone the copied project from your profile ( Not the original repository from FOSSASIA ).
3. ```cd``` into your project folder.
4. ```git remote add upstream https://github.com/fossasia/pslab-desktop.git``` This command will set up the upsteam link.

## Installing development dependencies :snowflake:
While in your project folder
```bash
npm install
```
This command will install all the necessary dependencies required by the electron app to run.  
  
As this app uses the **PSL** library under the hood for device communication, you'll have to install it as well.
The instructions to install it are provided [here](https://github.com/fossasia/pslab-python).
After installation of **PSL** make sure you can property import it in **Python3**. Run the following command in your bash shell.
```bash
python3
>>> from PSL import sciencelab
```
If this command runs without throwing an error, then we are good to go.

## Starting the app ( development ) :zap:
Everything command to start and debug the app are writen in package.json. To simply get it running run the following command while in your project repository.
```bash
npm start
```
And wait for the electron shell to open. 
Happy coding!  :fire:
  
*** 
		  
# Generating production build
Currently the build pipeline spits a **debian** and a **snap** file that can be installed on any debian based distro

## Build Step for Linux ( Debian bases OS ) :beginner:
While in the project root  
```bash
npm run build-linux
```  
## Build Step for Windows :beginner:
While in the project root  
```bash
npm run build-windows
```
This command will produce a **build** and a **dist** directory inside the project folder. The **build** folder contains the optimized react files, while the **dist** folder contains the final electron installers. 

---

## Build Step for universal platforms :beginner:
While in the project root  
```bash
npm run build
```
This will generate installers both for linux and windows in one step.

To pulish the app on snap store, follow the steps mentioned in the link https://docs.snapcraft.io/releasing-your-app

*** 

# Installer files
The [install](https://github.com/fossasia/pslab-desktop/tree/install) branch of the PSLab-Desktop repository hosts all the installers that we support for different desktop platforms. 

### Stable
The stable installers are generated and updated on a weekly basis and are created from the **master** branch automatically.

### Development
The development installers are generated and updated on every PR merge on **development** branch. These installers are used for testing purpose. 

***
		  
# Installation
Based on your preference, you can either install the app directly from the debian file produced in the previous step or from online servers.

## Install from file ( Linux ) :penguin: 
The *debian* file thus produced can be installed from the command line using 
```bash
sudo dpkg -i <deb-file-name>
```

## Installation from snap store ( Linux ) :penguin: 
The stable builds are published by our maintainers and can be installed from the command line using
```bash
sudo snap install pslab --edge
```

For testing purpose, you can install the snap package generated by the above command using:
```bash
sudo snap install --dangerous --classic <snap-package-name>
```