import time
import yaml

from rich import print

from app.workflows.research_graph import build_research_graph


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:

    # -----------------------------
    # Load configuration
    # -----------------------------
    config = load_config()

    # -----------------------------
    # Build LangGraph workflow
    # -----------------------------
    graph = build_research_graph()

    # -----------------------------
    # Initial workflow state
    # -----------------------------
    initial_state = {
        "config": config,
        "papers": [],
        "scored_papers": [],
        "summarized_papers": [],
        "top_papers": [],
        "report_path": "",
    }

    print("\n[bold yellow]Running Agentic Research Workflow...[/bold yellow]")

    # -----------------------------
    # Start workflow timer
    # -----------------------------
    workflow_start = time.time()

    try:

        # -----------------------------
        # Run workflow graph
        # -----------------------------
        final_state = graph.invoke(initial_state)

    except Exception as e:

        print(f"\n[bold red]Workflow failed:[/bold red] {e}")
        return

    # -----------------------------
    # Total workflow timing
    # -----------------------------
    workflow_elapsed = time.time() - workflow_start

    print("\n[bold green]Workflow completed successfully[/bold green]")

    print(
        f"\n[bold green]Total Workflow Time:[/bold green] "
        f"{workflow_elapsed:.2f}s"
    )

    # -----------------------------
    # Generated report path
    # -----------------------------
    print(
        f"\n[bold cyan]Generated Report:[/bold cyan] "
        f"{final_state['report_path']}"
    )

    # -----------------------------
    # Print top papers
    # -----------------------------
    print("\n[bold magenta]Top Papers[/bold magenta]")

    for idx, paper in enumerate(final_state["top_papers"], start=1):

        (
            title,
            published,
            score,
            matched,
            url,
            llm_summary,
            summary_method,
        ) = paper

        print(f"\n[bold cyan]{idx}. {title}[/bold cyan]")

        print(f"Published: {published}")
        print(f"Relevance Score: {score}/10")
        print(f"Matched Keywords: {matched}")
        print(f"Summary Method: {summary_method}")
        print(f"URL: {url}")

        print(f"\n[bold yellow]Summary[/bold yellow]")

        print(llm_summary)


if __name__ == "__main__":
    main()