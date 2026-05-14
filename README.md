# Agentic arXiv Research Scanner

An end-to-end agentic AI system that scans arXiv for recent AI/ML and quant finance papers, scores relevance, generates LLM summaries, stores results in SQLite, orchestrates workflows using LangGraph, indexes papers into ChromaDB, supports RAG research QA, ingests full-paper PDFs, and visualizes results through a Streamlit dashboard.

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
Streamlit Dashboard + RAG QA
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

### Data / Parsing

- arxiv Python SDK
- pandas
- plotly
- PyMuPDF
- requests
- tqdm

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
│   │   └── text_chunker.py
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

Avoid large models on limited RAM laptops:

```text
llama3.1:8b
deepseek-r1:8b
mixtral
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

Dashboard includes:

- Paper browser
- Keyword search
- Relevance score filtering
- Summary method filtering
- Workflow analytics charts
- RAG research QA tab
- Retrieved paper chunk display
- Direct arXiv links

---

## Run Command-Line RAG QA

```bash
python rag_query.py
```

Example questions:

```text
Which papers are most relevant to quant trading strategies?
What are the major trends in agentic AI?
What implementation ideas can I get from these papers?
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

---

## Portfolio Highlights

This project demonstrates:

- Agentic AI systems
- LangGraph orchestration
- LLM engineering
- RAG over research papers
- Full-paper PDF ingestion
- Chunked vector search
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
- Research trend detection
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

This section documents the step-by-step build process used to create the project.

## Step 1: Define Project Scope and MVP

Selected project direction:

```text
Agentic arXiv Research Scanner for both AI/ML and quant finance papers.
```

Initial goal:

```text
Scan arXiv, score relevance, summarize papers, store results, and generate research briefs.
```

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

Created folders:

```text
app/
app/agents/
app/data/
app/workflows/
app/dashboard/
reports/
tests/
```

Created base files:

```text
main.py
config.yaml
requirements.txt
README.md
.gitignore
```

---

## Step 3: Add Dependencies and Config Files

Added initial dependencies:

```text
arxiv
pandas
pyyaml
requests
python-dotenv
pytest
rich
```

Added project configuration in `config.yaml`.

Added `.gitignore`.

---

## Step 4: Add arXiv Paper Collector

Created:

```text
app/data/arxiv_client.py
```

Implemented:

- category query builder
- recent paper fetcher
- title, authors, abstract, date, URL, PDF URL extraction

---

## Step 5: Add Keyword Relevance Scoring Agent

Created:

```text
app/agents/relevance_agent.py
```

Implemented:

- keyword matching
- relevance score from 0 to 10
- matched keyword tracking
- sorting by relevance

---

## Step 6: Add SQLite Storage Layer

Created:

```text
app/data/storage.py
```

Implemented:

- database initialization
- paper saving
- top paper retrieval
- duplicate handling

---

## Step 7: Add Mock LLM Summarization Agent

Created:

```text
app/agents/summarizer_agent.py
```

Implemented:

- mock structured summaries
- summary field added to each paper
- fallback summarization logic

---

## Step 8: Store LLM Summary in SQLite

Updated SQLite schema to include:

```text
llm_summary
```

Updated:

- insert query
- top paper query
- terminal output

---

## Step 8A: Add Ollama Summarization

Added Ollama support using:

```text
llama3.2:1b
```

Implemented:

- local LLM summarization
- fallback to mock summarizer
- model configuration through `config.yaml`

---

## Step 8B: Track Summary Method

Added:

```text
summary_method
```

Possible values:

```text
ollama:<model>
mock
mock_fallback
unknown
```

Stored and printed the method used for each summary.

---

## Step 9: Generate Daily Markdown Research Report

Created:

```text
app/workflows/report_generator.py
```

Implemented:

- markdown report generation
- timestamped reports
- summaries, scores, keywords, URLs
- report storage in `reports/`

---

## Step 10: Add LangGraph Workflow Orchestration

Created:

```text
app/workflows/research_graph.py
```

Workflow:

```text
Fetch Papers → Score Relevance → Summarize → Store → Generate Report
```

Updated `main.py` to invoke the LangGraph workflow.

---

## Step 11: Add Observability and Timing Metrics

Created:

```text
app/utils.py
```

Added:

- `timed_node` decorator
- node-level execution times
- total workflow runtime
- clearer terminal logs

---

## Step 12: Add Streamlit Dashboard

Created:

```text
app/dashboard/streamlit_app.py
```

Added:

- paper dashboard
- score filtering
- summary method filtering
- expandable summaries
- arXiv links

---

## Step 12B: Add Dashboard Search and Charts

Added:

- keyword search
- relevance score bar chart
- summary method pie chart
- total/filtered paper metrics

---

## Step 13: Add Tests

Created:

```text
tests/test_relevance_agent.py
tests/test_report_generator.py
```

Test coverage:

- relevance scoring
- keyword matching
- sorting by relevance
- markdown report generation

---

## Step 14: Add GitHub Actions CI

Created:

```text
.github/workflows/tests.yml
```

CI workflow:

```text
checkout repo
setup Python
install dependencies
run pytest
```

---

## Step 15: Finalize README

Created a GitHub-ready README with:

- project overview
- architecture
- setup
- running instructions
- dashboard instructions
- tests
- CI
- portfolio highlights

---

## Step 16: Add Vector DB + RAG Foundation

Installed:

```text
chromadb
sentence-transformers
```

Created:

```text
app/data/vector_store.py
```

Implemented:

- ChromaDB persistent storage
- local embeddings
- semantic search

---

## Step 16B: Add Vector Indexing to LangGraph

Updated workflow to:

```text
store papers in SQLite
index papers in ChromaDB
```

---

## Step 17: Add Semantic Search Script

Created:

```text
rag_query.py
```

Implemented command-line semantic search over indexed papers.

---

## Step 18: Add RAG Answer Generator

Created:

```text
app/agents/rag_answer_agent.py
```

Implemented:

- context builder
- retrieved-context answering
- Ollama answer generation
- fallback to retrieved context

---

## Step 18B: Upgrade RAG Query Script

Updated:

```text
rag_query.py
```

Added:

- question input
- semantic retrieval
- RAG answer synthesis
- retrieved paper display

---

## Step 18C: Add RAG QA to Streamlit

Updated dashboard with:

```text
Paper Dashboard tab
RAG Research QA tab
```

Added:

- question input
- top-k retrieval slider
- Ollama toggle
- model input
- retrieved paper display

---

## Step 19: Add PDF Ingestion Dependencies

Installed:

```text
pymupdf
tqdm
```

Created:

```text
data/pdfs/
data/parsed/
app/data/pdf_ingestor.py
```

---

## Step 19A: Add PDF Download and Text Extraction

Implemented:

- PDF download
- safe filenames
- text extraction with PyMuPDF
- parsed text saving
- ingestion status tracking

---

## Step 19B: Add Full-Paper Text Chunking

Created:

```text
app/data/text_chunker.py
```

Implemented:

- chunking with overlap
- chunk records
- chunk metadata

---

## Step 19C: Add Chunked Vector Indexing

Updated:

```text
app/data/vector_store.py
```

Changed vector indexing from one embedding per paper to many embeddings per full-paper chunk.

---

## Step 19D: Add PDF Ingestion into LangGraph

Updated workflow:

```text
Fetch → Score → Summarize → PDF Ingest → Store + Index → Report
```

Added `pdf_ingest` node.

---

## Step 19E: Update RAG Answer Agent for Chunk Citations

Updated RAG context to include:

- paper title
- published date
- relevance score
- chunk index
- paper ID

Updated answer format to include supporting paper chunks.

---

## Step 20: Add PDF Ingestion Controls to Config

Added:

```yaml
pdf:
  ingest_full_text: true
  max_pdfs: 2
  chunk_size: 1000
  chunk_overlap: 150
```

Purpose:

- control long runtimes
- avoid laptop overload
- limit number of downloaded PDFs

---

## Step 20A: Limit PDF Ingestion Using Config

Updated `pdf_ingest_node` to:

- respect `ingest_full_text`
- only download first `max_pdfs`
- leave other papers as abstract-only records

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
Testing
GitHub Actions CI
```

---

## Recommended Next Steps

1. Add Docker support
2. Add better RAG evaluation tests
3. Add scheduled daily ingestion
4. Add email/Slack research digest
5. Add deployment instructions
6. Add page-level citation extraction
7. Add topic clustering and trend detection

---

## License

MIT License
