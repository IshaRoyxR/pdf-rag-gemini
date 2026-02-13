from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.chain import run_rag

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/query")
def chat_query(req: ChatRequest):
    answer = run_rag(req.question)
    return {"answer": answer}
