import pandas as pd

from app.data.trend_analysis import (
    extract_trending_terms,
    keyword_frequency_analysis,
)


def test_extract_trending_terms_returns_terms():
    df = pd.DataFrame(
        {
            "title": [
                "Agentic AI for Research",
                "RAG Systems for Quant Finance",
            ],
            "matched_keywords": [
                "agentic ai, llm",
                "rag, quant finance",
            ],
            "llm_summary": [
                "Agentic AI improves research workflows.",
                "RAG helps retrieve relevant quant finance papers.",
            ],
        }
    )

    terms = extract_trending_terms(df, top_n=5)

    assert isinstance(terms, list)
    assert len(terms) > 0


def test_extract_trending_terms_empty_df():
    df = pd.DataFrame()

    terms = extract_trending_terms(df)

    assert terms == []


def test_keyword_frequency_analysis():
    df = pd.DataFrame(
        {
            "matched_keywords": [
                "agentic ai, llm",
                "rag, llm",
                "quant finance",
            ]
        }
    )

    freq = keyword_frequency_analysis(df, top_n=3)

    assert isinstance(freq, list)
    assert freq[0][0] == "llm"
    assert freq[0][1] == 2