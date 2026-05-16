import pandas as pd

from app.data.topic_clustering import (
    build_documents,
    run_topic_clustering,
)


def test_build_documents():
    df = pd.DataFrame(
        {
            "title": ["Agentic AI Paper"],
            "matched_keywords": ["agentic ai, llm"],
            "llm_summary": ["This paper discusses agentic AI workflows."],
        }
    )

    docs = build_documents(df)

    assert len(docs) == 1
    assert "Agentic AI Paper" in docs[0]


def test_run_topic_clustering_small_df_returns_none():
    df = pd.DataFrame(
        {
            "title": ["Only One Paper"],
            "matched_keywords": ["rag"],
            "llm_summary": ["Only one document."],
        }
    )

    result = run_topic_clustering(df)

    assert result is None