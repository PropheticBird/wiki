import hmac

from constants import SECRET


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val
    else:
        return None


def make_cookie(username):
    return make_secure_val(str(username))


def read_cookie(handler, name):
    username_cookie_str = handler.request.cookies.get(name)
    if username_cookie_str:
        username = check_secure_val(username_cookie_str)
        if username:
            return username
    else:
        return None
