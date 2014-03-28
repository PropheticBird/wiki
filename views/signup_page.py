from model import User
from utils import validate
from simple_handler import SimpleHandler


class SignupPage(SimpleHandler):

    tempate = 'signup.html'

    def get(self):
        self.render_response(self.tempate, params=None)

    def post(self):
        '''This function handles the signup form and vlidates user input.'''

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        # check the input and return dict of errors
        errors = validate(username, password, verify, email)

        if len(errors) != 0:
            self.render_response(self.tempate, params=None, **errors)
        else:
            u = User.register(username, password, email)
            u.put()

            self.login(u)

            self.redirect_to('home')
