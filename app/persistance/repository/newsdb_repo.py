from app.persistance.model import News


def get_all_news_source():
    return News.all()

def get_news_source_by_name(name):
    return News.find(name=name).first_or_none()

def deactivate_news_source(name):
    news_source = get_news_source_by_name(name)
    news_source.is_available = "false"
    news_source.save()