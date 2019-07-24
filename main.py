import webapp2
import os
import jinja2
import json
from datetime import datetime
from datetime import timedelta

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

CANDIDATES=[

]

def get_students(prefix):
  results = []
  if len(prefix) == 0:
    return results
  for candidates in CANDIDATES:
    if candidates.lower().startswith(prefix.lower()):
      results.append(candidates)
      if len(results) == 5:
        return results
  return results

class CandidateHandler(webapp2.RequestHandler):
    def get(self):
      prefix = self.request.get('q')
      students = get_students(prefix)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.write(json.dumps(students))

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

app = webapp2.WSGIApplication([
    ('/', FoodHandler),
    ('/CandidateList', ShowCandidateHandler),
    ("/")
    ("/calendar", CalendarHandler)
], debug=True)
