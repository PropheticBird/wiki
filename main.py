# coding: utf-8
import logging

import webapp2
from webapp2_extras import routes

import views
from constants import PAGE_RE


def handle_404(request, response, exception):
    logging.exception(exception)
    response.set_status(404)
    response.write('<h1> Requested resource was not found </h1>')


def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    response.write('<h3> Server error, try again later </h3>')


app = webapp2.WSGIApplication([
    routes.PathPrefixRoute(r'/wiki', [
        webapp2.Route(r'/signup', handler=views.SignupPage, name='signup'),
        webapp2.Route(r'/login', handler=views.LoginPage, name='login'),
        webapp2.Route(r'/logout', handler=views.Logout, name='logout'),
        webapp2.Route(r'/', handler=views.WikiPage,
                      handler_method='front_page', name='home'),
        webapp2.Route(r'/<link:{0}>'.format(PAGE_RE),
                      handler=views.WikiPage, name='wiki'),
        webapp2.Route(r'/_edit/<link:{0}>'.format(PAGE_RE),
                      handler=views.EditPage, name='edit')]
    )
], debug=True)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
