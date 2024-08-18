import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from "chart.js";
import "./App.css";
import sourceData from "./data/sourceData.json";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export const App = () => {
  // Ensure data is properly formatted
  const downloadSpeedData = {
    labels: sourceData.map((data) => data.clientASN),
    datasets: [
      {
        label: "Average Download Speed",
        data: sourceData.map((data) => Number(data.avg_download_speed)),
        backgroundColor: "rgba(75, 192, 192, 0.8)",
        borderRadius: 5,
      },
    ],
  };

  const uploadSpeedData = {
    labels: sourceData.map((data) => data.clientASN),
    datasets: [
      {
        label: "Average Upload Speed",
        data: sourceData.map((data) => Number(data.avg_upload_speed)),
        backgroundColor: "rgba(153, 102, 255, 0.8)",
        borderRadius: 5,
      },
    ],
  };

  const latencyData = {
    labels: sourceData.map((data) => data.clientASN),
    datasets: [
      {
        label: "Average Latency",
        data: sourceData.map((data) => Number(data.avg_latency)),
        backgroundColor: "rgba(255, 99, 132, 0.8)",
        borderRadius: 5,
      },
    ],
  };

  return (
    <div className="App">
      <div className="dataCard downloadSpeedCard">
        <Bar
          data={downloadSpeedData}
          options={{
            plugins: {
              title: {
                display: true,
                text: "Average Download Speed by ASN",
              },
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: "Client ASN",
                },
              },
              y: {
                title: {
                  display: true,
                  text: "Speed (bps)",
                },
                beginAtZero: true,
              },
            },
          }}
        />
      </div>

      <div className="dataCard uploadSpeedCard">
        <Bar
          data={uploadSpeedData}
          options={{
            plugins: {
              title: {
                display: true,
                text: "Average Upload Speed by ASN",
              },
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: "Client ASN",
                },
              },
              y: {
                title: {
                  display: true,
                  text: "Speed (bps)",
                },
                beginAtZero: true,
              },
            },
          }}
        />
      </div>

      <div className="dataCard latencyCard">
        <Bar
          data={latencyData}
          options={{
            plugins: {
              title: {
                display: true,
                text: "Average Latency by ASN",
              },
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: "Client ASN",
                },
              },
              y: {
                title: {
                  display: true,
                  text: "Latency (ms)",
                },
                beginAtZero: true,
              },
            },
          }}
        />
      </div>
    </div>
  );
};
