import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# Folder where the vector DB will be stored
PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "chroma_db")

# Ollama host:
# - Docker container should reach Ollama on the Windows host via host.docker.internal
# - If you run backend directly on your machine, 127.0.0.1 also works
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")

# Ollama embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url=OLLAMA_BASE_URL
)

# Create / load Chroma vector database
vector_store = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embedding
)


def store_chunks(chunks, filename):
    """
    Store document chunks into the vector database.
    """
    docs = []

    for chunk in chunks:
        text = chunk["text"]
        page = chunk.get("page", 0)

        doc = Document(
            page_content=text,
            metadata={
                "source": filename,
                "page": page
            }
        )
        docs.append(doc)

    if docs:
        vector_store.add_documents(docs)


def get_retriever():
    """
    Returns retriever for the RAG pipeline.
    """
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )


def delete_from_vector_store(filename: str):
    """
    Delete all embeddings related to a file.
    """
    try:
        vector_store._collection.delete(where={"source": filename})
        print(f"Deleted embeddings for {filename}")
    except Exception as e:
        print("Error deleting from vector DB:", e)