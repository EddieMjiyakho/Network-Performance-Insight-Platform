import React from 'react';
import Heatmap from './Heatmap';
import FilterBar from './FilterBar';

function GeospatialMap() {
  return (
    <div className="App">
      <h1>Geospatial Heatmap with Leaflet</h1>
      <FilterBar/>
      <Heatmap />
    </div>
  );
}

export default GeospatialMap;

