from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user


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
    selections = request.form.getlist('news_checkbox')
    if selections == None:
        return redirect(url_for('bp_user.profile'))

    from app.controller.news_sources_controller import delete_all_news_sources_from_user
    delete_all_news_sources_from_user(current_user)

    from app.controller.news_sources_controller import add_news_source
    add_news_source(current_user, selections)
    return redirect(url_for('bp_user.profile'))


@bp_user.get('/newsfeed')
@login_required
def newsfeed():
    if not current_user.news_sources:
        return render_template('newsfeed.html', news='none')

    from app.controller.news_sources_controller import get_all_news_sources
    news = get_all_news_sources()

    return render_template('newsfeed.html', news=news)


@bp_user.get('/sign-out')
@login_required
def signout():
    logout_user()
    return redirect(url_for('bp_open.index'))
