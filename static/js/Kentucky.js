//Kentucky-Piechart
function buildCharts(sample) {

    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var chartsURL = "/api/v1.0/consumptionsector";
    d3.json(chartsURL).then(function (data) {
      var data = data[1]; 
      ind_key = Object.keys(data);
      ind_val = Object.values(data);
      
      var chart = [{
        values: ind_val,
        labels: ind_key,
        type: 'pie',
      }];
  
      Plotly.newPlot('pie', chart);
      });
    }
buildCharts();
  
  // Kentucky-LineChart
function buildLineCharts(sample) {
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var chartsURL = "/api/v1.0/electricityGeneration";
    d3.json(chartsURL).then(function (data) {
      var data_line = data[1]; 
      ind_key_line = Object.keys(data_line);
      ind_val_line = Object.values(data_line);
    
      var chart = [{
        x: ind_val_line,
        y: ind_key_line,
        type: 'bar',
        orientation: 'h',
      }];
  
      Plotly.newPlot('line-elec', chart);
      });
  }
buildLineCharts();

function buildConsumptionCharts(sample) {
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var chartsURL = "/api/v1.0/energyConsumption";
    d3.json(chartsURL).then(function (data) {
      var data_line = data[1]; 
      ind_key_line = Object.keys(data_line);
      ind_val_line = Object.values(data_line);
    
      var chart = [{
        x: ind_val_line,
        y: ind_key_line,
        type: 'bar',
        orientation: 'h',
      }];
  
      Plotly.newPlot('line-cons', chart);
      });
  }
buildConsumptionCharts();
  
  // var mydata = [{"Commercial":500,"Industrial":1176.2,"Residential":891.6}];
  // console.log(mydata);
  // for(var i=0;i<mydata.length;i++) {
  //   var obj = mydata[i]+[1];
  //   console.log(obj);
  // }
  
  // ind_key = console.log(Object.keys(obj));
  // ind_val = console.log(Object.values(obj));