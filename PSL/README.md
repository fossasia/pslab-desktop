### Documentation of back-end functions used in PSLab, taken from [sciencelab.py](https://github.com/fossasia/pslab-python/blob/development/PSL/sciencelab.py)

Sciencelab class contains methods that can be used to interact with the FOSSASIA PSLab. Run the following code to connect:

	>>> from PSL import sciencelab
	>>> I = sciencelab.connect()
	>>> self.__print__(I)
	<sciencelab.ScienceLab instance at 0xb6c0cac>
	
Once you have initiated this class,  its various methods will allow access to all the features built into the device.

<details>
<summary><code>get_resistance(self)</code></summary><br />
</details>

<details>
<summary><code>get_version(self)</code></summary>

+ Returns the version string of the device, format: LTS-......

</details>

<details>
<summary><code>getRadioLinks(self)</code></summary><br />
</details>

<details>
<summary><code>newRadioLink(self, **args)</code></summary>

+ Arguments
	+ \*\*Kwargs: Keyword Arguments
		+ address: Address of the node. a 24 bit number. Printed on the nodes. Can also be retrieved using :py:meth:`~NRF24L01_class.NRF24L01.get_nodelist` 
+ Return: :py:meth:`~NRF_NODE.RadioLink`

</details>

## ANALOG SECTION

This section has commands related to analog measurement and control. These include the oscilloscope routines, voltmeters, ammeters, and Programmable voltage sources.

<details>
<summary><code>reconnect(self, **kwargs)</code></summary>

+ Attempts to reconnect to the device in case of a commmunication error or accidental disconnect.

</details>

<details>
<summary><code>capture1(self, ch, ns, tg, *args, **kwargs)</code></summary>

+ Blocking call that fetches an oscilloscope trace from the specified input channel
+ Arguments
	+ ch: Channel to select as input. ['CH1'..'CH3','SEN']
	+ ns: Number of samples to fetch. Maximum 10000
	+ tg: Timegap between samples in microseconds
+ Return: Arrays X(timestamps),Y(Corresponding Voltage values)	

```
>>> from pylab import *
>>> from PSL import sciencelab
>>> I = sciencelab.connect()
>>> x,y = I.capture1('CH1',3200,1)
>>> plot(x,y)
>>> show()
```

</details>

<details>
<summary><code>capture2(self, ns, tg, TraceOneRemap = 'CH1')</code></summary>

+ Blocking call that fetches oscilloscope traces from CH1,CH2
+ Arguments
	+ ns: Number of samples to fetch. Maximum 5000
	+ tg: Timegap between samples in microseconds
	+ TraceOneRemap: Choose the analog input for channel 1. It is connected to CH1 by default. Channel 2 always reads CH2.
+ Return: Arrays X(timestamps),Y1(Voltage at CH1),Y2(Voltage at CH2)

```
>>> from pylab import *
>>> from PSL import sciencelab
>>> I = sciencelab.connect()
>>> x,y1,y2 = I.capture2(1600,2,'MIC')  #Chan1 remapped to MIC. Chan2 reads CH2
>>> plot(x,y1)              #Plot of analog input MIC
>>> plot(x,y2)              #plot of analog input CH2
>>> show()
```

</details>

<details>
<summary><code>capture4(self, ns, tg, TraceOneRemap = 'CH1')</code></summary>

+ Blocking call that fetches oscilloscope traces from CH1,CH2
+ Arguments
	+ ns: Number of samples to fetch. Maximum 2500
	+ tg: Timegap between samples in microseconds. Minimum 1.75uS
	+ TraceOneRemap: Choose the analog input for channel 1. It is connected to CH1 by default. Channel 2 always reads CH2.
+ Return: Arrays X(timestamps),Y1(Voltage at CH1),Y2(Voltage at CH2),Y3(Voltage at CH3),Y4(Voltage at CH4)

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> x,y1,y2,y3,y4 = I.capture4(800,1.75)
>>> plot(x,y1)
>>> plot(x,y2)
>>> plot(x,y3)
>>> plot(x,y4)
>>> show()
```

</details>

<details>
<summary><code>capture_multiple(self, samples, tg, *args)</code></summary>

+ Blocking call that fetches oscilloscope traces from a set of specified channels
+ Arguments
	+ samples: Number of samples to fetch. Maximum 10000/(total specified channels)
	+ tg: Timegap between samples in microseconds.
	+ \*args: Channel names
+ Return: Arrays X(timestamps),Y1,Y2 ...

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> x,y1,y2,y3,y4 = I.capture_multiple(800,1.75,'CH1','CH2','MIC','SEN')
>>> plot(x,y1)
>>> plot(x,y2)
>>> plot(x,y3)
>>> plot(x,y4)
>>> show()
```

</details>

<details>
<summary><code>capture_fullspeed(self, chan, samples, tg, *args, **kwargs)</code></summary>

+ Blocking call that fetches oscilloscope traces from a single oscilloscope channel at a maximum speed of 2MSPS

+ Arguments
	+ chan: Channel name 'CH1' / 'CH2' ... 'SEN'
	+ samples: Number of samples to fetch. Maximum 10000/(total specified channels)
	+ \*args: Specify if SQR1 must be toggled right before capturing.
		+ 'SET_LOW': Set SQR1 to 0V
		+ 'SET_HIGH': Set SQR1 to 1V
		+ 'FIRE_PULSES': output a preset frequency on SQR1 for a given interval (keyword arg 'interval' must be specified or it will default to 1000uS) before acquiring data. This is used for measuring speed of sound using piezos if no arguments are specified, a regular capture will be executed.
	+ \*\*kwargs
		+ interval: Units: uS. Necessary if 'FIRE_PULSES' argument was supplied. Default 1000uS  
+ Return: timestamp array ,voltage_value array

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> x,y = I.capture_fullspeed('CH1',2000,1)
>>> plot(x,y)
>>> show()
```

```
>>> x,y = I.capture_fullspeed('CH1',2000,1,'SET_LOW')
>>> plot(x,y)
>>> show()
```

```
>>> I.sqr1(40e3 , 50, True)   # Prepare a 40KHz, 50% square wave. Do not output it yet
>>> x,y = I.capture_fullspeed('CH1',2000,1,'FIRE_PULSES',interval = 250) #Output the prepared 40KHz(25uS) wave for 250uS(10 cycles) before acquisition
>>> plot(x,y)
>>> show()
```

</details>

<details>
<summary><code>capture_fullspeed_hr(self, chan, samples, tg, *args)</code></summary>
</details>

<details>
<summary><code>capture_traces(self, num, samples, tg, channel_one_input = 'CH1', CH123SA = 0, *kwargs)</code></summary>

+ Instruct the ADC to start sampling. use fetch_trace to retrieve the data

+ Arguments
	+ num: Channels to acquire. 1/2/4
	+ samples: Total points to store per channel. Maximum 3200 total.
	+ tg: Timegap between two successive samples (in uSec) 
	+ channel_one_input: Map channel 1 to 'CH1' ... 'CH9'
	+ \*\*kwargs
		+ \*trigger: Whether or not to trigger the oscilloscope based on the voltage level set by :func:`configure_trigger`
+ Return: nothing

The following example demonstrates how to use this function to record active events.

+ Connect a capacitor and an Inductor in series.
+ Connect CH1 to the spare leg of the inductor. Also Connect OD1 to this point
+ Connect CH2 to the junction between the capacitor and the inductor
+ Connect the spare leg of the capacitor to GND( ground )
+ Set OD1 initially high using set_state(SQR1 = 1)

```
>>> I.set_state(OD1 = 1)  #Turn on OD1
#Arbitrary delay to wait for stabilization
>>> time.sleep(0.5)
#Start acquiring data (2 channels,800 samples, 2microsecond intervals)
>>> I.capture_traces(2,800,2,trigger = False)
#Turn off OD1. This must occur immediately after the previous line was executed.
>>> I.set_state(OD1 = 0)
#Minimum interval to wait for completion of data acquisition.
#samples*timegap*(convert to Seconds)
>>> time.sleep(800*2*1e-6)
>>> x,CH1 = I.fetch_trace(1)
>>> x,CH2 = I.fetch_trace(2)
>>> plot(x,CH1-CH2) #Voltage across the inductor
>>> plot(x,CH2)     ##Voltage across the capacitor
>>> show()
```

The following events take place when the above snippet runs

+ The oscilloscope starts storing voltages present at CH1 and CH2 every 2 microseconds
+ The output OD1 was enabled, and this causes the voltage between the L and C to approach OD1 voltage. (It may or may not oscillate)
+ The data from CH1 and CH2 was read into x,CH1,CH2
+ Both traces were plotted in order to visualize the Transient response of series LC

</details>

<details>
<summary><code>capture_highres_traces(self, channel, samples, tg, **kwargs)</code></summary>

+ Instruct the ADC to start sampling. Use fetch_trace to retrieve the data

+ Arguments
	+ channel: Channel to acquire data from 'CH1' ... 'CH9'
	+ samples: Total points to store per channel. Maximum 3200 total.
	+ tg : Timegap between two successive samples (in uSec)
	+ \*\*kwargs
		+ \*trigger : Whether or not to trigger the oscilloscope based on the voltage level set by :func:`configure_trigger`
+ Return: nothing

</details>

<details>
<summary><code>fetch_trace(self, channel_number)</code></summary>

+ Fetches a channel(1-4) captured by :func:`capture_traces` called prior to this, and returns xaxis,yaxis

+ Arguments
	+ channel_number: Any of the maximum of four channels that the oscilloscope captured. 1/2/3/4
+ Return: time array,voltage array

</details>

<details>
<summary><code>oscilloscope_progress(self)</code></summary>

+ Returns the number of samples acquired by the capture routines, and the conversion_done status
+ Return: conversion done(bool) ,samples acquired (number)

```
>>> I.start_capture(1,3200,2)
>>> self.__print__(I.oscilloscope_progress())
(0,46)
>>> time.sleep(3200*2e-6)
>>> self.__print__(I.oscilloscope_progress())
(1,3200)
```

</details>

<details>
<summary><code>configure_trigger(self, chan, name, voltage, resolution = 10, **kwargs)</code></summary>

+ Configure trigger parameters for 10-bit capture commands
+ The capture routines will wait till a rising edge of the input signal crosses the specified level.
+ The trigger will timeout within 8mS, and capture routines will start regardless.
+ These settings will not be used if the trigger option in the capture routines are set to False
+ Arguments
	+ chan: Channel 0,1,2,3. Corresponding to the channels being recorded by the capture routine(not the analog inputs)
	+ name: Name of the channel. 'CH1'... 'V+'
	+ voltage: The voltage level that should trigger the capture sequence(in Volts)
+ Return: Nothing

```
>>> I.configure_trigger(0,'CH1',1.1)
>>> I.capture_traces(4,800,2)
#Unless a timeout occured, the first point of this channel will be close to 1.1Volts
>>> I.fetch_trace(1)
#This channel was acquired simultaneously with channel 1,
#So it's triggered along with the first
>>> I.fetch_trace(2)
```

</details>

<details>
<summary><code>set_gain(self, channel, gain, Force = False)</code></summary>

+ Set the gain of the selected PGA
+ Arguments
	+ channel: 'CH1','CH2'
	+ gain: (0-8) -> (1x,2x,4x,5x,8x,10x,16x,32x,1/11x)
	+ Force: If True, the amplifier gain will be set even if it was previously set to the same value.

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> I.set_gain('CH1',7)  #gain set to 32x on CH1
```

**Note**: The gain value applied to a channel will result in better resolution for small amplitude signals. However, values read using functions like :func:`get_average_voltage` or func:`capture_traces` will not be 2x, or 4x times the input signal. These are calibrated to return accurate values of the original input signal. In case the gain specified is 8 (1/11x) , an external 10MOhm resistor must be connected in series with the device. The input range will be +/-160 Volts

</details>

<details>
<summary><code>select_range(self, channel, voltage_range)</code></summary>

+ set the gain of the selected PGA
+ Arguments
	+ channel: 'CH1','CH2'
	+ voltage_range: Choose from [16,8,4,3,2,1.5,1,.5,160]

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> I.select_range('CH1',8)  #gain set to 2x on CH1. Voltage range +/-8V
```

**Note**: Setting the right voltage range will result in better resolution. In case the range specified is 160 , an external 10MOhm resistor must be connected in series with the device. This function internally calls `set_gain` with the appropriate gain value

</details>

<details>
<summary><code>get_voltage(self, channel_name, **kwargs)</code></summary><br />
</details>

<details>
<summary><code>voltmeter_autorange(self, channel_name)</code></summary><br />
</details>

<details>
<summary><code>get_average_voltage(self, channel_name, **kwargs)</code></summary>

+ Return the voltage on the selected channel
+ Arguments
	+ channel_name : 'CH1','CH2','CH3', 'MIC','IN1','SEN','V+'
	+ sleep: Read voltage in CPU sleep mode. not particularly useful. Also, Buggy. 
	+ \*\*kwargs: Samples to average can be specified. Eg, samples=100 will average a hundred readings

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> self.__print__(I.get_average_voltage('CH4'))
1.002
```

</details>

<details>
<summary><code>fetch_buffer(self, starting_position = 0, total_points = 100)</code></summary>

+ Fetches a section of the ADC hardware buffer

</details>

<details>
<summary><code>clear_buffer(self, starting_position, total_points)</code></summary>

+ Clears a section of the ADC hardware buffer

</details>

<details>
<summary><code>fill_buffer(slef, starting_position, poin_array)</code></summary>

+ Fill a section of the ADC hardware buffer with data

</details>

<details>
<summary><code>start_streaming(self, tg, channel = 'CH1')</code></summary>

+ Instruct the ADC to start streaming 8-bit data.  use stop_streaming to stop.
+ Arguments
	+ tg: timegap. 250KHz clock
	+ channel: channel 'CH1'... 'CH9','IN1','SEN'  

</details>

<details>
<summary><code>stop_streaming(self)</code></summary>

+ Instruct the ADC to stop streaming data

</details>

## DIGITAL SECTION

This section has commands related to digital measurement and control. These include the Logic Analyzer, frequency measurement calls, timing routines, digital outputs etc.

<details>
<summary><code>get_high_freq(self, pin)</code></summary>

+ Retrieves the frequency of the signal connected to ID1. For frequencies > 1MHz
+ Also good for lower frequencies, but avoid using it since the oscilloscope cannot be used simultaneously due to hardware limitations.
+ The input frequency is fed to a 32 bit counter for a period of 100mS.
+ The value of the counter at the end of 100mS is used to calculate the frequency.
+ Arguments
	+ pin: The input pin to measure frequency from : ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
+ Return: frequency

</details>

<details>
<summary><code>get_freq(self, channel = 'CNTR', timeout = 2)</code></summary>

+ Frequency measurement on IDx.
+ Measures time taken for 16 rising edges of input signal.
+ Returns the frequency in Hertz
+ Arguments
	+ channel: The input to measure frequency from. ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ timeout: This is a blocking call which will wait for one full wavelength before returning the calculated frequency. Use the timeout option if you're unsure of the input signal. Returns 0 if timed out
+ Return: float: frequency

Connect SQR1 to ID1

```
>>> I.sqr1(4000,25)
>>> self.__print__(I.get_freq('ID1'))
4000.0
>>> self.__print__(I.r2r_time('ID1'))
#time between successive rising edges
0.00025
>>> self.__print__(I.f2f_time('ID1'))
#time between successive falling edges
0.00025
>>> self.__print__(I.pulse_time('ID1'))
#may detect a low pulse, or a high pulse. Whichever comes first
6.25e-05
>>> I.duty_cycle('ID1')
#returns wavelength, high time
(0.00025,6.25e-05)
```

</details>

<details>
<summary><code>r2r_time(self, channel, skip_cycle = 0, timeout = 5)</code></summary>

+ Return a list of rising edges that occured within the timeout period.
+ Arguments
	+ channel: The input to measure time between two rising edges.['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ skip_cycle: Number of points to skip. eg. Pendulums pass through light barriers twice every cycle. SO 1 must be skipped
    + timeout: Number of seconds to wait for datapoints. (Maximum 60 seconds)
+ Return: list: Array of points

</details>

<details>
<summary><code>f2f_time(self,channel, skip_cycle = 0, timeout = 5)</code></summary>

+ Return a list of falling edges that occured within the timeout period.
+ Arguments
	+ channel: The input to measure time between two falling edges.['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ skip_cycle: Number of points to skip. eg. Pendulums pass through light barriers twice every cycle. SO 1 must be skipped
    + timeout: Number of seconds to wait for datapoints. (Maximum 60 seconds)
+ Return: list: Array of points

</details>

<details>
<summary><code>MeasureInterval(self, channel1, channel2, edge1, edge2, timeout = 0.1)</code></summary>

+ Measures time intervals between two logic level changes on any two digital inputs(both can be the same) and returns the calculated time.
+ For example, one can measure the time interval between the occurence of a rising edge on ID1, and a falling edge on ID3.
+ If the returned time is negative, it simply means that the event corresponding to channel2 occurred first.
+ Arguments
	+ channel1: The input pin to measure first logic level change
	+ channel2: The input pin to measure second logic level change -['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ edge1: The type of level change to detect in order to start the timer
		+ 'rising'
		+ 'falling'
		+ 'four rising edges'
	+ edge1: The type of level change to detect in order to stop the timer
		+ 'rising'
		+ 'falling'
		+ 'four rising edges'
    + timeout: Use the timeout option if you're unsure of the input signal time period.
						Returns -1 if timed out
+ Return: time

</details>

<details>
<summary><code>DutyCycle(self, channel = 'ID1', timeout = 1.)</code></summary>

+ Duty cycle measurement on channel. Returns wavelength(seconds), and length of first half of pulse(high time)
+ Low time = (wavelength - high time)
+ Arguments
	+ channel: The input pin to measure wavelength and high time.['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
    + timeout: Use the timeout option if you're unsure of the input signal time period. Returns 0 if timed out
+ Return: wavelength, duty cycle

</details>

<details>
<summary><code>PulseTime(self, channel = 'ID1', PulseType = 'LOW', timeout = 0.1)</code></summary>

+ Duty cycle measurement on channel. Returns wavelength(seconds), and length of first half of pulse(high time)
+ Low time = (wavelength - high time)
+ Arguments
	+ channel: The input pin to measure wavelength and high time.['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
    + PulseType: Type of pulse to detect. May be 'HIGH' or 'LOW'
    + timeout: Use the timeout option if you're unsure of the input signal time period.
						Returns 0 if timed out
+ Return: pulse width

</details>

<details>
<summary><code>MeasureMultipleDigitalEdges(self, channel1, channel2, edgeType1, edgeType2, points1, points2, timeout=0.1, **kwargs)</code></summary>

+ Measures a set of timestamped logic level changes(Type can be selected) from two different digital inputs.
+ Arguments
	+ channel1: The input pin to measure first logic level change
	+ channel2: The input pin to measure second logic level change
						 -['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ edgeType1: The type of level change that should be recorded
		+ 'rising'
		+ 'falling'
		+ 'four rising edges' [default]
	+ edgeType2: The type of level change that should be recorded
		+ 'rising'
		+ 'falling'
		+ 'four rising edges'
	+ points1: Number of data points to obtain for input 1 (Max 4)
	+ points2: Number of data points to obtain for input 2 (Max 4)
	+ timeout: Use the timeout option if you're unsure of the input signal time period.
						returns -1 if timed out
   	+ **kwargs
   		+ SQ1: Set the state of SQR1 output(LOW or HIGH) and then start the timer.  eg. SQR1 = 'LOW'
   		+ zero: subtract the timestamp of the first point from all the others before returning. Default: True
+ Return: time
+ Example, Aim : Calculate value of gravity using time of flight. The setup involves a small metal nut attached to an electromagnet powered via SQ1. When SQ1 is turned off, the set up is designed to make the nut fall through two different light barriers(LED,detector pairs that show a logic change when an object gets in the middle) placed at known distances from the initial position. One can measure the timestamps for rising edges on ID1 ,and ID2 to determine the speed, and then obtain value of g.

</details>

<details>
<summary><code>capture_edges1(self, waiting_time = 1., **args)</code></summary>

+ Log timestamps of rising/falling edges on one digital input
+ Arguments
	+ waiting_time:  Total time to allow the logic analyzer to collect data. This is implemented using a simple sleep routine, so if large delays will be involved, refer to :func:`start_one_channel_LA` to start the acquisition, and :func:`fetch_LA_channels` to retrieve data from the hardware after adequate time. The retrieved data is stored in the array self.dchans[0].timestamps.
	+ keyword arguments
	+ channel: 'ID1',...,'ID4'
	+ trigger_channel: 'ID1',...,'ID4'
	+ channel_mode: acquisition mode, default value: 3
		+ EVERY_SIXTEENTH_RISING_EDGE = 5
	 	+ EVERY_FOURTH_RISING_EDGE    = 4
		+ EVERY_RISING_EDGE           = 3
		+ EVERY_FALLING_EDGE          = 2
		+ EVERY_EDGE                  = 1
		+ DISABLED                    = 0
	+ trigger_mode: same as channel_mode. default_value : 3
+ Return: timestamp array in Seconds

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> I.capture_edges(0.2,channel = 'ID1',trigger_channel = 'ID1',channel_mode = 3,trigger_mode = 3)
#captures rising edges only. with rising edge trigger on ID1
```

</details>

<details>
<summary><code>start_one_channel_LA_backup__(self, trigger = 1, channel = 'ID1', maximum_time = 67, **args)</code></summary>

+ Start logging timestamps of rising/falling edges on ID1
+ Arguments
	+ trigger: Bool . Enable edge trigger on ID1. use keyword argument edge = 'rising' or 'falling'
	+ channel: ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ maximum_time: Total time to sample. If total time exceeds 67 seconds, a prescaler will be used in the reference clock.
	+ kwargs
		+ triggger_channels: array of digital input names that can trigger the acquisition. Eg, trigger = ['ID1','ID2','ID3'] will triggger when a logic change specified by the keyword argument 'edge' occurs on either or the three specified trigger inputs. 
		+ edge: 'rising' or 'falling' . trigger edge type for trigger_channels.
+ Return: Nothing

</details>

<details>
<summary><code>start_one_channel_LA(self, **args)</code></summary>

+ Start logging timestamps of rising/falling edges on ID1
+ Arguments
	+ channel: ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']
	+ channel_mode: Acquisition mode, default value: 1
		+ EVERY_SIXTEENTH_RISING_EDGE = 5
		+ EVERY_FOURTH_RISING_EDGE    = 4
		+ EVERY_RISING_EDGE           = 3
		+ EVERY_FALLING_EDGE          = 2
		+ EVERY_EDGE                  = 1
		+ DISABLED                    = 0
+ Return: Nothing

</details>

<details>
<summary><code>start_two_channel_LA(self, **args)</code></summary>

+ Start logging timestamps of rising/falling edges on ID1, AD2
+ Arguments
	+ trigger: Bool. Enable rising edge trigger on ID1
	+ \*\*args
		+ chans: Channels to acquire data from . default ['ID1','ID2'] 
		+ mode: modes for each channel. Array, default value: [1,1]
			+ EVERY_SIXTEENTH_RISING_EDGE = 5
			+ EVERY_FOURTH_RISING_EDGE    = 4
			+ EVERY_RISING_EDGE           = 3
			+ EVERY_FALLING_EDGE          = 2
			+ EVERY_EDGE                  = 1
			+ DISABLED                    = 0
		+ maximum_time: Total time to sample. If total time exceeds 67 seconds, a prescaler will be used in the reference clock
+ Return: Nothing

</details>

<details>
<summary><code>start_three_channel_LA(self, **args)</code></summary>

+ Start logging timestamps of rising/falling edges on ID1, ID2, ID3
+ Arguments
	+ \*\*args
		+ trigger_channel: ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR'] 
		+ mode: modes for each channel. Array, default value: [1,1,1]
			+ EVERY_SIXTEENTH_RISING_EDGE = 5
			+ EVERY_FOURTH_RISING_EDGE    = 4
			+ EVERY_RISING_EDGE           = 3
			+ EVERY_FALLING_EDGE          = 2
			+ EVERY_EDGE                  = 1
			+ DISABLED                    = 0
		+ trigger_mode: Same as modes(previously documented keyword argument)
							default_value : 3
+ Return: Nothing

</details>

<details>
<summary><code>start_four_channel_LA(self, trigger = 1, maximum_time = 0.001, mode = [1, 1, 1, 1], **args)</code></summary>

+ Four channel Logic Analyzer. Start logging timestamps from a 64MHz counter to record level changes on ID1,ID2,ID3,ID4.
+ Arguments
	+ trigger: Bool . Enable rising edge trigger on ID1
	+ maximum_time: Maximum delay expected between two logic level changes. <br />
	If total time exceeds 1 mS, a prescaler will be used in the reference clock. However, this only refers to the maximum time between two successive level changes. If a delay larger than .26 S occurs, it will be truncated by modulo .26 S.<br />
If you need to record large intervals, try single channel/two channel modes which use 32 bit counters capable of time interval up to 67 seconds.
	+ mode: modes for each channel. Array, default value: [1,1,1]
		+ EVERY_SIXTEENTH_RISING_EDGE = 5
		+ EVERY_FOURTH_RISING_EDGE    = 4
		+ EVERY_RISING_EDGE           = 3
		+ EVERY_FALLING_EDGE          = 2
		+ EVERY_EDGE                  = 1
		+ DISABLED                    = 0
	+ trigger_mode: Same as modes(previously documented keyword argument)
							default_value : 3
+ Return: Nothing
+ See also: Use :func:`fetch_long_data_from_LA` (points to read,x) to get data acquired from channel x.The read data can be accessed from :class:`~ScienceLab.dchans` [x-1]

</details>

<details>
<summary><code>get_LA_initial_states(self)</code></summary>

+ Fetches the initial states of digital inputs that were recorded right before the Logic analyzer was started, and the total points each channel recorded
+ Returns: chan1 progress,chan2 progress,chan3 progress,chan4 progress,[ID1,ID2,ID3,ID4]. eg. [1,0,1,1]

</details>

<details>
<summary><code>stop_LA(self)</code></summary>

+ Stop any running logic analyzer function

</details>

<details>
<summary><code>fetch_int_data_from_LA(self, bytes, chan = 1)</code></summary>

+ Fetches the data stored by DMA. integer address increments
+ Arguments
	+ bytes: Number of readings(integers) to fetch
	+ chan: Channel number (1-4)

</details>

<details>
<summary><code>fetch_LA_channels(self)</code></summary>

+ Fetches the data stored by DMA. Integer address increments
+ Arguments
	+ bytes: Number of readings(integers) to fetch
	+ chan: Channel number (1-4)

</details>

<details>
<summary><code>fetch_long_data_from_LA(self, bytes, chan = 1)</code></summary>

+ Fetches the data stored by DMA. long address increments
+ Arguments
	+ bytes: Number of readings(long integers) to fetch
	+ chan: Channel number (1-2)

</details>

<details>
<summary><code>fetch_LA_channels(self)</code></summary>

+ Reads and stores the channels in self.dchans.

</details>

<details>
<summary><code>get_states(self)</code></summary>

+ Gets the state of the digital inputs.
+ Returns: dictionary with keys 'ID1','ID2','ID3','ID4'

</details>

<details>
<summary><code>get_state(self, input_id)</code></summary>

+ Returns the logic level on the specified input (ID1,ID2,ID3, or ID4)
+ Arguments
	+ input_id: the input channel
		+ 'ID1' -> state of ID1
		+ 'ID4' -> state of ID4
+ Return: boolean

```
>>> from pylab import *
>>> I = sciencelab.ScienceLab()
>>> self.__print__(I.get_state(I.ID1))
	False
```

</details>

<details>
<summary><code>set_state(self, **kwargs)</code></summary>

+ Set the logic level on digital outputs SQR1,SQR2,SQR3,SQR4
+ Arguments
	+ \*\*kwargs: SQR1,SQR2,SQR3,SQR4 <br />
		states(0 or 1)
```
>>> I.set_state(SQR1 = 1,SQR2 = 0)
#Sets SQR1 HIGH, SQR2 LOw, but leave SQR3,SQR4 untouched.	
```

</details>

<details>
<summary><code>countPulses(self, channel = 'SEN')</code></summary>

+ Count pulses on a digital input. Retrieve total pulses using readPulseCount
+ Arguments
	+ channel: The input pin to measure rising edges on : ['ID1','ID2','ID3','ID4','SEN','EXT','CNTR']

</details>

<details>
<summary><code>readPulseCount(self)</code></summary>

+ Read pulses counted using a digital input. Call countPulses before using this.

</details>

<details>
<summary><code>capacitance_via_RC_discharge(self)</code></summary><br />
</details>

<details>
<summary><code>get_capacitor_range(self)</code></summary>

+ Charges a capacitor connected to IN1 via a 20K resistor from a 3.3V source for a fixed interval
+ This function allows an estimation of the parameters to be used with the :func:`get_capacitance` function.
+ Returns: Capacitance calculated using the formula Vc = Vs(1-exp(-t/RC))

</details>

<details>
<summary><code>get_capacitance(self)</code></summary>

+ Measures capacitance of component connected between CAP and ground
+ Returns: Capacitance (F)

</details>

<details>
<summary><code>get_temperature(self)</code></summary>

+ Return the processor's temperature
+ Returns: Chip Temperature in degree Celcius

</details>

<details>
<summary><code>get_ctmu_voltage(self, channel, Crange, tgen = 1)</code></summary>

+ get_ctmu_voltage(5,2)  will activate a constant current source of 5.5uA on IN1 and then measure the voltage at the output.
+ If a diode is used to connect IN1 to ground, the forward voltage drop of the diode will be returned. e.g. .6V for a 4148diode.  
+ Returns: Voltage
+ Channel = 5 for IN1

| CRange   |      Implies  | 
|----------|:-------------:|
| 0		   |  550uA		   |
| 1		   |  0.55uA       |
| 2		   | 5.5uA         |
| 3		   | 55uA          |
    
</details>

<details>
<summary><code>resetHardware(self)</code></summary>

+ Resets the device, and standalone mode will be enabled if an OLED is connected to the I2C port

</details>

<details>
<summary><code>read_flash(self, page, location)</code></summary>

+ Reads 16 BYTES from the specified location
+ Arguments
	+ page: page number. 20 pages with 2KBytes each
	+ location: The flash location(0 to 63) to read from.
+ Return: String of 16 characters read from the location

</details>

<details>
<summary><code>read_bulk_flash(self, page, numbytes)</code></summary>

+ Reads BYTES from the specified location
+ Arguments
	+ page: Block number. 0-20. each block is 2kB.
	+ numbytes: Total bytes to read
+ Return: String of 16 characters read from the locationamps),Y1(Voltage at CH1),Y2(Voltage at CH2),Y3(Voltage at CH3),Y4(Voltage at CH4)

</details>

<details>
<summary><code>write_flash(self, page, location, string_to_write)</code></summary>

+ Write a 16 BYTE string to the selected location (0-63)
+ Arguments
	+ page: page number. 20 pages with 2KBytes each
	+ location: The flash location(0 to 63) to write to.
	+ string_to_write: String of 16 characters can be written to each location
+ Note: DO NOT USE THIS UNLESS YOU'RE ABSOLUTELY SURE KNOW THIS!
		YOU MAY END UP OVERWRITING THE CALIBRATION DATA, AND WILL HAVE
		TO GO THROUGH THE TROUBLE OF GETTING IT FROM THE MANUFACTURER AND
		REFLASHING IT.

</details>

<details>
<summary><code>write_bulk_flash(self, location, data)</code></summary>

+ Write a byte array to the entire flash page. Erases any other data
+ Arguments
	+ location: Block number. 0-20. each block is 2kB.
	+ bytearray: Array to dump onto flash. Max size 2048 bytes
+ Note: DO NOT USE THIS UNLESS YOU'RE ABSOLUTELY SURE KNOW THIS!
		YOU MAY END UP OVERWRITING THE CALIBRATION DATA, AND WILL HAVE
		TO GO THROUGH THE TROUBLE OF GETTING IT FROM THE MANUFACTURER AND
		REFLASHING IT.

</details>

## WAVEGEN SECTION

This section has commands related to waveform generators W1, W2, PWM outputs, servo motor control etc. 

<details>
<summary><code>set_wave(self, chan, freq)</code></summary>

+ Set the frequency of wavegen
+ Arguments
	+ chan: Channel to set frequency for. W1 or W2
	+ frequency: Frequency to set on wave generator
+ Returns: frequency

</details>

<details>
<summary><code>set_sine1(self, freq)</code></summary>

+ Set the frequency of wavegen 1 after setting its waveform type to sinusoidal
+ Arguments
	+ frequency: Frequency to set on wave generator 1.
+ Returns: frequency

</details>

<details>
<summary><code>set_sine2(self, freq)</code></summary>

+ Set the frequency of wavegen 2 after setting its waveform type to sinusoidal
+ Arguments
	+ frequency: Frequency to set on wave generator 1.
+ Returns: frequency

</details>

<details>
<summary><code>set_w1(self, freq, waveType = None)</code></summary>

+ Set the frequency of wavegen 1
+ Arguments
	+ frequency: Frequency to set on wave generator 1.
	+ waveType: 'sine','tria' . Default : Do not reload table, and use last set table
+ Returns: frequency

</details>

<details>
<summary><code>set_w2(self, freq, waveType = None)</code></summary>

+ Set the frequency of wavegen 2
+ Arguments
	+ frequency: Frequency to set on wave generator 2.
+ Returns: frequency

</details>

<details>
<summary><code>readbackWavefrom(self, chan)</code></summary>

+ Set the frequency of wavegen 1
+ Arguments
	+ chan: Any of W1,W2,SQR1,SQR2,SQR3,SQR4
+ Returns: frequency

</details>

<details>
<summary><code>set_waves(self, freq, phase, f2 = None)</code></summary>

+ Set the frequency of wavegen
+ Arguments
	+ frequency: Frequency to set on both wave generators
	+ phase: Phase difference between the two. 0-360 degrees
	+ f2: Only specify if you require two separate frequencies to be set
+ Returns: frequency

</details>

<details>
<summary><code>load_equation(self, chan, function, span = None, **kwargs)</code></summary>

+ Load an arbitrary waveform to the waveform generators
+ Arguments
	+ chan: The waveform generator to alter. W1 or W2
	+ function: A function that will be used to generate the datapoints
	+ span: The range of values in which to evaluate the given function

```
fn = lambda x:abs(x-50)  #Triangular waveform
self.I.load_waveform('W1',fn,[0,100])
#Load triangular wave to wavegen 1
#Load sinusoidal wave to wavegen 2
self.I.load_waveform('W2',np.sin,[0,2*np.pi])
```

</details>

<details>
<summary><code>load_table(self, chan, points, mode = 'arbit', **kwargs)</code></summary>

+ Load an arbitrary waveform table to the waveform generators
+ Arguments
	+ chan: The waveform generator to alter. 'W1' or 'W2'
	+ points: A list of 512 datapoints exactly
	+ mode: Optional argument. Type of waveform. default value 'arbit'. accepts 'sine', 'tria'

```
>>> self.I.load_waveform_table(1,range(512))
#Load sawtooth wave to wavegen 1
```

</details>

<details>
<summary><code>sqr1(self, freq, duty_cycle = 50, onlyPrepare = False)</code></summary>

+ Set the frequency of sqr1
+ Arguments
	+ frequency: Frequency
	+ duty_cycle: Percentage of high time

</details>

<details>
<summary><code>sqr1_pattern(self, timing_array)</code></summary>

+ output a preset sqr1 frequency in fixed intervals. Can be used for sending IR signals that are packets of 38KHz pulses.
+ Arguments
	+ timing_array: A list of on & off times in uS units

```
>>> I.sqr1(38e3 , 50, True )   # Prepare a 38KHz, 50% square wave. Do not output it yet
>>> I.sqr1_pattern([1000,1000,1000,1000,1000])  #On:1mS (38KHz packet), Off:1mS, On:1mS (38KHz packet), Off:1mS, On:1mS (38KHz packet), Off: indefinitely..
```

</details>

<details>
<summary><code>sqr2(self, freq, duty_cycle)</code></summary>

+ Set the frequency of sqr2
+ Arguments
	+ frequency: Frequency
	+ duty_cycle: Percentage of high time

</details>

<details>
<summary><code>set_sqrs(self, wavelength, phase, high_time1, high_time2, prescaler = 1)</code></summary>

+ Set the frequency of sqr1,sqr2, with phase shift
+ Arguments
	+ wavelength: Number of 64Mhz/prescaler clock cycles per wave
	+ phase: Clock cycles between rising edges of SQR1 and SQR2
	+ high time1: Clock cycles for which SQR1 must be HIGH
	+ high time2: Clock cycles for which SQR2 must be HIGH
	+ prescaler: 0,1,2. Divides the 64Mhz clock by 8,64, or 256

</details>

<details>
<summary><code>sqrPWM(self, freq, h0, p1, h1, p2, h2, p3, h3, **kwargs)</code></summary>

+ Initialize phase correlated square waves on SQR1,SQR2,SQR3,SQR4
+ Arguments
	+ freq: Frequency in Hertz
	+ h0: Duty Cycle for SQR1 (0-1)
	+ p1: Phase shift for SQR2 (0-1)
	+ h1: Duty Cycle for SQR2 (0-1)
	+ p2: Phase shift for OD1  (0-1)
	+ h2: Duty Cycle for OD1  (0-1)
	+ p3: Phase shift for OD2  (0-1)
	+ h3: Duty Cycle for OD2  (0-1)

</details>

<details>
<summary><code>map_reference_clock(self, scaler, *args)</code></summary>

+ Map the internal oscillator output  to SQR1,SQR2,SQR3,SQR4 or WAVEGEN
+ The output frequency is 128/(1<<scaler) MHz

scaler [0-15]

* 0 -> 128MHz
* 1 -> 64MHz
* 2 -> 32MHz
* 3 -> 16MHz
* .
* .
* 15 ->128./32768 MHz

```
>>> I.map_reference_clock(2,'SQR1','SQR2')
```
Outputs 32 MHz on SQR1, SQR2 pins

+Note: If you change the reference clock for 'wavegen' , the external waveform generator(AD9833) resolution and range will also change. Default frequency for 'wavegen' is 16MHz. Setting to 1MHz will give you 16 times better resolution, but a usable range of 0Hz to about 100KHz instead of the original 2MHz.

</details>

## ANALOG OUTPUTS
This section has commands related to current and voltage sources PV1,PV2,PV3,PCS

<details>
<summary><code>set_pv1(self, val)</code></summary>

+ Set the voltage on PV1
+ 12-bit DAC...  -5V to 5V
+ Arguments
	+ val: Output voltage on PV1. -5V to 5V

</details>
 
<details>
<summary><code>set_pv2(self, val)</code></summary>

+ Set the voltage on PV2
+ 12-bit DAC...  0-3.3V
+ Arguments
	+ val: Output voltage on PV2. 0-3.3V
+ Return: Actual value set on pv2

</details>

<details>
<summary><code>set_pv3(self, val)</code></summary>

+ Set the voltage on PV3
+ Arguments
	+ val: Output voltage on PV3. 0V to 3.3V
+ Return: Actual value set on pv3

</details>

<details>
<summary><code>set_pcs(self, val)</code></summary>

+ Set programmable current source
+ Arguments
	+ val: Output current on PCS. 0 to 3.3mA. Subject to load resistance. Read voltage on PCS to check.
+ Return: value attempted to set on pcs

</details>

<details>
<summary><code>get_pv1(self)</code></summary>

+ Get the last set voltage on PV1
+ 12-bit DAC...  -5V to 5V

</details>

<details>
<summary><code>get_pv2(self)</code></summary>

+ Get the last set voltage on PV2

</details>

<details>
<summary><code>get_pv3(self)</code></summary>

+ Get the last set voltage on PV3

</details>
 
<details>
<summary><code>get_pcs(self)</code></summary>

+ Get the last set voltage on PCS

</details>
 
<details>
<summary><code>WS2812B(self, cols, output = 'CS1')</code></summary>

+ Set shade of WS2182 LED on SQR1
+ Arguments
	+ cols: 2Darray [[R,G,B],[R2,G2,B2],[R3,G3,B3]...] <br /> 
			brightness of R,G,B ( 0-255  )

```
>>> I.WS2812B([[10,0,0],[0,10,10],[10,0,10]])
#sets red, cyan, magenta to three daisy chained LEDs
```

</details>

## READ PROGRAM AND DATA ADDRESSES
Direct access to RAM and FLASH

<details>
<summary><code>read_program_address(self, address)</code></summary>

+ Reads and returns the value stored at the specified address in program memory
+ Arguments
	+ address: Address to read from. Refer to PIC24EP64GP204 programming manual

</details>
 
<details>
<summary><code>device_id(self)</code></summary><br />
</details>
 
<details>
<summary><code>read_data_address(self, address)</code></summary>

+ Reads and returns the value stored at the specified address in RAM
+ Arguments
	+ address: Address to read from.  Refer to PIC24EP64GP204 programming manual 

</details>
 
## MOTOR SIGNALLING
Set servo motor angles via SQ1-4. Control one stepper motor using SQ1-4

<details>
<summary><code>stepForward(self, steps, delay)</code></summary>

+ Control stepper motors using SQR1-4
+ Take a fixed number of steps in the forward direction with a certain delay( in milliseconds ) between each step.

</details>
 
<details>
<summary><code>stepBackward(self, steps, delay)</code></summary>

+ Control stepper motors using SQR1-4
+ Take a fixed number of steps in the backward direction with a certain delay( in milliseconds ) between each step.

</details>
 
<details>
<summary><code>servo(self, angle, chan = 'SQR1')</code></summary>

+ Output A PWM waveform on SQR1/SQR2 corresponding to the angle specified in the arguments.
+ This is used to operate servo motors. Tested with 9G SG-90 Servo motor.
+ Arguments
	+ angle: 0-180. Angle corresponding to which the PWM waveform is generated.
	+ chan: 'SQR1' or 'SQR2'. Whether to use SQ1 or SQ2 to output the PWM waveform used by the servo

</details>
 
<details>
<summary><code>servo4(self, a1, a2, a3, a4)</code></summary>

+ Operate Four servo motors independently using SQR1, SQR2, SQR3, SQR4.
+ tested with SG-90 9G servos.
+ For high current servos, please use a different power source, and a level convertor for the PWm output signals(if needed)
+ Arguments
	+ a1: Angle to set on Servo which uses SQR1 as PWM input. [0-180]
	+ a2: Angle to set on Servo which uses SQR2 as PWM input. [0-180]
	+ a3: Angle to set on Servo which uses SQR3 as PWM input. [0-180]
	+ a4: Angle to set on Servo which uses SQR4 as PWM input. [0-180]

</details>
 
<details>
<summary><code>enableUartPassthrough(self, baudrate, persist = False)</code></summary>

+ All data received by the device is relayed to an external port(SCL[TX],SDA[RX]) after this function is called.
+ If a period > .5 seconds elapses between two transmit/receive events, the device resets and resumes normal mode. This timeout feature has been implemented in lieu of a hard reset option.
+ Can be used to load programs into secondary microcontrollers with bootloaders such ATMEGA, and ESP8266
+ Arguments
	+ baudrate: BAUDRATE to use
	+ persist: If set to True, the device will stay in passthrough mode until the next power cycle. <br />
	Otherwise(default scenario), the device will return to normal operation if no data is sent/received for a period greater than one second at a time.

</details>
 
<details>
<summary><code>estimateDistance(self)</code></summary>

+ Read data from ultrasonic distance sensor HC-SR04/HC-SR05.  Sensors must have separate trigger and output pins.
+ First a 10uS pulse is output on SQR1.  SQR1 must be connected to the TRIG pin on the sensor prior to use.
+ Upon receiving this pulse, the sensor emits a sequence of sound pulses, and the logic level of its output pin(which we will monitor via ID1) is also set high.  The logic level goes LOW when the sound packet returns to the sensor, or when a timeout occurs.
+ The ultrasound sensor outputs a series of 8 sound pulses at 40KHz which corresponds to a time period of 25uS per pulse. These pulses reflect off of the nearest object in front of the sensor, and return to it. The time between sending and receiving of the pulse packet is used to estimate the distance. If the reflecting object is either too far away or absorbs sound, less than 8 pulses may be received, and this can cause a measurement error of 25uS which corresponds to 8mm.
+ Ensure 5V supply.  You may set SQR2 to HIGH [ I.set_state(SQR2 = True) ] , and use that as the power supply.
+ Return: 0 upon timeout

</details>
 
<details>
<summary><code>opticalArray(self, SS, delay, channel = 'CH3', **kwargs)</code></summary>

+ Read from 3648 element optical sensor array TCD3648P from Toshiba. Experimental feature. Neither Sine waves will be available.
+ Connect SQR1 to MS , SQR2 to MS , A0 to CHannel , and CS1(on the expansion slot) to ICG
+ delay : ICG low duration
+ tp : clock wavelength = tp*15nS,  SS = clock/4

</details>
 
<details>
<summary><code>setUARTBAUD(self, BAUD)</code></summary><br />
</details>
 
<details>
<summary><code>writeUART(self, character)</code></summary><br />
</details>
 
<details>
<summary><code>readUART(self)</code></summary><br />
</details>
 
<details>
<summary><code>readUARTStatus(self)</code></summary>

+ Return: available bytes in UART buffer

</details>
 
<details>
<summary><code>readLog(self)</code></summary>

+ Read hardware debug log.

</details>
 
<details>
<summary><code>raiseException(self, ex, msg)</code></summary><br />
</details>
