from fastapi import APIRouter, UploadFile, File
from app.core.file_router import extract_text_by_type
from app.core.text_splitter import split_text
from app.rag.vector_store import store_chunks
from app.core.document_status import add_document

router = APIRouter()

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = f"data/uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_by_type(file_path)

    chunks = split_text(text)

    store_chunks(chunks, source=file.filename)

    add_document(file.filename)

    return {
        "id": file.filename,
        "status": "processed"
    }
