from simple_handler import SimpleHandler
from model import Page


class WikiPage(SimpleHandler):

    def get(self, link):

        page = Page.by_path(link)

        if self.user and page:
            params = {
                'name': self.user.username,
                'name_ev': 'edit',
                'name_lio': 'logout',
                'link_ev': self.uri_for('edit', link=link),
                'link_lio': self.uri_for('logout')
            }

            self.render_response('wikipage.html', page=page, params=params)

        elif not self.user and page:
            params = {
                'name_lio': 'login',
                'link_lio': self.uri_for('login')
            }
            self.render_response('wikipage.html', page=page, params=params)

        else:
            self.redirect(self.uri_for('edit', link=link))

    def front_page(self):
        self.render_response('wikipage.html', page=None, params=None)
