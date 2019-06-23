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
strokeWidth: 3,
markerSymbol: '?'
}));

var scene = viewer.scene;
var clock = viewer.clock;
var referenceFramePrimitive;

function flyToSanDiego() {
  // Sandcastle.declare(flyToSanDiego);
  viewer.camera.flyTo({
      destination : Cesium.Cartesian3.fromDegrees(-117.16, 32.71, 15000.0)
  });
}

// flyToSanDiego();

function flyToLocation(Location) {
  // https://citylatitudelongitude.com/TX/Center.htm
  // Sandcastle.declare(flyToTexas);
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
var Location = "IL";

flyToLocation(Location);



