import React from "react";

const FilterBar = ({ handleFilterChange }) => {
  return (
    <div className="filter-bar">
      <select onChange={(e) => handleFilterChange("country", e.target.value)}>
        <option value="all">All Countries</option>
        {/* Add more options here */}
      </select>

      <select onChange={(e) => handleFilterChange("city", e.target.value)}>
        <option value="all">All Cities</option>
        {/* Add more options here */}
      </select>

      <select onChange={(e) => handleFilterChange("isp", e.target.value)}>
        <option value="all">All ISPs</option>
        {/* Add more options here */}
      </select>

      <select onChange={(e) => handleFilterChange("time", e.target.value)}>
        <option value="all">All Time Ranges</option>
        {/* Add more options here */}
      </select>
    </div>
  );
};

export default FilterBar;
