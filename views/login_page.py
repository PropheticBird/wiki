from simple_handler import SimpleHandler
from model import get_user, hash_password
from utils import make_cookie


class LoginPage(SimpleHandler):

    template = 'login.html'

    def get(self):
        self.render_response(self.template)

    def post(self):
        ''' This function handles the login form and
        redirects user to welcome page'''

        username = self.request.get('username')
        password = self.request.get('password')

        user = get_user(username)

        if user:

            # check if user entered a valid password
            if user.password == hash_password(username, password, user.salt):

                # set cookie
                cookie = make_cookie(username)
                self.response.set_cookie('username', cookie, path='/')

                self.redirect(self.uri_for('home'))

            else:
                self.render_response(self.template, password_error=
                                     "Password is not valid. Try again.")
        else:
            self.render_response(self.template, username_error=
                                 "User username %s doesn't exist." % username)
