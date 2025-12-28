from pydantic import BaseModel
from typing import List

class SymptomRequest(BaseModel):
    symptoms: List[str] | str
    age: int
    gender: str

class AIResponse(BaseModel):
    condition: str
    confidence: float
    severity: str
    precautions: List[str]
    explanation: str