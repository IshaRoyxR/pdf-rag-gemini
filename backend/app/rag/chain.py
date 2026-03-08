from .retriever import retrieve_docs
from .providers.factory import get_provider


def build_prompt(context: str, question: str, mode: str):

    if mode == "summary":
        return f"Summarize this briefly:\n{context}"

    elif mode == "qa":
        return f"""Answer using ONLY the context below.

Context:
{context}

Question: {question}
"""

    elif mode == "completion":
        return f"Continue this text:\n{question}"

    else:
        return f"""Use the following context to respond.

Context:
{context}

User: {question}
"""


def generate_answer(question: str, mode: str, provider_name: str):

    docs = retrieve_docs(question)

    if not docs:
        return {
            "answer": "Your question is outside the context of the uploaded document.",
            "sources": []
        }

    similarities = []

    for d in docs:
        distance = d.metadata.get("score", 1)
        similarity = 1 - distance
        similarities.append(similarity)

    best_similarity = max(similarities)

    # 🔥 Improved out-of-context detection
    if best_similarity < 0.65:
        return {
            "answer": "Your question is outside the context of the uploaded document.",
            "sources": []
        }

    context = "\n\n".join([d.page_content for d in docs])

    prompt = build_prompt(context, question, mode)

    provider = get_provider(provider_name)

    answer = provider.generate(prompt)

    sources = []

    for d in docs:

        distance = d.metadata.get("score", 1)
        similarity = (1 - distance) * 100

        sources.append({
            "file": d.metadata.get("source"),
            "page": d.metadata.get("page"),
            "score": round(similarity, 2),
            "excerpt": d.page_content[:120]
        })

    return {
        "answer": answer,
        "sources": sources
    }