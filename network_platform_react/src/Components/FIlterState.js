import React, { useState, useEffect } from 'react';
import FilterBar from './FilterBar';
import LineChart from './LineChart';

const FilterState = () => {
  const [filters, setFilters] = useState({
    time: 'all',
    country: 'South Africa',
    city: 'Cape Town',
    isp: 'MTN',
  });

  const handleFilterChange = (filterName, filterValue) => {
    setFilters((prevFilters) => ({
      ...prevFilters,
      [filterName]: filterValue,
    }));
  };

  useEffect(() => {
    
    
  }, [filters]);

  return (
    <div>
      <FilterBar handleFilterChange={handleFilterChange} />
      <LineChart filters={filters} />
    </div>
  );
};

export default FilterState;
