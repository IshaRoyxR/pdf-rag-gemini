from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
import os


def extract_text_pypdf2(pdf_path: str) -> str:
    """Extract text from normal (non-scanned) PDFs"""
    text = ""
    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_text_ocr(pdf_path: str) -> str:
    """Extract text from scanned PDFs using OCR"""
    images = convert_from_path(pdf_path)
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text.strip()


def load_pdf_text(pdf_path: str) -> str:
    """
    Smart PDF loader:
    1. Try PyPDF2
    2. If empty → OCR
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text = extract_text_pypdf2(pdf_path)

    if len(text) < 50:
        print("⚠️ Low text detected, falling back to OCR...")
        text = extract_text_ocr(pdf_path)

    if not text:
        raise ValueError("Could not extract any text from PDF")

    return text
