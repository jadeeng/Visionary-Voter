import webapp2
import os
import jinja2
from datetime import datetime
from datetime import timedelta
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        start_string = self.request.get('starttime')
        start_date= datetime.strptime(start_string, "%Y-%m-%dT%H:%M")
        start_utc=start_date+timedelta(hours=7)
        calendar_url="http://www.google.com/calendar/event?action=TEMPLATE&text=%s&dates=%s/%s"

        end_utc = start_utc+timedelta (hours=1)
        calendar_start = start_utc.strftime("%Y%m%dT%H%M00Z")
        calendar_end = end_utc.strftime("%Y%m%dT%H%M00Z")
        calendar_link = calendar_url%("TestEvent", calendar_start, calendar_end)
        #instead of putting testevent, you can insert a bunch of different links that they can follow for events occuring
        #HTML link open in new tab taget="_blank"
        calendar_HTML = "<HTML><BODY><A href='%s' target='_blank'>Test Event Link</A></BODY></HTML>"
        self.response.write(calendar_HTML % calendar_link)

class BlogPostHandler(webapp2.RequestHandler):
    def get(self):
        # [START user_details]
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        # [END user_details]
        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/calendar', CalendarHandler)
    ('/blogpost', BlogPostHandler)
], debug=True)
