from typing import List
import os
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


CHROMA_DIR = "data/chroma_db"
COLLECTION_NAME = "documents"

os.makedirs(CHROMA_DIR, exist_ok=True)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://host.docker.internal:11434"
)

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)


def store_chunks(chunks: List[str], source: str):
    docs = [
        Document(page_content=chunk, metadata={"source": source})
        for chunk in chunks
    ]

    vector_store.add_documents(docs)


def get_retriever(k: int = 10):
    return vector_store.as_retriever(search_kwargs={"k": k})
