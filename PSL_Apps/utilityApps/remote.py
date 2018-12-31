from __future__ import print_function
from PyQt5 import QtCore
import string,json,base64
import numpy as np

class NumpyEncoder(json.JSONEncoder): # Answered by SO user http://stackoverflow.com/users/3768982/tlausch
	def default(self, obj):
		"""If input object is an ndarray it will be converted into a dict 
		holding dtype, shape and the data, base64 encoded.
		"""
		if isinstance(obj, np.ndarray):
			return list(obj)
		# Let the base class default method raise the TypeError
		return json.JSONEncoder(self, obj)

class CherryPyThread(QtCore.QThread):
	def __init__(self,cls):
		super(CherryPyThread, self).__init__()
		self.cherryClass = cls

	def run(self):
		import cherrypy
		cherrypy.tree.mount(self.cherryClass, '',	{'/':	{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}		}	)
		cherrypy.engine.start()
		cherrypy.engine.block()



class CherryPyClass():
	exposed = True	#Expose all methods

	def __init__(self,S=None,methods=None):		
		self.functions = {}
		if S: self.functions = S
		self.methods = methods
		
	def GET(self, id=None):
		if id == None:
			return('Here are all the functions available: %s' % self.functions)

		fn_name=id.split('(')[0]
		args=str(id.split('(')[1]).split(',')

		if len(args):args[-1]=args[-1][:-1]
		total_args=[]
		for t in args:
			print (t,len(t))
			if t[0]=="'" or t[0]=='"':total_args.append(t[1:-1])
			else:total_args.append(string.atoi(t))
		
		method = self.methods.get(fn_name)[0]
		if method == None :
			print ('no such command :',fn_name)
			return 'no such command : %s'%fn_name
		else:
			print (method,total_args)
			#while self.hw_lock and self.active: pass
			#self.hw_lock=True
			result=method(*total_args)		
			#self.hw_lock=False
			return json.dumps(result,cls=NumpyEncoder)


if __name__ == '__main__':
	import sys,time
	app = QtCore.QCoreApplication([])
	cls = CherryPyClass()
	thread = CherryPyThread(cls)
	thread.finished.connect(app.exit)
	thread.start()
	sys.exit(app.exec_())
