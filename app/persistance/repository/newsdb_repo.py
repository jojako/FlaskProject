from app.persistance.model import News


def get_all_news_source():
    return News.all()