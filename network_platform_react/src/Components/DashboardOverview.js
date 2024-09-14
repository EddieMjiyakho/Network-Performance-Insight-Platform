import React from 'react';
import MetricCard from './MetricCard';
import FilterBar from './FilterBar';
import '../Styling/DashboardOverview.css';
import '../Styling/FilterBar.css';


const DashboardOverview = () => {
  return (
    <div className="dashboard-overview">
      <h1>Historical Dashboad Overview</h1>
      <FilterBar/>
      <div className="card-grid">
        <MetricCard title="Average Latency" value="50ms" />
        <MetricCard title="Download Speed" value="20Mbps" />
        <MetricCard title="Upload Speed" value="10Mbps" />
        <MetricCard title="Packet Loss" value="2%" />
        <MetricCard title="Top 3 ISPs" value="ISP1, ISP2, ISP3" />
        <MetricCard title="Highest Latency ISP" value="ISP4" />
      </div>
    </div>
  );
};

export default DashboardOverview;
