import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js';

// Register required components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement);

const LineChart = ({ filters }) => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [],
  });

  useEffect(() => {
    // Construct query parameters based on filters
    const query = new URLSearchParams(filters).toString();

    // Fetch ISP data with filters applied
    fetch(`/api/isp-data/?${query}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        const labels = [];
        const throughputData = [];
        const rttData = [];
        const packetLossData = [];

        data.forEach((item) => {
          labels.push(item.country);
          throughputData.push(item.throughput);
          rttData.push(item.min_rtt);
          packetLossData.push(item.packet_loss);
        });

        setChartData({
          labels: labels,
          datasets: [
            {
              label: 'Throughput',
              data: throughputData,
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.4)',
              type: 'line',
            },
            {
              label: 'Min RTT',
              data: rttData,
              borderColor: 'rgba(255, 99, 132, 1)',
              backgroundColor: 'rgba(255, 99, 132, 0.4)',
              type: 'line',
            },
            {
              label: 'Packet Loss',
              data: packetLossData,
              borderColor: 'rgba(153, 102, 255, 1)',
              backgroundColor: 'rgba(153, 102, 255, 0.4)',
              type: 'line',
            },
          ],
        });
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, [filters]);

  const options = {
    scales: {
      x: {
        title: {
          display: true,
          text: "Country",
        },
        ticks: {
          autoSkip: false,
        },
      },
      y: {
        title: {
          display: true,
          text: "Metrics",
        },
        beginAtZero: true,
      },
    },
  };

  return <Line data={chartData} options={options} />;
};

export default LineChart;
