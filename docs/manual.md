# Manual for PSLab by FOSSASIA

## Table of Content
1. Introduction
2. Layout
3. Installation
4. Setting up for Experiments
    - Blinking bulb
    - Microphone
    - Read resistance
    - Analyze a Zener diode

## Introduction
PSLab device is an open source hardware platform that can be used by college and high school students, teachers, undergraduates and hobbyists in their experiments and projects. The device is equipped with a set of debugging and analyzing tools such as oscilloscope, logic analyzer, waveform generator, programmable voltage and current source, multimeter and data logger.

PSLab device uses a PIC microcontroller as the central processing unit. The following diagram illustrates the block diagram of the PSLab device and how it is analyzing and presenting captured data.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/blockdiag.png" alt="Block Diagram">
</p>

## Layout
The PSLab device has 36 pins.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/pslab_layout.png" alt="PSLab device layout">
</p>

- GND : Creates a ground connection
- SQR(1-4) : Pins creating PWM waves
- ID(1-4) : Logic analyzer connections
- W(1-2) : Sine or Triangular waves
- PCS : Programmable Current Source
    - PCS → 0 mA ~ 3.3 mA
- PV(1-3) : Programmable Voltage Source
    - PV1 → -5V ~ +5V
    - PV2 → -3.3V ~ +3.3V
    - PV3 → 0V ~ +3.3V
- CH(1-3) : Oscilloscope input channels
- AC1 : Oscilloscope input channel (A/C)
- SEN : Resistance measurement / Sensor inputs
- CAP : Capacitor measurement
- MIC : Microphone in
- I2C set : I2C connectors
- W1 : Knob to control W1 frequency

## Installation

PSLab desktop application requires the following libraries pre-installed in the PC running Linux.

- PyQt 4.7
- python 2.6, 2.7, or 3.x
- NumPy, Scipy
- pyqt4-dev-tools
- Pyqtgraph
- pyopengl and qt-opengl
- iPython-qtconsole

The installation can be performed by running the `installer.sh` script as follows;
First download the installer.sh file from the following link. You may right click on the link and click "Save Link As..." to save the file.

[Installer.sh](https://github.com/fossasia/pslab-desktop-apps/blob/development/installer.sh)

Then browse to the folder where the `installer.sh` file was downloaded and type the following commands.

```
$ sudo chmod +x installer.sh
```

```
$ sudo ./installer.sh
```

Once the installation is complete, it will prompt to open the PSLab desktop application. By typing “Y” it will open the PSLab desktop application window.

The window will be reddish if the device is not connected or not configured properly. It will turn bluish when the device is connected.

## Setting up for Experiments

As a starter, few basic experiments can be performed using the device and the electronic components package. It consists of resistors with several values, capacitors with different capacities, few LED bulbs, transistor, microphone, small bread board and a few jumper wires.

### Blinking Bulb

This experiment demonstrates how to use square wave generation feature with the PSLab device.

#### Required components:

- PSLab device
- Personal Computer
- LED bulb
- 220 Ohm resistor
- Breadboard
- Two jumper wires

Setup the components according to the following figure.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/circuit_blinking_led.JPG" alt="Circuit Blinking LED">
</p>

Connect the positive pin of the LED bulb to the 220 Ohm resistor and connect a red wire to it. Then connect the red wire to the SQR1 pin and the yellow wire to the GND pin.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/schematic_blinking_led.png" alt="Schematic Blinking LED" width=500>
</p>

Following figure will help identifying the positive and negative pins of an LED bulb.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/led_pins.png" alt="LED Pins" width=200>
</p>

Note that the wires do not need to be in the same colors as illustrated in the figure.

Now connect the PSLab to computer and start the desktop application by executing the command “Experiments” in the console

Once the application is open, browse to “Adv.Control” tab to the left. In the “Configure PWM” section, there are 8 text boxes. We will be using the SQR1 Duty Cycle text box in this experiment. Type 0.800 in the SQR1 textbox and click on “Set” button and observe the LED bulb is lit. If it is not, check the circuit for any loose connections or if the LED pins are connected with polarity correctly.

<p align="center">
  <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_blinking_led.png" alt="Screen Blinking">
</p>

Now type 0.300 in SQR1 textbox and observe the intensity of the LED bulb reducing.

Continue the experiment with different values between 0 and 1 and observe how the intensity varies proportional to the value entered. The similar results can be generated using other three SQR pins. We can even connect four LED bulbs on the same breadboard and compare intensity using different duty cycle values to each text box.

### Microphone

This experiment demonstrates how to use and observe waveforms using the oscilloscope.

#### Required components:

- PSLab device
- Personal Computer
- Microphone

Setup the components according to the following figure. The red wire is the positive pin of the microphone and the orange wire is the negative pin of the microphone. Connect the wires correctly.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/circuit_microphone.JPG" alt="Circuit microphone">
</p>

Now connect the PSLab to computer and start the desktop application by executing the command “Experiments” in the console.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_microphone.png" alt="Screen microphone">
</p>

Once the application is open browse to oscilloscope. Select “MIC” channel and adjust the time axis resolution to different values to observe the variation of the ambient sound. Now speak to the microphone and observe the waveform is changing rapidly according to the sound.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_microphone2.png" alt="Screen microphone">
</p>

We can adjust the time axis range from “Timebase” knob and amplitude range from “Range” combo boxes against “Chan 1”.

### Read Resistance

This experiment demonstrates how to read resistance value using the PSLab device. The similar methodology is applicable to measure capacitance as well.

#### Required components:

- PSLab device
- Personal Computer
- Breadboard
- Resistor with any value
- Two jumper wires

Setup the components according to the following figure.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/circuit_resistance_measurement.JPG" alt="Circuit resistance measurement">
</p>

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/schematic_resistance_measurement.png" alt="Schematic resistance measurement"  width=400>
</p>

Now connect the PSLab to computer and start the desktop application by executing the command “Experiments” in the console.

Then browse to “Controls” tab to the left. Click “Read” button in the “Resistance” section, and observe the resistance value is read and displayed.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_resistance_measurement.png" alt="Screen resistance measurement">
</p>

A similar procedure can be carried out to measure capacitance. Using the “Read” button in “Capacitance” section, we can measure the capacitor value by connecting a capacitor across CAP pin and GND pin.

PSLab device also supports a pulse counter. Using the “Count Pulses” section we can read how many pulses are recorded through the ID(1-4) pins.

The same window is capable of generating waveforms and voltage, current sources.

Wave(1-2) is capable of generating sine or triangular waveforms while Square1 is capable of generating PWM waveforms.

PV(1-3) is capable of generating constant voltage sources from -5 V to +5 V as follows;

- PV1 → -5V ~ +5V
- PV2 → -3.3V ~ +3.3V
- PV3 → 0V ~ +3.3V
- PCS is capable of generating constant current from 0 mA to 3.3 mA. Note that the maximum current of 3.3 mA can be achieved only when the load is less than 200 Ohms.

The current is limited as the USB connection and the microcontroller cannot handle higher currents through them.

### Analyze a Zener Diode

This experiment demonstrates how to perform a built in experiment using the PSLab device. The desktop application supports over 70 pre built experiments. They are listed on the top bar of the desktop application. Experiments are categorized into electronic related experiments, electrical related experiment, school level experiments and experiments including various implementations.

#### Required components:

- PSLab device
- Personal Computer
- Breadboard
- Zener diode
- 1K Ohm resistor
- Three jumper wires

Setup the components according to the following figure

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/circuit_zener_characteristics.JPG" alt="Circuit Zener Characteristics">
</p>

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/schematic_zener_characteristics.png" alt="Schematic Zener Characteristics"  width=400>
</p>

Now connect the PSLab to computer and start the desktop application by executing the command “Experiments” in the console.

On the top side of the screen contains a combo box with link to all the built in experiments. Click on the “Electronics Experiments”. It will open a window like the one below. Click on the “Zener IV Characteristics” to begin with the experiment.

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_zener_characteristics.png" alt="Zener Characteristics">
</p>

Set Initial voltage value to -5V and Final voltage value to +5V. Step size will improve the smoothness of the curve generated by the experiment. Set it to 0.02V and click “Start”

<p align="center">
    <img src="https://github.com/fossasia/pslab-desktop-apps/blob/development/docs/images/screen_zener_characteristics2.png" alt="Zener Characteristics 2">
</p>

Now you can observe a graph being plotted as the following figure which is similar to the characteristics curve of a zener diode. You can change the diode and click “Start” again. It will plot another figure on top of the existing figure.

By selecting the number ID from “Acquired Data” section, you can delete the specified plot and keep the ones you want.
