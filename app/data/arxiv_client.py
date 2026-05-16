import time
from typing import List, Dict, Any

import arxiv


def build_query(categories: List[str]) -> str:
    return " OR ".join([f"cat:{category}" for category in categories])


def fetch_recent_papers(
    categories: List[str],
    max_results: int = 10,
) -> List[Dict[str, Any]]:
    query = build_query(categories)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    client = arxiv.Client(
        page_size=max_results,
        delay_seconds=10.0,
        num_retries=1,
    )

    papers = []

    for result in client.results(search):
        papers.append(
            {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary,
                "published": result.published.isoformat(),
                "updated": result.updated.isoformat(),
                "entry_id": result.entry_id,
                "pdf_url": result.pdf_url,
                "categories": result.categories,
            }
        )

        time.sleep(1)

    return papers