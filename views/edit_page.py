from google.appengine.api import memcache

from simple_handler import SimpleHandler
from model import Page

from utils import is_set_cookie


class EditPage(SimpleHandler):

    def get(self, page):

        if is_set_cookie(self, 'username'):
            params = {
                'edit_name': 'view',
                'logout_name': 'logout',
                'edit_link': self.uri_for('wiki', page=page),
                'logout_link': self.uri_for('logout')
            }
            self.render_response('newpage.html', params=params)
        else:
            self.redirect(self.uri_for('login'))

    def post(self, page):
        content = self.request.get('content')

        if content:
            p = Page(link=page, content=content)
            p.put()

            old_content = memcache.get(key=page)
            if old_content:
                memcache.set(key=page, value=str(content))

            memcache.add(key=page, value=str(content))
            self.redirect(self.uri_for('wiki', page=page))

        #ToDo:Add else branch and handle empty content
