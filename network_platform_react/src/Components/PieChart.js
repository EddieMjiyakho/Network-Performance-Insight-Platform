import React from "react";
import { Pie } from "react-chartjs-2"; // Import Pie from Chart.js

const PieChart = ({ data, options }) => {
  return (
    <div className="chart-container">
      <h2>Network Type Breakdown (Mobile vs. Fixed)</h2>
      <Pie data={data} options={options} />
    </div>
  );
};

export default PieChart;
