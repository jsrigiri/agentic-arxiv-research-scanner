from typing import List, Dict, Any

import chromadb
from sentence_transformers import SentenceTransformer

from app.data.text_chunker import build_paper_chunks


COLLECTION_NAME = "arxiv_paper_chunks"

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def build_document_text(
    paper: Dict[str, Any]
) -> str:

    return f"""
Title:
{paper.get('title', '')}

Summary:
{paper.get('summary', '')}

LLM Summary:
{paper.get('llm_summary', '')}

Matched Keywords:
{paper.get('matched_keywords', '')}
"""


def index_papers(
    papers: List[Dict[str, Any]]
) -> None:

    for paper in papers:

        # ---------------------------------
        # Full paper chunk indexing
        # ---------------------------------

        if paper.get("full_text"):

            chunk_records = build_paper_chunks(
                paper
            )

            for chunk_record in chunk_records:

                embedding = embedding_model.encode(
                    chunk_record["text"]
                ).tolist()

                metadata = {
                    "paper_id": chunk_record["paper_id"],
                    "title": chunk_record["title"],
                    "published": chunk_record["published"],
                    "relevance_score": chunk_record["relevance_score"],
                    "summary_method": chunk_record["summary_method"],
                    "chunk_index": chunk_record["chunk_index"],
                }

                collection.upsert(
                    ids=[chunk_record["chunk_id"]],
                    documents=[chunk_record["text"]],
                    embeddings=[embedding],
                    metadatas=[metadata],
                )

        else:

            # ---------------------------------
            # Fallback abstract indexing
            # ---------------------------------

            document = build_document_text(
                paper
            )

            embedding = embedding_model.encode(
                document
            ).tolist()

            doc_id = paper["entry_id"]

            metadata = {
                "paper_id": paper["entry_id"],
                "title": paper["title"],
                "published": paper["published"],
                "relevance_score": paper["relevance_score"],
                "summary_method": paper.get(
                    "summary_method",
                    "unknown",
                ),
                "chunk_index": -1,
            }

            collection.upsert(
                ids=[doc_id],
                documents=[document],
                embeddings=[embedding],
                metadatas=[metadata],
            )


def semantic_search(
    query: str,
    top_k: int = 5,
):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results