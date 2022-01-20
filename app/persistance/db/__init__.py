from pymongo import MongoClient

client = MongoClient(f'mongodb://root:s3cr37@localhost:27022')
db = client.login_db


def init_db(app):
    username = app.config['DB_USER']
    password = app.config['DB_PASSWORD']
    host = app.config['DB_HOST']
    port = app.config['DB_PORT']
    database = app.config['DB_NAME']

