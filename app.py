from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = "flutterflow_yesterday_today_tomorrow.csv"
df = pd.read_csv(CSV_PATH)

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/rain_prediction")
def rain_prediction(region: str, dayIndex: int):
    row = df[
        (df["region"].str.lower() == region.lower()) &
        (df["dayIndex"] == dayIndex)
    ]

    if row.empty:
        raise HTTPException(status_code=404, detail="No data found")

    r = row.iloc[0]
    pred = int(r["predictionInt"])

    return {
        "region": r["region"],
        "dayIndex": int(r["dayIndex"]),
        "date": str(r["date"]),
        "rain_mm": float(r["q50_mm"]),
        "predictionInt": pred,
        "predictionText": "Most likely to rain" if pred == 1 else "Most likely not to rain"
    }
