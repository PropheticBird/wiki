from google.appengine.api import memcache

from simple_handler import SimpleHandler
from model import get_link
from utils import is_set_cookie


class WikiPage(SimpleHandler):

    def get(self, page):

        wiki_content = memcache.get(page)
        if wiki_content is None:
            wiki = get_link(page)
            if wiki:
                wiki_content = wiki.content
            else:
                self.redirect(self.uri_for('edit', page=page))

        params = {
            'content': wiki_content,
        }

        if is_set_cookie(self, 'username'):
            params['edit_name'] = 'edit'
            params['logout_name'] = 'logout'
            params['edit_link'] = self.uri_for('edit', page=page)
            params['logout_link'] = self.uri_for('logout')
            self.render_response('wikipage.html', params=params)

        else:
            params['logout_name'] = 'login'
            params['logout_link'] = self.uri_for('login')
            self.render_response('wikipage.html', params=params)

    def front_page(self):
        content = """<h2> Welcome to wiki! </h2>
                     <br>
                     Eneter a url to create a new page."""
        params = {
            'content': content,
        }

        if is_set_cookie(self, 'username'):
            params['logout_name'] = 'logout'
            params['logout_link'] = self.uri_for('logout')
            self.render_response('wikipage.html', params=params)

        else:
            params['logout_name'] = 'login'
            params['logout_link'] = self.uri_for('login')
            self.render_response('wikipage.html', params=params)
