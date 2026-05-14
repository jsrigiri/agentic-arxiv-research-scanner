from datetime import datetime
from pathlib import Path
from typing import List, Tuple


REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def generate_markdown_report(
    papers: List[Tuple],
) -> str:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []

    lines.append("# Daily arXiv Research Brief\n")
    lines.append(f"Generated: {timestamp}\n")
    lines.append("---\n")

    for idx, paper in enumerate(papers, start=1):

        (
            title,
            published,
            score,
            matched,
            url,
            llm_summary,
            summary_method,
        ) = paper

        lines.append(f"## {idx}. {title}\n")

        lines.append(f"**Published:** {published}\n")
        lines.append(f"**Relevance Score:** {score}/10\n")
        lines.append(f"**Summary Method:** {summary_method}\n")
        lines.append(f"**Matched Keywords:** {matched}\n")
        lines.append(f"**URL:** {url}\n")

        lines.append("\n### Summary\n")
        lines.append(f"{llm_summary}\n")

        lines.append("\n---\n")

    report_content = "\n".join(lines)

    report_filename = (
        REPORTS_DIR
        / f"research_brief_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )

    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    return str(report_filename)