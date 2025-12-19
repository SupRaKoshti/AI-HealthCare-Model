import re
from difflib import get_close_matches

symptom_synonyms = {
    "stomach ache": "stomach_pain",
    "belly pain": "stomach_pain",
    "loose motion": "diarrhea",
    "motions": "diarrhea",
    "high temperature": "fever",
    "body ache": "muscle_pain",
    "breathing issue": "breathlessness"
}

def extract_symptoms(text, all_symptoms):
    text = text.lower().replace("-", " ")
    found = []

    # Phrase matching
    for phrase, mapped in symptom_synonyms.items():
        if phrase in text:
            found.append(mapped)

    # Exact symptom matching
    for s in all_symptoms:
        if s.replace("_", " ") in text:
            found.append(s)

    # Fuzzy matching
    words = re.findall(r"\w+", text)
    for w in words:
        match = get_close_matches(
            w,
            [s.replace("_", " ") for s in all_symptoms],
            n=1,
            cutoff=0.8
        )
        if match:
            for s in all_symptoms:
                if s.replace("_", " ") == match[0]:
                    found.append(s)

    return list(set(found))
