# Chatbot com OpenAI 
from fastapi import APIRouter

router = APIRouter()

@router.post("/chatbot")
def chatbot_response(message: str):
    return {"response": f"Resposta automática para: {message}"}