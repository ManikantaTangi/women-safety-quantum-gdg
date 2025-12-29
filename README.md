# 🚨 Quantum-Assisted Women Safety Emergency Response System

A real-time women safety web application that uses **classical + quantum hybrid optimization** to help **police reach a victim faster** after an SOS is triggered.

Built for hackathon evaluation with a **working MVP**, real maps, real routes, and a clear quantum use case.

---

## 🧠 Problem Statement

In emergency situations involving women safety (stalking, kidnapping, harassment), **every minute matters**.  
Traditional routing systems compute the shortest path, but **do not consider multiple probabilistic routes or optimization under uncertainty**.

Our solution assists **police and emergency responders** by:
- Receiving a victim’s live location via SOS
- Computing **multiple real-time routes**
- Using **quantum-inspired optimization** to select the fastest route
- Visually showing **optimal vs alternative routes** for transparency

---

## 💡 Key Idea

> **The goal is not to guide the victim — it is to help the police reach the victim faster.**

The system runs route optimization **on the responder side**, ensuring faster intervention.

---

## 🖥️ Project Architecture
Frontend (Web)
|
| SOS + Live Location
↓
Backend (FastAPI)
|
| Classical Preprocessing
| - Fetch real routes (OSRM)
| - Convert ETAs to cost functions
↓
Quantum Layer (Cirq)
|
| Probabilistic route optimization
↓
Classical Postprocessing
|
| Convert quantum output → optimal route
↓
Frontend Map

Optimal route (GREEN)

Alternative routes (GRAY)

---

## 🧩 Tech Stack (Google + Open)

### Frontend
- HTML, CSS, JavaScript
- Leaflet.js (OpenStreetMap)
- Deployed via **Firebase Hosting**

### Backend
- Python + FastAPI
- OSRM (Open Source Routing Machine)
- Dockerized backend
- Deployed on **Render**

### Quantum
- **Google Cirq**
- Hybrid quantum–classical optimization

### Google Technologies Used
- Google Cirq
- Firebase Hosting
- Google Cloud–compatible container deployment

---

## 🎯 Features

### User Interface
- SOS Button
- Women Safety Information
- Emergency Toll-Free Numbers
- Map-based visualization after SOS

### Backend Logic
- Live geolocation capture
- Real-time route fetching
- ETA normalization
- Quantum-assisted route selection
- Police location + route computation

### Visualization
- 📍 Victim Location
- 🚓 Police Location
- 🟢 Optimal Route (Quantum-selected)
- ⚪ Alternative Routes

---

## 🚀 How It Works (Step-by-Step)

1. User presses **SOS**
2. Browser sends **live latitude & longitude**
3. Backend fetches **real driving routes**
4. ETAs converted to **probability-based costs**
5. Quantum logic selects **optimal route**
6. Frontend displays:
   - Police station
   - Victim location
   - Optimized route (green)
   - Alternatives (gray)

---

## 📂 Repository Structure
women-safety-quantum-gdg/
├── frontend/
│ ├── index.html
│ ├── app.js
│ └── style.css
│
├── backend/
│ ├── main.py
│ ├── quantum.py
│ ├── requirements.txt
│ └── Dockerfile
│
└── README.md

---

## 🌐 Live Links

- **Frontend (Firebase Hosting):**  
  https://women-safety-quantum-gdg-17.web.app

- **Backend (Render):**  
  https://women-safety-backend-gdg.onrender.com

---

## 🎥 Demo Video
*(3-minute walkthrough covering SOS → route optimization → map visualization)*

> Link added in submission

---

## 📌 Why Quantum Here?

Route optimization with multiple alternatives is a **combinatorial optimization problem**.  
Quantum probabilistic sampling helps:
- Explore solution space efficiently
- Avoid local minima
- Demonstrate hybrid quantum advantage in real-world scenarios

---

## 🧪 Current Limitations & Future Scope

- Police station data can be expanded using official APIs
- Can integrate priority weighting (traffic, time of day)
- Can extend to ambulance & disaster response systems
- Scalable to smart-city safety infrastructure

---

## 👤 Author

**Manikanta**  
Electronics & Communication Engineering  
Hackathon Participant | Quantum + Systems Enthusiast

---

## 🏁 Final Note for Judges

This project:
- Has a **working MVP**
- Uses **real routes (not dummy data)**
- Applies **quantum logic meaningfully**
- Solves a **real societal problem**
- Is deployable, explainable, and extensible


