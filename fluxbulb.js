if (Meteor.isClient) {
  Template.hello.greeting = function () {
    return "Welcome to fluxbulb.";
  };

  Template.hello.events({
    'click input': function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
    }
  });

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

}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
