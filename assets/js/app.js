console.log("hello out here")
function buildPlot() {
    /* data route */
  var url = "/api/v1.0/statess";
  d3.json(url).then(function(response) {

    console.log(response);

    
  });
}

buildPlot();
