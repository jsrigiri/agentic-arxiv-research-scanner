import time
from functools import wraps

from rich import print


def timed_node(node_name: str):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            print(f"\n[bold blue]Starting node:[/bold blue] {node_name}")

            start = time.time()

            result = func(*args, **kwargs)

            elapsed = time.time() - start

            print(
                f"[bold green]Completed node:[/bold green] "
                f"{node_name} "
                f"({elapsed:.2f}s)"
            )

            return result

        return wrapper

    return decorator