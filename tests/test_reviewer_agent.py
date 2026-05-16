from app.agents.reviewer_agent import (
    mock_review_paper,
    review_paper,
)


def test_mock_review_paper_returns_all_reviews():
    paper = {
        "title": "Test Paper",
        "summary": "This is a test paper.",
    }

    reviews = mock_review_paper(paper)

    assert "critic_review" in reviews
    assert "implementation_review" in reviews
    assert "quant_relevance_review" in reviews
    assert "limitations_review" in reviews


def test_review_paper_mock_mode():
    paper = {
        "title": "Test Paper",
        "summary": "This is a test paper.",
    }

    result = review_paper(
        paper=paper,
        use_ollama=False,
        model="llama3.2:1b",
    )

    assert result["review_method"] == "mock"
    assert "critic_review" in result
    assert "implementation_review" in result
    assert "quant_relevance_review" in result
    assert "limitations_review" in result