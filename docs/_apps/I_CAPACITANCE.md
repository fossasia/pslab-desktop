<html>
  <head>
    <meta content="text/html; charset=windows-1252" http-equiv="content-type">
  </head>

  <body>
	<h3>Make your own parallel plate capacitor</h3>
	<img src="images/pPlate.svg" style="width:100%;max-width:500px;"><br><br>
	Stick a square piece of aluminium tape on either side of a piece of butter paper. Ensure that the two plates do not touch each other along the edges, and are separated by the butter paper.<br>
	Connect one plate to SEN, and the other to GND, and measure the capacitance.<br>
	Now cut this capacitor along the center, such that the area is reduced by half, and measure capacitance again.<br>
	<h3>Study how capacitors behave in combination</h3>
    Measure the values of the capacitors by individually connecting them between CAP and GND, and note these.<br>
	<img src="images/CMeasure.svg" style="width:100%;max-width:500px;"><br><br>
	<h3>In Parallel</h3>
    Connect the two capacitors in parallel as shown below, and observe the combined capacitance. Ctotal = C1+C2.<br>
	<img src="images/CParallelSimple.svg" style="width:100%;max-width:500px;"><br><br>
	<h3>In Series</h3>
	Now connect them in series, and measure the net capacitance <br>
	<img src="images/CSeriesSimple.svg" style="width:100%;max-width:500px;"><br><br>
	
	Calculate net capacitance of capacitors connected in series.<br>
	<form name="form2">
	R1  :<input type="text" size="20" name="r1" value = "100">pF<br>
	R2  :<input type="text" size="20" name="r2" value = "100">pF<br>
	<input type="button" name="B1" value="Calculate" onclick="cal2()"><br>
	Total capacitance:<input type="text" size="20" name="answer">pF<br>
	</form>

	 
	<script>
	function cal2(){
		var r1,r2;
		r1 = document.form2.r1.value;
		r2 = document.form2.r2.value;
		document.form2.answer.value=r1*r2/(r1+r2);
	}
	</script>



	<h3>Screenshot</h3>
	<img src="screenshots/capacitance_measurement.png" width="100%"><br>


  </body>

</html>
