<div align="center">

# 🚀 Agentic arXiv Research Scanner

### Agentic AI Research Intelligence System for AI/ML + Quant Finance Papers

<p>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/LangGraph-Agentic_AI-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit" />
</p>

<p>
  <b>Scan arXiv → Score Relevance → Summarize Papers → Ingest PDFs → Build RAG Index → Ask Research Questions → Analyze Trends</b>
</p>

</div>

---

## Project Overview

An end-to-end **agentic AI system** that scans arXiv for recent **AI/ML** and **quant finance** papers, scores relevance, generates LLM summaries, stores results in SQLite, orchestrates workflows using LangGraph, indexes papers into ChromaDB, supports RAG research QA, ingests full-paper PDFs, detects research trends, and visualizes results through a Streamlit dashboard.

---

## Features

- arXiv paper ingestion
- AI/ML + Quant Finance category scanning
- Keyword relevance scoring
- Ollama local LLM summarization
- Mock summarization fallback
- SQLite storage
- LangGraph workflow orchestration
- Markdown research brief generation
- Streamlit dashboard
- RAG research QA
- ChromaDB vector database
- Local embeddings with SentenceTransformers
- PDF download and full-text extraction
- Chunked full-paper indexing
- Research trend analytics
- TF-IDF term extraction
- Keyword frequency analysis
- Workflow observability and timing metrics
- Pytest unit tests
- GitHub Actions CI

---

## Architecture

```text
arXiv API
    ↓
Fetch Papers
    ↓
Relevance Scoring Agent
    ↓
LLM / Mock Summarization Agent
    ↓
PDF Ingestion
    ↓
Full-Text Chunking
    ↓
SQLite Storage + ChromaDB Indexing
    ↓
Markdown Report Generator
    ↓
Streamlit Dashboard
    ├── Paper Dashboard
    ├── RAG Research QA
    └── Trend Analytics
```

---

## Tech Stack

### Core

- Python 3.11
- LangGraph
- Streamlit
- SQLite
- Pytest
- Rich

### AI / LLM

- Ollama
- llama3.2:1b
- SentenceTransformers
- ChromaDB

### Data / Parsing / Analytics

- arxiv Python SDK
- pandas
- plotly
- scikit-learn
- PyMuPDF
- requests
- tqdm
- matplotlib
- wordcloud

---

## Project Structure

```text
agentic-arxiv-research-scanner/
├── app/
│   ├── agents/
│   │   ├── relevance_agent.py
│   │   ├── summarizer_agent.py
│   │   └── rag_answer_agent.py
│   │
│   ├── data/
│   │   ├── arxiv_client.py
│   │   ├── storage.py
│   │   ├── vector_store.py
│   │   ├── pdf_ingestor.py
│   │   ├── text_chunker.py
│   │   └── trend_analysis.py
│   │
│   ├── workflows/
│   │   ├── research_graph.py
│   │   └── report_generator.py
│   │
│   ├── dashboard/
│   │   └── streamlit_app.py
│   │
│   └── utils.py
│
├── data/
│   ├── pdfs/
│   └── parsed/
│
├── reports/
├── tests/
├── chroma_db/
├── .github/workflows/tests.yml
├── config.yaml
├── main.py
├── rag_query.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd agentic-arxiv-research-scanner
```

### 2. Create Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Ollama Setup

Install Ollama:

```text
https://ollama.com
```

Pull a lightweight model:

```bash
ollama pull llama3.2:1b
```

Start Ollama server:

```bash
ollama serve
```

Test model:

```bash
ollama run llama3.2:1b
```

Recommended laptop-safe model:

```text
llama3.2:1b
```

---

## Configuration

Example `config.yaml`:

```yaml
project:
  name: agentic-arxiv-research-scanner

arxiv:
  categories:
    - cs.AI
    - cs.LG
    - cs.CL
    - q-fin.TR
    - q-fin.ST
  max_results: 5
  sort_by: submittedDate

interests:
  keywords:
    - agentic ai
    - rag
    - retrieval augmented generation
    - large language models
    - llm
    - machine learning
    - deep learning
    - reinforcement learning
    - quant finance
    - trading
    - market microstructure
    - alpha
    - forecasting

llm:
  use_ollama: true
  model: llama3.2:1b

pdf:
  ingest_full_text: true
  max_pdfs: 2
  chunk_size: 1000
  chunk_overlap: 150
```

---

## Run Main Workflow

```bash
python main.py
```

Example output:

```text
Running Agentic Research Workflow...

Starting node: fetch_papers
Completed node: fetch_papers (2.41s)

Starting node: score_papers
Completed node: score_papers (0.01s)

Starting node: summarize_papers
Completed node: summarize_papers (8.73s)

Starting node: ingest_pdfs
Completed node: ingest_pdfs (12.42s)

Starting node: store_and_index_papers
Completed node: store_and_index_papers (3.51s)

Starting node: generate_report
Completed node: generate_report (0.01s)

Workflow completed successfully
Total Workflow Time: 27.08s
```

---

## arXiv Rate Limit Note

arXiv may return HTTP 429 if requests are repeated too quickly.

Recommended development settings:

```yaml
arxiv:
  max_results: 5
```

In `app/data/arxiv_client.py`, use a conservative client:

```python
client = arxiv.Client(
    page_size=max_results,
    delay_seconds=10.0,
    num_retries=1,
)
```

If arXiv blocks requests, wait before retrying.

---

## Run Streamlit Dashboard

```bash
streamlit run app/dashboard/streamlit_app.py
```

Dashboard tabs:

```text
Paper Dashboard
RAG Research QA
Trend Analytics
```

Dashboard includes:

- Paper browser
- Keyword search
- Relevance score filtering
- Summary method filtering
- Workflow analytics charts
- RAG research QA tab
- Retrieved paper chunk display
- Trend analytics tab
- TF-IDF research term charts
- Matched keyword frequency charts
- Direct arXiv links

---

## RAG Research QA

The dashboard supports questions such as:

```text
Which papers are most relevant to quant trading strategies?
What are the major trends in agentic AI?
What implementation ideas can I get from these papers?
Which retrieved chunks support the answer?
```

The RAG system:

```text
User Question
    ↓
SentenceTransformer Embedding
    ↓
ChromaDB Semantic Search
    ↓
Top Paper Chunks
    ↓
Ollama Answer Generator
    ↓
Grounded Research Answer
```

---

## Trend Analytics

The project includes a Streamlit **Trend Analytics** tab powered by:

- TF-IDF
- n-gram extraction
- matched keyword frequency
- Plotly visualizations

Trend module:

```text
app/data/trend_analysis.py
```

Analytics include:

```text
Top TF-IDF Research Terms
Top Matched Keywords
Research Theme Charts
```

---

## Run Command-Line RAG QA

```bash
python rag_query.py
```

---

## Run Tests

```bash
pytest -v
```

Example:

```text
3 passed
```

---

## GitHub Actions CI

The CI workflow automatically:

- installs dependencies
- runs tests
- validates project integrity

Workflow file:

```text
.github/workflows/tests.yml
```

---

## Observability Features

- Node-level timing
- Total workflow timing
- Summary backend tracking
- Ollama fallback handling
- SQLite persistence
- ChromaDB indexing
- Dashboard analytics
- RAG retrieval visibility
- Trend analytics visualization

---

## Portfolio Highlights

This project demonstrates:

- Agentic AI systems
- LangGraph orchestration
- LLM engineering
- RAG over research papers
- Full-paper PDF ingestion
- Chunked vector search
- Research trend detection
- Local-first GenAI development
- Production-style fallback handling
- AI workflow observability
- Streamlit application development
- GitHub Actions CI/CD
- Applied AI for research intelligence
- AI/ML + Quant Finance domain alignment

---

## Future Improvements

Potential future upgrades:

- Better page-level citations
- Paper clustering by topic
- Research trend detection over time
- Novelty scoring
- Email/Slack digest
- Scheduled daily ingestion
- Docker deployment
- Streamlit Cloud deployment
- Evaluation framework for RAG quality
- Multi-agent critic/reviewer
- Citation graph integration

---

# Project Build Steps

## Step 1: Define Project Scope and MVP

Built an agentic arXiv research scanner for both AI/ML and quant finance papers.

## Step 2: Create GitHub-Ready Folder Structure

Created the main project folders under `app/`, `reports/`, and `tests/`.

## Step 3: Add Dependencies and Config Files

Added initial Python dependencies, `.gitignore`, and `config.yaml`.

## Step 4: Add arXiv Paper Collector

Created `app/data/arxiv_client.py` to fetch recent arXiv papers.

## Step 5: Add Keyword Relevance Scoring Agent

Created `app/agents/relevance_agent.py`.

## Step 6: Add SQLite Storage Layer

Created `app/data/storage.py`.

## Step 7: Add Mock LLM Summarization Agent

Created `app/agents/summarizer_agent.py`.

## Step 8: Store LLM Summary in SQLite

Added `llm_summary` to the database schema.

## Step 8A: Add Ollama Summarization

Added local LLM summarization with Ollama.

## Step 8B: Track Summary Method

Stored whether each paper used Ollama, mock, or fallback summarization.

## Step 9: Generate Daily Markdown Research Report

Created `app/workflows/report_generator.py`.

## Step 10: Add LangGraph Workflow Orchestration

Created `app/workflows/research_graph.py`.

## Step 11: Add Observability and Timing Metrics

Created `app/utils.py` with timing decorators.

## Step 12: Add Streamlit Dashboard

Created `app/dashboard/streamlit_app.py`.

## Step 12B: Add Dashboard Search and Charts

Added search, filtering, score charts, and summary method charts.

## Step 13: Add Tests

Created relevance and report generation tests.

## Step 14: Add GitHub Actions CI

Created `.github/workflows/tests.yml`.

## Step 15: Finalize README

Created a GitHub-ready README.

## Step 16: Add Vector DB + RAG Foundation

Added ChromaDB and SentenceTransformers.

## Step 16B: Add Vector Indexing to LangGraph

Indexed papers into ChromaDB during workflow execution.

## Step 17: Add Semantic Search Script

Created `rag_query.py`.

## Step 18: Add RAG Answer Generator

Created `app/agents/rag_answer_agent.py`.

## Step 18B: Upgrade RAG Query Script

Added full command-line RAG QA.

## Step 18C: Add RAG QA to Streamlit

Added RAG Research QA tab.

## Step 19: Add PDF Ingestion Dependencies

Added PyMuPDF and PDF folders.

## Step 19A: Add PDF Download and Text Extraction

Created PDF ingestion logic.

## Step 19B: Add Full-Paper Text Chunking

Created `app/data/text_chunker.py`.

## Step 19C: Add Chunked Vector Indexing

Updated ChromaDB indexing to use full-paper chunks.

## Step 19D: Add PDF Ingestion into LangGraph

Added a PDF ingestion node.

## Step 19E: Update RAG Answer Agent for Chunk Citations

Added chunk metadata to RAG context.

## Step 20: Add PDF Ingestion Controls to Config

Added configurable PDF ingestion controls.

## Step 20A: Limit PDF Ingestion Using Config

Limited PDF downloading to `max_pdfs`.

## Step 21: Add Research Trend Detection

Added trend detection dependencies.

## Step 21B: Create Trend Analysis Module

Created `app/data/trend_analysis.py`.

## Step 21C: Add Trend Analytics to Streamlit

Added the Trend Analytics dashboard tab.

---

## Current Status

The project now supports:

```text
Agentic workflow orchestration
Local LLM summarization
Mock fallback summarization
SQLite storage
Markdown reporting
Streamlit dashboard
RAG QA
ChromaDB vector search
PDF ingestion
Full-paper chunked retrieval
Trend analytics
Testing
GitHub Actions CI
```

---

## Recommended Next Steps

1. Add Docker support
2. Add RAG evaluation tests
3. Add scheduled daily ingestion
4. Add email/Slack research digest
5. Add deployment instructions
6. Add page-level citation extraction
7. Add topic clustering and trend detection over time

---

## License

MIT License
