from pathlib import Path
from typing import Dict, Any

import fitz
import requests


PDF_DIR = Path("data/pdfs")
PARSED_DIR = Path("data/parsed")

PDF_DIR.mkdir(parents=True, exist_ok=True)
PARSED_DIR.mkdir(parents=True, exist_ok=True)


def safe_filename(text: str) -> str:
    return (
        text.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
        .replace(":", "_")
        .replace(".", "_")
    )


def download_pdf(paper: Dict[str, Any]) -> Path:
    pdf_url = paper["pdf_url"]
    filename = safe_filename(paper["entry_id"]) + ".pdf"
    pdf_path = PDF_DIR / filename

    if pdf_path.exists():
        return pdf_path

    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()

    with open(pdf_path, "wb") as f:
        f.write(response.content)

    return pdf_path


def extract_pdf_text(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")

        pages.append(
            f"\n\n--- Page {page_num} ---\n\n{text}"
        )

    doc.close()

    return "\n".join(pages)


def ingest_pdf_for_paper(paper: Dict[str, Any]) -> Dict[str, Any]:
    try:
        pdf_path = download_pdf(paper)
        full_text = extract_pdf_text(pdf_path)

        parsed_path = PARSED_DIR / f"{pdf_path.stem}.txt"

        with open(parsed_path, "w", encoding="utf-8") as f:
            f.write(full_text)

        paper["pdf_path"] = str(pdf_path)
        paper["parsed_text_path"] = str(parsed_path)
        paper["full_text"] = full_text
        paper["pdf_ingested"] = True

    except Exception as e:
        paper["pdf_path"] = ""
        paper["parsed_text_path"] = ""
        paper["full_text"] = ""
        paper["pdf_ingested"] = False
        paper["pdf_error"] = str(e)

    return paper