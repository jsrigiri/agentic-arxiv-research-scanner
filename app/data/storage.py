import sqlite3
from typing import List, Dict, Any

from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "papers.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            published TEXT,
            updated TEXT,
            summary TEXT,
            llm_summary TEXT,
            summary_method TEXT,
            critic_review TEXT,
            implementation_review TEXT,
            quant_relevance_review TEXT,
            limitations_review TEXT,
            review_method TEXT,
            entry_id TEXT UNIQUE,
            pdf_url TEXT,
            authors TEXT,
            categories TEXT,
            relevance_score INTEGER,
            matched_keywords TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_papers(papers: List[Dict[str, Any]]) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    for paper in papers:
        try:
            cursor.execute(
                """
                INSERT OR REPLACE INTO papers (
                    title,
                    published,
                    updated,
                    summary,
                    llm_summary,
                    summary_method,
                    critic_review,
                    implementation_review,
                    quant_relevance_review,
                    limitations_review,
                    review_method,
                    entry_id,
                    pdf_url,
                    authors,
                    categories,
                    relevance_score,
                    matched_keywords
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    paper["title"],
                    paper["published"],
                    paper["updated"],
                    paper["summary"],
                    paper.get("llm_summary", ""),
                    paper.get("summary_method", "unknown"),
                    paper.get("critic_review", ""),
                    paper.get("implementation_review", ""),
                    paper.get("quant_relevance_review", ""),
                    paper.get("limitations_review", ""),
                    paper.get("review_method", "unknown"),
                    paper["entry_id"],
                    paper["pdf_url"],
                    ", ".join(paper["authors"]),
                    ", ".join(paper["categories"]),
                    paper["relevance_score"],
                    ", ".join(paper["matched_keywords"]),
                ),
            )

        except Exception as e:
            print(f"Error saving paper: {e}")

    conn.commit()
    conn.close()


def fetch_top_papers(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            title,
            published,
            relevance_score,
            matched_keywords,
            entry_id,
            llm_summary,
            summary_method,
            critic_review,
            implementation_review,
            quant_relevance_review,
            limitations_review,
            review_method
        FROM papers
        ORDER BY relevance_score DESC, published DESC
        LIMIT ?
        """,
        (limit,),
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def initialize_trend_tables() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS trend_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_date TEXT,
            term TEXT,
            score REAL,
            source TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_trend_snapshot(
    snapshot_date: str,
    trend_terms,
    source: str = "tfidf",
) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    for term, score in trend_terms:
        cursor.execute(
            """
            INSERT INTO trend_snapshots (
                snapshot_date,
                term,
                score,
                source
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                snapshot_date,
                term,
                float(score),
                source,
            ),
        )

    conn.commit()
    conn.close()



def fetch_trend_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            snapshot_date,
            term,
            score,
            source
        FROM trend_snapshots
        ORDER BY snapshot_date ASC, score DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def fetch_recent_stored_papers(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            title,
            published,
            updated,
            summary,
            llm_summary,
            summary_method,
            entry_id,
            pdf_url,
            authors,
            categories,
            relevance_score,
            matched_keywords
        FROM papers
        ORDER BY published DESC
        LIMIT ?
        """,
        (limit,),
    )

    rows = cursor.fetchall()
    conn.close()

    papers = []

    for row in rows:
        (
            title,
            published,
            updated,
            summary,
            llm_summary,
            summary_method,
            entry_id,
            pdf_url,
            authors,
            categories,
            relevance_score,
            matched_keywords,
        ) = row

        papers.append(
            {
                "title": title,
                "published": published,
                "updated": updated,
                "summary": summary,
                "llm_summary": llm_summary,
                "summary_method": summary_method,
                "entry_id": entry_id,
                "pdf_url": pdf_url,
                "authors": authors.split(", ") if authors else [],
                "categories": categories.split(", ") if categories else [],
                "relevance_score": relevance_score,
                "matched_keywords": matched_keywords.split(", ") if matched_keywords else [],
            }
        )

    return papers