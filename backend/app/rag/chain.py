from app.rag.retriever import retrieve_docs
from app.rag.providers.factory import get_provider
from app.prompts.system_prompt import SYSTEM_PROMPT


def generate_answer(
    question: str,
    mode: str = "qa",
    provider_name: str = "gemini",
    filename: str = None
):

    try:
        # Retrieve documents (WITH FILE FILTER)
        if filename:
            docs = retrieve_docs(question, filename=filename)
        else:
            docs = retrieve_docs(question)

        # No documents found
        if not docs:
            return {
                "answer": "No relevant information found in the selected repository.",
                "source": None,
                "score": 0.0
            }

        # Limit retrieved documents
        limited_docs = docs[:2]

        # Top document
        top_doc = limited_docs[0]

        # Build context
        context = "\n\n".join(
            [doc.page_content for doc in limited_docs]
        )

        # Prevent huge prompts
        if len(context) > 5000:
            context = context[:5000]

        # -----------------------------
        # Prompt Building
        # -----------------------------

        if mode == "summary":

            prompt = f"""
{SYSTEM_PROMPT}

Repository Context

{context}

Task

Summarize the entire infrastructure repository.
"""

        elif mode == "completion":

            prompt = f"""
{SYSTEM_PROMPT}

Repository Context

{context}

Task

Complete the following request.

User Request

{question}
"""

        else:

            prompt = f"""
{SYSTEM_PROMPT}

Repository Context

{context}

User Question

{question}
"""

        # Get provider
        provider = get_provider(provider_name)

        print(f"Using provider: {provider_name}")
        print(f"Context Length: {len(context)}")

        # Generate answer
        answer = provider.generate(prompt)

        # Metadata
        source = top_doc.metadata.get("source", "unknown")

        # Similarity score
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

        print("CHAIN ERROR:", str(e))

        return {
            "answer": f"Failed to generate answer: {str(e)}",
            "source": "error",
            "score": 0.0
        }