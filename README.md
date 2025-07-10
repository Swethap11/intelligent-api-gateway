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
