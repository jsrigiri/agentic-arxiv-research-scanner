from pathlib import Path

import yaml
import subprocess


def test_config_has_required_sections():
    config_path = Path("config.yaml")
    assert config_path.exists()

    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    required_sections = [
        "project",
        "arxiv",
        "interests",
        "llm",
        "pdf",
        "scheduler",
        "email",
        "slack",
    ]

    for section in required_sections:
        assert section in config


def test_config_does_not_contain_slack_webhook_secret():
    config_text = Path("config.yaml").read_text(encoding="utf-8")

    assert "hooks.slack.com/services" not in config_text


def test_env_file_not_tracked_by_git():
    result = subprocess.run(
        ["git", "ls-files", ".env"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == ""