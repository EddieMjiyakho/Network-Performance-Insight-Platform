import React from 'react';
// import '../Styling/ReportPresetOptions.css';


const ReportPresetOptions = ({ onSelectPreset }) => {
  const handlePresetSelect = (event) => {
    const preset = event.target.value;
    onSelectPreset(preset);
  };

  return (
    <div className="preset-options">
      <h3>Preset Reports</h3>
      <select onChange={handlePresetSelect}>
        <option value="">Select a preset report</option>
        <option value="monthlyISP">Monthly ISP Performance (South Africa)</option>
        <option value="yearlyComparison">Yearly ISP Comparison</option>
        {/* Add more preset options here */}
      </select>
    </div>
  );
};

export default ReportPresetOptions;
