import React from 'react';
import '../Styling/TopBar.css';

const TopBar = () => {
  return (
    <div className="top-bar">
     <div>
       <h1 className="title">Network Performance Dashboard</h1>
     </div>
      <div className="filters">
        <select>
          <option>Time Range</option>
        </select>
        <select>
          <option>Region</option>
        </select>
        <select>
          <option>ISP</option>
        </select>
      </div>
    </div>
  );
};

export default TopBar;
