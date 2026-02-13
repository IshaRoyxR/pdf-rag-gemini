from fastapi import APIRouter
from app.core.document_status import get_all_documents, delete_document

router = APIRouter()


@router.get("/documents")
def list_documents():
    return get_all_documents()


@router.delete("/documents/{doc_id}")
def delete_doc(doc_id: str):
    delete_document(doc_id)
    return {"message": "deleted"}
