from simple_handler import SimpleHandler


class Logout(SimpleHandler):
    def get(self):
        ''' This function implements logout functionality
        by clearing the cookies and redirecting to the signup page '''

        next_url = self.request.headers.get('referer', '/')
        self.logout()
        self.redirect(next_url)
