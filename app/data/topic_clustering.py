from typing import List

import hdbscan
import numpy as np
import pandas as pd
import umap
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def build_documents(
    df: pd.DataFrame
) -> List[str]:

    documents = []

    for _, row in df.iterrows():

        text = " ".join(
            [
                str(row.get("title", "")),
                str(row.get("matched_keywords", "")),
                str(row.get("llm_summary", "")),
            ]
        )

        documents.append(text)

    return documents


def generate_embeddings(
    documents: List[str]
):

    embeddings = embedding_model.encode(
        documents,
        show_progress_bar=False,
    )

    return np.array(embeddings)


def reduce_dimensions(
    embeddings: np.ndarray
):

    reducer = umap.UMAP(
        n_neighbors=5,
        min_dist=0.1,
        metric="cosine",
        random_state=42,
    )

    reduced = reducer.fit_transform(
        embeddings
    )

    return reduced


def cluster_embeddings(
    reduced_embeddings: np.ndarray
):

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=2,
        metric="euclidean",
    )

    labels = clusterer.fit_predict(
        reduced_embeddings
    )

    return labels


def run_topic_clustering(
    df: pd.DataFrame
):

    documents = build_documents(df)

    if len(documents) < 2:
        return None

    embeddings = generate_embeddings(
        documents
    )

    reduced_embeddings = reduce_dimensions(
        embeddings
    )

    labels = cluster_embeddings(
        reduced_embeddings
    )

    clustered_df = df.copy()

    clustered_df["cluster"] = labels

    clustered_df["umap_x"] = reduced_embeddings[:, 0]
    clustered_df["umap_y"] = reduced_embeddings[:, 1]

    return clustered_df