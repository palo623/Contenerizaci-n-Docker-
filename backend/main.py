import os
import requests
from fastapi import FastAPI

app = FastAPI()

BACKEND_MODE = os.getenv("BACKEND_MODE", "local")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
REMOTE_API_URL = os.getenv("REMOTE_API_URL")


@app.get("/")
def root():
    return {"backend": BACKEND_MODE}


@app.post("/chat")
def chat(prompt: str):

    if BACKEND_MODE == "local":

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "gemma4:e4b",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()

    response = requests.post(
        f"{REMOTE_API_URL}/chat",
        json={"prompt": prompt}
    )

    return response.json()
