from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .api.api_v1.endpoints import iso_keyword

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://juvom-001:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(iso_keyword.router)
