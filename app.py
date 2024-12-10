from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Загрузка модели
model = joblib.load('model.joblib')

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict/")
async def predict(data: InputData):
    features = [[data.feature1, data.feature2]]
    prediction = model.predict(features)
    return {"prediction": prediction[0]}
