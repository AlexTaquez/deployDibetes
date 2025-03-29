from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estuduante: float

class dataPatient(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
