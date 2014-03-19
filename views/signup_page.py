from model import save_user_to_db
from utils import validate, make_cookie
from simple_handler import SimpleHandler


class SignupPage(SimpleHandler):

    tempate = 'signup.html'

    def get(self):
        self.render_response(self.tempate)

    def post(self):
        '''This function handles the signup form and vlidates user input.'''

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        # check the input and return dict of errors
        errors = validate(username, password, verify, email)

        if len(errors) != 0:
            self.render_response(self.tempate, **errors)
        else:
            save_user_to_db(username, password, email)

            # set cookies
            cookie = make_cookie(username)
            self.response.set_cookie('username', cookie, path='/')

            self.redirect(self.uri_for('home'))
