from webapp2 import uri_for

from simple_handler import SimpleHandler


class Logout(SimpleHandler):
    def get(self):
        ''' This function implements logout functionality
        by clearing the cookies and redirecting to the signup page '''

        self.response.delete_cookie('username', path='/')
        self.redirect(uri_for('login'))
