from flask import Blueprint, render_template
## TODO: Flask Login needs to make sure you're authenticated

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/account')
def profile():
    render_template('profile.html')
