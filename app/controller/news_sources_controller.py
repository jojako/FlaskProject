from flask_login import current_user
import requests
from app.settings import API_KEY


def get_all_news_sources():
    users_news_sources = current_user.news_sources
    if len(users_news_sources) == 0:
        return "No news sources selected! Please select them under account settings."

    art_headline = []
    art_image = []
    art_desc = []
    art_link = []
    if "BBC" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    news_data = zip(art_headline, art_desc, art_image, art_link)

    return news_data


def add_news_source_to_user(news_source):
    pass


def remove_news_source_from_user(news_source):
    pass

