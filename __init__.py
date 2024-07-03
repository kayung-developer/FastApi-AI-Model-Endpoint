from fastapi import FastAPI
from app.routers import inference

app = FastAPI()

app.include_router(inference.router)
