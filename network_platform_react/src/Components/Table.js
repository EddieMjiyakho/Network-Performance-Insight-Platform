import React from 'react';

const Table = ({ data, onSort, sortColumn, sortOrder }) => {
  const renderSortArrow = (column) => {
    if (column === sortColumn) {
      return sortOrder === 'asc' ? '▲' : '▼';
    }
    return null;
  };

  return (
    <table className="isp-table">
      <thead>
        <tr>
          <th onClick={() => onSort('name')}>ISP Name {renderSortArrow('name')}</th>
          <th onClick={() => onSort('latency')}>Latency {renderSortArrow('latency')}</th>
          <th onClick={() => onSort('downloadSpeed')}>Download Speed {renderSortArrow('downloadSpeed')}</th>
          <th onClick={() => onSort('uploadSpeed')}>Upload Speed {renderSortArrow('uploadSpeed')}</th>
          <th onClick={() => onSort('packetLoss')}>Packet Loss {renderSortArrow('packetLoss')}</th>
        </tr>
      </thead>
      <tbody>
        {data.map((isp, index) => (
          <tr key={index} className={index < 3 ? 'top-isp' : ''}>
            <td>{isp.name}</td>
            <td>{isp.latency} ms</td>
            <td>{isp.downloadSpeed} Mbps</td>
            <td>{isp.uploadSpeed} Mbps</td>
            <td>{isp.packetLoss} %</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
