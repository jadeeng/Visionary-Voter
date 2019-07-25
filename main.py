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

CANDIDATES =[
    "Steve",
    "Barbie",
    "Lewis"
]

def get_candidates(prefix):
  results = []
  if len(prefix) == 0:
    return results
  for candidates in CANDIDATES:
    if candidates.lower().startswith(prefix.lower()):
      results.append(candidates)
      if len(results) == 5:
        return results
  return results

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("index.html")
        self.response.write(start_template.render())

class CandidateHandler(webapp2.RequestHandler):
    def get(self):
      prefix = self.request.get('q')
      students = get_candidates(prefix)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.write(json.dumps(candidates))

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        start_string = self.request.get('starttime')
        start_date = datetime.strptime(start_string, "%Y-%m-%dT%H:%M")
        start_utc = start_date+timedelta(hours=7)
        calendar_url = "http://www.google.com/calendar/event?action=TEMPLATE&text=%s&dates=%s/%s"

        end_utc = start_utc+timedelta (hours=1)
        calendar_start = start_utc.strftime("%Y%m%dT%H%M00Z")
        calendar_end = end_utc.strftime("%Y%m%dT%H%M00Z")
        calendar_link = calendar_url%("TestEvent", calendar_start, calendar_end)
        #instead of putting testevent, you can insert a bunch of different links that they can follow for events occuring
        #HTML link open in new tab taget="_blank"
        calendar_HTML = "<HTML><BODY><A href='%s' target='_blank'>Test Event Link</A></BODY></HTML>"
        self.response.write(calendar_HTML % calendar_link)

class EventHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = 'text/json'
        if self.request.get('after'):
            latest_event_key = ndb.Key(urlsafe=self.request.get('after'))
            latest_event = latest_event_key.get()
            events = Event.query(Event.created_at > latest_meme.created_at).order(-Meme.created_at).fetch()
        else:
            latest_event = latest_event.query().order(-latest_event.created_at).fetch(10)
        new_events_list = []
        for event in latest_event:
            events_list.append({
              'image_file': image.image_file,
              'text': event.top_text,
              'created_at': event.created_at.isoformat(),
              'key': event.key.urlsafe(),
            })
        self.response.write(json.dumps(events_list))




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/CandidateList', CandidateHandler),
    ("/calendar", CalendarHandler)
    ("/events", EventHandler)
], debug=True)
