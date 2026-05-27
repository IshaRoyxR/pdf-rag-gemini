from fastapi import APIRouter, UploadFile, File
import os

from app.rag.loader import load_document
from app.rag.splitter import split_text
from app.rag.vector_store import store_chunks

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # load document
    text = load_document(file_path)

    # split into chunks
    chunks = split_text(text)

    # store in vector DB
    store_chunks(chunks, file.filename)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks": len(chunks)
    }