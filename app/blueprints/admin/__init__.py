from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from bson.objectid import ObjectId

from app.controller import user_controller

bp_admin = Blueprint('bp_admin', __name__)


@bp_admin.before_request
def before_request():
    if not current_user.is_authenticated or not current_user.has_access('admin'):
        return redirect(url_for('bp_open.index'))


@bp_admin.get('/edit-users')
@login_required
def edit_users():
    users = user_controller.find_all_users()
    return render_template('edit_users.html', userlist=users)


@bp_admin.post('/delete-user')
@login_required
def edit_users_post():
    if request.method == 'POST':
        for user_id in request.form.getlist('user_checkbox'):
            user_controller.delete_user(ObjectId(user_id))
        return redirect(url_for('bp_admin.edit_users'))
    return 'Could not delete selected users'


@bp_admin.post('/add-user')
@login_required
def add_users_post():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        button = request.form.get('sign-up-button')

        from app.persistance.model import User
        user = User.find(email=email).first_or_none()

        if user is not None:
            flash('Email already exists')
            return redirect(url_for('bp_admin.edit_users'))

        user_controller.create_user(first_name, last_name, email, password)
        return redirect(url_for('bp_admin.edit_users'))
    return "Couldn't add new user"


@bp_admin.get('/edit-news')
def edit_news_sources():
    return render_template('edit_news.html')
