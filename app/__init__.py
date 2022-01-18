from venv import create
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='./templates')

    return app


if __name__ == '__main__':
    create_app().run()
