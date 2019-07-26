from VotingModel import Event, Candidate

def seed_data():
    ted_lieu_key = Candidate(party="Democrat", name ="Ted Lieu", zipcode = "90004 90020 90024 90036 90048 90049 90073 90077 90095 90209 90211 90212 90213 90245 90254 90263 90264 90265 90266 90267 90272 90274 90275 90277 90278 90290 90291 90292 90293 90294 90295 90401 90402 90403 90404 90405 90406 90407 90408 90409 90410 90411 90503 90505",
    district="33", state="CA", level_government="Congress Representative", policies_supported="To amend the Education Sciences and Reform Act of 2002 to include racial subgroups in IPEDS data, and for other purposes.").put()

    event1= Event(zipcode= "90291", district= "33", state="CA", description="Attend a political rally featuring speakers like Congress Representative Ted Lieu and Senator Kamala Harris")
