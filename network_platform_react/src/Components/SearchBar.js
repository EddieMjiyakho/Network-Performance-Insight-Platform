import React from 'react';

const SearchBar = ({ onSearch }) => {
  const handleInputChange = (event) => onSearch(event.target.value);

  return (
    <input 
      type="text" 
      placeholder="Search ISP..." 
      onChange={handleInputChange} 
      className="search-bar"
    />
  );
};

export default SearchBar;
