from app.evaluation.rag_evaluator import (
    evaluate_retrieval_results,
    evaluate_answer_grounding,
    evaluate_rag_response,
)


def test_evaluate_retrieval_results():
    results = {
        "ids": [["doc1", "doc2"]],
        "documents": [["agentic ai research", "quant finance trading"]],
        "metadatas": [[
            {"paper_id": "paper1"},
            {"paper_id": "paper2"},
        ]],
        "distances": [[0.2, 0.4]],
    }

    metrics = evaluate_retrieval_results(results)

    assert metrics["retrieved_count"] == 2
    assert metrics["unique_papers"] == 2
    assert metrics["avg_distance"] == 0.30000000000000004
    assert metrics["has_results"] is True


def test_evaluate_answer_grounding():
    results = {
        "documents": [["agentic ai improves research workflows"]],
    }

    answer = "agentic ai improves workflows"

    metrics = evaluate_answer_grounding(answer, results)

    assert metrics["answer_length"] > 0
    assert metrics["grounding_overlap_score"] > 0


def test_evaluate_rag_response():
    results = {
        "ids": [["doc1"]],
        "documents": [["retrieval augmented generation"]],
        "metadatas": [[{"paper_id": "paper1"}]],
        "distances": [[0.1]],
    }

    metrics = evaluate_rag_response(
        question="What is RAG?",
        answer="retrieval augmented generation",
        results=results,
    )

    assert metrics["question"] == "What is RAG?"
    assert metrics["retrieved_count"] == 1
    assert metrics["unique_papers"] == 1