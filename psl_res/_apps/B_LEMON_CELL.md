---
layout: expt
title: Lemon cell
date: 2017-05-21
description: experiments with a lemon cell
---


## Measure the voltage of a lemon cell

![](images/schematics/lemon_cell.png){: width="250px"}

Make the connections as shown in the figure. Use a copper wire, and a galvanized(coated with zinc) nail as the two electrodes. 
Observe the voltmeter for CH1 ,and note the values . Also observe, that the graph for CH1 is a straight line. This is because the voltage is constant.

## Measure the internal resistance of a lemon cell

![](images/schematics/lemon_cell_ir.png){: width="250px"}

The purpose of this section is to understand why the lemon cell is not adequate to supply high currents.
Connect a 1000 (1K) Ohm resistor across the lemon cell, and observe that the voltage has now reduced.

This is a consequence of the internal resistance of the lemon cell, and using the measured voltage difference caused by connecting this resistor, we can calculate it.
The current flowing through the circuit with the load resistor connected, according to Ohm's law, is I = V/R = V(CH1)/1000 .
The voltage drop = ( V(CH1) without R connected - V(CH1) with R connected ) 
Internal resistance = voltage drop/current(I) 
	

Enter the measured values in the following boxes and click to calculate the internal resistance
<form name="form2">
V(CH1) without R  :<input type="text" size="20" name="v1">Volts<br>
V(CH1) with R  :<input type="text" size="20" name="v2">Volts<br>
Series Resistance :<input type="text" size="20" name="r1" value="1000">Ohms<br>
<input type="button" name="B1" value="Calculate" onclick="cal2()"><br>
Internal Resistance:<input type="text" size="20" name="answer">Ohms<br>
</form>

	 
<script>
function cal2(){
	var v1,v2,r1,i;
	r1 = document.form2.r1.value;
	v1 = document.form2.v1.value;
	v2 = document.form2.v2.value;
	i = v2/r1 ;
	document.form2.answer.value=(v1-v2)/i;
}
</script>

	
![](images/schematics/lemon_battery.png){: width="500px"}

Connect three lemon cells in series, and note the voltage. Try connecting an LED to this battery.
	
### Screenshot
![](images/screenshots/lemoncell.png)

