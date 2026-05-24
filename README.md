# 🤖 Interview Trainer Agent

An AI-powered Interview Preparation Platform that helps users practice technical and behavioral interviews using dynamic AI-generated questions and answers.

---

# 🌐 Live Demo

## 🚀 Frontend
https://watson-test.vercel.app

## ⚡ Backend API
https://interview-trainer-agent.onrender.com

---

# 📌 Problem Statement

Preparing for technical interviews requires:
- Continuous practice
- Role-specific preparation
- Real-time interaction
- Structured learning

Most platforms provide static content and lack intelligent interview simulation.

The AI Interview Trainer Agent solves this by generating personalized interview questions and answers dynamically using AI-powered architecture.

---

# 🎯 Objectives

✅ Generate interview questions dynamically  
✅ Support technical & HR interviews  
✅ Provide AI-generated answers  
✅ Build interactive interview preparation platform  
✅ Deploy full-stack AI application online  
✅ Create scalable architecture for future AI features  

---

# 💡 Proposed Solution

The system is designed as a full-stack AI-powered interview assistant.

It combines:
- React.js frontend
- FastAPI backend
- REST API communication
- RAG-inspired architecture
- IBM Watsonx / Granite AI concepts

The platform simulates real interview preparation experiences through intelligent conversational interaction.

---

# 🔑 Features

## ✅ Current Features

- 🎯 AI-generated interview questions
- 💬 Interactive chat interface
- ⚡ FastAPI backend integration
- 🌐 Frontend & backend deployment
- 📱 Responsive UI
- 🔄 Real-time API communication

---

## 🚀 Upcoming Features

- 📄 Resume upload
- 🧠 AI scoring system
- 🎙️ Voice interviews
- 🔐 Authentication system
- 📊 Dashboard analytics
- 📑 PDF report generation

---

# 🧰 Tech Stack

## 🎨 Frontend
- React.js
- JavaScript
- HTML5
- CSS3

## ⚙️ Backend
- FastAPI
- Python
- Uvicorn

## ☁️ Deployment
- Vercel
- Render
- GitHub

## 🧠 AI Concepts
- IBM Watsonx.ai
- Granite LLM
- Retrieval-Augmented Generation (RAG)

---

# 🏗️ System Architecture

```text
User Input
    ↓
React Frontend
    ↓
FastAPI Backend
    ↓
AI / RAG Processing
    ↓
Generated Interview Questions & Answers
    ↓
Frontend Response Display
```

---

# 📂 Project Structure

```text
watson-test/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── runtime.txt
│   └── __init__.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   │
│   ├── package.json
│   └── package-lock.json
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sushanth0963/watson-test.git
```

---

## 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

## 3️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# 🔄 API Endpoint

## POST Request

```text
POST /chat
```

---

## Example Request

```json
{
  "message": "Python interview questions"
}
```

---

## Example Response

```json
{
  "response": "Generated interview questions and answers"
}
```

---

# ☁️ Deployment

## 🚀 Frontend Deployment
Hosted on Vercel

```text
https://watson-test.vercel.app
```

---

## ⚡ Backend Deployment
Hosted on Render

```text
https://interview-trainer-agent.onrender.com
```

---

# 🧠 Workflow

## Step 1
User enters interview topic.

## Step 2
Frontend sends API request.

## Step 3
Backend processes query.

## Step 4
AI response is generated.

## Step 5
Frontend displays response dynamically.

---

# 📊 Sample Output

## Input

```text
Python interview questions
```

---

## Output

```text
1. What is the difference between list and tuple?
2. Explain OOP concepts in Python.
3. What is the purpose of self keyword?
4. Explain exception handling in Python.
```

---

# 🚧 Challenges Faced

## 🔹 Frontend Deployment Issues
- Frontend folder not visible in Vercel
- Git tracking problems
- node_modules cleanup

## 🔹 API Integration Issues
- Localhost backend URLs
- CORS handling
- Deployment configuration

## ✅ Solutions
- Correct GitHub repository structure
- Updated deployed backend URL
- Proper Vercel configuration

---

# 🔮 Future Scope

- 📄 Resume-based interview generation
- 🧠 AI scoring system
- 🎙️ Voice-enabled interviews
- 🌍 Multi-language support
- 📹 Video interview analysis
- 🤖 AI interviewer avatar
- 📊 Analytics dashboard

---

# 📚 References

- IBM Watsonx.ai Documentation
- FastAPI Documentation
- React.js Documentation
- Vercel Documentation
- Render Documentation
- RAG Research Papers

---

# 👨‍💻 Author

## Sushanth

---

# ⭐ Conclusion

AI Interview Trainer Agent demonstrates:

✅ Full-stack development  
✅ API integration  
✅ Cloud deployment  
✅ Frontend-backend communication  
✅ AI-powered interview preparation  
✅ Scalable AI architecture  

