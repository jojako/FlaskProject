<<<<<<< HEAD
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user
=======
import json

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user
>>>>>>> 47272c2dc4de4f9ce303f3e727bec97be6126c32
from app.controller.news_sources_controller import get_all_news_sources

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/account')
@login_required
def profile():
    from app.controller.news_sources_controller import list_all_news_sources
    news = list_all_news_sources()
    return render_template('profile.html', news_list=news)


@bp_user.post('/account')
@login_required
def save_selections():
    from app.controller.news_sources_controller import delete_all_news_sources_from_user
    delete_all_news_sources_from_user(current_user)

    selections = request.form.getlist('news_checkbox')
    from app.controller.news_sources_controller import add_news_source
    add_news_source(current_user, selections)
    return redirect(url_for('bp_user.profile'))


@bp_user.get('/newsfeed')
@login_required
def newsfeed():
    news = get_all_news_sources()
    return render_template('newsfeed.html', news=news)


@bp_user.get('/sign-out')
@login_required
def signout():
    logout_user()
    return redirect(url_for('bp_open.index'))
