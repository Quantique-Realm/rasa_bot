# rasa_bot

# 🧠 Campus Assistant Chatbot (Rasa + React)

A smart, multi-functional chatbot built using **Rasa** and integrated with a **React frontend**, designed for use on a university campus. It can provide real-time assistance with campus navigation, events, emergency help, reminders, and more.

---

## 🚀 Features

- ✅ Dynamic multi-turn conversations
- 📅 Google Calendar integration for reminders
- 📍 Location-aware responses (campus map & transport)
- 🗣️ Voice-to-text input and speech output
- 🎭 Avatar animations with mouth 
- 🌐 Multilingual (English + Hindi)
- 🔐 Secure login (Auth0/Google Auth)
- 📱 React-based frontend UI

---

## 🛠️ Tech Stack

| Tech       | Description                         |
|------------|-------------------------------------|
| 🧠 Rasa     | NLP & Dialogue Management           |
| ⚛️ React    | Frontend framework (with Tailwind)  |
| 🗣️ Web Speech API | Voice input/output          |
| 🌍 OpenStreetMaps   | Campus map and route data           |
| 🐳 Docker   | Containerized deployment            |


---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rasa_bot.git
cd rasa_bot
```
### 2. Setup Rasa Environment
```bash
python3.10 -m venv rasa_env
source rasa_env/bin/activate
pip install --upgrade pip
pip install rasa
```
### 3.Train the Model
```bash
rasa train
```
### 3.Train the Model
```bash
rasa train
```

### 4.Run Rasa on Server
```bash
rasa run --enable-api
```
### 5.Run Rasa Actions
```bash
rasa run actions
```
## Folder Structure
```bash
📦 rasa_bot
├── frontend/                 # React frontend
├── data/                     # NLU & stories
├── models/                   # Trained Rasa models
├── actions/                  # Custom actions (Python)
├── domain.yml                # Intent, slots, entities, responses
├── config.yml                # Pipeline & policies
├── credentials.yml           # API credentials
├── endpoints.yml             # Rasa server endpoints
└── README.md                 # You're here!
```

### Testing The Bot
```bash
rasa shell
```
### To Run using Docker 
To run everything via Docker:
```bash
docker-compose up --build
```

