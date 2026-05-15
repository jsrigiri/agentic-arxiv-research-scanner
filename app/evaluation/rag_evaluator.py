from typing import Dict, Any, List


def evaluate_retrieval_results(
    results: Dict[str, Any],
) -> Dict[str, Any]:
    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    retrieved_count = len(ids)

    avg_distance = (
        sum(distances) / len(distances)
        if distances
        else None
    )

    unique_papers = set()

    for metadata in metadatas:
        paper_id = metadata.get("paper_id") or metadata.get("title")
        unique_papers.add(paper_id)

    return {
        "retrieved_count": retrieved_count,
        "unique_papers": len(unique_papers),
        "avg_distance": avg_distance,
        "has_results": retrieved_count > 0,
    }


def evaluate_answer_grounding(
    answer: str,
    results: Dict[str, Any],
) -> Dict[str, Any]:
    documents = results.get("documents", [[]])[0]

    if not answer:
        return {
            "answer_length": 0,
            "grounding_overlap_score": 0.0,
        }

    answer_terms = set(answer.lower().split())

    context_text = " ".join(documents).lower()
    context_terms = set(context_text.split())

    overlap = answer_terms.intersection(context_terms)

    grounding_overlap_score = (
        len(overlap) / max(len(answer_terms), 1)
    )

    return {
        "answer_length": len(answer),
        "grounding_overlap_score": round(
            grounding_overlap_score,
            4,
        ),
    }


def evaluate_rag_response(
    question: str,
    answer: str,
    results: Dict[str, Any],
) -> Dict[str, Any]:
    retrieval_metrics = evaluate_retrieval_results(
        results
    )

    grounding_metrics = evaluate_answer_grounding(
        answer,
        results,
    )

    return {
        "question": question,
        **retrieval_metrics,
        **grounding_metrics,
    }