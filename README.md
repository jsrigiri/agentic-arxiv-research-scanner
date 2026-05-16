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
