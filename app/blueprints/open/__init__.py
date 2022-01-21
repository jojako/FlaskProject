from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controller.user_controller import create_user, verify_user_credentials, get_user_by_email, signin_user

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
    if not verify_user_credentials(email, password):
        flash('Wrong password or email')
        redirect(url_for('bp_open.login'))

    signin_user(email)

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

    if get_user_by_email(email) is not None:
        flash('Account already exists. Try to login instead.')
        return redirect(url_for('bp_open.login'))

    create_user(first_name, last_name, email, password)
    return redirect(url_for('bp_open.login'))
