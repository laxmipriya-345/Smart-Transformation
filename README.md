Smart Transformer Monitoring System

A full-stack IoT-based Smart Transformer Monitoring System that monitors transformer parameters in real time, predicts faults, and provides a web dashboard for visualization.

🚀 Project Overview

This project integrates:

🌐 IoT Device (ESP8266 / NodeMCU)

🧠 Backend API (Flask + JWT Authentication)

🗄 Database (MySQL)

💻 Frontend (React)

📊 Machine Learning (Optional – GRU / Fault Prediction)

The system collects transformer parameters like temperature, voltage, and current, stores them in a database, and displays real-time data on a dashboard.

🏗 System Architecture
ESP8266 (Sensors)
        ↓
Flask Backend API
        ↓
MySQL Database
        ↓
React Frontend Dashboard

🔧 Technologies Used
Backend
Python
Flask
JWT Authentication
MySQL
REST APIs
Frontend
React.js
Axios
React Router
IoT Layer
ESP8266 (NodeMCU)
PlatformIO
WiFi HTTP Communication
Machine Learning (Optional)
GRU / LSTM for time-series prediction
Fault detection model

📌 Features

✅ User Registration & Login (JWT secured)
✅ Secure REST APIs
✅ Real-time Transformer Data Monitoring
✅ Database Storage of Sensor Data
✅ Device Simulator for Testing
✅ ESP Integration Ready
✅ Dashboard for Data Visualization

🔮 Fault Prediction Module (Future Enhancement)

📂 Project Structure
smart-transformer/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── core/
│   ├── app.py
│   └── device_simulator.py
│
├── frontend-react/
│   ├── src/
│   └── package.json
│
└── esp-device/
    ├── platformio.ini
    └── src/main.cpp
▶ How to Run the Project
1️⃣ Run Backend
cd backend
python app.py

Backend runs on:

http://localhost:5000
2️⃣ Run Frontend
cd frontend-react
npm install
npm start

Frontend runs on:

http://localhost:3000
3️⃣ Run Device Simulator (Optional)
python device_simulator.py
🔐 API Endpoints
Authentication
POST /register
POST /login
Device APIs
POST /device-data → ESP sends data
GET /device-data → Dashboard fetches data (JWT required)

📊 Future Enhancements
🔮 GRU-based fault prediction
📈 Real-time charts & analytics
☁ Cloud deployment
📱 Mobile responsive UI
🚨 Alert & notification system
🎯 Project Status

✔ Backend Completed
✔ API Tested
✔ ESP Structure Created
✔ Frontend In Development

👩‍💻 Developed By

Smart Transformer Monitoring Team
(B.Tech CSE – Industry-Level IoT Project)
