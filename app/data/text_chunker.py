from typing import List, Dict, Any


def chunk_text(
    text: str,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> List[str]:
    """
    Split long paper text into overlapping chunks.
    """
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


def build_paper_chunks(
    paper: Dict[str, Any],
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> List[Dict[str, Any]]:
    """
    Convert one paper into chunk records for vector indexing.
    """
    full_text = paper.get("full_text", "")

    chunks = chunk_text(
        text=full_text,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunk_records = []

    for idx, chunk in enumerate(chunks):
        chunk_records.append(
            {
                "chunk_id": f"{paper['entry_id']}::chunk_{idx}",
                "paper_id": paper["entry_id"],
                "title": paper["title"],
                "published": paper["published"],
                "relevance_score": paper["relevance_score"],
                "summary_method": paper.get("summary_method", "unknown"),
                "chunk_index": idx,
                "text": chunk,
            }
        )

    return chunk_records