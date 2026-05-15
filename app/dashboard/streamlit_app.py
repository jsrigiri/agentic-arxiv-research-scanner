import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st
from ruamel.yaml import YAML

from datetime import timedelta
from app.data.vector_store import semantic_search
from app.agents.rag_answer_agent import generate_rag_answer

from app.data.trend_analysis import (
    extract_trending_terms,
    keyword_frequency_analysis,
)

from app.workflows.research_graph import build_research_graph
from app.notifications.slack_digest import send_slack_digest
from app.data.topic_clustering import run_topic_clustering
from app.evaluation.rag_evaluator import evaluate_rag_response


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


yaml_handler = YAML()
yaml_handler.preserve_quotes = True


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml_handler.load(f)


st.set_page_config(
    page_title="Agentic arXiv Research Scanner",
    layout="wide",
)

st.title("Agentic arXiv Research Scanner")

config = load_config()
df = load_papers()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Paper Dashboard",
        "RAG Research QA",
        "Trend Analytics",
        "Scheduler",
        "Topic Clusters",
    ]
)

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

            evaluation = evaluate_rag_response(
                question=question,
                answer=answer,
                results=results,
            )

            st.subheader("RAG Evaluation Metrics")

            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

            with metric_col1:
                st.metric(
                    "Retrieved Chunks",
                    evaluation["retrieved_count"],
                )

            with metric_col2:
                st.metric(
                    "Unique Papers",
                    evaluation["unique_papers"],
                )

            with metric_col3:
                avg_distance = evaluation["avg_distance"]

                st.metric(
                    "Avg Distance",
                    f"{avg_distance:.4f}"
                    if avg_distance is not None
                    else "N/A",
                )

            with metric_col4:
                st.metric(
                    "Grounding Score",
                    evaluation["grounding_overlap_score"],
                )

            with st.expander("Detailed Evaluation Metrics"):
                st.json(evaluation)

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


with tab3:
    st.subheader("Research Trend Analytics")

    st.write(
        "This section identifies frequent themes and high-signal research terms "
        "across the indexed arXiv papers."
    )

    top_n = st.slider(
        "Number of terms to show",
        min_value=5,
        max_value=30,
        value=15,
    )

    trending_terms = extract_trending_terms(df, top_n=top_n)
    keyword_freq = keyword_frequency_analysis(df, top_n=top_n)

    trend_df = pd.DataFrame(
        trending_terms,
        columns=["term", "score"],
    )

    keyword_df = pd.DataFrame(
        keyword_freq,
        columns=["keyword", "count"],
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top TF-IDF Research Terms")

        fig_terms = px.bar(
            trend_df,
            x="score",
            y="term",
            orientation="h",
            title="Trending Research Terms",
        )

        st.plotly_chart(fig_terms, use_container_width=True)

        st.dataframe(trend_df, use_container_width=True)

    with col2:
        st.subheader("Top Matched Keywords")

        fig_keywords = px.bar(
            keyword_df,
            x="count",
            y="keyword",
            orientation="h",
            title="Matched Keyword Frequency",
        )

        st.plotly_chart(fig_keywords, use_container_width=True)

        st.dataframe(keyword_df, use_container_width=True)


def save_config(config: dict, path: str = "config.yaml") -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml_handler.dump(config, f)


with tab4:
    st.subheader("Autonomous Scheduler Settings")

    scheduler_config = config.get("scheduler", {})

    enabled = st.checkbox(
        "Enable daily scheduled research workflow",
        value=scheduler_config.get("enabled", False),
    )
    
    scheduler_config = config.get("scheduler", {})

    current_run_time = scheduler_config.get(
        "run_time",
        "09:00",
    )

    if not isinstance(current_run_time, str):
        current_run_time = "09:00"

    try:
        current_hour, current_minute = current_run_time.split(":")
    except Exception:
        current_hour, current_minute = "09", "00"


    hour_options = [f"{h:02d}" for h in range(24)]

    minute_options = [
        "00",
        "05",
        "10",
        "15",
        "20",
        "25",
        "30",
        "35",
        "40",
        "45",
        "50",
        "55",
    ]

    col_hour, col_minute = st.columns(2)

    with col_hour:
        selected_hour = st.selectbox(
            "Hour",
            options=hour_options,
            index=hour_options.index(current_hour)
            if current_hour in hour_options
            else 9,
        )

    with col_minute:
        selected_minute = st.selectbox(
            "Minute",
            options=minute_options,
            index=minute_options.index(current_minute)
            if current_minute in minute_options
            else 0,
        )

    run_time = f"{selected_hour}:{selected_minute}"

    st.write("Current scheduler config:")

    st.code(
        f"""
    scheduler:
    enabled: {enabled}
    run_time: "{run_time}"    
    """,
        language="yaml",
    )

    if st.button("Save Scheduler Settings"):
        config["scheduler"] = {
            "enabled": enabled,
            "run_time": run_time,
        }

        save_config(config)

        st.success(
            f"Scheduler settings saved: enabled={enabled}, run_time={run_time}"
        )

    st.divider()

    st.subheader("Run Workflow Manually")

    if st.button("Run Research Workflow Now"):
        initial_state = {
            "config": config,
            "papers": [],
            "scored_papers": [],
            "summarized_papers": [],
            "top_papers": [],
            "report_path": "",
        }

        with st.spinner("Running agentic research workflow..."):
            graph = build_research_graph()
            final_state = graph.invoke(initial_state)

        st.success("Workflow completed successfully.")
        st.write(f"Generated report: {final_state['report_path']}")

    st.divider()

    st.subheader("Slack Notification Settings")

    slack_config = config.get("slack", {})

    slack_enabled = st.checkbox(
        "Enable Slack digest",
        value=slack_config.get("enabled", False),
    )

    slack_webhook_url = st.text_input(
        "Slack webhook URL",
        value=slack_config.get("webhook_url", ""),
        type="password",
    )

    if st.button("Save Slack Settings"):
        config["slack"] = {
            "enabled": slack_enabled,
            "webhook_url": slack_webhook_url,
        }

        save_config(config)

        st.success("Slack settings saved.")

    if st.button("Send Test Slack Message"):
        test_report_path = "reports/test_slack_message.md"

        with open(test_report_path, "w", encoding="utf-8") as f:
            f.write("# Test Slack Message\n\nSlack integration is working.")

        config["slack"] = {
            "enabled": slack_enabled,
            "webhook_url": slack_webhook_url,
        }

        success = send_slack_digest(
            config=config,
            report_path=test_report_path,
        )

        if success:
            st.success("Test Slack message sent.")
        else:
            st.error("Slack test failed. Check webhook URL.")


with tab5:
    st.subheader("Topic Clusters")

    st.write(
        "This section groups papers into research themes using embeddings, UMAP, and HDBSCAN."
    )

    if len(df) < 2:
        st.warning("Need at least 2 papers for clustering.")
    else:
        with st.spinner("Running topic clustering..."):
            clustered_df = run_topic_clustering(df)

        if clustered_df is None:
            st.warning("Not enough papers to cluster.")
        else:
            fig_clusters = px.scatter(
                clustered_df,
                x="umap_x",
                y="umap_y",
                color=clustered_df["cluster"].astype(str),
                hover_data=[
                    "title",
                    "relevance_score",
                    "matched_keywords",
                    "summary_method",
                ],
                title="Research Topic Clusters",
            )

            st.plotly_chart(fig_clusters, use_container_width=True)

            st.subheader("Clustered Papers")

            st.dataframe(
                clustered_df[
                    [
                        "title",
                        "published",
                        "relevance_score",
                        "matched_keywords",
                        "summary_method",
                        "cluster",
                    ]
                ],
                use_container_width=True,
            )