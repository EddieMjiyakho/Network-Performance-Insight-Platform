import React, { useEffect, useState } from 'react';
import MetricCard from './MetricCard';
import FilterBar from './FilterBar';
import '../Styling/DashboardOverview.css';
import '../Styling/FilterBar.css';

const DashboardOverview = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/isp-data/')  // Make sure this matches your actual API endpoint
      .then(response => response.json())
      .then(data => setData(data))  // Store the API data in the state
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // Check if data is available before rendering the MetricCards
  if (!data) {
    return <div>Loading...</div>;  // Add a loading indicator until data is fetched
  }

  return (
    <div className="dashboard-overview">
      <h1>Historical Dashboard Overview</h1>
      <FilterBar />
      <div className="card-grid">
        <MetricCard title="Average Throughput" value={Math.round(data.throughput*100 )/100|| 'N/A'} />
        <MetricCard title="Min rtt" value={Math.round(data.min_rtt*100 )/100 || 'N/A'} />
        <MetricCard title="Country" value={data.country || 'N/A'} />
        <MetricCard title="Packet Loss" value={Math.round(data.packet_loss*100 )/100 || 'N/A'} />
        <MetricCard title="Top 3 ISPs" value={Array.isArray(data.isp) ? data.isp.join(', ') : 'N/A'} />
        <MetricCard title="Highest Test Time" value={data.test_time || 'N/A'} />
      </div>
    </div>
  );
};

export default DashboardOverview;
