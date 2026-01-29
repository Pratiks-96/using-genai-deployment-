from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    # Later we’ll plug GenAI here
    return {"reply": f"Bot received: {req.message}"}

@app.get("/")
def root():
    return {"status": "GenAI DevOps Bot is running"}
