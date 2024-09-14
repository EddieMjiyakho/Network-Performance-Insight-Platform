import React, { useState } from 'react';
import ReportForm from './ReportForm';
import ReportPreview from './ReportPreview';
import ExportButtons from './ExportButtons';
import ReportPresetOptions from './ReportPresetOptions';
import '../Styling/HistoricalPerformanceAnalysis.css';

const HistoricalPerformanceAnalysis = () => {
  const [reportData, setReportData] = useState(null);
  const [presetReport, setPresetReport] = useState(null);

  // Mock function to simulate fetching report data
  const fetchReportData = (filters) => {
    // Simulate data fetching based on the filters
    return [
      { isp: 'Safaricom', latency: 50, downloadSpeed: 20, uploadSpeed: 5, packetLoss: 1 },
      { isp: 'MTN', latency: 40, downloadSpeed: 25, uploadSpeed: 10, packetLoss: 0.5 },
      { isp: 'Vodacom', latency: 60, downloadSpeed: 15, uploadSpeed: 7, packetLoss: 2 },
    ];
  };

  // Mock function to simulate fetching preset report data
  const fetchPresetReport = (preset) => {
    // Simulate preset report data based on the selected preset
    if (preset === 'monthlyISP') {
      return [
        { isp: 'Safaricom', latency: 52, downloadSpeed: 22, uploadSpeed: 6, packetLoss: 1.2 },
        { isp: 'MTN', latency: 42, downloadSpeed: 26, uploadSpeed: 11, packetLoss: 0.6 },
        { isp: 'Vodacom', latency: 62, downloadSpeed: 16, uploadSpeed: 8, packetLoss: 2.1 },
      ];
    }
    // Add other preset data as needed
    return [];
  };

  const handleGenerateReport = (filters) => {
    const data = fetchReportData(filters);
    setReportData(data);
  };

  const handleSelectPreset = (preset) => {
    const data = fetchPresetReport(preset);
    setReportData(data);
  };

  return (
    <div className="historical-performance-container">
      <h1>Historical Performance Analysis</h1>
      <ReportPresetOptions onSelectPreset={handleSelectPreset} />
      <ReportForm onGenerate={handleGenerateReport} />
      <ReportPreview data={reportData} />
      {reportData && <ExportButtons data={reportData} />}
    </div>
  );
};

export default HistoricalPerformanceAnalysis;
