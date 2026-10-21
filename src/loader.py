from pathlib import Path
from pypdf import PdfReader


def load_document(file_path):
    """Read a .txt or .pdf file and return all its text as one string."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".txt":
        return path.read_text(encoding="utf-8")

    elif extension == ".pdf":
        reader = PdfReader(path)
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)

    else:
        raise ValueError("Unsupported file type. Please use .txt or .pdf")