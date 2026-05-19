from pathlib import Path

import yaml


def test_dockerfile_exists_and_runs_streamlit():
    dockerfile = Path("Dockerfile")
    assert dockerfile.exists()

    text = dockerfile.read_text(encoding="utf-8")

    assert "FROM python:3.11-slim" in text
    assert "streamlit" in text
    assert "8501" in text


def test_docker_compose_has_expected_services():
    compose_path = Path("docker-compose.yml")
    assert compose_path.exists()

    compose = yaml.safe_load(compose_path.read_text(encoding="utf-8"))

    services = compose["services"]

    assert "agentic-arxiv-app" in services
    assert "agentic-arxiv-scheduler" in services
    assert "ollama" in services
    assert "chroma" in services


def test_dockerignore_excludes_secrets_and_data():
    dockerignore = Path(".dockerignore")
    assert dockerignore.exists()

    text = dockerignore.read_text(encoding="utf-8")

    assert ".env" in text
    assert "chroma_db/" in text
    assert "data/pdfs/" in text
    assert "reports/" in text