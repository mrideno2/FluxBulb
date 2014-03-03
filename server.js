var express = require('express');
var app = express();


var fluxType = "not set";
var fluxConstant = "not set";
var fluxInterval = "not set";

var passToArduino = "0";

app.get('/setType/:value', function(req,res) {
  res.type('jsonp');
  t = req.params.value;
  if (t == "standard" || t == "constant" || t == "interval" || t == "motion") {
  	fluxType=req.params.value;
  	res.jsonp({msg:"type set"})
  }
  else {
  	res.jsonp({msg:"bad type"})
  	console.log("bad type!")
  }
});

app.get('/setConstant/:value', function(req, res) {
  res.type('jsonp');
  t = (parseInt(req.params.value));
  console.log(">" + req.params.vaue + "<" + "   >" + t + "<");
  if (isNaN(t)) {
  	console.log("sending bad");
  	res.jsonp({msg:'bad constant'})
  }
  else { 
  	console.log("evaluating as number"); 

  	if (t > 0 && t < 255) {
  	fluxConstant = t
  	res.jsonp({msg:'set constant'});
  }}
});

app.get('/setInterval/:seconds', function(req,res) {
  res.type('jsonp')
  t = parseFloat(req.params.seconds);
  console.log(t);
  if (isNaN(t)) {
  	console.log("seconds is NaN");
  	res.jsonp({msg:'bad float'})
  } else {
  	fluxInterval = t;
  	res.jsonp({msg:'interval set'});
  }
});

app.get('/arduinoCommand', function(req, res) {
	res.type('text/plain')
	if (fluxType == "standard")
		res.send("s")
	else if (fluxType == "constant")
		res.send("c" + fluxConstant)
	else if (fluxType == "interval")
		res.send("i" + fluxInterval)
	else if (fluxType == "motion")
    res.send("m")
  else {
		console.log("bad type?")
		res.send("0");
	}

});

app.listen(process.env.PORT || 3000);

app.get('/hi', function(req, res) {
  res.type('jsonp')
  res.jsonp({user: 'tobi'});
});