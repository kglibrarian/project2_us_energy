var viewer = new Cesium.Viewer('cesiumContainer',{
  animation: false,
  baseLayerPicker: false,
  fullscreenButton: false,
  homeButton: false,
  navigationHelpButton: false,
  geocoder: false,
  sceneModePicker: false,
  timeline: false,
});

viewer.dataSources.add(Cesium.GeoJsonDataSource.load('../static/data/gz_2010_us_040_00_500k.json', {
stroke: Cesium.Color.BLACK,
fill: Cesium.Color.TRANSPARENT,
strokeWidth: 2,
markerSymbol: '?'
}));

var pinBuilder = new Cesium.PinBuilder();

function flyToLocation(Location) {
  if (Location == "TX") {
    var lon = -99.683617;
    var lat = 31.169621;
    var zoom = 1800000.0
  } else if (Location == "IL") {
    var lon = -89.30131;
    var lat = 39.84215;
    var zoom = 1000000.0
  } else if (Location == "KY") {
    var lon = -85.7700;
    var lat = 37.8393;
    var zoom = 600000.0
  } else {
    var lon = -98.5795;
    var lat = 39.8283;
    var zoom = 10000000.0
  }
  viewer.camera.flyTo({
      destination : Cesium.Cartesian3.fromDegrees(lon,lat,zoom)
  });
}


var Location = "TX";
flyToLocation(Location);

Cesium.Resource.fetchJson('http://127.0.0.1:5000/api/v1.0/plantData').then(function(jsonData) {
  jsonData.forEach(function(item) {
    if (item.State == "TX") {
      console.log(item);
      var lat = +item.Latitude;
      var lon = +item.Longitude;
      var kV = +item.Grid_Voltage_kV;
      console.log(lat, lon, kV);
      var bluePin = viewer.entities.add({
        name : 'Blank blue pin',
        position : Cesium.Cartesian3.fromDegrees(lon, lat),
        billboard : {
            image : pinBuilder.fromColor(Cesium.Color.ROYALBLUE, 48).toDataURL(),
            verticalOrigin : Cesium.VerticalOrigin.BOTTOM
        }
      });
      // viewer.entities.add(Cesium.Cartesian3.fromDegrees(lon, lat, kV));
      // viewer.entities.add({
      //   name : 'Blank blue pin',
      //   position : Cesium.Cartesian3.fromDegrees(lon, lat),
      //   billboard : {
      //       image : pinBuilder.fromColor(Cesium.Color.ROYALBLUE, 48),
      //       verticalOrigin : Cesium.VerticalOrigin.BOTTOM
      //   }
    };
    })
  });