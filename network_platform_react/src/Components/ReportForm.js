// src/ReportOptionsForm.js
import React, { useState } from 'react';
import '../Styling/ReportForm.css';


const ReportOptionsForm = ({ onSelectPreset, onGenerate }) => {
  const [timeRange, setTimeRange] = useState('');
  const [region, setRegion] = useState('');
  const [isp, setIsp] = useState('');
  const [metric, setMetric] = useState('');
  const [preset, setPreset] = useState('');

  const handlePresetSelect = (event) => {
    const preset = event.target.value;
    setPreset(preset);
    onSelectPreset(preset);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onGenerate({ timeRange, region, isp, metric });
  };

  return (
    <div className="options-form-container">
      <div className="preset-options">
        <h3>Preset Reports</h3>
        <select value={preset} onChange={handlePresetSelect}>
          <option value="">Select a preset report</option>
          <option value="monthlyISP">Monthly ISP Performance (South Africa)</option>
          <option value="yearlyComparison">Yearly ISP Comparison</option>
          {/* Add more preset options here */}
        </select>
      </div>

      <form onSubmit={handleSubmit} className="report-form">
        <div className="form-row">
          <label>
            Time Range:
            <input
              type="date"
              value={timeRange}
              onChange={(e) => setTimeRange(e.target.value)}
            />
          </label>
          <label>
            Region:
            <input
              type="text"
              value={region}
              onChange={(e) => setRegion(e.target.value)}
              placeholder="Enter region"
            />
          </label>
          <label>
            ISP:
            <input
              type="text"
              value={isp}
              onChange={(e) => setIsp(e.target.value)}
              placeholder="Enter ISP"
            />
          </label>
          <label>
            Metric:
            <select value={metric} onChange={(e) => setMetric(e.target.value)}>
              <option value="latency">Latency</option>
              <option value="downloadSpeed">Download Speed</option>
              <option value="uploadSpeed">Upload Speed</option>
              <option value="packetLoss">Packet Loss</option>
            </select>
          </label>
        </div>
        <button type="submit">Generate Report</button>
      </form>
    </div>
  );
};

export default ReportOptionsForm;
