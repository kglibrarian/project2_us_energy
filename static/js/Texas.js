//Texas-Piechart (Consumption by Sector)
function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/consumptionsector";
  d3.json(chartsURL).then(function (data) {
    var data = data[2]; 
    ind_key = Object.keys(data);
    ind_val = Object.values(data);
    
    var chart = [{
      values: ind_val,
      labels: ind_key,
      type: 'pie'
    }];

    var layout = {
      autosize: true,
      title: {
        text: 'Energy Consumption <br> by End-User Sector 2017',
        font: {
        size: 17
        },
      },
    };
    
    

    Plotly.newPlot('pie', chart, layout); 
    });
  }
buildCharts();

// Texas-LineChart (Electricity)
function buildLineCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/electricityGeneration";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[2]; 
    ind_key_line = Object.keys(data_line);
    ind_val_line = Object.values(data_line);
  
    var chart = [{
      x: ind_val_line,
      y: ind_key_line,
      type: 'bar',
      orientation: 'h',

    }];

    var layout = {
      autosize: true,
      yaxis: {
        automargin: true
      },
      title: {
        text: 'Net Electricity Generation <br> by Source Mar 2019',
        font: {
        size: 17
        },
      },
      xaxis: {
        title: 'thousand MWh',
        titlefont: {
          size: 10,
        },
        showticklabels: true,
      }
    };

    Plotly.newPlot('line-elec', chart, layout);
    });
}
buildLineCharts();

// Texas-LineChart (Consumption)
function buildConsumptionCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/energyConsumption";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[2]; 
    ind_key_line = Object.keys(data_line);
    ind_val_line = Object.values(data_line);
  
    var chart = [{
      x: ind_val_line,
      y: ind_key_line,
      type: 'bar',
      orientation: 'h',
    }];

    var layout = {
      autosize: true,
      yaxis: {
        automargin: true
      },
      title: {
        text: 'Energy Consumption Estimates, 2017',
        font: {
        size: 17
        },
      },
      xaxis: {
        title: 'Trillion Btu',
        titlefont: {
          size: 10,
        },
        showticklabels: true,
      }
    };

    Plotly.newPlot('line-cons', chart, layout);
    });
}
buildConsumptionCharts();

// // Texas-LineChart (Production)
// function buildProductionCharts(sample) {
//   // @TODO: Use `d3.json` to fetch the sample data for the plots
//   var chartsURL = "/api/v1.0/energyProduction";
//   d3.json(chartsURL).then(function (data) {
//     var data_line = data[2]; 
//     ind_key_line = Object.keys(data_line);
//     ind_val_line = Object.values(data_line);
  
//     var chart = [{
//       x: ind_val_line,
//       y: ind_key_line,
//       type: 'bar',
//       orientation: 'h',
//       title: "Texas Production Estimates, 2016"
//     }];

//     var layout = {
//       autosize: true,
//       yaxis: {
//         automargin: true
//       },
//       title: {
//         text: 'Energy Production Estimates, 2016',
//         font: {
//         size: 17
//         },
//       },
//       xaxis: {
//         title: 'Trillion Btu',
//         titlefont: {
//           size: 10,
//         },
//         showticklabels: true,
//       }
//     };

//     Plotly.newPlot('line-prod', chart, layout);
//     });
// }
// buildProductionCharts();



// Texas-LineChart (Price)
function buildPriceCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/priceDifferences";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[2]; 
    ind_key_line = Object.keys(data_line);
    ind_val_line = Object.values(data_line);
  
    var chart = [{
      x: ind_val_line,
      y: ind_key_line,
      type: 'bar',
      orientation: 'h',
      title: "Price Differences from U.S. Average <br> Most Recent Monthly"
    }];

    var layout = {
      autosize: true,
      yaxis: {
        automargin: true
      },
      title: {
        text: 'Price Differences from U.S Average, <br> Most Recent Monthly',
        font: {
        size: 17
        },
      },
      xaxis: {
        title: 'Percent',
        titlefont: {
          size: 10,
        },
        showticklabels: true,
      }
    };

    Plotly.newPlot('line-price', chart, layout);
    });
}
buildPriceCharts();