from .vector_store import vector_store


def retrieve_docs(query: str, k: int = 8, filename: str = None):
    """
    Retrieve relevant repository documents from ChromaDB.

    Supports:
    - filename filtering
    - similarity scores
    - sorting
    """

    try:

        if filename:
            results = vector_store.similarity_search_with_score(
                query=query,
                k=k,
                filter={"source": filename},
            )
        else:
            results = vector_store.similarity_search_with_score(
                query=query,
                k=k,
            )

        docs = []

        for doc, distance in results:

            similarity = 1 / (1 + distance)

            doc.metadata["score"] = similarity

            docs.append(doc)

        # Highest similarity first
        docs.sort(
            key=lambda d: d.metadata.get("score", 0),
            reverse=True,
        )

        return docs

    except Exception as e:

        print("Retriever Error:", str(e))

        return []