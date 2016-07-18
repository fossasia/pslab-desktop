#!/usr/bin/env python

from __future__ import print_function
#from distutils.core import setup
from setuptools import setup, find_packages
from setuptools.command.install import install
import os,shutil
from distutils.util import execute
from distutils.cmd import Command
from subprocess import call

class CustomInstall(install):
    def run(self):
        install.run(self)

setup(name='PSL_Apps',
	version='1.0.0',
  	description='GUIs for Experiments with PSLab. Requires PSL',
  	author='Jithin B.P. and Praveen Patil',
	install_requires = ['numpy>=1.8.1','pyqtgraph>=0.9.10'], #PSL>=
	packages=['PSL_Apps','PSL_Apps.templates','PSL_Apps.utilityApps','PSL_Apps.utilityApps.templates','PSL_Apps.stylesheets','PSL_Apps.templates.widgets'],
	scripts=["PSL_Apps/bin/"+a for a in os.listdir("PSL_Apps/bin/")],
	package_data={'': ['*.css','*.png','*.gif','*.html','*.css','*.js','*.png','*.jpg','*.jpeg','*.htm','99-pslab.rules']},
	cmdclass={'install': CustomInstall},
)
