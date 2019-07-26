from google.appengine.ext import ndb

class Event(ndb.Model):
    zipcode = ndb.IntegerProperty(required=True)
    district= ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)

class Candidate(ndb.Model):
    party = ndb.StringProperty(required=True)
    name = ndb. StringProperty(required=True)
    zipcode = db.ListProperty(required=True)
    district = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    level_government = ndb.KeyProperty(required=True)
    policies_supported = ndb.StringProperty(required=False)
#policies supported only includes the latest policy supported
    name = ndb.StringProperty(required=True)
    policies_supported = ndb.StringProperty(required=False)

# class BlogPost
# user, date_time, content

class BlogPost(ndb.Model):
    creator_id = ndb.StringProperty(required=True)
    creator_username = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(required=True, auto_now_add=True)
    post_content = ndb.StringProperty(required=True)
