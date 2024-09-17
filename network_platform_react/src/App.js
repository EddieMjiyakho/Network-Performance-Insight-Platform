import React, { useState } from "react";
import Sidebar from "./Components/Sidebar";
import DashboardOverview from "./Components/DashboardOverview";
import GeospatialMap from "./Components/GeospatialMap"; // Placeholder component
import ChartsGraphs from "./Components/ChartsGraphs"; // Placeholder component
import ISPLeaderboard from "./Components/ISPLeaderboard"; // Placeholder component
import HistoryAnalysis from "./Components/HistoricalPerformanceAnalysis"; // Placeholder component
import "./App.css";

function App() {
  const [activeComponent, setActiveComponent] = useState("DashboardOverview");

  const renderComponent = () => {
    switch (activeComponent) {
      case "DashboardOverview":
        return <DashboardOverview />;
      case "GeospatialMap":
        return <GeospatialMap />;
      case "ChartsGraphs":
        return <ChartsGraphs />;
      case "ISPLeaderboard":
        return <ISPLeaderboard />;
      case "HistoryAnalysis":
        return <HistoryAnalysis />;
      default:
        return <DashboardOverview />;
    }
  };

  return (
    <div className="app">
      <Sidebar setActiveComponent={setActiveComponent} />
      <div className="main-content">{renderComponent()}</div>
    </div>
  );
}

export default App;
