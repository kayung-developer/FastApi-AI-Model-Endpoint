# app/schemas/sentiment.py
from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float
