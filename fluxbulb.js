var REST_URL = "http://fluxbulb.hackmason.org:3000/"

if (Meteor.isClient) {

  Template.standardInterface.show = function() {return Session.get("controlType") == "standard"}
  Template.intervalInterface.show = function() {return Session.get("controlType") == "interval"}
  Template.constantInterface.show = function() {return Session.get("controlType") == "constant"}

  Template.navlist.events({
  	'click #standard': function() {
  		Session.set("controlType", "standard");
  	},
  	'click #interval': function() {
  		Session.set("controlType", "interval");
  	},
  	'click #constant': function() {
  		Session.set("controlType", "constant");
  	}
  })

  Template.constantInterface.events({
  	'click .btn': function() {
  		var val = $("#const_control0").val()
  		console.log(val)
  		console.log(REST_URL + "setConstant/" + val)
  		console.log(REST_URL + "setType/" + "constant")
  		var xhr = createCORSRequest('GET', REST_URL + "setConstant/" + val);
  		xhr.onload = function() {
		 var responseText = xhr.responseText;
 			console.log(responseText);
 			// process the response.
			};
			xhr.onerror = function() {
  console.log('There was an error!');
};
		xhr.send();


  		    // xhr = createCORSRequest('GET', REST_URL + "setType/" + "constant");
		if (!xhr) {
		  throw new Error('CORS not supported');
		}
  		console.log("requesting")

  	}
  })

  Template.intervalInterface.events({
  	'click .btn': function() {
  		console.log("interval set" + $("#interval_control0").val());
  	}
  })

}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}

































function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {

    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);

  } else if (typeof XDomainRequest != "undefined") {

    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);

  } else {

    // Otherwise, CORS is not supported by the browser.
    console.log("this is bad");
    xhr = null;

  }
  return xhr;
}
