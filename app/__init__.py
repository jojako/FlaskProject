from flask import Flask
def create_app():
    app = Flask(__name__, template_folder='./templates')

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    return app

if __name__ == '__main__':
    create_app().run()
