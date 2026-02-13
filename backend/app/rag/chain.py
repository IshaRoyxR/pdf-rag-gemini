from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from app.rag.vector_store import get_retriever


def run_rag(question: str) -> str:
    retriever = get_retriever(k=8)

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    if not docs or len(docs) == 0:
        return "No relevant information found in uploaded documents."

    context = "\n\n".join(d.page_content for d in docs)

    prompt = ChatPromptTemplate.from_template("""
You are an intelligent assistant answering questions ONLY from uploaded documents.

RULES:
- Answer ONLY using the context provided.
- Ignore any document that is not relevant to the question.
- If the context does NOT contain the answer, say exactly: "I don't know".
- If the question has multiple parts, answer each part clearly.

Relevant Context:
{context}

User Question:
{question}

Final Answer:
""")

    llm = OllamaLLM(
        model="llama3",
        base_url="http://host.docker.internal:11434"
    )

    chain = prompt | llm

    return chain.invoke({
        "context": context,
        "question": question
    })
