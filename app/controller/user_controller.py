import datetime

from app.persistance.model import User
from app.persistance.repository import user_repo
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user


def create_user(first_name, last_name, email, password):
    user = User(
        {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': generate_password_hash(password),
            'admin': False,
            'date_created': datetime.datetime.now(),
            'last_signin': None,
            'activated': False
        }
    )
    user.save()

"""
def get_user_by_email(email):
    return user_repo.get_user_by_email(email)


def verify_user_credentials(email, password):
    user = user_repo.get_user_by_email(email)
    if user is None:
        return False

    return check_password_hash(user.password, password)


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)
"""

