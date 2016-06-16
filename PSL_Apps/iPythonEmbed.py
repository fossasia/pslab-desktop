from __future__ import print_function

from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
class QIPythonWidget(RichIPythonWidget):
	def __init__(self,customBanner=None,*args,**kwargs):
		print ('importing KernelManager')
		from IPython.qt.inprocess import QtInProcessKernelManager
		print ('import GuiSupport')
		from IPython.lib import guisupport
		if customBanner!=None: self.banner=customBanner
		print ('initializing')
		super(QIPythonWidget, self).__init__(*args,**kwargs)
		print ('kernel manager creating')
		self.kernel_manager = kernel_manager = QtInProcessKernelManager()
		print ('kernel manager starting')
		kernel_manager.start_kernel()
		kernel_manager.kernel.gui = 'qt4'
		self.kernel_client = kernel_client = self._kernel_manager.client()
		kernel_client.start_channels()
	
		def stop():
				kernel_client.stop_channels()
				kernel_manager.shutdown_kernel()
				guisupport.get_app_qt4().exit()            
		self.exit_requested.connect(stop)

	def pushVariables(self,variableDict):
		""" Given a dictionary containing name / value pairs, push those variables to the IPython console widget """
		self.kernel_manager.kernel.shell.push(variableDict)
	def clearTerminal(self):
		""" Clears the terminal """
		self._control.clear()    
	def printText(self,text):
		""" Prints some plain text to the console """
		self.append_stream(text)        
	def executeCommand(self,command,hidden=False):
		""" Execute a command in the frame of the console widget """
		self._execute(command,hidden)


