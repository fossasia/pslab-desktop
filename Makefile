DESTDIR =

# the variable CUSTOM will be 'true' if we are *not* in the context of
# building a debian package (you must be rrot or use fakeroot, the
# directory .. is supposed to be the root directory of the package
# seelablet
CUSTOM = $(shell cd ..; if [ -x /usr/bin/dh_testroot -a -x /usr/bin/dh_testdir ] && dh_testroot && dh_testdir; then echo false; else echo true; fi)

all:
	#make -C docs html
	#make -C docs/misc all
	python setup.py build
	python3 setup.py build

clean:
	rm -rf PSL_Apps.egg-info build
	if $(CUSTOM); then rm -rf /usr/share/pslab/; fi
	find . -name "*~" -o -name "*.pyc" -o -name "__pycache__" | xargs rm -rf
	#make -C docs clean
	#make -C docs/misc clean
	###### uninstalls only if in non-debian-packaging context
	if $(CUSTOM); then make uninstall_custom; fi

uninstall_custom:
	rm -rf /usr/lib/python2.7/dist-packages/PSL_Apps*
	sudo rm -rf /usr/lib/python2.7/dist-packages/psl_res
	sudo rm -f /usr/bin/Experiments

IMAGEDIR=$(DESTDIR)/usr/share/doc/pslab-common/images

install:
	# install documents
	install -d $(DESTDIR)/usr/share/doc/pslab
	mkdir -p $(DESTDIR)/usr/share/pslab/psl_res
	cp -r psl_res/* $(DESTDIR)/usr/share/pslab/psl_res/

	#cp docs/misc/build/*.html $(DESTDIR)/usr/share/doc/pslab/html
	# create ditributions for Python2 and Python3
	python setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
	python3 setup.py install --install-layout=deb \
	         --root=$(DESTDIR)/ --prefix=/usr
