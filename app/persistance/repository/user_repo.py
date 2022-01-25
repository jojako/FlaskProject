from app.persistance.model import User


def get_user_by_email(email):
    return User.find(email=email).first_or_none()

"""
def create_user(user):
    User.collection.insert_one(user)


def get_user_by_email(email):
    # return User.collection.find({email: str(email)})
    # return User.find(email=email).first_or_none()
    return User.collection.find_one({email: str(email)})
"""
