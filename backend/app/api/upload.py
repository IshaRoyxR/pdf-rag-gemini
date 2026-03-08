from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.rag.loader import load_document
from app.rag.splitter import split_text
from app.rag.vector_store import store_chunks

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # ❌ Prevent empty upload
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")

    # Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Load document text
    text = load_document(file_path)

    if not text:
        raise HTTPException(status_code=400, detail="Failed to read document")

    # Split into chunks
    chunks = split_text(text)

    # Store in vector DB
    store_chunks(chunks, file.filename)

    return {"status": "uploaded", "file": file.filename}