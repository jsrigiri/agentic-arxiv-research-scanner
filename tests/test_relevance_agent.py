from app.agents.relevance_agent import score_paper_relevance, score_papers


def test_score_paper_relevance_matches_keywords():
    paper = {
        "title": "Agentic AI for Trading",
        "summary": "This paper uses large language models for quant finance.",
        "categories": ["cs.AI", "q-fin.TR"],
    }

    keywords = ["agentic ai", "large language models", "quant finance"]

    result = score_paper_relevance(paper, keywords)

    assert result["relevance_score"] == 6
    assert "agentic ai" in result["matched_keywords"]
    assert "large language models" in result["matched_keywords"]
    assert "quant finance" in result["matched_keywords"]


def test_score_papers_sorts_by_relevance():
    papers = [
        {
            "title": "Random Paper",
            "summary": "No strong match.",
            "categories": ["cs.CL"],
        },
        {
            "title": "RAG for LLM Systems",
            "summary": "Retrieval augmented generation with large language models.",
            "categories": ["cs.AI"],
        },
    ]

    keywords = ["rag", "retrieval augmented generation", "large language models"]

    results = score_papers(papers, keywords)

    assert results[0]["title"] == "RAG for LLM Systems"
    assert results[0]["relevance_score"] > results[1]["relevance_score"]