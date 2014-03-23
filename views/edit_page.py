from simple_handler import SimpleHandler
from model import Page


class EditPage(SimpleHandler):

    def get(self, link):

        if not self.user:
            self.redirect(self.uri_for('login'))

        else:
            page = None
            page = Page.by_path(link)

            params = {
                'name': self.user.username,
                'name_ev': 'view',
                'name_lio': 'logout',
                'link_ev': self.uri_for('wiki', link=link),
                'link_lio': self.uri_for('logout')
            }

            self.render_response('newpage.html', page=page, params=params)

    def post(self, link):
        if not self.user:
            self.notfound()

        content = self.request.get('content')
        print content

        if content:
            p = Page(parent=Page.parent_key(link), link=link, content=content)
            p.put()

            self.redirect(self.uri_for('wiki', link=link))

        else:
            error = 'You must add some content before submitting.'
            self.render_response('newpage.html', error=error)
