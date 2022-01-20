from app.persistance.repository import user_repo


def create_user(first_name, last_name, email, password):
    return user_repo.create_user(first_name, last_name, email, password)