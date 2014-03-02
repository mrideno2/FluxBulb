var REST_URL = "http://fluxbulb.hackmason.org:3000/"

if (Meteor.isClient) {

  Template.standardInterface.show = function() {return Session.get("controlType") == "standard"}
  Template.intervalInterface.show = function() {return Session.get("controlType") == "interval"}
  Template.constantInterface.show = function() {return Session.get("controlType") == "constant"}

  Template.navlist.events({
  	'click #standard': function() {
  		Session.set("controlType", "standard");
      restGet("setType/standard")
      $("#rdS").prop("checked", true)
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
      restGet("setConstant/" + val);
      restGet("setType/constant");
      $("#rdC").prop("checked", true)
  	}
  })

  Template.intervalInterface.events({
  	'click .btn': function() {
      var val = $("#interval_control0").val()
      if (val == "") return
      restGet("setInterval/" + val)
      restGet("setType/interval")
      // $("[type='radio']").removeClass("emboldened")
      $("#rdI").prop("checked", true)
      // $("#rdI > div").addClass("emboldened")

  	}
  })

}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}





function restGet(method) {
  var url = REST_URL + method

  console.log(url)

  $.ajax(url, {
        type:"GET",
        dataType:"jsonp",
        data:{action:"something"}, 
        success:function(data, textStatus, jqXHR) {console.log("success");},
        error: function(jqXHR, textStatus, errorThrown) {console.log("failure");}
  });
}
