import re

from model import get_user


def valid_username(username):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(username)


def valid_password(password):
    password_re = re.compile(r"^.{3,20}$")
    return password_re.match(password)


def valid_email(email):
    email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return email_re.match(email)


def validate(username, password, verify, email):
    template_values = {}

    if not valid_username(username):
        template_values.update({'username_error':
                                'That\'s not a valid username.'})

    if get_user(username):
        template_values.update({'user_exists_error':
                                'User with this username already exists.'})

    if not valid_password(password):
        template_values.update({'password_error':
                                'That wasn\'t a valid password.'})

    if email != '' and not valid_email(email):
            template_values.update({'email_error':
                                    'That\'s not a valid email.'})

    if password != verify:
        template_values.update({'verify_error':
                                'Your passwords don\'t match.'})

    return template_values
