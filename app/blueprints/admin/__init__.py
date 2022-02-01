from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user
from bson.objectid import ObjectId

import app
from app.controller import user_controller

bp_admin = Blueprint('bp_admin', __name__)


@bp_admin.before_request
def before_request():
    if not current_user.is_authenticated or not current_user.has_access('admin'):
        return redirect(url_for('bp_open.index'))


@bp_admin.get('/edit-users')
def edit_users():
    users = user_controller.find_all_users()
    return render_template('edit_users.html', userlist=users)


@bp_admin.post('/edit-users')
def edit_users_post():
    if request.method == 'POST':
        for user_id in request.form.getlist('user_checkbox'):
            print(ObjectId(user_id))
            app.controller.user_controller.delete_user(ObjectId(user_id))
        return redirect(url_for('bp_admin.edit_users'))
    return 'Could not delete selected users'


@bp_admin.get('/edit-news')
def edit_news_sources():
    return render_template('edit_news.html')


