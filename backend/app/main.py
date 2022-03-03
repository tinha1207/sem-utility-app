from fastapi import FastAPI
from .api.api_v1 import endpoints

app = FastAPI()

app.include_router(
    
)