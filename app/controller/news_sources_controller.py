from flask_login import current_user
import requests
from app.settings import API_KEY


def get_all_news_sources():
    users_news_sources = current_user.news_sources
    if len(users_news_sources) == 0:
        return "No news sources selected! Please select them under account settings."

    # headlines_list = []
    # if "BBC" in users_news_sources:
    #     r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}')
    #     data = r.json()
    #     for article in data['articles']:
    #         headlines_list.append(f"BBC News: <a href={article['url']}>{article['title']}</a>")
    # if "Reuters" in users_news_sources:
    #     r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=reuters&apiKey={API_KEY}')
    #     data = r.json()
    #     for article in data['articles']:
    #         headlines_list.append(f"Reuters: <a href={article['url']}>{article['title']}</a>")

    headlines = []
    images = []
    descriptions = []
    links = []
    if "BBC" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            headlines.append(article['title'])
            images.append(article['urlToImage'])
            descriptions.append(article['description'])
            links.append(article['url'])

    if "Reuters" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=reuters&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            headlines.append(article['title'])
            images.append(article['urlToImage'])
            descriptions.append(article['description'])
            links.append(article['url'])

    news_data = zip(headlines, images, descriptions, links)
    return news_data


def add_news_source_to_user(news_source):
    pass

def remove_news_source_from_user(news_source):
    pass

