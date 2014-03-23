from simple_handler import SimpleHandler
from model import User


class LoginPage(SimpleHandler):

    template = 'login.html'

    def get(self):
        next_url = self.request.headers.get('referer', '/')
        self.render_response(self.template, params=None, next_url=next_url)

    def post(self):
        ''' This function handles the login form and
        redirects user to welcome page'''

        username = self.request.get('username')
        password = self.request.get('password')
        next_url = str(self.request.get('next_url'))

        user = User.by_name(username)

        if user:
            u = User.login(user.username, password)

            if u:
                self.login(u)

                print next_url

                if not next_url or '/login' in next_url:
                    self.redirect(self.uri_for('home'))
                else:
                    self.redirect(next_url)

            else:
                self.render_response(self.template, password_error=
                                     "Password is not valid. Try again.",
                                     params=None)
        else:
            self.render_response(self.template, username_error=
                                 "User username %s doesn't exist." % username,
                                 params=None)
