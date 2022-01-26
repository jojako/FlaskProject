from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.controller import user_controller
#from app.persistance.repository.user_repo import get_user_by_email

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

    if not user_controller.verify_user(email, password):
        flash("Wrong email or password")
        return redirect(url_for('bp_open.login'))

    user_controller.signin_user(email)

    return redirect(url_for('bp_open.index'))


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

    user_controller.create_user(first_name, last_name, email, password)
    return redirect(url_for('bp_open.login'))


@bp_open.get('/about')
def about():
    return redirect(url_for('bp_open.index', _anchor='about'))