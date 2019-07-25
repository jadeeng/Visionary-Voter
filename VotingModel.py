from google.appengine.ext import ndb

class Event(ndb.Model):
    zipcode = ndb.IntegerProperty(required=True)
    district= ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)

class Candidate(ndb.Model):
    party = ndb.StringProperty(required=True)
    name = ndb. StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)
    district = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    level_government = ndb.KeyProperty(required=True)
    policies_supported = ndb.StringProperty(required=False)
#policies supported only includes the latest policy supported
