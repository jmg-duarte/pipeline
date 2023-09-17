import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

def get_top_headlines(query, sources=None, language=None, country=None, category=None, page_size=None, page=None):
    return api.get_top_headlines(query, sources, language, country, category, page_size, page)

def get_everything(query, sources=None, language=None, country=None, category=None, page_size=None, page=None, domains=None, exclude_domains=None):
    return api.get_everything(query, sources, language, country, category, page_size, page, domains, exclude_domains)

