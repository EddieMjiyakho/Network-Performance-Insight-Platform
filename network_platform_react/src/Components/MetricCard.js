import React from 'react';
import '../Styling/MetricCard.css';

const MetricCard = ({ title, value, description }) => {
  return (
    <div className="metric-card">
      <h3>{title}</h3>
      <p>{value}</p>
      <p>{description}</p>
    </div>
  );
};

export default MetricCard;
