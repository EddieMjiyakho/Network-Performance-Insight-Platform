// src/Heatmap.js
import React, { useRef, useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.heat/dist/leaflet-heat.js';
import '../Styling/Heatmap.css'; // Ensure this CSS file is included for any custom styles

const Heatmap = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    // Ensure the map is initialized only once
    if (!mapRef.current._leaflet_id) {
      // Initialize the map
      const map = L.map(mapRef.current, {
        center: [9.0820, 8.6753], // Center the map on Africa
        zoom: 3, // Set initial zoom level
      });

      // Add tile layer for map background
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);

      // Fetch and add GeoJSON data for countries
      fetch('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson')
        .then(response => response.json())
        .then(geoData => {
          L.geoJSON(geoData, {
            onEachFeature: (feature, layer) => {
              // Add a click event to each country
              layer.on('click', (e) => {
                const countryName = feature.properties.ADMIN; 
                const { lat, lng } = e.latlng;

                // Show a popup with country name and coordinates
                L.popup()
                  .setLatLng([lat, lng])
                  .setContent(`<strong>${countryName}</strong><br>Coordinates: ${lat.toFixed(2)}, ${lng.toFixed(2)}`)
                  .openOn(map);
              });
            },
            style: {
              color: '#3388ff', // Boundary color
              weight: 2,
              fillOpacity: 0.1
            }
          }).addTo(map);
        });

      // Heatmap data example
      const heatData = [
        [9.0820, 8.6753, 1],  // Example points
        [10.7749, 7.4194, 3],
        [8.7949, 9.4294, 5],
        [-29.86, 24.08, 0.9],
        [-22.13, 17.05, 0.5],
        [8.7949, 9.4294, 5],
        [ -2.13, 21.45, 0.3]
      ];

      // Add heatmap layer
      L.heatLayer(heatData, { radius: 25 }).addTo(map);

      // Add map legend for heat intensity
      const legend = L.control({ position: 'bottomright' });

      legend.onAdd = function () {
        // Create a div element for the legend
        const div = L.DomUtil.create('div', 'info legend');
        const grades = [0, 0.1, 0.2, 0.3, 0.4, 0.5]; // Define intensity levels
        const colors = ['#0000ff', '#00ffff', '#00ff00', '#ffff00', '#ff8000', '#ff0000']; // Colors from blue to red

        div.innerHTML += '<strong>Heat Intensity</strong><br>';

        // Loop through the grades and create colored squares and labels
        for (let i = 0; i < grades.length; i++) {
          div.innerHTML +=
            `<i style="background:${colors[i]}; width: 18px; height: 18px; display:inline-block;"></i> ` +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
      };

      legend.addTo(map);

      // Cleanup function to properly remove the map when the component unmounts
      return () => {
        if (map) {
          map.remove();
        }
      };
    }
  }, []);

  // Return the map container with specific dimensions
  return <div ref={mapRef} style={{ height: '500px', width: '100%' }} />;
};

export default Heatmap;