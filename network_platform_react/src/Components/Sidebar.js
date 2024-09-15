import React from "react";
import "../Styling/Sidebar.css";
import logo from "../assets/logo3.jpg"; // Replace with your logo path

function Sidebar({ setActiveComponent }) {
  return (
    <div className="sidebar">
      <div className="logo">
        <img src={logo} alt="Logo" className="logo-image" />
      </div>
      <div className="menu">
        <button onClick={() => setActiveComponent("DashboardOverview")}>
          Dashboard Overview
        </button>
        <button onClick={() => setActiveComponent("GeospatialMap")}>
          Geospatial Map
        </button>
        <button onClick={() => setActiveComponent("ChartsGraphs")}>
          Charts & Graphs
        </button>
        <button onClick={() => setActiveComponent("ISPLeaderboard")}>
          ISP Leaderboard
        </button>
        <button onClick={() => setActiveComponent("HistoryAnalysis")}>
          History Analysis
        </button>
      </div>
    </div>
  );
}

export default Sidebar;
