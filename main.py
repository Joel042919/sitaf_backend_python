from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="SITAF AI Models API", description="API para predicción de stock y detección de anomalías usando Machine Learning", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class StockPredictionRequest(BaseModel):
    sismed_code: str
    hospital_unit: str

class AnomalyDetectionRequest(BaseModel):
    user_id: str
    sismed_code: str
    quantity_dispensed: int
    timestamp: str

@app.get("/")
def read_root():
    return {"message": "SITAF AI Service is running"}

@app.post("/predict/stock")
def predict_stock(request: StockPredictionRequest):
    # Mock de Prophet
    recommended_quantity = random.randint(100, 5000)
    confidence = round(random.uniform(0.7, 0.99), 2)
    return {
        "sismed_code": request.sismed_code,
        "recommended_quantity": recommended_quantity,
        "confidence": confidence,
        "model": "Prophet"
    }

@app.post("/detect/anomaly")
def detect_anomaly(request: AnomalyDetectionRequest):
    # Mock de Random Forest (Isolation Forest)
    is_anomaly = random.choice([True, False, False, False, False]) # 20% chance of anomaly
    risk_score = round(random.uniform(0.1, 0.95), 2) if is_anomaly else round(random.uniform(0.01, 0.2), 2)
    return {
        "is_anomaly": is_anomaly,
        "risk_score": risk_score,
        "model": "Random Forest Anomaly Detection",
        "action": "BLOCK" if risk_score > 0.8 else "ALLOW"
    }
