import asyncio
from typing import Optional
import httpx

BASE_URL = "https://export.arxiv.org/api/query"

class ArxivClient:
    
    def __init__(self):
        self.client = httpx.AsyncClient()
    
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def search_arxiv(self, query: str, max_results: Optional[int] = 10):
        """Searches the arXiv API for papers.

        Args:
            query: The search query string (e.g., "cat:cs.AI").
            max_results: The maximum number of results to return.

        Returns:
            The raw XML response content as a string, or None if an error occurs.
        """
        params = {
            "search_query": query,
            "max_results": max_results
        }
        try:
            response = await self.client.get(BASE_URL, params=params, timeout=10.0)
            response.raise_for_status()
            return response.text
        except httpx.TimeoutException:
            print("Request timed out.")
            return None
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code}")
            return None


async def fetch_recent_ai_papers():
    """Solution for Exercise 1"""
    async with ArxivClient() as arxiv_client:
        response_content = await arxiv_client.search_arxiv(
            query="cat:cs.AI",
            max_results=10
        )
        if response_content:
            print("Fetched recent AI papers successfully.")
            # print(response_content) # Uncomment to see full response
        else:
            print("Failed to fetch recent AI papers.")


if __name__ == "__main__":
    # To run Exercise 1:
    # asyncio.run(fetch_recent_ai_papers())

    # To run Exercise 2:
    print("--- Running Exercise 2 ---")
    # async def run_exercise_2():
    #     async with ArxivClient() as arxiv_client:
    #         response_content = await arxiv_client.search_arxiv(query="cat:cs.CV", max_results=5)
    #         if response_content:
    #             print(response_content[:1000] + "...")
    #         else:
    #             print("Failed to search arXiv for 'cat:cs.CV'.")
    #
    # asyncio.run(run_exercise_2())

    obj = ArxivClient()
    response = asyncio.run(obj.search_arxiv(query="cat:cs.CV", max_results=5))
    print(response)
