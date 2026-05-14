import yaml

from rich import print

from app.data.vector_store import semantic_search
from app.agents.rag_answer_agent import generate_rag_answer


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:

    config = load_config()

    use_ollama = config["llm"]["use_ollama"]
    model = config["llm"]["model"]

    question = input("\nAsk a research question: ")

    print("\n[bold yellow]Running semantic retrieval...[/bold yellow]")

    results = semantic_search(
        query=question,
        top_k=5,
    )

    print("[bold green]Retrieved relevant papers[/bold green]")

    answer = generate_rag_answer(
        question=question,
        results=results,
        use_ollama=use_ollama,
        model=model,
    )

    print("\n[bold cyan]RAG Answer[/bold cyan]\n")

    print(answer)

    print("\n[bold magenta]Retrieved Papers[/bold magenta]")

    ids = results["ids"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for idx, (doc_id, metadata, distance) in enumerate(
        zip(ids, metadatas, distances),
        start=1,
    ):
        print(f"\n[bold cyan]{idx}. {metadata['title']}[/bold cyan]")
        print(f"Published: {metadata['published']}")
        print(f"Relevance Score: {metadata['relevance_score']}")
        print(f"Summary Method: {metadata['summary_method']}")
        print(f"Distance: {distance:.4f}")
        print(f"URL: {doc_id}")


if __name__ == "__main__":
    main()