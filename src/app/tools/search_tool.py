from langchain_tavily import TavilySearch
from langchain.tools import tool
from app.config.settings import TAVILY_API_KEY

# @tool
# def general_search(query:str):
#     """Search for general information"""
#     print("General Search tool loaded")

#     return TavilySearch(
#         max_results=5,
#         topic="general"
#     ).run(query)


@tool
def news_search(query: str):
    """Search for news"""
    print("News Search tool loaded")
    return TavilySearch(tavily_api_key=TAVILY_API_KEY,max_results=5, topic="news").run(query)
