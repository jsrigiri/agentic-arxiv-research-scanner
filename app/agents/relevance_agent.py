from typing import Dict, Any, List


def score_paper_relevance(
    paper: Dict[str, Any],
    keywords: List[str],
) -> Dict[str, Any]:
    """
    Score paper relevance from 0 to 10 based on keyword matches
    in title, abstract, and categories.
    """
    text = " ".join(
        [
            paper.get("title", ""),
            paper.get("summary", ""),
            " ".join(paper.get("categories", [])),
        ]
    ).lower()

    matched_keywords = []

    for keyword in keywords:
        if keyword.lower() in text:
            matched_keywords.append(keyword)

    raw_score = len(matched_keywords)
    relevance_score = min(10, raw_score * 2)

    paper["matched_keywords"] = matched_keywords
    paper["relevance_score"] = relevance_score

    return paper


def score_papers(
    papers: List[Dict[str, Any]],
    keywords: List[str],
) -> List[Dict[str, Any]]:
    scored = [
        score_paper_relevance(paper, keywords)
        for paper in papers
    ]

    return sorted(
        scored,
        key=lambda x: x["relevance_score"],
        reverse=True,
    )