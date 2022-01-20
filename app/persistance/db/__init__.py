from pymongo import MongoClient

client = None
db = None


def init_db(app):
    global client, db
    username = app.config['DB_USER']
    password = app.config['DB_PASSWORD']
    host = app.config['DB_HOST']
    port = int(app.config['DB_PORT'])
    database = app.config['DB_NAME']
    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
    db = client[database]


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None
