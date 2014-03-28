import hashlib
import random
from string import letters

from model import User, user_key
from constants import SECRET


def login(username, password):
    u = User.by_name(username)
    if u and u.password == hash_password(password, u.salt):
        return u
    else:
        return None


def register(username, password, email=None):
    uid = generate_uid(username)
    salt = make_salt()
    password = hash_password(password, salt)
    return User(parent=user_key(),
                keyname=uid,
                username=username,
                password=password,
                salt=salt,
                email=email)


def generate_uid(username):
    return hashlib.md5(username).hexdigest()


def make_salt():
    return ''.join(random.choice(letters) for c in range(5))


def hash_password(password, salt):
    return hashlib.md5(password + salt + SECRET).hexdigest()
