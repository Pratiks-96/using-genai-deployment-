from fastapi import FastAPI, HTTPException
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
    try:
        response = requests.post(AI_SERVICE_URL, json={"message": req.message}, timeout=10)
        response.raise_for_status()
        return {"reply": response.json().get("reply", "No reply from AI service")}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")
