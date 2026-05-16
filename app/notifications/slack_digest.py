from pathlib import Path

import requests
from rich import print

import os
from dotenv import load_dotenv


load_dotenv()


def send_slack_digest(
    config: dict,
    report_path: str,
) -> bool:

    slack_config = config.get("slack", {})

    if not slack_config.get("enabled", False):
        print("[bold yellow]Slack digest disabled[/bold yellow]")
        return False
    
    webhook_url = os.getenv(
        "SLACK_WEBHOOK_URL",
        ""
    )

    if not webhook_url:
        print(
            "[bold red]Slack webhook URL missing[/bold red]"
        )
        return False

    report_file = Path(report_path)

    if not report_file.exists():
        print(
            f"[bold red]Report not found:[/bold red] "
            f"{report_path}"
        )
        return False

    report_content = report_file.read_text(
        encoding="utf-8"
    )

    truncated_content = report_content[:3500]

    payload = {
        "text": (
            "📚 *Daily arXiv Research Brief*\n\n"
            f"```{truncated_content}```"
        )
    }

    try:

        response = requests.post(
            webhook_url,
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

        print(
            "[bold green]"
            "Slack digest sent successfully"
            "[/bold green]"
        )

        return True

    except Exception as e:

        print(
            f"[bold red]"
            f"Slack sending failed:"
            f"[/bold red] {e}"
        )

        return False