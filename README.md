<div align="center">

# 🚀 Agentic arXiv Research Scanner

### Agentic AI Research Intelligence System for AI/ML + Quant Finance Papers

<p>
  <img src="https://img.shields.io/badge/Agentic-AI-8B5CF6?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Citation_Aware-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Multi--Agent-Review_System-EC4899?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Trend-Analytics-10B981?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/LangGraph-Agentic_AI-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit" />
</p>

<p>
  <img src="https://img.shields.io/badge/PDF-Full_Text_RAG-F59E0B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scheduler-Autonomous-06B6D4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Slack-Notifications-4A154B?style=for-the-badge&logo=slack" />
  <img src="https://img.shields.io/badge/Docker-Deployment-2496ED?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes" />
</p>

<p>
<b>
Scan arXiv → Score Relevance → Summarize Papers → Ingest PDFs → Build RAG Index → Ask Research Questions → Analyze Trends
</b>
</p>

</div>

---

# 📌 Project Overview

An end-to-end **agentic AI research intelligence platform** that scans arXiv for recent **AI/ML** and **quant finance** papers, scores relevance, generates local LLM summaries, ingests full PDFs, builds vector embeddings, performs semantic and citation-aware RAG retrieval, analyzes research trends, clusters research topics, evaluates RAG quality, supports multi-agent paper reviewing, and delivers autonomous reports through Streamlit, email, Slack, scheduled workflows, Docker, and Kubernetes.

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
- Citation-aware RAG research QA
- ChromaDB vector database
- ChromaDB server container support
- Full-paper PDF ingestion
- Chunked semantic retrieval
- Trend analytics
- Historical trend evolution
- Topic clustering
- RAG evaluation metrics
- Multi-agent reviewer system
- Autonomous scheduler
- Email digest
- Slack notifications
- Docker deployment
- Multi-container Docker Compose architecture
- Kubernetes deployment manifests
- Kubernetes ConfigMap and Secret support
- Persistent Docker/Kubernetes storage patterns
- Workflow observability
- GitHub Actions CI
- Expanded Pytest test suite

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
Multi-Agent Reviewer
    ↓
PDF Ingestion
    ↓
Chunking + Embeddings
    ↓
SQLite + ChromaDB
    ↓
Citation-Aware RAG QA
    ↓
Trend Analytics + Topic Clustering
    ↓
Streamlit Dashboard
    ↓
Scheduler + Email + Slack
    ↓
Docker / Kubernetes Runtime
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

## Deployment

- Docker
- Docker Compose
- Kubernetes
- ConfigMaps
- Secrets
- Services
- Deployments
- GitHub Actions CI

---

# 📂 Project Structure

```text
agentic-arxiv-research-scanner/
├── app/
│   ├── agents/
│   ├── data/
│   ├── workflows/
│   ├── dashboard/
│   ├── notifications/
│   ├── evaluation/
│   └── utils.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── app-deployment.yaml
│   ├── scheduler-deployment.yaml
│   ├── ollama-deployment.yaml
│   ├── chroma-deployment.yaml
│   └── pvc.yaml
│
├── chroma_db/
├── data/
├── reports/
├── tests/
├── .github/workflows/tests.yml
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
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

```bash
ollama pull llama3.2:1b
ollama serve
```

---

# ▶️ Run Main Workflow

```bash
python main.py
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

# 🔍 Citation-Aware RAG

The RAG system supports:

- Semantic retrieval
- Chunked PDF indexing
- Inline citations like `[S1]`
- Retrieved chunk display
- Local embeddings
- ChromaDB vector search
- ChromaDB HTTP server mode for Docker/Kubernetes

---

# 🤖 Multi-Agent Reviewer System

Reviewer agents generate:

- Critic Review
- Implementation Review
- Quant Relevance Review
- Limitations Review

Review outputs are:

- stored in SQLite
- displayed in Streamlit
- included in markdown reports

---

# 📈 Trend Analytics

Includes:

- TF-IDF term extraction
- Keyword frequency analysis
- Historical trend tracking
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

```bash
python scheduler.py
```

Features:

- Live config reloads
- Streamlit scheduler controls
- Hour/minute dropdown selectors
- Automatic report generation
- Automatic email delivery
- Automatic Slack notifications

---

# 🐳 Docker Deployment

```bash
docker compose up --build
```

Run workflow inside Docker:

```bash
docker compose exec agentic-arxiv-app python main.py
```

Run scheduler inside Docker:

```bash
docker compose exec agentic-arxiv-scheduler python scheduler.py
```

Docker services:

```text
agentic-arxiv-app        Streamlit dashboard
agentic-arxiv-scheduler  autonomous scheduler
agentic-arxiv-ollama     local LLM server
agentic-arxiv-chroma     vector DB server
```

---

# ☸️ Kubernetes Deployment

Create namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Create ConfigMap:

```bash
kubectl apply -f k8s/configmap.yaml
```

Create Kubernetes secrets from `.env`:

```bash
kubectl create secret generic agentic-arxiv-secrets \
  --from-env-file=.env \
  -n agentic-arxiv
```

Deploy ChromaDB:

```bash
kubectl apply -f k8s/chroma-deployment.yaml
```

Deploy Ollama:

```bash
kubectl apply -f k8s/ollama-deployment.yaml
```

Pull Ollama model inside Kubernetes:

```bash
kubectl exec -it deployment/ollama -n agentic-arxiv -- ollama pull llama3.2:1b
```

Deploy Streamlit app:

```bash
kubectl apply -f k8s/app-deployment.yaml
```

Port-forward dashboard:

```bash
kubectl port-forward svc/agentic-arxiv-app 8501:8501 -n agentic-arxiv
```

Run workflow inside Kubernetes:

```bash
kubectl exec -it deployment/agentic-arxiv-app -n agentic-arxiv -- python main.py
```

---

# 📬 Email Digest

Supported providers:

- Yahoo
- Gmail

Secrets stored securely in:

```env
EMAIL_PASSWORD=...
```

---

# 💬 Slack Integration

Uses Slack Incoming Webhooks.

Webhook stored securely in:

```env
SLACK_WEBHOOK_URL=...
```

---

# 🔐 Secret Management

Sensitive credentials are stored in `.env` and should never be committed.

Kubernetes secrets are created from `.env` using:

```bash
kubectl create secret generic agentic-arxiv-secrets \
  --from-env-file=.env \
  -n agentic-arxiv
```

---

# 🧪 Run Tests

```bash
pytest -v
```

Current status:

```text
26 passed
```

Test coverage includes:

- relevance scoring
- report generation
- RAG evaluator
- text chunking
- trend analysis
- reviewer agent
- topic clustering
- Docker files
- Kubernetes manifests
- config safety

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
- Citation-aware RAG
- PDF ingestion pipelines
- Semantic retrieval
- AI workflow observability
- Autonomous scheduling
- Dockerized AI deployment
- Kubernetes orchestration
- Containerized GenAI systems
- Research intelligence systems
- AI + Quant Finance integration

---

### 🛠️ Major Build Steps

#### Step 1: Define Project Scope and MVP

- Step 1A: Select Project Direction
- Step 1B: Select AI/ML + Quant Finance Coverage
- Step 1C: Define MVP Goals
- Step 1D: Select Initial arXiv Categories

#### Step 2: Create GitHub-Ready Folder Structure

- Step 2A: Create Root Project Folder
- Step 2B: Create App Subfolders
- Step 2C: Add Python Package Files
- Step 2D: Add Base Project Files

#### Step 3: Add Dependencies and Config Files

- Step 3A: Add Initial Dependencies
- Step 3B: Add `.gitignore`
- Step 3C: Add `config.yaml`

#### Step 4: Add arXiv Paper Collector

- Step 4A: Create arXiv Client Module
- Step 4B: Build Category Query Logic
- Step 4C: Fetch Recent Papers
- Step 4D: Handle arXiv Rate Limits

#### Step 5: Add Keyword Relevance Scoring Agent

- Step 5A: Create Relevance Agent
- Step 5B: Match Interest Keywords
- Step 5C: Compute Relevance Score
- Step 5D: Sort Papers by Relevance

#### Step 6: Add SQLite Persistence

- Step 6A: Create Storage Module
- Step 6B: Initialize Database
- Step 6C: Save Papers
- Step 6D: Fetch Top Papers

#### Step 7: Add Ollama + Mock Summarization

- Step 7A: Create Summarizer Agent
- Step 7B: Add Mock Summaries
- Step 7C: Add Ollama Integration
- Step 7D: Add Laptop-Safe LLM Settings
- Step 7E: Add Fallback Summaries

#### Step 8: Add LangGraph Workflow Orchestration

- Step 8A: Install LangGraph
- Step 8B: Create Research Workflow Graph
- Step 8C: Add Workflow State
- Step 8D: Add Workflow Nodes
- Step 8E: Update `main.py`

#### Step 9: Add Observability and Timing Metrics

- Step 9A: Create Utility Module
- Step 9B: Add `timed_node` Decorator
- Step 9C: Add Total Workflow Timing

#### Step 10: Generate Markdown Research Reports

- Step 10A: Create Report Generator
- Step 10B: Save Timestamped Reports
- Step 10C: Add LLM Summaries to Reports

#### Step 11: Add Streamlit Dashboard

- Step 11A: Create Streamlit App
- Step 11B: Load Papers from SQLite
- Step 11C: Add Filters and Metrics
- Step 11D: Add Search and Charts
- Step 11E: Add Paper Cards and Expanders

#### Step 12: Add Testing and GitHub Actions CI

- Step 12A: Add Pytest Tests
- Step 12B: Test Relevance Scoring
- Step 12C: Test Report Generation
- Step 12D: Add GitHub Actions Workflow

#### Step 13: Add Vector Database + RAG

- Step 13A: Install ChromaDB + SentenceTransformers
- Step 13B: Create Vector Store Module
- Step 13C: Add Embedding Model
- Step 13D: Add Semantic Search
- Step 13E: Index Papers in LangGraph

#### Step 14: Add RAG Question Answering

- Step 14A: Create RAG Query Script
- Step 14B: Create RAG Answer Agent
- Step 14C: Add Semantic Retrieval
- Step 14D: Add Ollama-Based Answer Generation
- Step 14E: Add Streamlit RAG QA Tab

#### Step 15: Add PDF Ingestion + Chunked Retrieval

- Step 15A: Install PDF Dependencies
- Step 15B: Download arXiv PDFs
- Step 15C: Extract PDF Text
- Step 15D: Chunk Full Papers
- Step 15E: Index Chunks into ChromaDB
- Step 15F: Add PDF Ingestion Node to LangGraph

#### Step 16: Add Trend Analytics

- Step 16A: Install Trend Dependencies
- Step 16B: Create Trend Analysis Module
- Step 16C: Add TF-IDF Extraction
- Step 16D: Add Keyword Frequency Analysis
- Step 16E: Add Trend Analytics Dashboard Tab

#### Step 17: Add Autonomous Scheduler

- Step 17A: Install Scheduler Dependency
- Step 17B: Create Scheduler Script
- Step 17C: Add Configurable Scheduling
- Step 17D: Add Live Config Reloads
- Step 17E: Add Streamlit Scheduler Controls

#### Step 18: Add Email Digest

- Step 18A: Add Email Config
- Step 18B: Store Email Password in `.env`
- Step 18C: Create Email Notification Module
- Step 18D: Send Reports Automatically
- Step 18E: Integrate Email into Workflow

#### Step 19: Add Slack Notifications

- Step 19A: Add Slack Config
- Step 19B: Store Slack Webhook in `.env`
- Step 19C: Create Slack Notification Module
- Step 19D: Add Slack Workflow Integration
- Step 19E: Add Streamlit Slack Controls

#### Step 20: Add Topic Clustering

- Step 20A: Install UMAP + HDBSCAN
- Step 20B: Create Topic Clustering Module
- Step 20C: Generate Embeddings
- Step 20D: Reduce Dimensions with UMAP
- Step 20E: Cluster Papers with HDBSCAN
- Step 20F: Add Topic Clusters Dashboard Tab

#### Step 21: Add RAG Evaluation Metrics

- Step 21A: Create Evaluation Module
- Step 21B: Evaluate Retrieval Results
- Step 21C: Evaluate Grounding Overlap
- Step 21D: Add Evaluation Metrics to Streamlit

#### Step 22: Add Multi-Agent Reviewer System

- Step 22A: Create Reviewer Agent
- Step 22B: Add Critic Review
- Step 22C: Add Implementation Review
- Step 22D: Add Quant Relevance Review
- Step 22E: Add Limitations Review
- Step 22F: Store Reviews in SQLite
- Step 22G: Add Reviewer Node to LangGraph
- Step 22H: Display Reviews in Streamlit

#### Step 23: Add Citation-Aware RAG

- Step 23A: Add Citation Formatting
- Step 23B: Add Inline Citations like `[S1]`
- Step 23C: Display Citation Sources in Streamlit
- Step 23D: Add Chunk Index References

#### Step 24: Add Historical Trend Tracking

- Step 24A: Create Trend Snapshot Table
- Step 24B: Save Historical Trend Snapshots
- Step 24C: Add Trend Evolution Charts
- Step 24D: Add Historical Trend DataFrames

#### Step 25: Add Secret Management Cleanup

- Step 25A: Move Secrets into `.env`
- Step 25B: Remove Webhooks from `config.yaml`
- Step 25C: Update `.gitignore`
- Step 25D: Clean Git History
- Step 25E: Prevent Future Secret Leaks

#### Step 26: Add Docker Deployment

- Step 26A: Add `.dockerignore`
- Step 26B: Create Dockerfile
- Step 26C: Create `docker-compose.yml`
- Step 26D: Add persistent volumes
- Step 26E: Run Streamlit inside Docker
- Step 26F: Run workflow inside Docker
- Step 26G: Run scheduler inside Docker

#### Step 27: Expand Automated Testing

- Step 27A: Add RAG Evaluator Tests
- Step 27B: Add Text Chunker Tests
- Step 27C: Add Trend Analysis Tests
- Step 27D: Add Reviewer Agent Tests
- Step 27E: Add Topic Clustering Tests
- Step 27F: Add Docker File Tests
- Step 27G: Add Kubernetes Manifest Tests
- Step 27H: Add Config Safety Tests
- Step 27I: Run Full Test Suite
- Step 27J: Confirm `26 passed`

#### Step 28: Add Multi-Container Docker Architecture

- Step 28A: Add Dashboard Container
- Step 28B: Add Scheduler Container
- Step 28C: Add Ollama Container
- Step 28D: Add ChromaDB Container
- Step 28E: Add Shared Volumes
- Step 28F: Add Container Environment Variables

#### Step 29: Add Kubernetes Deployment

- Step 29A: Enable Kubernetes in Docker Desktop
- Step 29B: Add Kubernetes Namespace
- Step 29C: Add Kubernetes ConfigMap
- Step 29D: Create Kubernetes Secrets from `.env`
- Step 29E: Deploy ChromaDB Service
- Step 29F: Deploy Ollama Service
- Step 29G: Pull Ollama Model in Kubernetes
- Step 29H: Deploy Streamlit App Service
- Step 29I: Add Port Forwarding
- Step 29J: Run Workflow Inside Kubernetes
- Step 29K: Validate Kubernetes Dashboard Flow

---

# 🔮 Future Improvements

- Cloud Kubernetes deployment
- Helm chart packaging
- CI/CD deployment pipeline
- Persistent production storage classes
- GPU-backed Ollama deployment
- Streamlit Cloud deployment
- Multi-agent reviewer collaboration
- Trend evolution over time
- Citation graph analysis
- Research recommendation engine
- Fine-tuned reranking models

---

# 📄 License

MIT License
