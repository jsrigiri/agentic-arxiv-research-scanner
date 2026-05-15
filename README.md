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
  <b>
  Scan arXiv → Score Relevance → Summarize Papers → Ingest PDFs → Build RAG Index → Ask Research Questions → Analyze Trends
  </b>
</p>

</div>

---

# 📌 Project Overview

An end-to-end **agentic AI research intelligence platform** that scans arXiv for recent **AI/ML** and **quant finance** papers, scores relevance, generates local LLM summaries, ingests full PDFs, builds vector embeddings, performs semantic RAG retrieval, analyzes research trends, clusters research topics, evaluates RAG quality, and delivers autonomous reports through Streamlit, email, Slack, and scheduled workflows.

---

# ✨ Features

- arXiv paper ingestion
- AI/ML + Quant Finance categories
- Keyword relevance scoring
- Ollama local LLM summarization
- Mock summarization fallback
- SQLite persistence
- LangGraph workflow orchestration
- Markdown report generation
- Streamlit dashboard
- RAG research QA
- ChromaDB vector database
- Full-paper PDF ingestion
- Chunked semantic retrieval
- Trend analytics
- Topic clustering
- RAG evaluation metrics
- Autonomous scheduler
- Email digest
- Slack notifications
- Workflow observability
- GitHub Actions CI
- Pytest unit tests

---

# 🏗️ Architecture

```text
arXiv API
    ↓
Fetch Papers
    ↓
Relevance Scoring Agent
    ↓
LLM / Mock Summarization
    ↓
PDF Ingestion
    ↓
Chunking + Embeddings
    ↓
SQLite + ChromaDB
    ↓
RAG QA + Trend Analytics
    ↓
Streamlit Dashboard
    ↓
Scheduler + Email + Slack
```

---

# 🧠 AI / ML Stack

## Core

- Python 3.11
- LangGraph
- Streamlit
- SQLite
- Rich
- Pytest

## AI / LLM

- Ollama
- llama3.2:1b
- SentenceTransformers
- ChromaDB

## Analytics / Clustering

- scikit-learn
- UMAP
- HDBSCAN
- Plotly

## Parsing / Ingestion

- arxiv SDK
- PyMuPDF
- requests
- tqdm

---

# 📂 Project Structure

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
│   │   ├── trend_analysis.py
│   │   └── topic_clustering.py
│   │
│   ├── workflows/
│   │   ├── research_graph.py
│   │   └── report_generator.py
│   │
│   ├── dashboard/
│   │   └── streamlit_app.py
│   │
│   ├── notifications/
│   │   ├── email_digest.py
│   │   └── slack_digest.py
│   │
│   ├── evaluation/
│   │   └── rag_evaluator.py
│   │
│   └── utils.py
│
├── chroma_db/
├── data/
│   ├── pdfs/
│   └── parsed/
│
├── reports/
├── tests/
├── .github/workflows/tests.yml
├── config.yaml
├── main.py
├── scheduler.py
├── rag_query.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# ⚙️ Setup

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd agentic-arxiv-research-scanner
```

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Mac/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

Install Ollama:

```text
https://ollama.com
```

Pull lightweight model:

```bash
ollama pull llama3.2:1b
```

Start Ollama:

```bash
ollama serve
```

Test model:

```bash
ollama run llama3.2:1b
```

Recommended lightweight model:

```text
llama3.2:1b
```

---

# ▶️ Run Main Workflow

```bash
python main.py
```

Example output:

```text
Running Agentic Research Workflow...

Starting node: fetch_papers
Completed node: fetch_papers (2.41s)

Starting node: summarize_papers
Completed node: summarize_papers (8.73s)

Starting node: store_and_index_papers
Completed node: store_and_index_papers (3.51s)

Workflow completed successfully
```

---

# 📊 Run Streamlit Dashboard

```bash
streamlit run app/dashboard/streamlit_app.py
```

Dashboard tabs:

- Paper Dashboard
- RAG Research QA
- Trend Analytics
- Scheduler
- Topic Clusters

---

# 🔍 RAG Features

The project supports:

- Semantic retrieval
- Chunked PDF indexing
- Grounded QA
- Retrieved chunk display
- Local embeddings
- ChromaDB vector search

Example questions:

```text
What are the major trends in agentic AI?
Which papers are relevant to quant trading?
What implementation ideas can I get from these papers?
```

---

# 📈 Trend Analytics

Includes:

- TF-IDF term extraction
- Keyword frequency analysis
- Topic clustering
- UMAP visualization
- HDBSCAN clustering

---

# 🧪 RAG Evaluation Metrics

Evaluates:

- Retrieved chunk count
- Unique paper count
- Embedding distance
- Grounding overlap score

---

# ⏰ Autonomous Scheduler

Run scheduler:

```bash
python scheduler.py
```

Features:

- Live config reloads
- Streamlit scheduler controls
- Automatic report generation
- Automatic email delivery
- Automatic Slack notifications

---

# 📬 Email Digest

Supported providers:

- Yahoo
- Gmail

Configured via:

```yaml
email:
  enabled: true
```

Password stored securely in:

```env
EMAIL_PASSWORD=...
```

---

# 💬 Slack Integration

Uses Slack Incoming Webhooks.

Configured via:

```yaml
slack:
  enabled: true
```

Webhook stored securely in:

```env
SLACK_WEBHOOK_URL=...
```

---

# 🧪 Run Tests

```bash
pytest -v
```

---

# 🚀 GitHub Actions CI

CI pipeline automatically:

- installs dependencies
- runs tests
- validates project integrity

Workflow:

```text
.github/workflows/tests.yml
```

---

# 📌 Portfolio Highlights

This project demonstrates:

- Agentic AI systems
- GenAI engineering
- LangGraph orchestration
- Local-first AI tooling
- RAG pipelines
- PDF ingestion pipelines
- Semantic retrieval
- AI workflow observability
- Autonomous scheduling
- Research intelligence systems
- AI + Quant Finance integration

---

# 🛠️ Project Build Steps

## Step 1: Define Project Scope and MVP

### Step 1A: Select Project Direction

Selected a portfolio-grade project focused on an **agentic arXiv research scanner**.

### Step 1B: Select Domain Coverage

Chose combined coverage for:

- AI/ML research
- Quant finance research

### Step 1C: Define MVP Goal

The MVP goal was to:

- scan arXiv papers
- score paper relevance
- summarize papers
- store results
- generate a research brief

### Step 1D: Select Initial arXiv Categories

Initial categories:

```text
cs.AI
cs.LG
cs.CL
q-fin.TR
q-fin.ST
```

---

## Step 2: Create GitHub-Ready Folder Structure

### Step 2A: Create Root Project Folder

Created:

```text
agentic-arxiv-research-scanner/
```

### Step 2B: Create Application Folders

Created:

```text
app/
app/agents/
app/data/
app/workflows/
app/dashboard/
reports/
tests/
```

### Step 2C: Add Python Package Markers

Added:

```text
__init__.py
```

inside relevant app subfolders.

### Step 2D: Add Base Project Files

Created:

```text
main.py
config.yaml
requirements.txt
README.md
.gitignore
```

---

## Step 3: Add Dependencies and Config Files

### Step 3A: Add Initial Dependencies

Added:

```text
arxiv
pandas
pyyaml
requests
python-dotenv
pytest
rich
```

### Step 3B: Add `.gitignore`

Excluded:

```text
.venv/
__pycache__/
.env
*.db
reports/*.md
data/
chroma_db/
```

### Step 3C: Add `config.yaml`

Configured:

- project name
- arXiv categories
- max results
- interest keywords

---

## Step 4: Add arXiv Paper Collector

### Step 4A: Create arXiv Client Module

Created:

```text
app/data/arxiv_client.py
```

### Step 4B: Build Category Query Logic

Implemented category query generation such as:

```text
cat:cs.AI OR cat:cs.LG
```

### Step 4C: Fetch Recent Papers

Implemented paper fetching with:

- title
- authors
- abstract
- published date
- updated date
- arXiv URL
- PDF URL
- categories

### Step 4D: Handle arXiv Rate Limits

Added conservative client settings:

```python
page_size=max_results
delay_seconds=10.0
num_retries=1
```

---

## Step 5: Add Keyword Relevance Scoring Agent

### Step 5A: Create Relevance Agent

Created:

```text
app/agents/relevance_agent.py
```

### Step 5B: Match Interest Keywords

Matched keywords across:

- title
- abstract
- categories

### Step 5C: Compute Relevance Score

Computed score from `0` to `10`.

### Step 5D: Sort Papers by Relevance

Sorted papers by descending relevance score.

---

## Step 6: Add SQLite Storage Layer

### Step 6A: Create Storage Module

Created:

```text
app/data/storage.py
```

### Step 6B: Initialize Database

Created a `papers` table.

### Step 6C: Save Papers

Saved:

- title
- summary
- authors
- categories
- URLs
- relevance score
- matched keywords

### Step 6D: Fetch Top Papers

Added function to retrieve top papers by relevance score and date.

---

## Step 7: Add Mock LLM Summarization Agent

### Step 7A: Create Summarizer Agent

Created:

```text
app/agents/summarizer_agent.py
```

### Step 7B: Add Mock Summary

Implemented a lightweight summary fallback.

### Step 7C: Add Structured Summary Format

Included:

- key idea
- why it matters
- implementation angle

---

## Step 8: Store LLM Summary in SQLite

### Step 8A: Add `llm_summary` Field

Updated database schema.

### Step 8B: Update Insert Logic

Updated paper save logic to persist LLM summaries.

### Step 8C: Update Print Output

Printed summaries in terminal output.

---

## Step 9: Add Ollama Summarization

### Step 9A: Add Ollama Dependency

Added:

```text
ollama
```

### Step 9B: Configure Local LLM

Added:

```yaml
llm:
  use_ollama: true
  model: llama3.2:1b
```

### Step 9C: Add Ollama Summary Function

Used `ollama.chat()` to summarize paper abstracts.

### Step 9D: Add Laptop-Safe Options

Limited:

- context length
- output length
- model keep-alive behavior

### Step 9E: Add Mock Fallback

Fallback is used when Ollama fails or is disabled.

---

## Step 10: Track Summary Method

### Step 10A: Add `summary_method`

Added tracking for:

```text
ollama:<model>
mock
mock_fallback
unknown
```

### Step 10B: Store Method in SQLite

Updated schema and insert logic.

### Step 10C: Display Method

Printed summary method in terminal and Streamlit dashboard.

---

## Step 11: Generate Daily Markdown Research Report

### Step 11A: Create Report Generator

Created:

```text
app/workflows/report_generator.py
```

### Step 11B: Generate Markdown Brief

Included:

- title
- published date
- relevance score
- matched keywords
- URL
- LLM summary
- summary method

### Step 11C: Save Reports

Saved reports to:

```text
reports/
```

---

## Step 12: Add LangGraph Workflow Orchestration

### Step 12A: Install LangGraph

Added:

```text
langgraph
```

### Step 12B: Create Research Graph

Created:

```text
app/workflows/research_graph.py
```

### Step 12C: Define Workflow State

Created a typed state object containing:

- config
- papers
- scored papers
- summarized papers
- top papers
- report path

### Step 12D: Add Workflow Nodes

Added nodes for:

- fetch
- score
- summarize
- store
- report

### Step 12E: Update `main.py`

Updated `main.py` to invoke the compiled LangGraph workflow.

---

## Step 13: Add Observability and Timing Metrics

### Step 13A: Create Utility Module

Created:

```text
app/utils.py
```

### Step 13B: Add `timed_node` Decorator

Added node-level timing logs.

### Step 13C: Add Total Workflow Timing

Added workflow runtime measurement in `main.py`.

---

## Step 14: Add Streamlit Dashboard

### Step 14A: Install Streamlit

Added:

```text
streamlit
```

### Step 14B: Create Dashboard App

Created:

```text
app/dashboard/streamlit_app.py
```

### Step 14C: Load Papers from SQLite

Loaded stored papers into a Pandas DataFrame.

### Step 14D: Add Dashboard Filters

Added:

- relevance score filter
- summary method filter

### Step 14E: Add Paper Cards

Displayed:

- paper title
- score
- matched keywords
- summary
- arXiv URL

---

## Step 15: Add Dashboard Search and Charts

### Step 15A: Add Plotly

Added:

```text
plotly
```

### Step 15B: Add Search

Added search across:

- title
- matched keywords
- summaries

### Step 15C: Add Metrics

Added:

- total papers
- filtered papers
- average relevance

### Step 15D: Add Charts

Added:

- relevance score bar chart
- summary method distribution pie chart

---

## Step 16: Add Tests

### Step 16A: Create Test Files

Created:

```text
tests/test_relevance_agent.py
tests/test_report_generator.py
```

### Step 16B: Fix Python Path for Pytest

Added:

```text
pytest.ini
```

### Step 16C: Test Relevance Scoring

Tested:

- keyword matching
- score calculation
- sorting

### Step 16D: Test Report Generation

Tested that markdown report files are generated correctly.

---

## Step 17: Add GitHub Actions CI

### Step 17A: Create Workflow Folder

Created:

```text
.github/workflows/
```

### Step 17B: Add Test Workflow

Created:

```text
.github/workflows/tests.yml
```

### Step 17C: Configure CI

Configured CI to:

- check out code
- install Python
- install dependencies
- run tests

---

## Step 18: Add Vector DB + RAG Foundation

### Step 18A: Install Vector Dependencies

Added:

```text
chromadb
sentence-transformers
```

### Step 18B: Create Vector Store Module

Created:

```text
app/data/vector_store.py
```

### Step 18C: Add Embedding Model

Used:

```text
all-MiniLM-L6-v2
```

### Step 18D: Add ChromaDB Persistent Client

Configured persistent storage under:

```text
chroma_db/
```

### Step 18E: Add Semantic Search

Implemented vector similarity search.

---

## Step 19: Add Vector Indexing to LangGraph

### Step 19A: Import Vector Indexer

Imported `index_papers`.

### Step 19B: Update Store Node

Updated store node to:

- save papers in SQLite
- index papers in ChromaDB

---

## Step 20: Add Semantic Search Script

### Step 20A: Create RAG Query Script

Created:

```text
rag_query.py
```

### Step 20B: Add User Question Input

Allowed users to ask research questions.

### Step 20C: Print Top Semantic Matches

Printed:

- title
- published date
- relevance score
- distance
- URL
- retrieved context

---

## Step 21: Add RAG Answer Generator

### Step 21A: Create RAG Answer Agent

Created:

```text
app/agents/rag_answer_agent.py
```

### Step 21B: Build Retrieved Context

Combined retrieved documents into context blocks.

### Step 21C: Generate Answer with Ollama

Used local LLM to answer using retrieved context.

### Step 21D: Add Fallback

Returned retrieved context when Ollama fails or is disabled.

---

## Step 22: Add RAG QA to Streamlit

### Step 22A: Add RAG Tab

Added:

```text
RAG Research QA
```

### Step 22B: Add Question Input

Added a text area for research questions.

### Step 22C: Add Top-K Slider

Allowed controlling number of retrieved chunks.

### Step 22D: Add Ollama Toggle

Added option to enable or disable local LLM answer generation.

### Step 22E: Display Retrieved Papers

Displayed retrieved documents and metadata.

---

## Step 23: Add PDF Ingestion

### Step 23A: Install PDF Dependencies

Added:

```text
pymupdf
tqdm
```

### Step 23B: Create PDF Folders

Created:

```text
data/pdfs/
data/parsed/
```

### Step 23C: Create PDF Ingestor

Created:

```text
app/data/pdf_ingestor.py
```

### Step 23D: Download PDFs

Downloaded arXiv PDFs using paper PDF URLs.

### Step 23E: Extract PDF Text

Used PyMuPDF to extract text page by page.

### Step 23F: Save Parsed Text

Saved extracted text into:

```text
data/parsed/
```

---

## Step 24: Add Text Chunking

### Step 24A: Create Chunker Module

Created:

```text
app/data/text_chunker.py
```

### Step 24B: Add Overlapping Chunk Logic

Added configurable:

- chunk size
- chunk overlap

### Step 24C: Build Chunk Records

Created metadata-rich chunk records for indexing.

---

## Step 25: Add Chunked Vector Indexing

### Step 25A: Update Vector Store

Updated `vector_store.py`.

### Step 25B: Index Full-Paper Chunks

Embedded and stored each chunk separately.

### Step 25C: Add Abstract Fallback

Indexed abstract-level text if full PDF text was unavailable.

---

## Step 26: Add PDF Ingestion into LangGraph

### Step 26A: Add PDF Ingest Node

Added:

```text
pdf_ingest_node
```

### Step 26B: Update Workflow Edges

Updated workflow:

```text
Fetch → Score → Summarize → PDF Ingest → Store + Index → Report
```

---

## Step 27: Add PDF Ingestion Controls

### Step 27A: Update Config

Added:

```yaml
pdf:
  ingest_full_text: true
  max_pdfs: 2
  chunk_size: 1000
  chunk_overlap: 150
```

### Step 27B: Limit PDF Downloads

Limited ingestion to the first `max_pdfs` papers.

### Step 27C: Prevent Laptop Overload

Kept full-paper ingestion configurable.

---

## Step 28: Add Chunk-Aware RAG Answers

### Step 28A: Add Chunk Metadata

Included:

- title
- published date
- relevance score
- chunk index
- paper ID

### Step 28B: Update RAG Prompt

Asked answer generator to include supporting paper chunks.

---

## Step 29: Add Trend Analytics

### Step 29A: Install Trend Dependencies

Added:

```text
scikit-learn
wordcloud
matplotlib
```

### Step 29B: Create Trend Module

Created:

```text
app/data/trend_analysis.py
```

### Step 29C: Add TF-IDF Term Extraction

Extracted high-signal research terms.

### Step 29D: Add Keyword Frequency Analysis

Counted matched keyword frequency.

### Step 29E: Add Trend Analytics Dashboard Tab

Added charts for:

- top TF-IDF terms
- top matched keywords

---

## Step 30: Add Autonomous Scheduler

### Step 30A: Install Scheduler Dependency

Added:

```text
schedule
```

### Step 30B: Create Scheduler Script

Created:

```text
scheduler.py
```

### Step 30C: Add Daily Workflow Scheduling

Scheduled workflow execution from config.

### Step 30D: Add Config Auto-Reload

Scheduler watches `config.yaml` and reloads changes.

### Step 30E: Add Streamlit Scheduler Controls

Added:

- enable scheduler
- hour dropdown
- minute dropdown
- save settings

---

## Step 31: Add Email Digest

### Step 31A: Add Email Config

Configured:

```yaml
email:
  enabled: false
  smtp_server: smtp.mail.yahoo.com
  smtp_port: 587
  sender_email: ""
  recipient_email: ""
```

### Step 31B: Store Password in `.env`

Used:

```env
EMAIL_PASSWORD=...
```

### Step 31C: Create Email Module

Created:

```text
app/notifications/email_digest.py
```

### Step 31D: Send Markdown Report by Email

Attached generated report content as email body.

### Step 31E: Add Email to Workflow

Called email sender after report generation.

---

## Step 32: Add Slack Notifications

### Step 32A: Add Slack Config

Configured:

```yaml
slack:
  enabled: false
```

### Step 32B: Store Webhook in `.env`

Used:

```env
SLACK_WEBHOOK_URL=...
```

### Step 32C: Create Slack Module

Created:

```text
app/notifications/slack_digest.py
```

### Step 32D: Add Slack to Workflow

Sent Slack digest after report generation.

### Step 32E: Add Slack Controls to Streamlit

Added:

- enable Slack
- webhook input
- save settings
- test Slack message

---

## Step 33: Add Topic Clustering

### Step 33A: Install Clustering Dependencies

Added:

```text
umap-learn
hdbscan
```

### Step 33B: Create Topic Clustering Module

Created:

```text
app/data/topic_clustering.py
```

### Step 33C: Generate Embeddings

Embedded paper text with SentenceTransformers.

### Step 33D: Reduce Dimensions

Used UMAP for 2D projection.

### Step 33E: Cluster Papers

Used HDBSCAN for unsupervised topic clustering.

### Step 33F: Add Topic Clusters Dashboard Tab

Visualized clusters in Streamlit using Plotly scatter charts.

---

## Step 34: Add RAG Evaluation Metrics

### Step 34A: Create Evaluation Folder

Created:

```text
app/evaluation/
```

### Step 34B: Create RAG Evaluator

Created:

```text
app/evaluation/rag_evaluator.py
```

### Step 34C: Evaluate Retrieval Results

Tracked:

- retrieved count
- unique papers
- average distance
- whether results exist

### Step 34D: Evaluate Answer Grounding

Computed overlap between generated answer terms and retrieved context terms.

### Step 34E: Add Metrics to Streamlit

Displayed:

- retrieved chunks
- unique papers
- average distance
- grounding score

---

## Step 35: Update README and GitHub Repo

### Step 35A: Add Polished README Header

Added badge-style header.

### Step 35B: Add Updated Feature List

Included:

- scheduler
- email
- Slack
- topic clustering
- RAG evaluation

### Step 35C: Remove Secrets from Git

Moved secrets to `.env`.

### Step 35D: Push to GitHub

Updated Git history to avoid committing secrets.

---

# 🔮 Future Improvements

- Docker deployment
- Streamlit Cloud deployment
- Multi-agent reviewer system
- Trend evolution over time
- Citation graph analysis
- Research recommendation engine
- Fine-tuned reranking models

---

# 📄 License

MIT License
