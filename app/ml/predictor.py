import numpy as np
import pandas as pd
from app.ml.model import model, le, symptoms_dict, cols

def predict_disease(symptoms_list):
    input_vector = np.zeros(len(symptoms_dict))

    for s in symptoms_list:
        if s in symptoms_dict:
            input_vector[symptoms_dict[s]] = 1

    input_df = pd.DataFrame([input_vector], columns=cols)

    probabilities = model.predict_proba(input_df)[0]
    index = probabilities.argmax()

    disease = le.inverse_transform([index])[0]
    confidence = round(probabilities[index] * 100, 2)

    return disease, confidence