import React, { useEffect, useState } from 'react';
import MetricCard from './MetricCard';
import FilterBar from './FilterBar';
import '../Styling/DashboardOverview.css';
import '../Styling/FilterBar.css';

const DashboardOverview = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null); // Track errors

  useEffect(() => {
    fetch('/api/isp-data/')  // Ensure this endpoint is correct
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setData(data))  // Store the fetched data in state
      .catch(error => setError(error.message)); // Set error state if the fetch fails
  }, []);

  // Check if there's an error
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Display loading indicator if data is still being fetched
  if (!data) {
    return <div>Loading...</div>;
  }

  // Safeguard against missing data points by using fallback values
  return (
    <div className="dashboard-overview">
      <h1>Historical Dashboard Overview</h1>
      <FilterBar />
      <div className="card-grid">
        <MetricCard title="Average Throughput" value={data.throughput ? Math.round(data.throughput * 100) / 100 : 'N/A'} />
        <MetricCard title="Min rtt" value={data.min_rtt ? Math.round(data.min_rtt * 100) / 100 : 'N/A'} />
        <MetricCard title="Country" value={data.country || 'N/A'} />
        <MetricCard title="Packet Loss" value={data.packet_loss ? Math.round(data.packet_loss * 100) / 100 : 'N/A'} />
        <MetricCard title="Top 3 ISPs" value={Array.isArray(data.isp) ? data.isp.join(', ') : 'N/A'} />
        <MetricCard title="Highest Test Time" value={data.test_time || 'N/A'} />
      </div>
    </div>
  );
};

export default DashboardOverview;
