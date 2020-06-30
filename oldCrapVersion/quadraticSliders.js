// this function doesn't do anything right now and has global vars which aren't declared yet so will probably never work
/*var totalUsed = document.getElementById("total");
function updateTotal(){
	var t = squared0.value + squared1.value;
    return t;
}*/

var max_points = 100;
var t=0;

var slider0 = document.getElementById("r0");
var output0 = document.getElementById("s0");
var squared0 = document.getElementById("sqrdVal0");

output0.innerHTML = slider0.value;

slider0.oninput = function() {
  output0.innerHTML = this.value;
  //s0.textContent = (output0.innerHTML).toFixed(2);
  squared0.innerHTML = this.value * this.value;
}
//----------------------------

var slider1 = document.getElementById("r1");
var output1 = document.getElementById("s1");
var squared1 = document.getElementById("sqrdVal1");
  
output1.innerHTML = slider1.value;

slider1.oninput = function() {
  output1.innerHTML = this.value;
  squared1.innerHTML = this.value * this.value;
}
//----------------------------
var slider2 = document.getElementById("r2");
var output2 = document.getElementById("s2");
var squared2 = document.getElementById("sqrdVal2");
  
output1.innerHTML = slider1.value;

slider2.oninput = function() {
  output2.innerHTML = this.value;
  squared2.innerHTML = this.value * this.value;
}
//----------------------------


const f_update = (() => { t = Number(squared0.innerHTML) + Number(squared1.innerHTML) + Number(squared2.innerHTML);
							total.textContent = t.toFixed(2);
							remaining.textContent = (max_points - t).toFixed(2)});
slider0.addEventListener ("input", f_update , false);
slider1.addEventListener ("input", f_update , false);
slider2.addEventListener ("input", f_update , false);
