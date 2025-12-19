import csv
from model import cols

description_list = {}
precautionDictionary = {}

with open("MasterData/symptom_Description.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        description_list[row[0]] = row[1]

with open("MasterData/symptom_precaution.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        precautionDictionary[row[0]] = row[1:]