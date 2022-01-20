from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for
from app.controller import create_user


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
    
    # Import models for database after it has been set up.
    # Compare password with password hash.

    print(email, password)


@bp_open.get('/signup')
def signup():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    create_user(first_name, last_name, email, password)
    return redirect(url_for('bp_open.login'))
