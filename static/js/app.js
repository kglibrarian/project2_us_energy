var Coal_Consumption_2014_all_sectors_thousand_tons = [];
// var Coal_Consumption_2018_all_sectors_thousand_tons = [];
// var Consumption_per_Capita_Million_Btu= [];
// var Consumption_per_Capita_Rank = [];
// var Expenditures_per_Capita_Dollars = []; 
// var Expenditures_per_Capita_Rank = []; 
// var Production_Rank = [];
// var Production_US_Share = [];
var State_lower_name = [];
var stateAbbr = [];

var dataURL = "http://127.0.0.1:5000/api/v1.0/USProductionConsumption";

d3.json(dataURL).then(function(data) {

    // var stateLowerArray = []


    data.forEach(function(name) {
        var State_lower_name_single = name.State_lower_name;
        var Coal_Consumption_2014_all_sectors_thousand_tons_single = name.Coal_Consumption_2014_all_sectors_thousand_tons;
        var State_abbr_name = name.State_abbr_name.toLowerCase();

        // var thingToSave =  {
        //     State_lower_name:h State_lower_name,
        //     Coal_Consumption_2014_all_sectors_thousand_tons: Coal_Consumption_2014_all_sectors_thousand_tons,
        //     State_abbr_name: State_abbr_name
        // }
        var stringData = Coal_Consumption_2014_all_sectors_thousand_tons_single.toFixed(2)
        Coal_Consumption_2014_all_sectors_thousand_tons.push(stringData)
        stateAbbr.push(State_abbr_name)
        State_lower_name.push(State_lower_name_single)
        // console.log(State_abbr_name);
      })

      //console.log(State_abbr_name);
    var dataFirst = [{
        type: 'choropleth',
        locationmode: 'USA-states',
        locations: stateAbbr,
        z: Coal_Consumption_2014_all_sectors_thousand_tons,
        text: State_lower_name,
        zmin: 0,
        zmax: 17000,
        colorscale: [
            [0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
            [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
            [0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
        ],
        colorbar: {
            title: 'Millions USD',
            thickness: 0.2
        },
        marker: {
            line:{
                color: 'rgb(0,0,255)',
                width: 2
            }
        }
    }];

    console.log('BROKEN DATA 1', dataFirst);


    var layoutFirst = {
        title: 'Coal Consumption 2014',
        geo:{
            scope: 'usa',
            showlakes: true,
            lakecolor: 'rgb(255,255,255)'
        }
    };

    Plotly.plot(myDiv, dataFirst, layoutFirst, {showLink: false});
});

d3.selectAll("h2")
    .on("click", function(){
        console.log("Hello");
        var value = d3.select(this);
        console.log(value);
        if(value.attr("value") !== "Data2") {
            value.classed("inactive", false)
                .classed("active", true);
            var other = d3.select("#Data2");
            console.log(other);
            other.classed("active", false)
                .classed("inactive", true);
            Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv', function(err, rows){
                console.log('INSIDE THE PLOTLY!!!!!!!');   
            
            function unpack(rows, key) {
                    return rows.map(function(row) { return row[key]; });
                }



                var data1 = [{
                    type: 'choropleth',
                    locationmode: 'USA-states',
                    locations: unpack(rows, 'code'),
                    z: unpack(rows, 'total exports'),
                    text: unpack(rows, 'state'),
                    zmin: 0,
                    zmax: 17000,
                    colorscale: [
                        [0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
                        [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
                        [0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
                    ],
                    colorbar: {
                        title: 'Millions USD',
                        thickness: 0.2
                    },
                    marker: {
                        line:{
                            color: 'rgb(255,255,255)',
                            width: 2
                        }
                    }
                }];

                console.log('THIS WORKINGGGGG DATA 1', data1);

                var layout1 = {
                    title: '2011 US Agriculture Exports by State',
                    geo:{
                        scope: 'usa',
                        showlakes: true,
                        lakecolor: 'rgb(255,255,255)'
                    }
                };

                Plotly.plot(myDiv, data1, layout1, {showLink: false});
            });
        }
        else { 
            value.classed("inactive", false)
                .classed("active", true);
            var other = d3.select("#Data1");
            console.log(other);
            other.classed("active", false)
                .classed("inactive", true);
            Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv', function(err, rows){
                            function unpack(rows, key) {
            return rows.map(function(row) { return row[key]; });
            }
            var data2 = [{
                type: 'choropleth',
                locationmode: 'USA-states',
                locations: unpack(rows, 'Postal'),
                z: unpack(rows, 'Population'),
                text: unpack(rows, 'State'),
                autocolorscale: true
            }];

            var layout2 = {
            title: '2014 US Popultaion by State',
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
            Plotly.plot(myDiv, data2, layout2, {showLink: false});
            });
        }
    });
