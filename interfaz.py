from pydantic import BaseModel

class dataCultivo(BaseModel):
    N: int
    P: int
    K: int
    temperature: float 
    humidity: float 
    ph: float 
    rainfall: float
