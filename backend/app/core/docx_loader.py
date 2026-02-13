from docx import Document


def load_docx_text(file_path: str) -> str:
    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text.strip()
