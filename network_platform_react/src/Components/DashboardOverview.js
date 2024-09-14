import React from 'react';
import MetricCard from './MetricCard';
import '../Styling/DashboardOverview.css';

const DashboardOverview = () => {
  return (
    <div className="dashboard-overview">
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
