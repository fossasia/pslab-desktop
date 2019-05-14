#!/bin/bash

# Define colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
ORANGE='\033[0;33m'
NOCOLOR='\033[0m'

echo -e "${GREEN}Welcome to PSLab Desktop app installer${NOCOLOR}"
echo -e "${YELLOW}Installing ...${NOCOLOR}"
sudo apt-get update >/dev/null
# Install Python
echo -e "${ORANGE}Downloading Python 3.7.3${NOCOLOR}"
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
echo -e "${ORANGE}Extracting Python source file${NOCOLOR}"
tar -xvf Python-3.7.3.tgz >/dev/null
echo -e "${ORANGE}Removing source file${NOCOLOR}"
rm -rf Python-3.7.3.tgz >/dev/null
echo -e "${ORANGE}Installing GCC Compilers and SSL certificates for new Python Library${NOCOLOR}"
sudo apt-get install gcc zlib1g-dev libffi-dev make -y
sudo apt-get install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev -y
echo -e "${ORANGE}Move into Python folder${NOCOLOR}"
cd Python-3.7.3
echo -e "${ORANGE}Execute installer scripts for Python 3.7.3${NOCOLOR}"
./configure >/dev/null
make
sudo make install
# Install pip
sudo python3 -m pip install --upgrade pip >/dev/null
echo -e "${YELLOW}Setting up and upgrading pip is complete!${NOCOLOR}"
# Install PyQt5
sudo python3 -m pip install pyqt5 >/dev/null
echo -e "${YELLOW}Setting up PyQt5 is complete!${NOCOLOR}"
# Install Numpy
sudo python3 -m pip install numpy --upgrade >/dev/null
echo -e "${YELLOW}Setting up Numpy is complete!${NOCOLOR}"
# Install Serial libraries
sudo python3 -m pip install pyserial --upgrade >/dev/null
echo -e "${YELLOW}Setting up PySerial is complete!${NOCOLOR}"
# Install PyQt Graph
sudo python3 -m pip install pyqtgraph --upgrade >/dev/null
echo -e "${YELLOW}Setting up PyQt Graph is complete!${NOCOLOR}"
# Install SIP packages
sudo python3 -m pip install PyQt5-sip --upgrade >/dev/null
echo -e "${YELLOW}Setting up PyQt-SIP is complete!${NOCOLOR}"
# Install Webengine for HTML rendering
sudo python3 -m pip install PyQtWebEngine --upgrade >/dev/null
echo -e "${YELLOW}Setting up PyQtWebEngine is complete!${NOCOLOR}"
# Install PyOpenGl
sudo python3 -m pip install PyOpenGL --upgrade >/dev/null
echo -e "${YELLOW}Setting up PyOpenGL is complete!${NOCOLOR}"
# Install Dev Tools
sudo apt-get install pyqt5-dev-tools -y >/dev/null
echo -e "${YELLOW}Setting up dev tools is complete!${NOCOLOR}"
# Install iPython Console
sudo python3 -m pip install qtconsole >/dev/null
echo -e "${YELLOW}Setting up qtconsole is complete!${NOCOLOR}"
# Clone Desktop apps and Python repos
sudo apt-get install git -y >/dev/null
echo -e "${YELLOW}Setting up git is complete!${NOCOLOR}"
cd .. & mkdir pslab_temp_ins && cd pslab_temp_ins
git clone -b development https://github.com/fossasia/pslab-desktop.git
git clone -b development https://github.com/fossasia/pslab-python.git

# cd into Python repo and install
echo -e "${YELLOW}Cloning repositories is now complete! Let's start installation!${NOCOLOR}"
echo -e "${YELLOW}Installing Python Communication Library ...${NOCOLOR}"
cd pslab-python
make clean
make all
sudo make install
echo -e "${YELLOW}Python Communication Library installed!${NOCOLOR}"
cd ..
# cd into Desktop apps repo and install
echo -e "${YELLOW}Installing desktop application ...${NOCOLOR}"
cd pslab-desktop
make clean
make
sudo make install
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
	sudo Experiments
else
	echo -e "${GREEN}Installation complete!${NOCOLOR}"
fi
