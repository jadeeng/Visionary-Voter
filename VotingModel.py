from google.appengine.ext import ndb

class Event(ndb.Model):
    description = ndb.StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)
    city= ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)

class Candidate(ndb.Model):
    party = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    level_government = ndb.KeyProperty(required=True)
    name = ndb. StringProperty(required=True)
    policies_supported = ndb.StringProperty(required=False)
