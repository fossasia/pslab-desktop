from setuptools import setup
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        install.run(self)


setup(name='pslab',
      version='2.0.0',
      description='GUI for Pocket Science Lab. Requires PSLab Python library',
      author='FOSSASIA PSLab Developers',
      author_email='pslab-fossasia@googlegroups.com',
      url='https://pslab.io/',
      install_requires=['numpy>=1.16.3', 'pyqtgraph>=0.10.0', 'setuptools>=35.0.2', 'PyQt5-sip>=4.19.17',
                        'PyQt5>=5.12.2', 'PyQtWebEngine>=5.12.1', 'pyserial >= 3.4', 'scipy >= 1.2.2'],
      packages=['pslab', 'pslab.docs', 'pslab.layouts', 'pslab.resources', 'pslab.tools', 'pslab.tests'],
      package_data={'': ['*.css', '*.png', '*.gif', '*.html', '*.css', '*.js', '*.png', '*.jpg', '*.jpeg', '*.htm',
                         '99-pslab.rules']},
      cmdclass={'install': CustomInstall})
