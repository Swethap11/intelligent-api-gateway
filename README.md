# 🛡️ Intelligent API Gateway with Threat Detection

This project is a lightweight API gateway that does more than just forward traffic — it actively monitors incoming HTTP requests and flags potentially malicious ones using machine learning.

Whether it’s suspicious payloads, unusual traffic spikes, or known attack patterns, this gateway helps detect threats in real-time and gives you visibility through a live dashboard.

---

## 🔧 Project Overview

This is a custom-built reverse proxy that:

- Forwards valid API requests to backend services  
- Detects malicious behavior (SQL injections, DDoS patterns, etc.) using an ML classifier  
- Tracks request stats and flags threats  
- Visualizes everything in a live dashboard (IP activity, threat scores, etc.)

It’s designed as a modular system so you can plug it into any microservice architecture or test it as a standalone project.

---

## 📁 Folder Structure

intelligent-api-gateway/
├── proxy/ # Reverse proxy server (Flask)
│ └── app.py # Core proxy logic
├── ml_threat_detector/ # ML-based anomaly detection service
│ └── model.py # Model training and prediction
├── dashboard/ # Real-time visualization dashboard
│ └── app.py # UI logic (Flask or Streamlit)
├── data/ # Sample logs, test data
│ └── sample_logs.csv
├── config/ # IP blocklist, rate-limiting rules
│ └── config.yaml
├── scripts/ # Utility scripts (e.g., data generator)
│ └── simulate_logs.py
├── Dockerfile # Containerize the full system
├── requirements.txt # Python dependencies
└── README.md


---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/intelligent-api-gateway.git
cd intelligent-api-gateway

# Set up virtual environment
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
