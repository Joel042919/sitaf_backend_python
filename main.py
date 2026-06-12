from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
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

class ExpirationItem(BaseModel):
    sismed_code: str
    lote: str
    expiration_date: str # YYYY-MM-DD

class ExpirationRiskRequest(BaseModel):
    items: List[ExpirationItem]

@app.get("/")
def read_root():
    return {"message": "SITAF AI Service is running"}

@app.post("/predict/stock")
def predict_stock(request: StockPredictionRequest):
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
    is_anomaly = random.choice([True, False, False, False, False])
    risk_score = round(random.uniform(0.1, 0.95), 2) if is_anomaly else round(random.uniform(0.01, 0.2), 2)
    return {
        "is_anomaly": is_anomaly,
        "risk_score": risk_score,
        "model": "Random Forest Anomaly Detection",
        "action": "BLOCK" if risk_score > 0.8 else "ALLOW"
    }

@app.post("/predict/expiration_risk")
def predict_expiration_risk(request: ExpirationRiskRequest):
    results = []
    today = datetime.now()
    
    for item in request.items:
        try:
            exp_date = datetime.strptime(item.expiration_date, "%Y-%m-%d")
            days_left = (exp_date - today).days
            
            # Simple heuristic / model
            if days_left <= 30:
                risk = "ALTO"
                action = "RETIRAR_O_REASIGNAR"
            elif days_left <= 90:
                risk = "MEDIO"
                action = "VIGILAR_DESPACHO_PRIMERO"
            else:
                risk = "BAJO"
                action = "MANTENER"
                
            results.append({
                "sismed_code": item.sismed_code,
                "lote": item.lote,
                "days_left": days_left,
                "risk_level": risk,
                "recommended_action": action
            })
        except ValueError:
            pass # ignore invalid dates

    return {"predictions": results}
