# app/models/sentiment_model.py
from transformers import pipeline
import os

class SentimentModel:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), 'local_model')
        self.model = pipeline(
            "sentiment-analysis",
            model=model_path,
            tokenizer=model_path
        )

# Create a global instance of the model
sentiment_model = SentimentModel()
