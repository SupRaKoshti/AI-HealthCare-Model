import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

# Load dataset
training = pd.read_csv("Data/Training.csv")

# Clean column names
training.columns = training.columns.str.replace(r"\.\d+$", "", regex=True)
training = training.loc[:, ~training.columns.duplicated()]

cols = training.columns[:-1]
X = training[cols]
y = training["prognosis"]

# Encode target
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)
model.fit(X, y)

# Symptom index mapping
symptoms_dict = {symptom: i for i, symptom in enumerate(cols)}
