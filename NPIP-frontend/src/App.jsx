import React from "react";
import { Chart as ChartJS, defaults } from "chart.js/auto";
import { Bar } from "react-chartjs-2";

import "./App.css";
import sourceData from "./data/sourceData.json"; 

defaults.maintainAspectRatio = false;
defaults.responsive = true;

defaults.plugins.title.display = true;
defaults.plugins.title.align = "start";
defaults.plugins.title.font.size = 20;
defaults.plugins.title.color = "black";

export const App = () => {
  return (
    <div className="App">
      <div className="dataCard downloadSpeedCard">
        <Bar
          data={{
            labels: sourceData.map((data) => data.clientASN),
            datasets: [
              {
                label: "Average Download Speed",
                data: sourceData.map((data) => Number(data.avg_download_speed)),
                backgroundColor: "rgba(75, 192, 192, 0.8)",
                borderRadius: 5,
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                text: "Average Download Speed by ASN",
              },
            },
          }}
        />
      </div>

      <div className="dataCard uploadSpeedCard">
        <Bar
          data={{
            labels: sourceData.map((data) => data.clientASN),
            datasets: [
              {
                label: "Average Upload Speed",
                data: sourceData.map((data) => Number(data.avg_upload_speed)),
                backgroundColor: "rgba(153, 102, 255, 0.8)",
                borderRadius: 5,
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                text: "Average Upload Speed by ASN",
              },
            },
          }}
        />
      </div>

      <div className="dataCard latencyCard">
        <Bar
          data={{
            labels: sourceData.map((data) => data.clientASN),
            datasets: [
              {
                label: "Average Latency",
                data: sourceData.map((data) => Number(data.avg_latency)),
                backgroundColor: "rgba(255, 99, 132, 0.8)",
                borderRadius: 5,
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                text: "Average Latency by ASN",
              },
            },
          }}
        />
      </div>
    </div>
  );
};