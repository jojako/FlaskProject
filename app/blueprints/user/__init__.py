from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/account')
@login_required
def profile():
    return render_template('profile.html')


@bp_user.get('/newsfeed')
@login_required
def newsfeed():
    return render_template('newsfeed.html')


@bp_user.get('/sign-out')
@login_required
def signout():
    logout_user()
    return redirect(url_for('bp_open.index'))
