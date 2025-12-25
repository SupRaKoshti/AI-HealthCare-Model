from fastapi import FastAPI
from pydantic import BaseModel

from symptom_extractor import extract_symptoms
from app.ml.predictor import predict_disease
from app.ml.model import cols
from app.llm.prompts import build_explanation_prompt
from app.llm.groq_client import generate_human_reply
from app.schemas import SymptomRequest, AIResponse
from data_loader import description_list, precautionDictionary

app = FastAPI(
    title="Healthcare AI Microservice",
    description="ML-based disease prediction using symptoms",
    version="1.0"
)

@app.post("/predict", response_model=AIResponse)
def predict(req: SymptomRequest):
    symptoms_list = extract_symptoms(req.symptoms, cols)

    if not symptoms_list:
        return {"error": "No valid symptoms detected"}
    
    disease, confidence = predict_disease(symptoms_list)

    severity = "mild"
    if confidence > 70:
        severity = "severe"
    elif confidence > 40:
        severity = "moderate"

    ai_result = {
        "condition": disease,
        "confidence": confidence,
        "severity": severity,
        "description": description_list.get(disease, ""),
        "precautions": precautionDictionary.get(disease, [])
    }

    try:
        prompt = build_explanation_prompt(ai_result)
        explanation = generate_human_reply(prompt)
    except Exception:
        explanation = (
            f"You may have {disease} with a confidence of {confidence}%. "
            "Please consult a qualified doctor for further evaluation."
        )

    return {
        "condition": disease,
        "confidence": float(confidence),
        "severity": "moderate",
        "precautions": precautionDictionary.get(disease, []),
        "explanation": explanation
    }