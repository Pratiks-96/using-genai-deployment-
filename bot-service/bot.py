from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="GenAI DevOps Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://ai-service:8000/chat")

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "GenAI DevOps Bot is running"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = requests.post(AI_SERVICE_URL, json={"message": req.message})
    return {"reply": response.json()["reply"]}
