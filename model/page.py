from google.appengine.ext import db


class Page(db.Model):
    link = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def parent_key(cls, path):
        return db.Key.from_path('/root' + path, 'Page')

    @classmethod
    def by_path(cls, link):
        q = Page.all()
        q.ancestor(cls.parent_key(link))
        page = q.filter('link =', link).get()
        return page

    @classmethod
    def by_id(cls, page_id, path):
        return cls.get_by_id(page_id, cls.parent_key(path))
