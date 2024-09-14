import React from 'react';

const ExportButtons = ({ data }) => {
  const handleExportPDF = () => {
    // Logic to export data as PDF
    console.log('Exporting data as PDF...');
  };

  const handleExportCSV = () => {
    // Logic to export data as CSV
    console.log('Exporting data as CSV...');
  };

  return (
    <div className="export-buttons">
      <button onClick={handleExportPDF}>Export as PDF</button>
      <button onClick={handleExportCSV}>Export as CSV</button>
    </div>
  );
};

export default ExportButtons;
