from typing import Dict, Any

import ollama


def mock_review_paper(paper: Dict[str, Any]) -> Dict[str, str]:
    return {
        "critic_review": "The paper appears relevant, but a full critical review requires deeper method and experiment analysis.",
        "implementation_review": "Potential implementation depends on clarity of method, available data, and reproducibility of experiments.",
        "quant_relevance_review": "Quant relevance depends on whether the method can improve forecasting, signal extraction, risk modeling, or trading workflows.",
        "limitations_review": "Possible limitations include data dependency, lack of out-of-sample validation, scalability issues, or unclear practical deployment path.",
    }


def ollama_review_paper(
    paper: Dict[str, Any],
    model: str = "llama3.2:1b",
) -> Dict[str, str]:

    prompt = f"""
You are a multi-agent AI research review system.

Review this arXiv paper from four perspectives.

Return exactly this format:

Critic Review:
Implementation Review:
Quant Relevance Review:
Limitations Review:

Title:
{paper.get("title", "")}

Abstract:
{paper.get("summary", "")}

LLM Summary:
{paper.get("llm_summary", "")}

Categories:
{paper.get("categories", [])}

Matched Keywords:
{paper.get("matched_keywords", [])}

Relevance Score:
{paper.get("relevance_score", 0)}/10
"""

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        options={
            "num_ctx": 1024,
            "num_predict": 500,
            "temperature": 0.2,
        },
        keep_alive=0,
    )

    text = response["message"]["content"]

    return {
        "critic_review": text,
        "implementation_review": text,
        "quant_relevance_review": text,
        "limitations_review": text,
    }


def review_paper(
    paper: Dict[str, Any],
    use_ollama: bool = True,
    model: str = "llama3.2:1b",
) -> Dict[str, Any]:

    try:
        if use_ollama:
            reviews = ollama_review_paper(
                paper=paper,
                model=model,
            )
            paper["review_method"] = f"ollama:{model}"
        else:
            reviews = mock_review_paper(paper)
            paper["review_method"] = "mock"

    except Exception as e:
        reviews = mock_review_paper(paper)
        paper["review_method"] = f"mock_fallback: {e}"

    paper.update(reviews)

    return paper


def review_papers(
    papers,
    use_ollama: bool = True,
    model: str = "llama3.2:1b",
):
    return [
        review_paper(
            paper=paper,
            use_ollama=use_ollama,
            model=model,
        )
        for paper in papers
    ]