import React, { useState } from 'react';
import SearchBar from './SearchBar';
import Filters from './Filters';
import Table from './Table';
import './Leaderboard.css';

const Leaderboard = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [filterRegion, setFilterRegion] = useState('');
  const [sortColumn, setSortColumn] = useState('latency');
  const [sortOrder, setSortOrder] = useState('asc'); // 'asc' for ascending, 'desc' for descending

  // Placeholder data
  const ispData = [
    { name: 'ISP A', latency: 50, downloadSpeed: 100, uploadSpeed: 50, packetLoss: 0.1, region: 'Kenya' },
    { name: 'ISP B', latency: 30, downloadSpeed: 150, uploadSpeed: 75, packetLoss: 0.05, region: 'South Africa' },
    // More data here...
  ];

  const handleSearch = (query) => setSearchQuery(query);
  const handleFilter = (region) => setFilterRegion(region);
  const handleSort = (column) => {
    const newSortOrder = sortColumn === column && sortOrder === 'asc' ? 'desc' : 'asc';
    setSortColumn(column);
    setSortOrder(newSortOrder);
  };

  // Filter, search, and sort data logic
  const filteredData = ispData
    .filter(isp => isp.name.toLowerCase().includes(searchQuery.toLowerCase()) && (!filterRegion || isp.region === filterRegion))
    .sort((a, b) => {
      const valueA = a[sortColumn];
      const valueB = b[sortColumn];
      return sortOrder === 'asc' ? valueA - valueB : valueB - valueA;
    });

  return (
    <div className="leaderboard-container">
      <h1>ISP Leaderboard</h1>
      <SearchBar onSearch={handleSearch} />
      <Filters onFilter={handleFilter} />
      <Table data={filteredData} onSort={handleSort} sortColumn={sortColumn} sortOrder={sortOrder} />
    </div>
  );
};

export default Leaderboard;
