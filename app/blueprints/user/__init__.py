from flask import Blueprint, render_template
from flask_login import login_required
## TODO: Flask Login needs to make sure you're authenticated

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/account')
@login_required
def profile():
    render_template('profile.html')


@bp_user.get('/newsfeed')
@login_required
def newsfeed():
    render_template('newsfeed.html')
