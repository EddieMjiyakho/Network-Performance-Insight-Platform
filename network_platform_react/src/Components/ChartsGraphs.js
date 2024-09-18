import React from 'react';
import LineChart from './LineChart';
import FilterBar from './FilterBar';


function ChartsGraphs() {
  return (
    <div>
      <h1>Graphs & Charts </h1>
      {/* Add content specific to Charts & Graphs */}
      <FilterBar/>
      <LineChart/>
    </div>

    
  );
}

export default ChartsGraphs;
