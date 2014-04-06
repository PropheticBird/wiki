from google.appengine.ext import db


class Page(db.Model):
    link = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_path(cls, link):
        q = Page.all()
        q.order('-last_modified')
        page = q.filter('link =', link).get()
        return page

    @classmethod
    def by_id(cls, page_id):
        return cls.get_by_id(page_id)
