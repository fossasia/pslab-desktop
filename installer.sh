#!/bin/bash

# Define colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
ORANGE='\033[0;33m'
NOCOLOR='\033[0m'

echo -e "${GREEN}Welcome to PSLab Desktop app installer${NOCOLOR}"
echo -e "${YELLOW}Installing ...${NOCOLOR}"
apt-get update
# Install Python
apt-get install python3 -y
echo -e "${YELLOW}Setting up Python3 is complete!${NOCOLOR}"
# Install pip
apt-get install python3-pip -y
apt-get install python-dev build-essential -y
pip3 install --upgrade pip
echo -e "${YELLOW}Setting up and upgrading pip is complete!${NOCOLOR}"
# Install PyQt5
pip3 install pyqt5
echo -e "${YELLOW}Setting up PyQt5 is complete!${NOCOLOR}"
# Install Numpy
pip3 install numpy
echo -e "${YELLOW}Setting up Numpy is complete!${NOCOLOR}"
pip3 install pyserial
echo -e "${YELLOW}Setting up PySerial is complete!${NOCOLOR}"
# Install Dev Tools
apt-get install pyqt5-dev-tools -y
echo -e "${YELLOW}Setting up dev tools is complete!${NOCOLOR}"
# Install PyQt Graph
pip3 install pyqtgraph
echo -e "${YELLOW}Setting up PyQt Graph is complete!${NOCOLOR}"
# Install SIP packages
pip3 install PyQt5-sip
echo -e "${YELLOW}Setting up PyQt-SIP is complete!${NOCOLOR}"
# Install Webengine for HTML rendering
pip3 install PyQtWebEngine
echo -e "${YELLOW}Setting up PyQtWebEngine is complete!${NOCOLOR}"
# Install PyOpenGl
pip install PyOpenGL
echo -e "${YELLOW}Setting up PyOpenGL is complete!${NOCOLOR}"
# Install QtOpenGl
apt-get install python-qt5-gl -y
echo -e "${YELLOW}Setting up QtOpenGl is complete!${NOCOLOR}"
# Install iPython Console
pip3 install qtconsole
pip3 install
echo -e "${YELLOW}Setting up qtconsole is complete!${NOCOLOR}"
# Clone Desktop apps and Python repos
apt-get install git -y
echo -e "${YELLOW}Setting up git is complete!${NOCOLOR}"
cd /opt/
git clone https://github.com/fossasia/pslab-desktop.git
git clone https://github.com/fossasia/pslab-python.git

# cd into Python repo and install
echo -e "${YELLOW}Cloning repositories is now complete! Let's start installation!${NOCOLOR}"
echo -e "${YELLOW}Installing Python Communication Library ...${NOCOLOR}"
cd /opt/pslab-python
make clean
make
make install
echo -e "${YELLOW}Python Communication Library installed!${NOCOLOR}"

# cd into Desktop apps repo and install
echo -e "${YELLOW}Installing desktop application ...${NOCOLOR}"
cd /opt/pslab-desktop
make clean
make
make install
echo -e "${YELLOW}Python Desktop application installed!${NOCOLOR}"

if (whiptail --title "Add PSLab Desktop Application" --yesno "Do you want to add PSLab Application to desktop and dash now?" 8 46) then
	cp PSLab.desktop ~/Desktop/PSLab.desktop
	cp PSLab.desktop ~/.local/share/applications/PSLab.desktop
	cd ~/Desktop
	chmod +x PSLab.desktop
	echo -e "${GREEN}Application shortcuts are set!${NOCOLOR}"
else
	echo -e "${GREEN}Didn't create any shortcuts!${NOCOLOR}"
fi

echo -e "${GREEN}Installation is now complete!${NOCOLOR}"

if (whiptail --title "Open PSLab Desktop Application" --yesno "Do you want to open PSLab Desktop now?" 8 46) then
	echo -e "${GREEN}Starting application ...${NOCOLOR}"
	Experiments
else
	echo -e "${GREEN}Installation complete!${NOCOLOR}"
fi
