console.log("hello out here")
function buildPlot() {
    /* data route */
  var url = "/api/v1.0/consumptionsector";
  d3.json(url).then(function(response) {
    console.log("hello in here")
    console.log(response);

    
  });
}

buildPlot();
