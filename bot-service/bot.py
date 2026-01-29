import requests
import os

AI_URL = os.getenv("AI_SERVICE_URL", "http://ai-service:8000/analyze")

def chat():
    print("GenAI DevOps Bot started. Type your issue:")
    while True:
        msg = input("> ")
        res = requests.post(AI_URL, json={"text": msg})
        print("\nAI:", res.json()["result"], "\n")

if __name__ == "__main__":
    chat()
