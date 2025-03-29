import pickle
from fastapi import APIRouter
import numpy as np
from interfaz import dataCultivo

router = APIRouter()

with open("cultivo.pkl","rb") as file:
    model=pickle.load(file)


@router.post("/cultivo")
def patient(data: dataCultivo):
    data = data.model_dump()
    print("========================================")

    N=data["N"]
    P=data["P"]
    K=data["K"]
    temperature=data["temperature"]
    humidity=data["humidity"]
    ph=data["ph"]
    rainfall=data["rainfall"]

    xin = np.array([N,P,K,temperature,humidity,ph,rainfall]).reshape(1,7)

    print(xin)
    prediction = model.predict(xin)

    print(prediction)

    return {"patient":prediction[0]}

