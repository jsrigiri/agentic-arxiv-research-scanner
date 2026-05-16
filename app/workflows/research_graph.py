from typing import TypedDict, List, Dict, Any

from langgraph.graph import StateGraph, END

from app.data.arxiv_client import fetch_recent_papers
from app.agents.relevance_agent import score_papers
from app.agents.summarizer_agent import summarize_papers
from app.data.storage import initialize_database, save_papers, fetch_top_papers
from app.workflows.report_generator import generate_markdown_report
from app.utils import timed_node
from app.data.vector_store import index_papers
from app.data.pdf_ingestor import ingest_pdf_for_paper
from app.notifications.email_digest import send_email_digest
from app.notifications.slack_digest import send_slack_digest

from datetime import datetime
import pandas as pd

from app.data.trend_analysis import extract_trending_terms

from app.data.storage import (
    initialize_trend_tables,
    save_trend_snapshot,
)

from app.agents.reviewer_agent import review_papers
from app.data.storage import fetch_recent_stored_papers


class ResearchState(TypedDict):
    config: Dict[str, Any]
    papers: List[Dict[str, Any]]
    scored_papers: List[Dict[str, Any]]
    summarized_papers: List[Dict[str, Any]]
    reviewed_papers: List[Dict[str, Any]]
    top_papers: List[Any]
    report_path: str


@timed_node("fetch_papers")
def fetch_node(state: ResearchState) -> ResearchState:
    config = state["config"]

    try:
        state["papers"] = fetch_recent_papers(
            categories=config["arxiv"]["categories"],
            max_results=config["arxiv"]["max_results"],
        )

    except Exception as e:
        print(f"[bold red]arXiv fetch failed:[/bold red] {e}")
        print("[yellow]Using recently stored papers as fallback.[/yellow]")

        state["papers"] = fetch_recent_stored_papers(
            limit=config["arxiv"]["max_results"]
        )

    return state


@timed_node("score_papers")
def score_node(state: ResearchState) -> ResearchState:
    config = state["config"]

    state["scored_papers"] = score_papers(
        papers=state["papers"],
        keywords=config["interests"]["keywords"],
    )

    return state


@timed_node("summarize_papers")
def summarize_node(state: ResearchState) -> ResearchState:
    config = state["config"]

    state["summarized_papers"] = summarize_papers(
        papers=state["scored_papers"],
        use_ollama=config["llm"]["use_ollama"],
        model=config["llm"]["model"],
    )

    return state


@timed_node("ingest_pdfs")
def pdf_ingest_node(state: ResearchState) -> ResearchState:

    config = state["config"]

    ingest_full_text = config["pdf"]["ingest_full_text"]
    max_pdfs = config["pdf"]["max_pdfs"]

    if not ingest_full_text:
        return state

    ingested_papers = []

    for idx, paper in enumerate(
        state["reviewed_papers"]
    ):

        # ---------------------------------
        # Limit number of PDFs ingested
        # ---------------------------------

        if idx < max_pdfs:

            ingested_papers.append(
                ingest_pdf_for_paper(paper)
            )

        else:

            paper["pdf_ingested"] = False
            paper["full_text"] = ""

            ingested_papers.append(
                paper
            )

    state["reviewed_papers"] = ingested_papers

    return state


@timed_node("store_and_index_papers")
def store_node(state: ResearchState) -> ResearchState:

    initialize_database()
    initialize_trend_tables()

    save_papers(state["reviewed_papers"])

    index_papers(state["reviewed_papers"])

    # ---------------------------------
    # Save trend snapshots
    # ---------------------------------

    trend_df = pd.DataFrame(
        state["reviewed_papers"]
    )

    trend_terms = extract_trending_terms(
        trend_df,
        top_n=20,
    )

    snapshot_date = datetime.now().strftime(
        "%Y-%m-%d"
    )

    save_trend_snapshot(
        snapshot_date=snapshot_date,
        trend_terms=trend_terms,
        source="tfidf",
    )

    state["top_papers"] = fetch_top_papers(limit=10)

    return state


@timed_node("generate_report")
def report_node(state: ResearchState) -> ResearchState:

    state["report_path"] = generate_markdown_report(
        state["top_papers"]
    )

    # ---------------------------------
    # Send email digest
    # ---------------------------------

    send_email_digest(
        config=state["config"],
        report_path=state["report_path"],
    )

    # ---------------------------------
    # Send Slack digest
    # ---------------------------------

    send_slack_digest(
        config=state["config"],
        report_path=state["report_path"],
    )

    return state


@timed_node("review_papers")
def review_node(state: ResearchState) -> ResearchState:

    config = state["config"]

    state["reviewed_papers"] = review_papers(
        papers=state["summarized_papers"],
        use_ollama=config["llm"]["use_ollama"],
        model=config["llm"]["model"],
    )

    return state


def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("fetch", fetch_node)
    graph.add_node("score", score_node)
    graph.add_node("summarize", summarize_node)
    graph.add_node("review", review_node)
    graph.add_node("pdf_ingest", pdf_ingest_node)
    graph.add_node("store", store_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("fetch")

    graph.add_edge("fetch", "score")
    graph.add_edge("score", "summarize")

    graph.add_edge("summarize", "review")
    graph.add_edge("review", "pdf_ingest")
    graph.add_edge("pdf_ingest", "store")
    graph.add_edge("store", "report")
    graph.add_edge("report", END)

    return graph.compile()