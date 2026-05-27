from app.rag.retriever import retrieve_docs
from app.rag.providers.factory import get_provider


def generate_answer(
    question: str,
    mode: str = "qa",
    provider_name: str = "gemini",
    filename: str = None
):

    try:
        # ✅ Retrieve documents (WITH FILE FILTER)
        if filename:
            docs = retrieve_docs(question, filename=filename)
        else:
            docs = retrieve_docs(question)

        # ✅ No docs found
        if not docs:
            return {
                "answer": "No relevant information found in the selected document.",
                "source": None,
                "score": 0.0
            }

        # 🔥 LIMIT CONTEXT (CRITICAL FIX FOR OLLAMA)
        limited_docs = docs[:2]   # 👈 prevents overload/crash

        # 🔥 Top document (after limiting)
        top_doc = limited_docs[0]

        # ✅ Build context safely
        context = "\n\n".join([d.page_content for d in limited_docs])

        # ⚠️ EXTRA SAFETY (avoid very large prompts)
        if len(context) > 3000:
            context = context[:3000]

        # ✅ Prompt building
        if mode == "summary":
            prompt = f"""
Summarize the following content:

{context}
"""

        elif mode == "completion":
            prompt = f"""
Complete based on context:

{context}

Question:
{question}
"""

        else:  # qa
            prompt = f"""
Answer the question using ONLY the context below.

If the answer is NOT present, say:
"There is no information in the provided documents."

Context:
{context}

Question:
{question}
"""

        # ✅ Get provider (Gemini / Ollama / OpenAI)
        provider = get_provider(provider_name)

        print(f"🚀 Using provider: {provider_name}")
        print(f"📏 Context length: {len(context)}")

        # 🔥 Generate answer
        answer = provider.generate(prompt)

        # ✅ Metadata
        source = top_doc.metadata.get("source", "unknown")

        # ✅ SMART SCORE
        answer_lower = answer.lower()

        if (
            "no information" in answer_lower
            or "not mentioned" in answer_lower
            or "not available" in answer_lower
        ):
            score = 0.0
        else:
            score = (
                top_doc.metadata.get("score")
                or top_doc.metadata.get("similarity")
                or 0.75
            )

        return {
            "answer": answer,
            "source": source,
            "score": float(score)
        }

    except Exception as e:
        print("🔥 CHAIN ERROR:", str(e))

        return {
            "answer": f"Failed to generate answer: {str(e)}",
            "source": "error",
            "score": 0.0
        }