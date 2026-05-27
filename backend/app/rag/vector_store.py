from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# Folder where the vector DB will be stored
PERSIST_DIR = "chroma_db"

# Ollama embedding model
embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://127.0.0.1:11434"
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
                "source": filename,   # 🔥 IMPORTANT (used for delete)
                "page": page
            }
        )

        docs.append(doc)

    # ✅ Add to vector DB
    vector_store.add_documents(docs)


def get_retriever():
    """
    Returns retriever for the RAG pipeline.
    """

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )


# ✅ DELETE FUNCTION (FINAL FIX)
def delete_from_vector_store(filename: str):
    """
    Delete all embeddings related to a file
    """

    try:
        vector_store._collection.delete(
            where={"source": filename}
        )

        print(f"Deleted embeddings for {filename}")

    except Exception as e:
        print("Error deleting from vector DB:", e)