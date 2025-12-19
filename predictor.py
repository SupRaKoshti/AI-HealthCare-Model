import numpy as np
from model import model, le, symptoms_dict

def predict_disease(symptoms_list):
    input_vector = np.zeros(len(symptoms_dict))

    for s in symptoms_list:
        if s in symptoms_dict:
            input_vector[symptoms_dict[s]] = 1

    probabilities = model.predict_proba([input_vector])[0]
    index = probabilities.argmax()

    disease = le.inverse_transform([index])[0]
    confidence = round(probabilities[index] * 100, 2)

    return disease, confidence
