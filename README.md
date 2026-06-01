# 🌱 Smart Irrigation System using Machine Learning

An intelligent irrigation management system that uses **Machine Learning** and **IoT sensors** to automate water supply for agricultural fields based on real-time environmental conditions.

---

## 📌 Project Overview

The Smart Irrigation System aims to reduce water wastage and improve agricultural efficiency by analyzing sensor data such as:

* Soil Moisture
* Temperature
* Humidity
* Rainfall Conditions

Using Machine Learning algorithms, the system predicts whether irrigation is required and automatically controls the water pump.

---

## 🚀 Features

* 🌡 Real-time temperature and humidity monitoring
* 💧 Soil moisture detection
* 🤖 Machine Learning-based irrigation prediction
* ⚡ Automatic water pump control
* 📊 Dashboard for monitoring sensor data
* ☁ Future-ready IoT integration
* 📈 Historical data analysis

---

## 🛠 Tech Stack

### Hardware

* Arduino / NodeMCU / Raspberry Pi
* Soil Moisture Sensor
* DHT11 / DHT22 Sensor
* Relay Module
* Water Pump

### Software

* Python
* Scikit-learn
* Flask / FastAPI
* HTML, CSS, JavaScript
* React (Optional)
* MongoDB / MySQL

---

## 🧠 Machine Learning Model

The ML model predicts irrigation requirements using environmental data.

### Input Parameters

* Soil Moisture
* Temperature
* Humidity
* Rainfall
* Water Level

### Algorithms Used

* Decision Tree
* Random Forest
* Logistic Regression

---

## 📂 Project Structure

```bash
smart-irrigation-system/
│
├── dataset/
│   └── irrigation_data.csv
│
├── model/
│   └── irrigation_model.pkl
│
├── backend/
│   ├── app.py
│   └── routes/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── arduino/
│   └── irrigation_controller.ino
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/smart-irrigation-system.git
cd smart-irrigation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

---

## 📊 Dataset Fields

| Parameter     | Description               |
| ------------- | ------------------------- |
| Soil Moisture | Moisture level in soil    |
| Temperature   | Environmental temperature |
| Humidity      | Air humidity              |
| Rainfall      | Rain prediction/value     |
| Pump Status   | ON/OFF condition          |

---

## 🔄 Workflow

1. Collect sensor data
2. Store data in database
3. Preprocess data
4. Train ML model
5. Predict irrigation requirement
6. Activate water pump automatically
7. Display results on dashboard

---

## 📈 Future Enhancements

* Mobile application support
* Weather API integration
* Cloud-based monitoring
* AI crop recommendation system
* Solar-powered irrigation

---

## 🌍 Applications

* Smart Agriculture
* Precision Farming
* Greenhouse Automation
* Water Resource Management

---

## ✅ Advantages

* Saves water
* Reduces manual effort
* Improves crop productivity
* Prevents over-irrigation
* Cost-effective solution

---

## 📸 Screenshots

*Add screenshots here*

---

## 🤝 Contributors

* Your Name

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Conclusion

The Smart Irrigation System using Machine Learning provides an efficient and sustainable solution for modern farming by combining IoT devices with intelligent prediction models to automate irrigation and optimize water usage.
