import os
import json
import uuid
from datetime import datetime

CONV_DIR = "data/conversations"
os.makedirs(CONV_DIR, exist_ok=True)


def _get_path(conversation_id: str):
    return os.path.join(CONV_DIR, f"{conversation_id}.json")


# ==============================
# Create
# ==============================
def create_conversation():
    conversation_id = str(uuid.uuid4())

    data = {
        "id": conversation_id,
        "created_at": datetime.utcnow().isoformat(),
        "messages": []
    }

    with open(_get_path(conversation_id), "w") as f:
        json.dump(data, f, indent=2)

    return data


# ==============================
# Get history
# ==============================
def get_history(conversation_id: str):
    path = _get_path(conversation_id)
    if not os.path.exists(path):
        return []

    with open(path) as f:
        return json.load(f)["messages"]


# ==============================
# Append message
# ==============================
def append_message(conversation_id: str, role: str, content: str):
    path = _get_path(conversation_id)

    if not os.path.exists(path):
        raise ValueError("Conversation not found")

    with open(path) as f:
        data = json.load(f)

    data["messages"].append({
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# ==============================
# List conversations
# ==============================
def list_conversations():
    convs = []
    for file in os.listdir(CONV_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONV_DIR, file)) as f:
                convs.append(json.load(f))
    return convs


# ==============================
# Delete
# ==============================
def delete_conversation(conversation_id: str):
    path = _get_path(conversation_id)
    if os.path.exists(path):
        os.remove(path)