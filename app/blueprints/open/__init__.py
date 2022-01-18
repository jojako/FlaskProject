from flask import Blueprint, render_template

bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template('home.html')


@bp_open.get('/login')
def login():
    return render_template('login.html')


@bp_open.get('/signup')
def signup():
    return render_template('signup.html')


@bp_open.get('/about')
def about():
    return render_template('about.html')


