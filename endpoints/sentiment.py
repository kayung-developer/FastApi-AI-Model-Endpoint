# app/endpoints/sentiment.py
from fastapi import APIRouter
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.models.sentiment_model import sentiment_model

router = APIRouter()

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):
    result = sentiment_model.model(request.text)[0]
    return SentimentResponse(label=result['label'], score=result['score'])
