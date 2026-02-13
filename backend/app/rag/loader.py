import os
from langchain_community.document_loaders import PyPDFLoader


def load_document(file_path: str):
    if not file_path.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are supported")

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    for doc in documents:
        doc.metadata["source"] = os.path.basename(file_path)

    return documents
