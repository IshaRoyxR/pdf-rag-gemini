from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.rag.chain import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    message: Optional[str] = None
    question: Optional[str] = None
    mode: Optional[str] = "qa"
    provider: Optional[str] = "gemini"
    filename: Optional[str] = None   # ✅ IMPORTANT


@router.post("/chat")
async def chat(req: ChatRequest):

    # ✅ Support both message & question
    question = req.message if req.message else req.question

    if not question:
        return {
            "answer": "No question provided.",
            "source": "N/A",
            "score": 0.0
        }

    try:
        result = generate_answer(
            question=question,
            mode=req.mode,
            provider_name=req.provider,
            filename=req.filename   # ✅ PASS FILE
        )

        return {
            "answer": result.get("answer", "No answer"),
            "source": result.get("source", "N/A"),
            "score": round(result.get("score", 0.0) * 100, 2)
        }

    except Exception as e:
        print("🔥 CHAT ERROR:", str(e))   # ✅ SEE REAL ERROR

        return {
            "answer": f"Error: {str(e)}",
            "source": "error",
            "score": 0.0
        }