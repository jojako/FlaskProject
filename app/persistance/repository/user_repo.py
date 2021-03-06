import datetime
from app.persistance.model import User


def get_user_by_email(email):
    return User.find(email=email).first_or_none()


def create_user_and_save(user):
    User(user).save()


def set_lastsignin(email):
    user = get_user_by_email(email)
    user.last_signin = datetime.datetime.now()
    user.save()


def find_all_users():
    return User.find()


def delete_user(user_id):
    return User.delete(_id=user_id)
