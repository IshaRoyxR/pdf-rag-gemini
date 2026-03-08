from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.chain import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    mode: str
    provider: str


@router.post("/chat")
async def chat(req: ChatRequest):
    return generate_answer(
        question=req.question,
        mode=req.mode,
        provider_name=req.provider
    )