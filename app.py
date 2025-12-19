from fastapi import FastAPI
from pydantic import BaseModel

from symptom_extractor import extract_symptoms
from predictor import predict_disease
from model import cols
from data_loader import description_list, precautionDictionary

app = FastAPI(
    title="Healthcare AI Microservice",
    description="ML-based disease prediction using symptoms",
    version="1.0"
)

class SymptomRequest(BaseModel):
    symptoms: str

@app.post("/predict")
def predict(req: SymptomRequest):
    symptoms_list = extract_symptoms(req.symptoms, cols)

    if not symptoms_list:
        return {"error": "No valid symptoms detected"}

    disease, confidence = predict_disease(symptoms_list)

    return {
        "disease": disease,
        "confidence": confidence,
        "description": description_list.get(disease, ""),
        "precautions": precautionDictionary.get(disease, []),
        "disclaimer": "This is not medical advice. Consult a doctor."
    }