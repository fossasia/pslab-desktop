#!/usr/bin/env python

from __future__ import print_function

import os

from setuptools import setup
from setuptools.command.install import install


class CustomInstall(install):
    def run(self):
        install.run(self)


setup(name='PSL_Apps',
      version='1.1.0',
      description='GUIs for Experiments with PSLab. Requires PSLab Python library',
      author='FOSSASIA PSLab Developers',
      author_email='pslab-fossasia@googlegroups.com',
      url='https://pslab.io/',
      install_requires=['numpy>=1.8.1', 'pyqtgraph>=0.9.10'],
      packages=['PSL_Apps', 'PSL_Apps.templates', 'PSL_Apps.utilityApps', 'PSL_Apps.utilityApps.templates',
                'PSL_Apps.stylesheets', 'PSL_Apps.templates.widgets'],
      scripts=["PSL_Apps/bin/" + a for a in os.listdir("PSL_Apps/bin/")],
      package_data={'': ['*.css', '*.png', '*.gif', '*.html', '*.css', '*.js', '*.png', '*.jpg', '*.jpeg', '*.htm',
                         '99-pslab.rules']},
      cmdclass={'install': CustomInstall})
