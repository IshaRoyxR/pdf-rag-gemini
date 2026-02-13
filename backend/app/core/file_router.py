import os
from app.core.pdf_loader import load_pdf_text
from app.core.ppt_loader import load_ppt_text
from app.core.docx_loader import load_docx_text


def extract_text_by_type(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf_text(file_path)

    if ext in [".pptx", ".ppt"]:
        return load_ppt_text(file_path)

    if ext in [".docx", ".doc"]:
        return load_docx_text(file_path)

    raise ValueError("Unsupported file type")
