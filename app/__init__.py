from flask import Flask
from app.persistance.db import init_db


def create_app():
    app = Flask(__name__, template_folder='./templates')
    app.config.from_pyfile('settings.py')
    init_db(app)

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    return app


if __name__ == '__main__':
    create_app().run()
