import React, { useEffect, useState } from 'react';
import '../Styling/MetricCard.css';

const MetricCard = ({ title, value, previousValue }) => {
  const [animateValue, setAnimateValue] = useState(0);

  // Trigger number animation when the card loads
  useEffect(() => {
    let start = 0;
    const duration = 1000; // 1 second for the animation
    const increment = value / (duration / 10);

    const interval = setInterval(() => {
      start += increment;
      if (start >= value) {
        setAnimateValue(value);
        clearInterval(interval);
      } else {
        setAnimateValue(Math.floor(start));
      }
    }, 10);

    return () => clearInterval(interval);
  }, [value]);

  // Check if the value has increased or decreased
  const isIncreased = value > previousValue;

  return (
    <div className="card">
      <h3>{title}</h3>
      <p className="value">
        {animateValue} Mbps
        <span className={`arrow ${isIncreased ? 'up' : 'down'}`}>
          {isIncreased ? '↑' : '↓'}
        </span>
      </p>
    </div>
  );
};

export default MetricCard;
