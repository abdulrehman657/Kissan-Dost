from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# 1. Initialize API
app = FastAPI()

# 2. Allow your Vercel frontend to talk to this API safely (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Load your trained model brain
model = joblib.load("crop_model.pkl")

# 4. Define what data fields Vercel will send us
class FarmInput(BaseModel):
    Rainfall_mm: float
    GDD_HeatUnits: float
    Solar_Radiation: float
    Soil_pH: float
    Clay_Percent: float
    Sand_Percent: float
    Organic_Carbon: float
    Nitrogen_Base: float
    Phosphorus_Base: float
    Urea_Bags: float
    DAP_Bags: float
    Water_Source: int
    Seed_Type: int
    Land_Size_Acres: float

@app.get("/")
def home():
    return {"status": "Kisaan Dost AI Brain is Online"}

# 5. Calculate prediction when Vercel sends data
@app.post("/predict")
def predict_yield(data: FarmInput):
    features = [
        data.Rainfall_mm, data.GDD_HeatUnits, data.Solar_Radiation, data.Soil_pH,
        data.Clay_Percent, data.Sand_Percent, data.Organic_Carbon, data.Nitrogen_Base,
        data.Phosphorus_Base, data.Urea_Bags, data.DAP_Bags, data.Water_Source,
        data.Seed_Type, data.Land_Size_Acres
    ]
    
    prediction = model.predict([features])[0]
    
    return {
        "yield_per_acre": round(float(prediction), 2),
        "total_yield": round(float(prediction * data.Land_Size_Acres), 2)
    }