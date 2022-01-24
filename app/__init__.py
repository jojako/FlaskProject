from flask import Flask
from flask_login import LoginManager
from app.settings import SECRET_KEY


def create_app():
    app = Flask(__name__, template_folder='./templates')
    app.config.from_pyfile('settings.py')
    app.config['SECRET_KEY'] = f'{SECRET_KEY}'

    from app.persistance.db import init_db
    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.persistance.model import User
        return User.find(email=user_id).first_or_none()

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    from app.blueprints.user import bp_user
    app.register_blueprint(bp_user)

    return app


if __name__ == '__main__':
    create_app().run()
