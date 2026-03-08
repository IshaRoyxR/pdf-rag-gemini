from fastapi import APIRouter
from app.core.conversation_manager import (
    create_conversation,
    list_conversations,
    get_history,
    delete_conversation
)

router = APIRouter(prefix="/conversations", tags=["Conversations"])


# =========================
# Create new conversation
# =========================
@router.post("/")
def new_conversation():
    conv_id = create_conversation()
    return {"conversation_id": conv_id}


# =========================
# List all conversations
# =========================
@router.get("/")
def all_conversations():
    return list_conversations()


# =========================
# Get conversation history
# =========================
@router.get("/{conversation_id}")
def conversation_history(conversation_id: str):
    history = get_history(conversation_id)
    return {"messages": history}


# =========================
# Delete conversation
# =========================
@router.delete("/{conversation_id}")
def remove_conversation(conversation_id: str):
    delete_conversation(conversation_id)
    return {"deleted": conversation_id}