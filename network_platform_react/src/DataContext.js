// src/DataContext.js
import React, { createContext, useState, useEffect, useCallback } from 'react';
import { fetchDataFromAPI } from './api/dataApi';

const DataContext = createContext();

export const DataProvider = ({ children }) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({
    region: '',
    country: '',
    isp: '',
    time: ''
  });

  const fetchData = useCallback(async () => {
    setLoading(true);
    try {
      const result = await fetchDataFromAPI(filters);
      setData(result);
      setError(null);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const updateFilters = (newFilters) => {
    setFilters(prevFilters => ({ ...prevFilters, ...newFilters }));
  };

  return (
    <DataContext.Provider value={{ data, loading, error, filters, updateFilters, refetchData: fetchData }}>
      {children}
    </DataContext.Provider>
  );
};

export default DataContext;