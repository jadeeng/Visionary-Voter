from VotingModel import Event, Candidate, BlogPost

def seed_data():
    ted_lieu_zipcodes = [
        "90004", "90020", "90024", "90036", "90048", "90049", "90073", "90077",
        "90095", "90209", "90211", "90212", "90213", "90245", "90254", "90263",
        "90264", "90265", "90266", "90267", "90272", "90274", "90275", "90277",
        "90278", "90290", "90291", "90292", "90293", "90294", "90295", "90401",
        "90402", "90403", "90404", "90405", "90406", "90407", "90408", "90409",
        "90410", "90411", "90503", "90505"]
    ted_lieu_key = Candidate(party="Democrat", name="Ted Lieu",
                             zipcode=ted_lieu_zipcodes, district="33",
                             state="CA",
                             level_government="Congress Representative",
                             policies_supported=(
                             "To amend the Education Sciences and Reform Act of"
                             " 2002 to include racial subgroups in IPEDS data, "
                             "and for other purposes.")).put()

    dianne_feinstein_zipcodes = ["CA"]
    dianne_feinstein_key = Candidate(party="Democrat", name="Dianne Feinstein", zipcode=dianne_feinstein_zipcodes,
    district="CA", )

    event1= Event(zipcode= "90291", district= "33", state="CA",
                  description=("Attend a political rally featuring speakers "
                               "Congress Representative Ted Lieu and Senator "
                               "Kamala Harris"))
    event1.put()

    blog_post_1 = BlogPost(creator_id= "123456789" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_1.put()
    blog_post_2 = BlogPost(creator_id= "898765432" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_2.put()
