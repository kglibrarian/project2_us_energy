var Coal_Consumption_2014_all_sectors_thousand_tons = [];
var Coal_Consumption_2018_all_sectors_thousand_tons = [];
var Production_US_Share = [];
var State_lower_name = [];
var stateAbbr = [];

var dataURL = "http://127.0.0.1:5000/api/v1.0/USProductionConsumption";

d3.json(dataURL).then(function(data) {

    // var stateLowerArray = []


    data.forEach(function(name) {
        var State_lower_name_single = name.State_lower_name;
        var Coal_Consumption_2014_all_sectors_thousand_tons_single = name.Coal_Consumption_2014_all_sectors_thousand_tons;
        var Coal_Consumption_2018_all_sectors_thousand_tons_single = name.Coal_Consumption_2018_all_sectors_thousand_tons;
        var State_abbr_name_single = name.State_abbr_name;
        var Production_US_Share_single = name.Production_US_Share;

        var string2014 = Coal_Consumption_2014_all_sectors_thousand_tons_single.toFixed(2);
        var string2018= Coal_Consumption_2018_all_sectors_thousand_tons_single.toFixed(2);

        Coal_Consumption_2014_all_sectors_thousand_tons.push(string2014);
        Coal_Consumption_2018_all_sectors_thousand_tons.push(string2018);
        Production_US_Share.push(Production_US_Share_single);
        stateAbbr.push(State_abbr_name_single);
        State_lower_name.push(State_lower_name_single);
        // console.log(State_abbr_name);
      })

      //console.log(State_abbr_name);
    var dataSet = [{
        type: 'choropleth',
        locationmode: 'USA-states',
        locations: stateAbbr,
        z: Coal_Consumption_2014_all_sectors_thousand_tons,
        text: State_lower_name,
        autocolorscale: true,
        colorbar: {
            title: 'Thousand Tons',
        }
    }];

    // console.log('BROKEN DATA 1', dataFirst);


    var layoutSet = {
        title: 'Coal Consumption 2014',
        geo:{
            scope: 'usa',
            countrycolor: 'rgb(255, 255, 255)',
            showland: true,
            landcolor: 'rgb(217, 217, 217)',
            showlakes: true,
            lakecolor: 'rgb(255, 255, 255)',
            subunitcolor: 'rgb(255, 255, 255)',
            lonaxis: {},
            lataxis: {}
        }
    };

    Plotly.newPlot(myDiv, dataSet, layoutSet, {showLink: false});
});

d3.selectAll("h2")
    .on("click", function(){
        var value = d3.select(this);
        // console.log(value);
        if(value.attr("value") !== "Data2" && value.attr("value") !== "Data3") {
            value.classed("inactive", false)
                .classed("active", true);
            var other = d3.select("#Data2");
            // console.log(other);
            other.classed("active", false)
                .classed("inactive", true);
            var other2 = d3.select("#Data3");
            // console.log(other);
            other2.classed("active", false)
                .classed("inactive", true);
            dataSet = [{
                type: 'choropleth',
                locationmode: 'USA-states',
                locations: stateAbbr,
                z: Coal_Consumption_2014_all_sectors_thousand_tons,
                text: State_lower_name,
                autocolorscale: true,
                colorbar: {
                    title: 'Thousand Tons',
                }
            }];
        
            // console.log('BROKEN DATA 1', dataFirst);
        
        
            layoutSet = {
                title: 'Coal Consumption 2014',
                geo:{
                    scope: 'usa',
                    countrycolor: 'rgb(255, 255, 255)',
                    showland: true,
                    landcolor: 'rgb(217, 217, 217)',
                    showlakes: true,
                    lakecolor: 'rgb(255, 255, 255)',
                    subunitcolor: 'rgb(255, 255, 255)',
                    lonaxis: {},
                    lataxis: {}
                }
            };
        
            Plotly.newPlot(myDiv, dataSet, layoutSet, {showLink: false});
        }
        else if (value.attr("value") !== "Data1" && value.attr("value") !== "Data2") {
            value.classed("inactive", false)
                .classed("active", true);
            var other = d3.select("#Data1");
            // console.log(other);
            other.classed("active", false)
                .classed("inactive", true);
            var other2 = d3.select("#Data2");
            // console.log(other);
            other2.classed("active", false)
                .classed("inactive", true);
            dataSet = [{
                type: 'choropleth',
                locationmode: 'USA-states',
                locations: stateAbbr,
                z: Production_US_Share,
                text: State_lower_name,
                colorscale: [
                    [0, 'rgb(255,255,255)'], [0.2, 'rgb(224,255,255)'],
                    [0.4, 'rgb(144,238,144)'], [0.6, 'rgb(34,139,34)'],
                    [0.8, 'rgb(0,128,0)'], [1, 'rgb(0,100,0)']
                ],
                colorbar: {
                    title: 'Percent of US Share',
                }
            }];
        
            // console.log('BROKEN DATA 1', dataFirst);
        
        
            layoutSet = {
                title: 'Total Percent US Energy Production 2016',
                geo:{
                    scope: 'usa',
                    countrycolor: 'rgb(255, 255, 255)',
                    showland: true,
                    landcolor: 'rgb(217, 217, 217)',
                    showlakes: true,
                    lakecolor: 'rgb(255, 255, 255)',
                    subunitcolor: 'rgb(255, 255, 255)',
                    lonaxis: {},
                    lataxis: {}
                }
            };
        
            Plotly.newPlot(myDiv, dataSet, layoutSet, {showLink: false});

        }
        else { 
            value.classed("inactive", false)
                .classed("active", true);
            var other = d3.select("#Data1");
            console.log(other);
            other.classed("active", false)
                .classed("inactive", true);
            var other2 = d3.select("#Data3");
            // console.log(other);
            other2.classed("active", false)
                .classed("inactive", true);
            dataSet = [{
                type: 'choropleth',
                locationmode: 'USA-states',
                locations: stateAbbr,
                z: Coal_Consumption_2018_all_sectors_thousand_tons,
                text: State_lower_name,
                colorscale: [
                    [0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
                    [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
                    [0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
                ],
                colorbar: {
                    title: 'Thousand Tons',
                }
            }];
        
            // console.log('BROKEN DATA 1', dataFirst);
        
        
            var layoutSet = {
                title: 'Coal Consumption 2018',
                geo:{
                    scope: 'usa',
                    countrycolor: 'rgb(255, 255, 255)',
                    showland: true,
                    landcolor: 'rgb(217, 217, 217)',
                    showlakes: true,
                    lakecolor: 'rgb(255, 255, 255)',
                    subunitcolor: 'rgb(255, 255, 255)',
                    lonaxis: {},
                    lataxis: {}
                }
            };
        
            Plotly.newPlot(myDiv, dataSet, layoutSet, {showLink: false});
        }
    });
