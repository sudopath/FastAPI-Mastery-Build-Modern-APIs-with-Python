from fastapi import FastAPI
from models import get_sentiment_model


app = FastAPI()

model = get_sentiment_model()

@app.post("/analyze/")
async def predict_sentiment(text: str):
    result = model(text)
    return {"text":text,"sentiment": result}