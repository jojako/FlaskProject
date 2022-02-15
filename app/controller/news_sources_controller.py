from flask_login import current_user
import requests

import app.persistance.db
from app.settings import API_KEY
from app.persistance.repository import newsdb_repo


def get_all_news_sources():
    users_news_sources = current_user.news_sources

    if users_news_sources == None:
        return None

    art_headline = []
    art_image = []
    art_desc = []
    art_link = []
    if "THE-WASHINGTON-POST" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=the-washington-post&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    if "BBC" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    if "CNN" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    if "REUTERS" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=reuters-news&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    if "GOTEBORGS-POSTEN" in users_news_sources:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?sources=goteborgs-posten&apiKey={API_KEY}')
        data = r.json()
        for article in data['articles']:
            art_headline.append(article['title'])
            art_image.append(article['urlToImage'])
            art_desc.append(article['description'])
            art_link.append(article['url'])

    news_data = zip(art_headline, art_desc, art_image, art_link)
    return news_data


def list_all_news_sources():
    return newsdb_repo.get_all_news_source()


def deactivate_news_source(name):
    return newsdb_repo.deactivate_news_source(name)


def activate_news_source(name):
    return newsdb_repo.activate_news_source(name)


def delete_all_news_sources_from_user(user):
    return newsdb_repo.delete_all_news_sources(user)


def add_news_source(user, news_source):
    return newsdb_repo.add_news_source(user, news_source)
