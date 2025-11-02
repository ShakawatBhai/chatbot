from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import get_ai_response
from app.database.db import save_chat

router = APIRouter(prefix="/chat", tags=["Chatbot"])

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(request: ChatRequest):
    response = get_ai_response(request.message)
    save_chat(request.message, response)
    return {
        "user_message": request.message,
        "bot_response": response
    }
