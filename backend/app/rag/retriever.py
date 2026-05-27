from .vector_store import vector_store


def retrieve_docs(query: str, k: int = 5, filename: str = None):
    """
    Retrieve top-k relevant documents from the vector store
    Supports optional filename filtering
    """

    # ✅ WITH FILE FILTER
    if filename:
        results = vector_store.similarity_search_with_score(
            query,
            k=k,
            filter={"source": filename}   # 🔥 IMPORTANT
        )
    else:
        results = vector_store.similarity_search_with_score(query, k=k)

    docs = []

    for doc, distance in results:
        # ✅ Convert distance → similarity score (0 to 1)
        similarity = 1 / (1 + distance)

        # Save score inside metadata
        doc.metadata["score"] = similarity

        docs.append(doc)

    return docs