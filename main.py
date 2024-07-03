from fastapi import FastAPI

from app import app
import pytouch

from app.endpoints import sentiment

app = FastAPI()

app.include_router(sentiment.router, prefix="/sentiment", tags=["sentiment"])

# Add a root endpoint for health check or basic info
@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API"}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
