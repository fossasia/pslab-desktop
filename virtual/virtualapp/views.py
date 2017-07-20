from virtualapp import app,cursor,conn
from flask import Flask, render_template,request,json,session,redirect,jsonify

#from werkzeug import generate_password_hash, check_password_hash
#import os

import inspect,random

# A dummy class that will pretend to be a minimal PSLab . we shall use this for testing purposes.
class dummy:
	def __init__(self):
		self.x=np.linspace(0,8*np.pi,samples)
		self.r = random.random()
	def capture1(self,chan,samples,tg):
		'''
		Example doc for capture command. returns a sine wave
		'''
		return self.x,np.sin(self.x+np.pi*random.random()/10)
	def capture2(self,samples,tg):
		return self.x,np.sin(self.x+np.pi*random.random()/10),np.sin(self.x+np.pi*random.random()/10)

	def get_voltage(self,chan):
		'''
		bloo blahs
		a454
		*&^ "23"
		'''
		return self.r+random.random()
	def set_pv1(self,val):
		return val+self.r


try:
	from PSL import sciencelab
	I = sciencelab.connect(verbose=True)
	I.set_sine2(1000)
except Exception as e:
	print ('using dummy class',str(e))
	I = dummy()

# Use the inspect module to prepare a list of methods available in the class. This is quite flexible, and in theory this framework should easily adapt to serve any hardware with a python communication library
functionList = {}
for a in dir(I):
	attr = getattr(I, a)
	if inspect.ismethod(attr) and a!='__init__':
		functionList[a] = attr

@app.route('/')
@app.route('/index')
@app.route('/main')
def index():
    return render_template('index.html')


