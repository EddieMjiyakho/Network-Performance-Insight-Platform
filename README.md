**Introduction**
The Network Performance Insights Platform (NPIP) is a web-based application designed to analyze and visualize internet performance metrics across Africa. By leveraging data from MLAB, Google BigQuery, and PostgreSQL, NPIP provides insights into key network performance indicators such as latency, throughput, packet loss, upload speed, download speed, and user satisfaction. The platform offers interactive dashboards, geospatial analysis, and historical data tracking, enabling stakeholders to identify regional disparities, detect anomalies, and improve internet infrastructure in underserved areas.

**Features**
Data Filtering: Filter network performance data by country, region, city, and ISP.

Date Range Selection: Analyze data for specific time periods.

Data Visualization: Visualize metrics using interactive charts (line, bar, pie) and geospatial maps.

Geospatial Analysis: View network performance across Africa using latitude and longitude.

Data Export: Export filtered data for further analysis.

User Authentication: Public access without requiring login.

Error Handling: Graceful handling of missing or invalid data.

**Requirements**
**Functional Requirements**
Filter data by country, region, city, and ISP.

Support date range selection for data analysis.

Visualize network performance metrics (latency, throughput, packet loss, etc.).

Provide geospatial analysis using latitude and longitude.

Allow data export in a user-friendly format.

Handle errors gracefully (e.g., no data available for selected criteria).

**Non-Functional Requirements**
Performance: Efficiently query large datasets from BigQuery and PostgreSQL, with data retrieval and visualization within 3 seconds.

Scalability: Handle data across various countries and regions in Africa.

Security: Encrypt data transmission using TLS.

Availability: Ensure 99.5% uptime for reliable access.

**Usability Requirements**
Intuitive user interface with easy-to-access filters and visualizations.

Responsive design for desktops, tablets, and smartphones.

Help section to guide users through key tasks.

Installation
Prerequisites
Python 3.x

Django

PostgreSQL

Google Cloud BigQuery API access

Node.js (for frontend dependencies)

Steps
Clone the Repository:

bash
Copy
git clone https://github.com/your-repo/NPIP.git
cd NPIP
Set Up Virtual Environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up PostgreSQL Database:

Create a PostgreSQL database and update the settings.py file with your database credentials.

Run migrations:

bash
Copy
python manage.py migrate
Load Data from BigQuery:

Use the provided Python script to fetch data from BigQuery and load it into PostgreSQL:

bash
Copy
python scripts/load_data.py
Run the Development Server:

bash
Copy
python manage.py runserver
Access the Platform:
Open your browser and navigate to http://127.0.0.1:8000/.

**Usage**
Dashboard Overview
Interactive Map: Visualize network performance metrics across Africa.

Metric Cards: View key performance indicators (latency, throughput, packet loss, etc.).

Filters: Filter data by region, country, city, and date range.

**How to Use**
Select Region: Use the region filter to narrow down data based on geographic location.

Select Country/Province/City: Refine your insights by choosing specific countries, provinces, or cities.

View Insights: Visualizations and metric cards will update dynamically based on your selections.

**Common Issues**
No Data Visualized: Ensure the selected country or region has available data. Try selecting a broader region or different country.

Slow Loading: Narrow down your filter options or check your internet connection.

**Architecture**
**Design Overview**
NPIP is built using Django’s Model-View-Template (MVT) pattern:

Model: Manages data interaction with PostgreSQL.

View: Handles business logic and data flow between the model and UI.

Template: Renders the user interface using HTML, CSS (Bootstrap), and JavaScript (Chart.js, Leaflet).

**Data Structure**
NetworkPerformanceData: Central model for storing network performance metrics.

AfricaRegion, Country, Region, City, ASN: Normalized tables for geographic and ISP data.

**External Services**
Google BigQuery: Data source for historical and real-time network performance data.

PostgreSQL: Database for storing and querying network performance data.

Chart.js: JavaScript library for interactive data visualization.

Leaflet: JavaScript library for geospatial maps.

**Testing**
**Testing Approach**
Unit Testing: Test individual components (API integrations, database queries, etc.).

Integration Testing: Verify data flow between frontend, backend, and database.

Functional Testing: Ensure features like data filtering and visualization work as intended.

Regression Testing: Automate tests using GitLab CI to ensure new updates don’t break existing functionality.

**Test Cases**
Normal Functioning: Filtering data by region, country, and city.

Extreme Boundary Cases: Handling areas with little to no data.

Invalid Data Handling: Graceful handling of invalid inputs.

**Contributing**
We welcome contributions to the NPIP project! If you'd like to contribute, please follow these steps:

**Fork the repository.**

Create a new branch for your feature or bug fix.

Commit your changes and push to your branch.

Submit a pull request with a detailed description of your changes.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**
For any questions or feedback, please contact:

Sakhile Mjiyakho: MJYSAK001@example.com

Lehlohonolo Mosikili: MSKLEH001@example.com

Maphuti Shilabje: SHLMAP001@example.com
