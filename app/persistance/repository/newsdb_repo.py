from app.persistance.model import News


def get_all_news_source():
    return News.all()


def get_news_source_by_name(name):
    return News.find(name=name).first_or_none()


def delete_all_news_sources(user):
    user.delete_field('news_sources')
    user.news_sources = [None]


def add_news_source(user, news_source):
    user.news_sources = news_source
    user.save()

def deactivate_news_source(name):
    news_source = get_news_source_by_name(name)
    news_source.is_available = False
    news_source.save()