from fastapi import APIRouter, HTTPException
from app.schemas.text_data import TextData
from app.models.sentiment_model import SentimentModel

router = APIRouter()

try:
    sentiment_model = SentimentModel()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Model loading failed: {str(e)}")

@router.post("/predict/")
async def predict_sentiment(data: TextData):
    try:
        result = sentiment_model.predict(data.text)
        return {"label": result[0]['label'], "score": result[0]['score']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference failed: {str(e)}")
