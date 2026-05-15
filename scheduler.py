import time
from datetime import datetime
from pathlib import Path

import schedule
from rich import print
from ruamel.yaml import YAML

from app.workflows.research_graph import build_research_graph


CONFIG_PATH = Path("config.yaml")
CONFIG_RELOAD_SECONDS = 30

yaml_handler = YAML()
yaml_handler.preserve_quotes = True


def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml_handler.load(f)


def normalize_run_time(run_time) -> str:
    if isinstance(run_time, str):
        return run_time

    if hasattr(run_time, "strftime"):
        return run_time.strftime("%H:%M")

    if isinstance(run_time, int):
        run_time_str = str(run_time).zfill(4)
        return f"{run_time_str[:2]}:{run_time_str[2:]}"

    return "09:00"


def get_scheduler_signature(config: dict) -> tuple:
    scheduler_config = config.get("scheduler", {})

    enabled = bool(scheduler_config.get("enabled", False))
    run_time = normalize_run_time(
        scheduler_config.get("run_time", "09:00")
    )

    return enabled, run_time


def run_research_workflow() -> None:
    print(
        f"\n[bold yellow]Running scheduled workflow at "
        f"{datetime.now()}[/bold yellow]"
    )

    config = load_config()
    graph = build_research_graph()

    initial_state = {
        "config": config,
        "papers": [],
        "scored_papers": [],
        "summarized_papers": [],
        "top_papers": [],
        "report_path": "",
    }

    try:
        final_state = graph.invoke(initial_state)

        print("\n[bold green]Workflow completed successfully[/bold green]")
        print(
            f"[bold cyan]Generated Report:[/bold cyan] "
            f"{final_state['report_path']}"
        )

    except Exception as e:
        print(f"\n[bold red]Scheduled workflow failed:[/bold red] {e}")


def apply_schedule(config: dict) -> tuple:
    schedule.clear()

    enabled, run_time = get_scheduler_signature(config)

    if enabled:
        schedule.every().day.at(run_time).do(run_research_workflow)
        print(f"[bold cyan]Daily workflow scheduled for {run_time}[/bold cyan]")
    else:
        print("[bold yellow]Scheduler is disabled in config.yaml[/bold yellow]")

    return enabled, run_time


def main() -> None:
    print("\n[bold green]Autonomous Research Scheduler Started[/bold green]")
    print(
        f"[bold blue]Watching config.yaml every "
        f"{CONFIG_RELOAD_SECONDS}s[/bold blue]"
    )

    config = load_config()
    current_signature = apply_schedule(config)

    last_reload = time.time()

    while True:
        schedule.run_pending()

        now = time.time()

        if now - last_reload >= CONFIG_RELOAD_SECONDS:
            try:
                new_config = load_config()
                new_signature = get_scheduler_signature(new_config)

                if new_signature != current_signature:
                    print(
                        "\n[bold yellow]Scheduler config changed. "
                        "Reloading schedule...[/bold yellow]"
                    )

                    current_signature = apply_schedule(new_config)

            except Exception as e:
                print(f"[bold red]Config reload failed:[/bold red] {e}")

            last_reload = now

        time.sleep(5)


if __name__ == "__main__":
    main()