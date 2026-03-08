from langchain.memory import ConversationBufferWindowMemory

# 🧠 In-memory cache per conversation
_memory_store = {}

def get_langchain_memory(conversation_id: str):
    """
    Returns memory object per conversation.
    Keeps last 5 messages.
    """
    if conversation_id not in _memory_store:
        _memory_store[conversation_id] = ConversationBufferWindowMemory(
            k=5,
            return_messages=True
        )

    return _memory_store[conversation_id]