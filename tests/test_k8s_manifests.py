from pathlib import Path

import yaml


K8S_DIR = Path("k8s")


def load_yaml_documents(path: Path):
    return list(yaml.safe_load_all(path.read_text(encoding="utf-8")))


def test_k8s_directory_exists():
    assert K8S_DIR.exists()


def test_namespace_manifest_exists():
    path = K8S_DIR / "namespace.yaml"
    assert path.exists()

    docs = load_yaml_documents(path)
    assert docs[0]["kind"] == "Namespace"
    assert docs[0]["metadata"]["name"] == "agentic-arxiv"


def test_configmap_contains_required_sections():
    path = K8S_DIR / "configmap.yaml"
    assert path.exists()

    docs = load_yaml_documents(path)
    configmap = docs[0]

    assert configmap["kind"] == "ConfigMap"

    config_text = configmap["data"]["config.yaml"]
    parsed_config = yaml.safe_load(config_text)

    for section in [
        "project",
        "arxiv",
        "interests",
        "llm",
        "pdf",
        "scheduler",
        "email",
        "slack",
    ]:
        assert section in parsed_config


def test_chroma_service_uses_safe_name():
    path = K8S_DIR / "chroma-deployment.yaml"
    assert path.exists()

    docs = load_yaml_documents(path)

    service_docs = [
        doc for doc in docs
        if doc and doc.get("kind") == "Service"
    ]

    service_names = [
        doc["metadata"]["name"]
        for doc in service_docs
    ]

    assert "chromadb" in service_names
    assert "chroma" not in service_names


def test_app_deployment_has_chroma_and_ollama_env():
    path = K8S_DIR / "app-deployment.yaml"
    assert path.exists()

    docs = load_yaml_documents(path)

    deployment = [
        doc for doc in docs
        if doc and doc.get("kind") == "Deployment"
    ][0]

    container = deployment["spec"]["template"]["spec"]["containers"][0]

    env = {
        item["name"]: item["value"]
        for item in container.get("env", [])
        if "value" in item
    }

    assert env["OLLAMA_HOST"] == "http://ollama:11434"
    assert env["CHROMA_HOST"] == "chromadb"
    assert env["CHROMA_PORT"] == "8000"