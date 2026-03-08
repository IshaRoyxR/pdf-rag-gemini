from .vector_store import vector_store


def retrieve_docs(query: str, k: int = 5):
    """
    Retrieve top-k relevant documents from the vector store
    """

    results = vector_store.similarity_search_with_score(query, k=k)

    docs = []

    for doc, distance in results:
        similarity = 1 / (1 + distance)  # convert distance → similarity

        doc.metadata["score"] = similarity
        docs.append(doc)

    return docs