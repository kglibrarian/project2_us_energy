function buildCharts(sample) {

    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var chartsURL = "/api/v1.0/consumptionsector";
    d3.json(chartsURL).then(function (data) {
    // var data = [data];
    var data = [{
        values: data.Residential,
        labels: data.State,
        hovertext: data.State,
        type: 'pie',
    }];
    
    var layout = {
    showlegend: true,
    height: 400,
    width: 500,
    };

    Plotly.newPlot('pie', data, layout);
    })
}
buildCharts();  
    //  @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    //var data = [{
    //    values: data.Residential,
    //    labels: data.State['Illinois'],
//         hovertext: data.State['Illinois'],
//         type: 'pie',
//         }];
//         var layout = {
//             showlegend: true,
//         };
//         Plotly.newPlot('pie', data, layout); 
//     }
// )}
  

// // function optionChanged(newSample) {
//     // Fetch new data each time a new sample is selected
//     // buildCharts(newSample);
// // }
  