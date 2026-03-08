from typing import List, Dict, Any
import os
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

CHROMA_DIR = "data/chroma_db"
COLLECTION_NAME = "documents"

os.makedirs(CHROMA_DIR, exist_ok=True)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
)

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)

def store_chunks(chunks: List[Dict[str, Any]], source: str):
    docs = []
    for chunk in chunks:
        docs.append(
            Document(
                page_content=chunk["text"],
                metadata={
                    "source": source,
                    "page": chunk.get("page", 0),
                },
            )
        )
    vector_store.add_documents(docs)

def get_retriever(k: int = 5):
    return vector_store.as_retriever(search_kwargs={"k": k})

def similarity_search(query: str, k: int = 5):
    return vector_store.similarity_search_with_score(query, k=k)