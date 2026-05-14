import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st
import yaml

from app.data.vector_store import semantic_search
from app.agents.rag_answer_agent import generate_rag_answer


DB_PATH = "papers.db"


@st.cache_data
def load_papers():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        title,
        published,
        relevance_score,
        matched_keywords,
        summary_method,
        entry_id,
        llm_summary
    FROM papers
    ORDER BY relevance_score DESC, published DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


st.set_page_config(
    page_title="Agentic arXiv Research Scanner",
    layout="wide",
)

st.title("Agentic arXiv Research Scanner")

config = load_config()
df = load_papers()

tab1, tab2 = st.tabs(["Paper Dashboard", "RAG Research QA"])

with tab1:
    st.sidebar.header("Filters")

    search_text = st.sidebar.text_input("Search title / keywords / summary")

    min_score = st.sidebar.slider(
        "Minimum Relevance Score",
        min_value=0,
        max_value=10,
        value=0,
    )

    summary_method = st.sidebar.selectbox(
        "Summary Method",
        options=["All"] + sorted(df["summary_method"].dropna().unique().tolist()),
    )

    filtered_df = df[df["relevance_score"] >= min_score]

    if summary_method != "All":
        filtered_df = filtered_df[
            filtered_df["summary_method"] == summary_method
        ]

    if search_text:
        search_lower = search_text.lower()

        filtered_df = filtered_df[
            filtered_df["title"].str.lower().str.contains(search_lower, na=False)
            | filtered_df["matched_keywords"].str.lower().str.contains(search_lower, na=False)
            | filtered_df["llm_summary"].str.lower().str.contains(search_lower, na=False)
        ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Papers", len(df))

    with col2:
        st.metric("Filtered Papers", len(filtered_df))

    with col3:
        avg_score = filtered_df["relevance_score"].mean()
        st.metric(
            "Average Relevance",
            f"{avg_score:.2f}" if not pd.isna(avg_score) else "0.00",
        )

    st.subheader("Workflow Analytics")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        score_counts = (
            filtered_df["relevance_score"]
            .value_counts()
            .sort_index()
            .reset_index()
        )
        score_counts.columns = ["relevance_score", "count"]

        fig_score = px.bar(
            score_counts,
            x="relevance_score",
            y="count",
            title="Paper Count by Relevance Score",
        )

        st.plotly_chart(fig_score, use_container_width=True)

    with chart_col2:
        method_counts = (
            filtered_df["summary_method"]
            .value_counts()
            .reset_index()
        )
        method_counts.columns = ["summary_method", "count"]

        fig_method = px.pie(
            method_counts,
            names="summary_method",
            values="count",
            title="Summary Method Distribution",
        )

        st.plotly_chart(fig_method, use_container_width=True)

    st.subheader("Papers")

    st.write(f"Showing {len(filtered_df)} papers")

    for _, row in filtered_df.iterrows():
        with st.container():
            st.subheader(row["title"])

            paper_col1, paper_col2, paper_col3 = st.columns(3)

            with paper_col1:
                st.metric("Relevance Score", row["relevance_score"])

            with paper_col2:
                st.write("Published")
                st.write(row["published"])

            with paper_col3:
                st.write("Summary Method")
                st.write(row["summary_method"])

            st.write("Matched Keywords")
            st.write(row["matched_keywords"])

            st.markdown(f"[Open arXiv Paper]({row['entry_id']})")

            with st.expander("LLM Summary"):
                st.write(row["llm_summary"])

            st.divider()


with tab2:
    st.subheader("Ask Questions Over Indexed Papers")

    question = st.text_area(
        "Research question",
        placeholder="Example: Which papers are most relevant to quant trading strategies?",
        height=100,
    )

    top_k = st.slider(
        "Number of papers to retrieve",
        min_value=1,
        max_value=10,
        value=5,
    )

    use_ollama = st.checkbox(
        "Use Ollama to generate answer",
        value=config["llm"]["use_ollama"],
    )

    model = st.text_input(
        "Ollama model",
        value=config["llm"]["model"],
    )

    if st.button("Run RAG QA"):
        if not question.strip():
            st.warning("Please enter a research question.")
        else:
            with st.spinner("Retrieving relevant papers..."):
                results = semantic_search(
                    query=question,
                    top_k=top_k,
                )

            with st.spinner("Generating RAG answer..."):
                answer = generate_rag_answer(
                    question=question,
                    results=results,
                    use_ollama=use_ollama,
                    model=model,
                )

            st.subheader("RAG Answer")
            st.write(answer)

            st.subheader("Retrieved Papers")

            ids = results["ids"][0]
            metadatas = results["metadatas"][0]
            distances = results["distances"][0]

            for idx, (doc_id, metadata, distance) in enumerate(
                zip(ids, metadatas, distances),
                start=1,
            ):
                with st.expander(f"{idx}. {metadata['title']}"):
                    st.write(f"Published: {metadata['published']}")
                    st.write(f"Relevance Score: {metadata['relevance_score']}")
                    st.write(f"Summary Method: {metadata['summary_method']}")
                    st.write(f"Distance: {distance:.4f}")
                    st.markdown(f"[Open arXiv Paper]({doc_id})")