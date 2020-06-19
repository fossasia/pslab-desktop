# PSLab Desktop

Desktop application for the [Pocket Science Lab (PSlab)](https://pslab.io) open hardware platform.

Development [![Build Status](https://travis-ci.org/fossasia/pslab-desktop.svg?branch=development)](https://travis-ci.org/fossasia/pslab-desktop)
Master [![Build Status](https://travis-ci.org/fossasia/pslab-desktop.svg?branch=master)](https://travis-ci.org/fossasia/pslab-desktop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8259e5c2220f484e95a88cf4aaed1a96)](https://www.codacy.com/app/mb/pslab-desktop?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fossasia/pslab-desktop&amp;utm_campaign=Badge_Grade)
[![Mailing List](https://img.shields.io/badge/Mailing%20List-FOSSASIA-blue.svg)](https://groups.google.com/forum/#!forum/pslab-fossasia)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Twitter Follow](https://img.shields.io/twitter/follow/pslabio.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/pslabio)

## About

_TODO: move this to the general documentation and reference it (?)_

The goal of PSLab is to create an Open Source hardware device (open on all
layers) and software applications that can be used for experiments by teachers,
students and scientists. Our tiny pocket lab provides an array of instruments
for doing science and engineering experiments. It provides functions of numerous
measurement tools including an oscilloscope, a waveform generator, a frequency
counter, a programmable voltage, current source and even a component to
control robots with up to four servos.
For more details, see [pslab.io](https://pslab.io).

[![PSLab](docs/images/project_banner.jpg)](https://pslab.io)

## Buy

* You can get a PSLab device from the [FOSSASIA Shop](https://fossasia.com).
* More resellers are listed on the [PSLab website](https://pslab.io/shop/).

## PSLab Desktop App

This repository holds the PSLab Desktop application.

It is built with the [Electron](https://www.electronjs.org/) cross-platform
desktop application framework, using [React](https://reactjs.org/) for the UI,
and Python scripts under the hood for device communication.

See also the [screenshots and demos](docs/screenshots-and-demos.md).

## Downloads and Distribution

**TODO**

- [ ] redo the build pipeline and publish assets as release attachments
- [ ] document building, bundling and distribution steps

### Arch Linux

If you are running Arch Linux or another distribution based on it, install
[`pslab-desktop`](https://aur.archlinux.org/packages/pslab-desktop).

### Debian based distributions (outdated)

We have been building snapshots for Debian based distributions. Please see the
[install branch](https://github.com/fossasia/pslab-desktop/tree/install).

* [development build](https://github.com/fossasia/pslab-desktop/raw/install/pslab-desktop-development-linux.deb)
* [stable build](https://github.com/fossasia/pslab-desktop/raw/install/pslab-desktop-master-linux.deb)

### Windows (outdated)

As for Debian, we have been building Windows installers, also found in the
[install branch](https://github.com/fossasia/pslab-desktop/tree/install).

### macOS

We are not producing builds for macOS, but provide instructions to do so.

First you need to follow the instructions to [set up a development environment](
#setting-up-a-development-environment). Then [build the app](#building-the-app).

After the process, open the newly created directory named `dist/` in Finder.

Open the `PSLab-*.dmg` file, drag and drop the `PSLab` icon to the `Application`
directory within the installation window, and PSLab will appear in your
Launchpad.

## Communication

Please join us on the following channels:

* [PSLab Gitter Channel](https://gitter.im/fossasia/pslab)
* [Mailing List](https://groups.google.com/forum/#!forum/pslab-fossasia)

## Development

### Features and Implementation Status

|   **Feature**          | **Description**                                                   | **Status**         |
|------------------------|-------------------------------------------------------------------|--------------------|
| Home Screen            | Show status and version of PSLab device                           | :heavy_check_mark: |
| Instruments            | Exposes PSLab instruments like Oscilloscope, etc                  | :heavy_check_mark: |
| Oscilloscope           | Shows variation of analog signals                                 | :heavy_check_mark: |
| Multimeter             | Measures voltage, current, resistance and capacitance             | :heavy_check_mark: |
| Logical Analyzer       | Captures and displays signals from digital system                 | :heavy_check_mark: |
| Wave Generator         | Generates arbitrary analog and digital waveforms                  | :heavy_check_mark: |
| Power Source           | Generates programmable voltage and currents	                     | :heavy_check_mark: |
| Lux Meter              | Measures the ambient light intensity                              | :negative_squared_cross_mark: |
| Barometer              | Measures the Pressure                                             | :negative_squared_cross_mark: |
| Accelerometer          | Measures the acceleration of the device                           | :negative_squared_cross_mark: |
| Gyrometer              | Measures the rate of rotation                                     | :negative_squared_cross_mark: |
| Compass                | Measures the absolute rotation relative to earth magnetic poles   | :negative_squared_cross_mark: |
| Thermometer            | Measures the ambient temperature                                  | :negative_squared_cross_mark: |
| Gas Sensor             | Detects gases, including NH3, NOx, alcohol, benzene, smoke and CO2| :negative_squared_cross_mark: |
| Robotic Arm Controller | Allows to control 4 servo motors of the robotic arm independently | :heavy_check_mark: |

### Roadmap

The goal of the project is to provide a fully functional science application
that works with PSLab and other open scientific hardware. Furthermore the
application should be fully compatible and feature matching to the PSLab Android
app. Current status of the development:

* [x] Implement all major instruments
* [x] Have an effective build system for linux and windows
* [x] Have a basic data logging feature in place
* [/] Implement interface for I2C sensors
* [ ] Implement more minor instruments 
	- [ ] Lux meter
	- [ ] Gas meter
	- [ ] Compass
	- [ ] pH meter
	- [ ] Accelerometer
	- [ ] Barometer 
* [ ] Make data logging and playback more robust
* [ ] Code refactoring and architecture improvement

### How to Contribute

Great you are interested in contributing! Please check the [issue tracker
](https://github.com/fossasia/pslab-desktop/issues) for open bugs and feature
requests and read the [FOSSASIA community guidelines](
https://blog.fossasia.org/open-source-developer-guide-and-best-practices-at-fossasia/)
to get started.

### Branch Policy

* The **development** branch is the standard branch of the project. Pull
  requests are merged to this branch and tests run through Travis CI.
* The **master** branch is currently not maintained and held the stable releases
  of the project and merged the development branch regularly after it was tested
  thouroughly.
* The **install** branch is outdated and holds autogenerated install images for
  some Linux distributions and Windows. It was generated through Travis CI on
  merged pull requests in the development and master branches.
* The **gh-pages** is currently outdated, but is intended to hold information of
  the project from the Readme.md and /docs folder.

### Setting up a Development Environment

1. Fork the project to get a copy of the repository in your GitHub profile.
2. Clone the forked project from your profile (not from FOSSASIA):
   `git clone git@github.com:your-profile/pslab-desktop`
3. Change into the project folder: `cd pslab-desktop`
4. Add the original FOSSASIA repository as a remote:
   `git remote add upstream https://github.com/fossasia/pslab-desktop.git`

### Prerequisites and Dependencies

**Please note**: If you are in China, you need to [configure a mirror for npm](
https://www.npmjs.com/package/mirror-config-china). In short, add the following
to your `~/.npmrc` file (create it if it doesn't yet exist):

```
registry = http://registry.npm.taobao.org/
```

While in your project folder, run `npm install`.
This will install all the necessary dependencies required by the app to run.

### Python library

As this app uses the **PSL** library under the hood for device communication,
you need to have it installed as well. Instructions are provided in the
[pslab-python repository](https://github.com/fossasia/pslab-python).

### Starting the app

All commands to start and debug the app are outlined in the `package.json` file.
To simply get it running run the following command while in your project
repository.

```sh
npm start
```

And wait for Electron to open.

### IPC and Stack

The stack comprises multiple pieces:

- hardware offering phyiscal ports
- firmware for the PIC MCU
- Python backend library communicates with MCU via USB serial
- bridge in `scripts/` talks to the Python library
- Electron app offers UI and communicates with the bridge via stdout

Electron builds on top of Node.js and Chromium. The UI is running in its own
rendering process, requiring IPC in order to communicate with the main process.
See `public/electron.js` for the entry point in this project.

To communicate with the Python bridge, there are extra Electron processes that
spawn Python processes. See `background_tasks/`.

Any action from the UI thus requires the following:

- an appropriate handler to pick up the action from the UI element
- a function invoking the corresponding IPC method
- an Electron-side IPC method definition (`public/electron.js`)
- a Python-side IPC method definition (`scripts/bridge.py`)

## Building the App

While in the project root, run the build script as defined in `package.json`:

```sh
npm run build
```

For a platform-specific build, run `npm run build-{linux,mac,win}` instead.

This command will produce two directories in the project root. The `build/`
directory contains the optimized React files, while the `dist/` directory
contains the final Electron build with everything else.

## License

This project is Free and Open Source software. The project is licensed under the
[GPL v3](LICENSE). Copyright is owned by FOSSASIA. More details in the license
files.

## Maintainers

The project is maintained by

- Daniel Maslowski ([@orangecms](https://github.com/orangecms))
- Padmal ([@CloudyPadmal](https://github.com/CloudyPadmal))
- Mario Behling ([@mariobehling](http://github.com/mariobehling))
- Wei Tat ([@cweitat](https://github.com/cweitat))
- Aakash Mallik ([@AakashMallik](https://github.com/AakashMallik))
