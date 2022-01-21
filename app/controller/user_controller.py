from app.persistance.repository import user_repo
from werkzeug.security import check_password_hash


def create_user(first_name, last_name, email, password):
    return user_repo.create_user(first_name, last_name, email, password)


def get_user_by_email(email):
    return user_repo.get_user_by_email(email)


def verify_user_credentials(email, password):
    user = user_repo.get_user_by_email(email)
    if user is None:
        return False
    return check_password_hash(user.password, password)
