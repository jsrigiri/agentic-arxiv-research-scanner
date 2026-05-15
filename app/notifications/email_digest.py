import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv
from rich import print


load_dotenv()


def send_email_digest(
    config: dict,
    report_path: str,
) -> bool:

    email_config = config.get("email", {})

    if not email_config.get("enabled", False):
        print("[bold yellow]Email digest disabled[/bold yellow]")
        return False

    smtp_server = email_config["smtp_server"]
    smtp_port = email_config["smtp_port"]

    sender_email = email_config["sender_email"]
    recipient_email = email_config["recipient_email"]

    subject_prefix = email_config.get(
        "subject_prefix",
        "Daily arXiv Research Brief",
    )

    password = os.getenv("EMAIL_PASSWORD")

    if not password:
        print(
            "[bold red]EMAIL_PASSWORD not found in .env[/bold red]"
        )
        return False

    report_file = Path(report_path)

    if not report_file.exists():
        print(
            f"[bold red]Report not found:[/bold red] {report_path}"
        )
        return False

    report_content = report_file.read_text(
        encoding="utf-8"
    )

    subject = f"{subject_prefix} - {report_file.stem}"

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    body = MIMEText(
        report_content,
        "plain",
    )

    message.attach(body)

    try:

        server = smtplib.SMTP(
            smtp_server,
            smtp_port,
        )

        server.starttls()

        server.login(
            sender_email,
            password,
        )

        server.sendmail(
            sender_email,
            recipient_email,
            message.as_string(),
        )

        server.quit()

        print(
            "[bold green]Email digest sent successfully[/bold green]"
        )

        return True

    except Exception as e:

        print(
            f"[bold red]Email sending failed:[/bold red] {e}"
        )

        return False