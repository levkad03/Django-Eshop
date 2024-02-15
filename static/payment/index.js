var stripe = Stripe(
  "pk_test_51Ok36zGN46pmt5AWmxaq5XDGZvjDorLrw5PLiFhoVK00N1mNKOLrtUsgXqZSaXn6tXZSEepRhN3MBaPDlRuLRI8x00eY9l9qsO"
);

var elem = document.getElementById("submit");
clientsecret = elem.getAttribute("data-secret");

// Setup Stripe.js and Elements
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    lineHeight: "2.4",
    fontSize: "16px",
  },
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on("change", function (event) {
  var displayError = document.getElementById("card-errors");
  if (event.error) {
    displayError.textContent = event.error.message;
    $("#card-errors").addClass("alert alert-info");
  } else {
    displayError.textContent = "";
    $("#card-errors").removeClass("alert alert-info");
  }
});
