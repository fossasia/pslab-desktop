<html>
  <head>
    <meta content="text/html; charset=windows-1252" http-equiv="content-type">
    <title>Experiment Designer</title>
  </head>
  <body style = "background-color:#fff">Experiment Designer<br>
	<img src="images/astable-trans.svg" style="width:100%;max-width:500px;"><br>

Experiment Designer allows you to define the control and readback sequences of parameters and execute them, explained below
using Transistor CE characteristics as an example.<br><br>

To plot Vc vs Ic, we need to:<br>
1. Select a base current by setting the value of PV2.<br>
2. Sweep PV1 from 0 to 5V in steps and read CH1 (Vc) in each step. <br>
3. Calculate Ic by the equation (PV1 - CH1)/Rc<br>
4. Plot CH1 vs Ic<br>

Step 1: Select PV2 for manual control and PV1 for sweep as shown below.<br>
        Add a derived parameter for Ic using the format I = (PV1() - CH1())/1000, the empty parantheses are
        necessary in the equation.        <br>
	<h3>Screenshot</h3>
	<img src="screenshots/design2a.png" width="100%"><br>


	<h3>Screenshot</h3>
	<img src="screenshots/design3.png" width="100%"><br>

	<h3>Screenshot</h3>
	<img src="screenshots/design4.png" width="100%"><br>
	
	<h3>Screenshot</h3>
	<img src="screenshots/design5.png" width="100%"><br>

	<h3>Screenshot</h3>
	<img src="screenshots/design6.png" width="100%"><br>


  </body>
</html>
