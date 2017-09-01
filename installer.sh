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
apt-get install python -y
echo -e "${YELLOW}Setting up Python is completed!${NOCOLOR}"
# Install pip
apt-get install python-pip python-dev build-essential -y
sudo pip install --upgrade pip
echo -e "${YELLOW}Setting up pip is completed!${NOCOLOR}"
# Install PyQt
apt-get install python-qt4 -y
echo -e "${YELLOW}Setting up PyQt is completed!${NOCOLOR}"
# Install Numpy and Scipy
apt-get install python-numpy python-scipy -y
echo -e "${YELLOW}Setting up Numpy and Scipy is completed!${NOCOLOR}"
# Install Dev Tools
apt-get install pyqt4-dev-tools -y
echo -e "${YELLOW}Setting up dev tools is completed!${NOCOLOR}"
# Install PyQt Graph
pip install pyqtgraph
echo -e "${YELLOW}Setting up PyQt Graph is completed!${NOCOLOR}"
# Install PyOpenGl
pip install PyOpenGL
echo -e "${YELLOW}Setting up PyOpenGL is completed!${NOCOLOR}"
# Install QtOpenGl
apt-get install python-qt4-gl -y
echo -e "${YELLOW}Setting up QtOpenGl is completed!${NOCOLOR}"
# Install iPython Console
pip install qtconsole
echo -e "${YELLOW}Setting up qtconsole is completed!${NOCOLOR}"
# Clone Desktop apps and Python repos
apt-get install git -y
echo -e "${YELLOW}Setting up git is completed!${NOCOLOR}"
git clone https://github.com/fossasia/pslab-desktop-apps.git
git clone https://github.com/fossasia/pslab-python.git

# cd into Python repo and install
echo -e "${YELLOW}Cloning repositories is completed!${NOCOLOR}"
echo -e "${YELLOW}Installing python repository ...${NOCOLOR}"
cd pslab-python
make clean
make
make install

echo -e "${YELLOW}Python repository installed!${NOCOLOR}"
# cd into Desktop apps repo and install
echo -e "${YELLOW}Installing desktop application ...${NOCOLOR}"
cd ..
cd pslab-desktop-apps
make clean
make
make install
echo -e "${ORANGE}Desktop application installed!${NOCOLOR}"
echo -e "${GREEN}Starting application!${NOCOLOR}"

Experiments
