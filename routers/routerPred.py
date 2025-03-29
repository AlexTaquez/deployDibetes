import pickle
from fastapi import APIRouter
import numpy as np
from interfaz import dataPatient

router = APIRouter()

with open("RFDiabetesv132.pkl","rb") as file:
    model=pickle.load(file)


@router.post("/patient")
def patient(data: dataPatient):
    data = data.model_dump()
    print("========================================")

    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]
    Age=data["Age"]

    xin = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)

    print(xin)
    prediction = model.predict(xin)

    labels = ['ENFERMO','SANO']
    return {"patient":labels[prediction[0]]}

