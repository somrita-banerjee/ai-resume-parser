import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
from typing import Optional
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(path:str) -> str:
    text_chunks = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text_chunks.append(page.extract_text() or "")

    except Exception:
        reader = PdfReader(path)
        for p in reader.pages:
            text_chunks.append(p.extract_text() or "")

    return "\n".join(text_chunks).strip()

def extract_text_from_docx(path: str) -> str:
    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs]
    return "\n".join(paragraphs).strip()

def extract_text_from_image(path: str) -> str:
    img = Image.open(path)
    return pytesseract.image_to_string(img)

def extract_text(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in [".pdf"]:
        return extract_text_from_pdf(path)
    if ext in [".doc", ".docx"]:
        return extract_text_from_docx(path)
    if ext in [".png", ".jpg", ".jpeg", ".tiff"]:
        return extract_text_from_image(path)
    raise ValueError(f"Unsupported file type: {ext}")