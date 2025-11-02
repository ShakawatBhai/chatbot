from fastapi import FastAPI
from app.routers import chat

app = FastAPI(
    title="Free AI Chatbot Backend",
    version="1.0",
    description="A chatbot backend using FastAPI and Hugging Face API"
)

# Include chat routes
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Free AI Chatbot Backend!"}
