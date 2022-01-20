from werkzeug.security import generate_password_hash
import datetime


def create_user(first_name, last_name, email, password):
    from app.persistance.model import User
    user = (
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
    User.collection.insert_one(user)
