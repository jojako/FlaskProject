from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.controller.user_controller import create_user

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('home.html')


@bp_open.get('/login')
def login():
    return render_template('login.html')


@bp_open.post('/login')
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    from app.persistance.model import User
    user = User.find(email=email).first_or_none()
    if user is None:
        flash('Wrong password or email')
        return redirect(url_for('bp_open.login'))

    if not check_password_hash(user.password, password):
        flash('Wrong password or email')
        return redirect(url_for('bp_open.login'))

    login_user(user)
    #Last sign in här (med user.save)

    return redirect(url_for('bp_user.newsfeed'))


@bp_open.get('/signup')
def signup():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    from app.persistance.model import User
    user = User.find(email=email).first_or_none()

    if user is not None:
        flash('Email already exists')
        return redirect(url_for('bp_open.signup'))

    create_user(first_name, last_name, email, password)
    return redirect(url_for('bp_open.login'))


@bp_open.get('/about')
def about():
    return redirect(url_for('bp_open.index', _anchor='about'))



    """
    if get_user_by_email(email) is not None:
        flash('Account already exists. Try to login instead.')
        return redirect(url_for('bp_open.login'))

    create_user(first_name, last_name, email, password)
    return redirect(url_for('bp_open.login'))
    """
