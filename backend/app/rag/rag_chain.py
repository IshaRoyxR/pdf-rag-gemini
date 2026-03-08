from langchain_ollama import ChatOllama
from app.rag.vector_store import get_retriever

# LLM
llm = ChatOllama(
    model="llama3",
    base_url="http://host.docker.internal:11434",
    temperature=0
)


def ask_rag(question: str) -> str:
    retriever = get_retriever()
    docs = retriever.invoke(question)

    if not docs:
        return "No relevant context found in documents."

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful assistant.
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content