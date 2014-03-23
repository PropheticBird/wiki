import webapp2
from webapp2_extras import jinja2

from utils import make_cookie, read_cookie
from model import User


class SimpleHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)

    def notfound(self):
        self.error(404)
        self.render_response('error404.html')

    def login(self, user):
        user_key = str(user.key().id())
        self.response.set_cookie('username', make_cookie(user_key), path='/')

    def logout(self):
        self.response.delete_cookie('username', path='/')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = read_cookie(self, 'username')
        self.user = uid and User.by_id(int(uid))

