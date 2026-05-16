from app.data.text_chunker import (
    chunk_text,
    build_paper_chunks,
)


def test_chunk_text_returns_chunks():
    text = "A" * 5000

    chunks = chunk_text(
        text=text,
        chunk_size=1000,
        chunk_overlap=100,
    )

    assert len(chunks) > 1
    assert all(len(chunk) > 0 for chunk in chunks)


def test_build_paper_chunks():
    paper = {
        "entry_id": "paper123",
        "title": "Test Paper",
        "published": "2026-05-15",
        "relevance_score": 8,
        "summary_method": "mock",
        "full_text": "B" * 3000,
    }

    chunk_records = build_paper_chunks(
        paper=paper,
        chunk_size=1000,
        chunk_overlap=100,
    )

    assert len(chunk_records) > 1

    first_chunk = chunk_records[0]

    assert first_chunk["paper_id"] == "paper123"
    assert first_chunk["title"] == "Test Paper"
    assert "text" in first_chunk