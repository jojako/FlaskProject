from urllib import request
from flask import Blueprint, render_template, request


bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('home.html')


@bp_open.get('/login')
def login():
    return render_template('login.html')

@bp_open.post('/login')
def login_post():
    email = request.form.get(email)
    password = request.form.get(password)
    


@bp_open.get('/signup')
def signup():
    return render_template('signup.html')
