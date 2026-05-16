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

        title = paper[0]
        published = paper[1]
        score = paper[2]
        matched = paper[3]
        url = paper[4]
        llm_summary = paper[5]
        summary_method = paper[6]

        critic_review = paper[7] if len(paper) > 7 else ""
        implementation_review = paper[8] if len(paper) > 8 else ""
        quant_relevance_review = paper[9] if len(paper) > 9 else ""
        limitations_review = paper[10] if len(paper) > 10 else ""
        review_method = paper[11] if len(paper) > 11 else "unknown"

        lines.append(f"## {idx}. {title}\n")

        lines.append(f"**Published:** {published}\n")
        lines.append(f"**Relevance Score:** {score}/10\n")
        lines.append(f"**Summary Method:** {summary_method}\n")
        lines.append(f"**Matched Keywords:** {matched}\n")
        lines.append(f"**URL:** {url}\n")

        lines.append("\n### Summary\n")
        lines.append(f"{llm_summary}\n")

        lines.append("\n### Multi-Agent Review\n")
        lines.append(f"**Review Method:** {review_method}\n")

        lines.append("\n#### Critic Review\n")
        lines.append(f"{critic_review}\n")

        lines.append("\n#### Implementation Review\n")
        lines.append(f"{implementation_review}\n")

        lines.append("\n#### Quant Relevance Review\n")
        lines.append(f"{quant_relevance_review}\n")

        lines.append("\n#### Limitations Review\n")
        lines.append(f"{limitations_review}\n")

        if len(paper) >= 12:
            (
                critic_review,
                implementation_review,
                quant_relevance_review,
                limitations_review,
                review_method,
            ) = paper[7:12]

            lines.append("\n### Multi-Agent Review\n")
            lines.append(f"**Review Method:** {review_method}\n")

            lines.append("\n#### Critic Review\n")
            lines.append(f"{critic_review}\n")

            lines.append("\n#### Implementation Review\n")
            lines.append(f"{implementation_review}\n")

            lines.append("\n#### Quant Relevance Review\n")
            lines.append(f"{quant_relevance_review}\n")

            lines.append("\n#### Limitations Review\n")
            lines.append(f"{limitations_review}\n")

        lines.append("\n---\n")

    report_content = "\n".join(lines)

    report_filename = (
        REPORTS_DIR
        / f"research_brief_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )

    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    return str(report_filename)