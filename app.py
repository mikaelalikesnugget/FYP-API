from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/rain_prediction")
def rain_prediction():
    predicted_rain = [0.0, 0.1, 0.3, 1.2, 0.0, 0.0, 0.0]
    RAIN_THRESHOLD = 0.2
    will_rain = any(r >= RAIN_THRESHOLD for r in predicted_rain)

    return {
        "prediction": "Most likely to rain" if will_rain else "Unlikely to rain",
        "max_rain_mm": max(predicted_rain),
        "next_7_days": predicted_rain
    }
