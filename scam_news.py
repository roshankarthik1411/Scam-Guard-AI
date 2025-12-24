from typing import List, Dict

from tavily import TavilyClient
from config import TAVILY_API_KEY


# ---- Safety check (fail fast, clear error) ----
if not TAVILY_API_KEY:
    raise RuntimeError(
        "TAVILY_API_KEY is not set. Please add it to your .env file."
    )


# ---- Initialize Tavily client once ----
client = TavilyClient(api_key=TAVILY_API_KEY)


def fetch_scam_news(query: str, max_results: int = 5) -> List[Dict]:
    """
    Fetch recent scam-related news/articles from the internet.

    Args:
        query (str): Search query (intent or user message)
        max_results (int): Number of results to return

    Returns:
        List[Dict]: List of news result objects
    """

    if not query or not query.strip():
        return []

    response = client.search(
        query=f"{query} scam",
        max_results=max_results,
        include_answer=False,
        include_raw_content=False,
    )

    return response.get("results", [])
