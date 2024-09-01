// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Function to fetch data from the API
async function fetchData() {
  try {
      const response = await fetch('/api/country-download-speeds/');
      const result = await response.json();

      const countries = result.countries; // e.g., ["US", "CA", "GB", ...]
      const downloadSpeeds = result.download_speeds; // e.g., [20, 25, 30, ...]

      // Create the chart using the fetched data
      createChart(countries, downloadSpeeds);
  } catch (error) {
      console.error('Error fetching country download speeds data:', error);
  }
}

// Function to create the chart
function createChart(countries, downloadSpeeds) {
  var ctx = document.getElementById("myBarChart");
  var myBarChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: countries,
          datasets: [{
              label: "Average Download Speed",
              backgroundColor: "rgba(78, 115, 223, 0.5)",
              borderColor: "rgba(78, 115, 223, 1)",
              data: downloadSpeeds,
          }],
      },
      options: {
          maintainAspectRatio: false,
          layout: {
              padding: {
                  left: 10,
                  right: 25,
                  top: 25,
                  bottom: 0
              }
          },
          scales: {
              xAxes: [{
                  ticks: {
                      autoSkip: false,
                      maxRotation: 90,
                      minRotation: 45
                  },
                  gridLines: {
                      display: false
                  }
              }],
              yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      callback: function(value, index, values) {
                          return value; // Customize if needed
                      }
                  },
                  gridLines: {
                      color: "rgb(234, 236, 244)",
                      zeroLineColor: "rgb(234, 236, 244)",
                      drawBorder: false,
                      borderDash: [2],
                      zeroLineBorderDash: [2]
                  }
              }],
          },
          legend: {
              display: false
          },
          tooltips: {
              backgroundColor: "rgb(255,255,255)",
              bodyFontColor: "#858796",
              titleMarginBottom: 10,
              titleFontColor: '#6e707e',
              titleFontSize: 14,
              borderColor: '#dddfeb',
              borderWidth: 1,
              xPadding: 15,
              yPadding: 15,
              displayColors: false,
              intersect: false,
              mode: 'index',
              caretPadding: 10,
              callbacks: {
                  label: function(tooltipItem, chart) {
                      var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                      return datasetLabel + ': ' + tooltipItem.yLabel;
                  }
              }
          }
      }
  });
}

// Fetch and create the chart with dynamic data
fetchData();
