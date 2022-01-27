import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user
from app.persistance.repository import user_repo


def create_user(first_name, last_name, email, password):
    user = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': generate_password_hash(password),
            'accesslevel': 'user',
            'date_created': datetime.datetime.now(),
            'last_signin': None,
            'activated': False
    }
    user_repo.create_user_and_save(user)


def get_user_by_email(email):
    return user_repo.get_user_by_email(email)


def verify_user(email, password):
    user = user_repo.get_user_by_email(email)
    if user is None:
        return False
    if not check_password_hash(user.password, password):
        return False
    else:
        return True


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)

        user_repo.set_lastsignin(email)


def find_all_users():
    return user_repo.find_all_users()