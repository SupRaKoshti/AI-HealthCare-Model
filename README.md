# Healthcare AI Service

A FastAPI-based AI microservice that predicts diseases from symptoms using a machine learning model and generates human-readable explanations using an LLM (Groq).

---

## Table of Contents

- [Environment Setup](#environment-setup)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [LLM Configuration](#llm-configuration)
  - [Create .env File](#create-env-file)
  - [LLM Model Used](#llm-model-used)
- [Running the Server](#running-the-server)
  - [Verify Server is Running](#verify-server-is-running)
- [API Documentation](#api-documentation)
- [API Usage](#api-usage)
  - [Disease Prediction with AI Explanation](#disease-prediction-with-ai-explanation)
- [AI Processing Flow](#ai-processing-flow)
- [Tech Stack](#tech-stack)
- [Disclaimer](#disclaimer)

---

## Environment Setup

### Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:
```bash
pip install fastapi uvicorn pandas numpy scikit-learn python-dotenv requests
```

---

## LLM Configuration

This service uses **Groq LLM** for generating explanation text.

### Create .env File

Create a `.env` file in the root of the AI service:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### LLM Model Used
```
llama-3.1-8b-instant
```

This model does not require GPU and works well on CPU-based environments.

---

## Running the Server

From inside the `ai_service` directory:
```bash
uvicorn app.app:app --reload
```

The server will start at:
```
http://127.0.0.1:8000
```

### Verify Server is Running

Open the browser and visit:
```
http://127.0.0.1:8000
```

Expected response:
```json
{"detail":"Not Found"}
```

---

## API Documentation

FastAPI provides built-in **Swagger UI**.

Open:
```
http://127.0.0.1:8000/docs
```

You can view all endpoints and test APIs directly from the browser.

---

## API Usage

### Disease Prediction with AI Explanation

**Endpoint:**
```
POST /predict
```

#### Request Body (List of Symptoms)
```json
{
  "symptoms": ["fever", "headache", "cough"]
}
```

#### Request Body (Free Text)
```json
{
  "symptoms": "I have high fever and body pain for two days"
}
```

#### Sample Response
```json
{
  "condition": "Viral Fever",
  "confidence": 87.3,
  "severity": "Moderate",
  "precautions": [
    "Take adequate rest",
    "Drink plenty of fluids",
    "Avoid cold food"
  ],
  "explanation": "Based on the symptoms provided, this condition is commonly associated with a viral infection. Rest and hydration are important. Please consult a doctor for confirmation.",
  "disclaimer": "This information is for educational purposes only and is not medical advice."
}
```

---

## AI Processing Flow

1. Symptoms are received as text or list
2. Symptoms are normalized and extracted
3. ML model predicts disease and confidence
4. Structured prompt is generated
5. Prompt is sent to Groq LLM
6. LLM generates explanation text
7. Combined response is returned to client

---

## Tech Stack

- **FastAPI** - Web framework
- **Python** - Programming language
- **Scikit-learn** - Machine learning
- **Groq LLM (LLaMA 3.1)** - AI explanation generation
- **Swagger UI** - API documentation

---

## Disclaimer

⚠️ **Important Notice:**

- This system does **not** provide medical diagnosis
- Always consult a qualified medical professional
- This information is for educational purposes only and is not medical advice

---
