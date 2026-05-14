from typing import Dict, Any, List

import ollama


DEFAULT_MODEL = "llama3.2:latest"


def mock_summarize_paper(paper: Dict[str, Any]) -> str:
    summary = paper.get("summary", "").replace("\n", " ").strip()

    if len(summary) > 700:
        summary = summary[:700] + "..."

    return (
        "Key idea: " + summary + "\n\n"
        "Why it matters: This paper may be relevant based on its topic, categories, "
        "and matched research keywords.\n\n"
        "Implementation angle: Review the method and identify whether it can be "
        "converted into a reproducible experiment or portfolio project."
    )


def ollama_summarize_paper(
    paper: Dict[str, Any],
    model: str = DEFAULT_MODEL,
) -> str:
    prompt = f"""
You are an AI research assistant.

Summarize this arXiv paper for a machine learning / quant finance practitioner.

Return exactly this format:

Key idea:
Why it matters:
Methods used:
Implementation angle:
Quant/AI relevance score explanation:

Title:
{paper.get("title", "")}

Abstract:
{paper.get("summary", "")}

Categories:
{paper.get("categories", [])}

Matched keywords:
{paper.get("matched_keywords", [])}

Relevance score:
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
            "num_ctx": 512,
            "num_predict": 150,
            "temperature": 0.1,
        },
        keep_alive=0,
    )

    return response["message"]["content"]


def summarize_paper(
    paper: Dict[str, Any],
    use_ollama: bool = True,
    model: str = DEFAULT_MODEL,
) -> Dict[str, Any]:

    try:
        if use_ollama:
            paper["llm_summary"] = ollama_summarize_paper(
                paper,
                model=model,
            )

            paper["summary_method"] = f"ollama:{model}"

        else:
            paper["llm_summary"] = mock_summarize_paper(paper)
            paper["summary_method"] = "mock"

    except Exception as e:
        paper["llm_summary"] = (
            f"Ollama summarization failed: {e}\n\n"
            f"Fallback summary:\n{mock_summarize_paper(paper)}"
        )

        paper["summary_method"] = "mock_fallback"

    return paper


def summarize_papers(
    papers: List[Dict[str, Any]],
    use_ollama: bool = True,
    model: str = DEFAULT_MODEL,
) -> List[Dict[str, Any]]:
    return [
        summarize_paper(
            paper=paper,
            use_ollama=use_ollama,
            model=model,
        )
        for paper in papers
    ]