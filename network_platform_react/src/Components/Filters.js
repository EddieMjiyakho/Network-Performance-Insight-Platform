import React from 'react';

const Filters = ({ onFilter }) => {
  const handleFilterChange = (event) => onFilter(event.target.value);

  return (
    <select onChange={handleFilterChange} className="filter-select">
      <option value="">All Regions</option>
      <option value="Kenya">Kenya</option>
      <option value="South Africa">South Africa</option>
      {/* Add more regions here */}
    </select>
  );
};

export default Filters;
