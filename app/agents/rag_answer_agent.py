from typing import Dict, Any

import ollama


def build_context(results: Dict[str, Any]) -> str:
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_blocks = []

    for idx, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1,
    ):
        context_blocks.append(
    f"""
Source {idx}
Citation ID: [S{idx}]
Title: {metadata.get("title", "")}
Published: {metadata.get("published", "")}
Relevance Score: {metadata.get("relevance_score", "")}
Chunk Index: {metadata.get("chunk_index", "")}
Paper ID: {metadata.get("paper_id", "")}

Context:
{document}
"""
)

    return "\n---\n".join(context_blocks)


def generate_rag_answer(
    question: str,
    results: Dict[str, Any],
    use_ollama: bool = True,
    model: str = "llama3.2:1b",
) -> str:
    context = build_context(results)

    if not use_ollama:
        return (
            "Ollama is disabled. Here is the retrieved context:\n\n"
            + context[:4000]
        )

    prompt = f"""
You are a research assistant for AI/ML and quant finance papers.

Answer the user's question using only the retrieved paper context.

Question:
{question}

Retrieved Context:
{context}

Return:
1. Direct answer with inline citations like [S1], [S2]
2. Supporting evidence table with Citation ID, paper title, and chunk index
3. Practical implementation ideas
4. Limitations or missing evidence
"""

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "num_ctx": 2048,
                "num_predict": 500,
                "temperature": 0.2,
            },
            keep_alive=0,
        )

        return response["message"]["content"]

    except Exception as e:
        return (
            f"Ollama RAG answer failed: {e}\n\n"
            f"Retrieved context:\n\n{context[:4000]}"
        )