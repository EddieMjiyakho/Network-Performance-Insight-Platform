import React from "react";
import { Bar } from "react-chartjs-2"; // Import Bar from Chart.js

const BarChart = ({ data, options }) => {
  return (
    <div className="chart-container">
      <h2>ISP Comparison by Download Speed</h2>
      <Bar data={data} options={options} />
      <div className="filters">
        {/* Add country/region dropdown filter component here */}
      </div>
    </div>
  );
};

export default BarChart;
