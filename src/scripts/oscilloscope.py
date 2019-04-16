from PSL import sciencelab
import sys
import threading
import time

# time gap in microseconds
time_gap = int(sys.argv[1])
# number of samples
number_of_samples = int(sys.argv[2])
# channel name to chapture
channel_name = sys.argv[3]
# delay in milliseconds
delay = int(sys.argv[4])

# global variable to keep thread alive till STOP command
isReading = False

def readData():
	while isReading:
		x, y = I.capture1( channel_name, number_of_samples, time_gap )
		print( y.tolist() )
		# print( "[-1.2806451612903231, -1.2870967741935484, -1.2677419354838708, -1.2612903225806456, -1.274193548387097, -1.2806451612903231, -1.2677419354838708, -1.2548387096774194, -1.274193548387097, -1.2806451612903231]" )
		sys.stdout.flush()
		time.sleep( 0.001 * delay )

try:
	I = sciencelab.connect()
	
	I.set_gain( 'CH1', 3 )
	I.set_sine1( number_of_samples )
	
	# start read thread
	isReading = True
	t1 = threading.Thread(target=readData, name='read_data_thread') 
	t1.start()

	# wait for STOP command from stdin
	command = input()
	if command == "STOP":
		isReading = False

	t1.join()
except:
	pass

sys.stdout.flush()
