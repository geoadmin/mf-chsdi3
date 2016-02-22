// Create IE + others comaptible event handler
var eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
var eventer = window[eventMethod];
var messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";

// Listen to message from child window
eventer(messageEvent, function(e) {
  $('.feature-id').html(e.data.id);
  $('.feature-name').html(e.data.properties.name);
  $('.layer-id').html(e.data.properties.layerId);
}, false);
