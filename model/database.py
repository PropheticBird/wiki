import hashlib
import random
from string import letters

from google.appengine.ext import db

from constants import SECRET

#SignUP


class Users(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    salt = db.StringProperty(required=True)
    email = db.StringProperty()


def generate_uid(username):
    return hashlib.md5(username).hexdigest()


def get_user(username):
    user_db = db.GqlQuery("SELECT * FROM Users WHERE username=:1", username)
    user = user_db.get()
    return user


def make_salt():
    return ''.join(random.choice(letters) for c in range(5))


def hash_password(username, password, salt):
    return hashlib.md5(username + password + salt + SECRET).hexdigest()


def save_user_to_db(username, password, email):
    uid = generate_uid(username)
    salt = make_salt()
    password = hash_password(username, password, salt)
    user = Users(keyname=uid, username=username,
                 password=password, salt=salt, email=email)
    user.put()


# Wiki Pages
class Page(db.Model):
    link = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)


def get_link(link):
    q = Page.all()
    q.filter('link =', link)
    page = q.get()
    return page
