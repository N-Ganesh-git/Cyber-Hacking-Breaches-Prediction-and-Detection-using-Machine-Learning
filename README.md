# Cyber Hacking Breaches – Prediction and Detection using Machine Learning

This project focuses on detecting **phishing URLs** using **Machine Learning** and deploying the model through a clean, user-friendly **Flask web application**.  
Users can enter any URL, and the system instantly predicts whether it is:

- **Legitimate (Safe)**  
- **Phishing (Malicious)**  

The model also provides a **confidence score** for transparency and reliability.

---

## Project Overview

Phishing attacks are one of the most widespread cyber threats.  
This project predicts malicious URLs using **lexical URL features** and a **RandomForestClassifier**, forming a complete **end-to-end ML pipeline**, including:

- Feature engineering  
- Model training  
- Evaluation  
- Flask deployment  
- Web UI with real-time predictions  

---

## Tech Stack

### **Machine Learning**
- Python  
- scikit-learn  
- NumPy  
- Pandas  

### **Web Application**
- Flask  
- HTML  
- Bootstrap 5  

---

## Project Structure
phishing-url-detection/
│
├── app.py # Main Flask application
├── feature.py # URL feature extraction logic
├── requirements.txt # Dependencies list
├── README.md # Project documentation
├── .gitignore # Ignored files
│
├── model/
│ └── model.pkl # Trained RandomForest model
│
└── templates/
└── index.html # Bootstrap-based web UI

