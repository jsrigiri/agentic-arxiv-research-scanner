from collections import Counter
from typing import List

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def build_corpus(df: pd.DataFrame) -> List[str]:

    corpus = []

    for _, row in df.iterrows():

        text = " ".join(
            [
                str(row.get("title", "")),
                str(row.get("matched_keywords", "")),
                str(row.get("llm_summary", "")),
            ]
        )

        corpus.append(text)

    return corpus


def extract_trending_terms(
    df: pd.DataFrame,
    top_n: int = 20,
):
    if df.empty:
        return []

    corpus = build_corpus(df)

    corpus = [
        text.strip()
        for text in corpus
        if text and text.strip()
    ]

    if not corpus:
        return []

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=1000,
        ngram_range=(1, 2),
    )

    try:
        tfidf_matrix = vectorizer.fit_transform(corpus)
    except ValueError:
        return []

    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.sum(axis=0).A1

    term_scores = list(zip(feature_names, scores))

    term_scores.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return term_scores[:top_n]


def keyword_frequency_analysis(
    df: pd.DataFrame,
    top_n: int = 20,
):
    if df.empty or "matched_keywords" not in df.columns:
        return []

    keywords = []

    for kw_string in df["matched_keywords"].dropna():
        split_keywords = [
            kw.strip()
            for kw in str(kw_string).split(",")
            if kw.strip()
        ]

        keywords.extend(split_keywords)

    counter = Counter(keywords)

    return counter.most_common(top_n)