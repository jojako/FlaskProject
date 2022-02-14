from app.persistance.db import db, Document

ACCESS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}


class User(Document):
    collection = db.users

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.emailNews

    def has_access(self, level):
        return ACCESS[self.accesslevel] >= ACCESS[level]


class News(Document):
    collection = db.news

