🌍 Network Performance Insights Platform (NPIP)

📖 Overview  
The **Network Performance Insights Platform (NPIP)** is a web-based application designed to analyze and visualize internet performance metrics across Africa.  
By integrating data from **MLAB**, **Google BigQuery**, and **PostgreSQL**, NPIP provides valuable insights into key indicators such as **latency**, **throughput**, **packet loss**, **upload/download speed**, and **user satisfaction**.

This project was developed as part of my final-year capstone to demonstrate my skills in:

- Full-stack web development (Django + HTML/CSS/JS)
- Data engineering with BigQuery and PostgreSQL
- Data visualization using Chart.js and Leaflet
- API integration and backend automation
- Agile development and collaborative teamwork

👨‍💻 My Role & Contributions  
As the **Team Leader and Fullstack Developer**, my responsibilities included:

- Designing the system architecture using Django’s MVT pattern.  
- Implementing backend logic to fetch and process network performance data from BigQuery to PostgreSQL.  
- Developing interactive visualizations and geospatial dashboards.  
- Conducting regression testing using GitLab CI/CD.  
- Coordinating development tasks and sprint reviews with team members.

Team Members:
- **Sakhile Mjiyakho** – Fullstack (Team Leader)  
- **Lehlohonolo Mosikili** – Backend (Architect)  
- **Maphuti Shilabje** – Frontend (Communicator)

🚀 Features  

**Core Features**
- 📊 **Data Visualization:** Interactive charts (line, bar, pie) and geospatial maps.  
- 🌐 **Geospatial Analysis:** Visualize performance across Africa using latitude and longitude.  
- 🎚️ **Filtering:** Filter data by **region**, **country**, **province**, **city**, and **ISP**.  
- 🗓️ **Date Range Selection:** Analyze data across custom time periods.  
- 💾 **Data Export:** Export filtered data for extended analysis.  
- 🔒 **Error Handling:** Graceful handling of missing or invalid data.  
- 📱 **Responsive Design:** Optimized for desktop and mobile users.  

🛠️ Tech Stack  

**Backend:** Django (Python)  
**Frontend:** HTML, CSS, JavaScript, Chart.js, Leaflet  
**Database:** PostgreSQL  
**Cloud Services:** Google BigQuery  
**CI/CD:** GitLab for regression testing and automation  
**Hosting:** Localhost (development)  

🧠 System Architecture  

The NPIP follows the **Model-View-Template (MVT)** architecture pattern:

- **Model:** Manages data storage and interaction with PostgreSQL.  
- **View:** Processes data from BigQuery, applies filters, and passes data to templates.  
- **Template:** Displays visualizations and maps using Chart.js and Leaflet.  

Data Flow:
1. Fetch data from Google BigQuery.  
2. Store processed data in PostgreSQL.  
3. Visualize metrics on the frontend dashboard.  

🧪 Testing  

**Testing Methods**
- ✅ **Unit Testing:** Tested individual components (API integrations, data models, etc.)  
- ✅ **Integration Testing:** Verified data flow between backend and frontend.  
- ✅ **Functional Testing:** Confirmed data filtering and visualizations operate correctly.  
- ✅ **Regression Testing:** Automated via GitLab to ensure stability after updates.  

**Example Test Scenarios**
- Normal use: Filtering data by region/country/city.  
- Edge cases: Handling empty or invalid datasets.  
- Boundary testing: Testing large data queries from BigQuery.  

📑 Project Report  
A detailed project report covering the **design, implementation, testing**, and **evaluation** of NPIP is available here: [`Final_Report`](https://drive.google.com/file/d/1kIWECehAAe9QiEAno0cgxXhs4kvpkijw/view?usp=sharing).

▶️ Running the Project
Clone the repository

Navigate into the project folder
cd NPIP

Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Set up the PostgreSQL database

Create a PostgreSQL database.

Update your settings.py with database credentials.

Run migrations:

python manage.py migrate

Load data from BigQuery
python scripts/load_data.py

Run the development server
python manage.py runserver


📊 Usage
Dashboard Overview

🗺️ Interactive Map: Visualizes network performance across Africa.

📈 Metric Cards: Display KPIs (latency, throughput, packet loss, etc.).

🎚️ Filters: Filter by region, country, city, and date range.

How to Use

Select a region or country using the filters.

Adjust the date range to focus on a specific period.

Visualizations update dynamically to reflect your selections.

Common Issues

❌ No Data: Try selecting a different region or broader time range.

🕒 Slow Load: Narrow filters or check your internet connection.

📈 Performance & Scalability

⚡ Query Efficiency: Optimized queries retrieve data within ~3 seconds.

🌍 Scalability: Supports multiple African countries and large datasets.

🔒 Security: TLS encryption ensures secure data transfer.

💻 Availability: Designed for 99.5% uptime in production environments.

📌 Future Improvements

🔐 Add user authentication and role-based access.

🧠 Integrate real-time data from RIPE Atlas or similar APIs.

📉 Add advanced analytics (trend forecasting, anomaly detection).

☁️ Deploy to a cloud-based production environment (AWS or GCP).
