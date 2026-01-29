from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="GenAI DevOps Bot")

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://ai-service:8000/chat")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/health")
def health():
    return {"status": "GenAI DevOps Bot is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    response = requests.post(AI_SERVICE_URL, json={"message": req.message})
    response.raise_for_status()
    return {"reply": response.json()["reply"]}
