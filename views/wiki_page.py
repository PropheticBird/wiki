from simple_handler import SimpleHandler
from model import Page


class WikiPage(SimpleHandler):

    template = 'wikipage.html'

    def get(self, link):

        page = Page.by_path(link)
        params = {}

        if self.user and page:

            params = {
                'name': self.user.username,
                'name_ev': 'edit',
                'name_lio': 'logout',
                'link_ev': self.uri_for('edit', link=link),
                'link_lio': self.uri_for('logout')
            }

        elif not self.user and page:

            params = {
                'name_lio': 'login',
                'link_lio': self.uri_for('login')
            }

        else:
            return self.redirect_to('edit', link=link)

        self.render_response(self.template, page=page, params=params)

    def front_page(self):
        pages = Page.all()
        self.render_response('frontpage.html', pages=pages, params=None)
