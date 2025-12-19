🧪 Environment Setup
1️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is not available:

pip install fastapi uvicorn pandas numpy scikit-learn pillow torch torchvision

▶️ Run the FastAPI Server

From inside the ai-service directory:

uvicorn main:app --reload


Server will start at:

http://127.0.0.1:8000

✅ Verify Server is Running

Open your browser and visit:

http://127.0.0.1:8000


Expected response:

{"detail":"Not Found"}


This confirms the FastAPI server is running correctly.

📚 API Documentation (Swagger UI)

FastAPI provides built-in interactive documentation.

Open:

http://127.0.0.1:8000/docs


From here you can:

View all AI endpoints

Test APIs directly

Validate request/response formats

🔍 API Testing Guide
1️⃣ Disease Prediction API

Endpoint

POST /predict


Request Body

{
  "symptoms": ["fever", "headache", "cough"]
}


Sample Response

{
  "disease": "Viral Fever",
  "confidence": 87.3,
  "description": "A viral infection causing fever and body pain",
  "precautions": [
    "Take rest",
    "Drink fluids",
    "Consult a doctor"
  ]
}
