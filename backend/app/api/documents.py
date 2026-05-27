from fastapi import APIRouter
from app.core.document_status import get_all_documents, delete_document as delete_from_db
from app.rag.vector_store import delete_from_vector_store  # ✅ IMPORTANT
import os

router = APIRouter()

UPLOAD_DIR = "uploads"


# ✅ GET DOCUMENTS
@router.get("/documents")
def list_documents():
    try:
        docs = get_all_documents()

        if docs:
            formatted = []
            for doc in docs:
                if isinstance(doc, dict):
                    formatted.append(doc.get("filename", doc.get("name")))
                else:
                    formatted.append(str(doc))

            return {"documents": formatted[::-1]}  # latest first

    except Exception:
        pass

    # 🔥 fallback: read from uploads folder
    if os.path.exists(UPLOAD_DIR):
        files = os.listdir(UPLOAD_DIR)
        return {"documents": files[::-1]}

    return {"documents": []}


# ✅ DELETE DOCUMENT (FULL FIX)
@router.delete("/documents/{filename}")
def delete_doc(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    # 🔥 1. delete file from uploads folder
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        return {"status": "error", "message": "File not found"}

    # 🔥 2. delete from tracking DB
    try:
        delete_from_db(filename)
    except Exception:
        pass

    # 🔥 3. DELETE FROM VECTOR DATABASE (MOST IMPORTANT)
    try:
        delete_from_vector_store(filename)
    except Exception as e:
        print("Vector delete error:", e)

    return {
        "status": "success",
        "filename": filename
    }