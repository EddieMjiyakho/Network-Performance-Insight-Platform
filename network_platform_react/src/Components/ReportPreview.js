import React from 'react';

const ReportPreview = ({ data }) => {
  if (!data) return null;

  return (
    <div className="report-preview">
      <h2>Report Preview</h2>
      {/* Conditionally render either a table or graph */}
      <table>
        <thead>
          <tr>
            <th>ISP</th>
            <th>Latency</th>
            <th>Download Speed</th>
            <th>Upload Speed</th>
            <th>Packet Loss</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.isp}</td>
              <td>{item.latency} ms</td>
              <td>{item.downloadSpeed} Mbps</td>
              <td>{item.uploadSpeed} Mbps</td>
              <td>{item.packetLoss} %</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ReportPreview;
