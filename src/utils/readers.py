from typing import Optional
from PyPDF2 import PdfReader
from docx import Document


def read_text_bytes(filename: str, file_bytes: bytes, mime: Optional[str]) -> str:
    name = filename.lower()

    if name.endswith(".txt"):
        return file_bytes.decode("utf-8", errors="ignore")
    
    if name.endswith(".pdf"):
        reader = PdfReader(io_bytes(file_bytes))  
        return "\n".join(page.extract_text() or "" for page in reader.pages)  
    
    if name.endswith(".docx"):
        doc = Document(io_bytes(file_bytes))
        return "\n".join(p.text for p in doc.paragraphs)  
    
    return file_bytes.decode("utf-8", errors="ignore")  # fallback: treat as text


def io_bytes(b: bytes):
    import io
    return io.BytesIO(b)


def trim_if_needed(text: str, max_chars: int = 16000) -> str:
    return text if len(text) <= max_chars else text[:max_chars] + "\n... [truncated]..."
