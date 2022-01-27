from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

bp_admin = Blueprint('bp_admin', __name__)


@bp_admin.before_request
def before_request():
    if not current_user.is_authenticated or not current_user.has_access('admin'):
        return redirect(url_for('bp_open.index'))


@bp_admin.get('/admin')
def admin_get():
    return render_template('admin.html')


@bp_admin.get('/edit-users')
def edit_users():
    return render_template('edit_users.html')


@bp_admin.get('/edit-news')
def edit_users():
    return render_template('edit_news.html')
