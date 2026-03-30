from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Modelin doğru konumda olduğundan emin olarak yüklüyoruz
model = joblib.load("models/model.pkl")

# API'nin beklediği veri şemasını net bir şekilde tanımlıyoruz
class ModelInput(BaseModel):
    data: list[float]

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(input_data: ModelInput):
    # input_data.data bize tam olarak [5.1, 3.5, 1.4, 0.2] şeklinde sayısal bir liste verir
    prediction = model.predict([input_data.data])
    return {"prediction": prediction.tolist()}

