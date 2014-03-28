import hashlib
import random
from string import letters

from google.appengine.ext import db

from constants import SECRET

#SignUP


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

    @classmethod
    def login(cls, username, password):
        u = cls.by_name(username)
        if u and u.password == hash_password(password, u.salt):
            return u
        else:
            return None

    @classmethod
    def register(cls, username, password, email=None):
        uid = generate_uid(username)
        salt = make_salt()
        password = hash_password(password, salt)
        return User(parent=user_key(),
                    keyname=uid,
                    username=username,
                    password=password,
                    salt=salt,
                    email=email)


def user_key(group='default'):
    return db.Key.from_path('User', group)


def generate_uid(username):
    return hashlib.md5(username).hexdigest()


def make_salt():
    return ''.join(random.choice(letters) for c in range(5))


def hash_password(password, salt):
    return hashlib.md5(password + salt + SECRET).hexdigest()


# Wiki Pages
class Page(db.Model):
    link = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def parent_key(cls, path):
        return db.Key.from_path('/root' + path, 'Page')

    @classmethod
    def by_path(cls, link):
        q = Page.all()
        q.ancestor(cls.parent_key(link))
        page = q.filter('link =', link).get()
        return page

    @classmethod
    def by_id(cls, page_id, path):
        return cls.get_by_id(page_id, cls.parent_key(path))
