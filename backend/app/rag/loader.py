from app.core.pdf_loader import extract_text_from_pdf
from app.core.docx_loader import extract_text_from_docx
from app.core.ppt_loader import extract_text_from_ppt


def load_document(path: str) -> str:
    path_lower = path.lower()

    if path_lower.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path_lower.endswith(".docx"):
        text = extract_text_from_docx(path)
    elif path_lower.endswith(".pptx"):
        text = extract_text_from_ppt(path)
    else:
        raise ValueError("Unsupported file type")

    # Ensure string
    if isinstance(text, list):
        return "\n".join(text)

    return text