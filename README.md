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

# 🛠️ Major Build Steps

1. arXiv ingestion
2. Relevance scoring
3. SQLite persistence
4. Ollama summarization
5. LangGraph orchestration
6. Streamlit dashboard
7. Vector DB + RAG
8. PDF ingestion
9. Chunked retrieval
10. Autonomous scheduler
11. Email notifications
12. Slack notifications
13. Trend analytics
14. Topic clustering
15. RAG evaluation metrics

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
