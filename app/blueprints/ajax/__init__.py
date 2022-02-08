import json

from flask import Blueprint
from app.controller.news_sources_controller import get_all_news_sources

bp_ajax = Blueprint('bp_ajax', __name__)


@bp_ajax.get('/get_feed')
def fetch_feed():
    news = get_all_news_sources()
    return news
