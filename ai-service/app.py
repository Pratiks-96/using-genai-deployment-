from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(req: Request):
    prompt = f"""
    You are a DevOps expert. Analyze the following logs or incident and suggest root cause and fix:
    {req.text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {"result": response.choices[0].message.content}
