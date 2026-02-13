from typing import Dict

documents: Dict[str, dict] = {}


def add_document(filename: str):
    documents[filename] = {
        "filename": filename,
        "status": "processed"
    }


def get_all_documents():
    return documents


def delete_document(filename: str):
    if filename in documents:
        del documents[filename]
