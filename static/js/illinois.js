//Illinois-Piechart (Consumption by Sector)
function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/consumptionsector";
  d3.json(chartsURL).then(function (data) {
    var data = data[0]; 
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

// Illinois-LineChart (Electricity)
function buildLineCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/electricityGeneration";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[0]; 
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

// Illinois-LineChart (Consumption)
function buildConsumptionCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/energyConsumption";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[0]; 
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

// Illinois-LineChart (Production)
function buildProductionCharts(sample) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/v1.0/energyProduction";
  d3.json(chartsURL).then(function (data) {
    var data_line = data[0]; 
    ind_key_line = Object.keys(data_line);
    ind_val_line = Object.values(data_line);
  
    var chart = [{
      x: ind_val_line,
      y: ind_key_line,
      type: 'bar',
      orientation: 'h',
      title: "Illinois Production Estimates, 2016"
    }];

    var layout = {
      autosize: true,
      yaxis: {
        automargin: true
      },
      title: {
        text: 'Energy Production Estimates, 2016',
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

    Plotly.newPlot('line-prod', chart, layout);
    });
}
buildProductionCharts();




// var mydata = [{"Commercial":500,"Industrial":1176.2,"Residential":891.6}];
// console.log(mydata);
// for(var i=0;i<mydata.length;i++) {
//   var obj = mydata[i]+[1];
//   console.log(obj);
// }

// ind_key = console.log(Object.keys(obj));
// ind_val = console.log(Object.values(obj));