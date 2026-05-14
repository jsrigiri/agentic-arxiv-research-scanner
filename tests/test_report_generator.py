from pathlib import Path

from app.workflows.report_generator import generate_markdown_report


def test_generate_markdown_report_creates_file():
    papers = [
        (
            "Test Paper",
            "2026-05-13",
            8,
            "llm, trading",
            "https://arxiv.org/abs/test",
            "This is a test summary.",
            "mock",
        )
    ]

    report_path = generate_markdown_report(papers)

    assert Path(report_path).exists()

    content = Path(report_path).read_text(encoding="utf-8")

    assert "# Daily arXiv Research Brief" in content
    assert "Test Paper" in content
    assert "This is a test summary." in content