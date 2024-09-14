import React, { useState } from 'react';

const ReportForm = ({ onGenerate }) => {
  const [timeRange, setTimeRange] = useState('');
  const [region, setRegion] = useState('');
  const [isp, setIsp] = useState('');
  const [metric, setMetric] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onGenerate({ timeRange, region, isp, metric });
  };

  return (
    <form onSubmit={handleSubmit} className="report-form">
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
      <button type="submit">Generate Report</button>
    </form>
  );
};

export default ReportForm;
