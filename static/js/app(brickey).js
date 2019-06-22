var viewer = new Cesium.Viewer('cesiumContainer');
viewer.dataSources.add(Cesium.GeoJsonDataSource.load('../static/data/gz_2010_us_040_00_500k.json', {
  stroke: Cesium.Color.HOTPINK,
  fill: Cesium.Color.TRANSPARENT,
  strokeWidth: 3,
  markerSymbol: '?'
}));
