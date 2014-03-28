from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    salt = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=user_key())

    @classmethod
    def by_name(cls, username):
        u = User.all().filter('username =', username).get()
        return u


def user_key(group='default'):
    return db.Key.from_path('User', group)
