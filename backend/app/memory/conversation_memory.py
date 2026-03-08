import json
import os
import uuid
from datetime import datetime

CONV_DIR = "data/conversations"
os.makedirs(CONV_DIR, exist_ok=True)


def _conv_path(conv_id: str):
    return os.path.join(CONV_DIR, f"{conv_id}.json")


# =========================
# Create Conversation
# =========================
def create_conversation(title: str = "New Chat") -> dict:
    conv_id = str(uuid.uuid4())

    data = {
        "id": conv_id,
        "title": title,
        "created_at": datetime.utcnow().isoformat(),
        "messages": []
    }

    with open(_conv_path(conv_id), "w") as f:
        json.dump(data, f, indent=2)

    return data


# =========================
# Load Conversation
# =========================
def load_conversation(conv_id: str) -> dict:
    path = _conv_path(conv_id)

    if not os.path.exists(path):
        raise ValueError("Conversation not found")

    with open(path, "r") as f:
        return json.load(f)


# =========================
# Save Message
# =========================
def add_message(conv_id: str, role: str, content: str):
    conv = load_conversation(conv_id)

    conv["messages"].append({
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(_conv_path(conv_id), "w") as f:
        json.dump(conv, f, indent=2)


# =========================
# List Conversations
# =========================
def list_conversations():
    conversations = []

    for file in os.listdir(CONV_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONV_DIR, file), "r") as f:
                conversations.append(json.load(f))

    # Sort newest first
    conversations.sort(key=lambda x: x["created_at"], reverse=True)
    return conversations


# =========================
# Delete Conversation
# =========================
def delete_conversation(conv_id: str):
    path = _conv_path(conv_id)
    if os.path.exists(path):
        os.remove(path)