import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# You can change model to any free one available on Hugging Face
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_ai_response(prompt: str) -> str:
    try:
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            return "I'm sorry, I couldn’t generate a response at the moment."
    except Exception as e:
        return f"Error: {e}"
