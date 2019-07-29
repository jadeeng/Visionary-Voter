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
                             "and for other purposes."),
                             link=("https://lieu.house.gov/")).put()

    nancy_pelosi_zipcodes = [
        "94102", "94103", "94104", "94105", "94107", "94108", "94109", "94110",
        "94111", "94112", "94114", "94115", "94116", "94117", "94118", "94121",
        "94122", "94123", "94124", "94127", "94129", "94130", "94131", "94133",
        "94134", "94158"]

    nancy_pelosi_key = Candidate(party="Democrat", name="Nancy Pelosi",
                             zipcode=nancy_pelosi_zipcodes, district="12",
                             state="CA",
                             level_government="Congress Representative",
                             policies_supported=(
                             "To amend the Education Sciences and Reform Act of"
                             " 2002 to include racial subgroups in IPEDS data, "
                             "and for other purposes.")).put()

    dianne_feinstein_zipcodes = ["CA"]
    dianne_feinstein_key = Candidate(party="Democrat", name="Dianne Feinstein",
                                    zipcode=dianne_feinstein_zipcodes, district="CA",
                                    level_government="Senator", policies_supported="").put()

    kamala_harris_zipcodes = ["CA"]
    kamala_harris_key = Candidate(party="Democrat", name="Kamala Harris",
                                    zipcode=kamala_harris_zipcodes, district="CA",
                                    level_government="Senator", policies_supported="").put()

    gavin_newsom_zipcodes = ["CA"]
    gavin_newsom_key = Candidate(party="Democrat", name="Gavin Newsom",
                                    zipcode=gavin_newsom_zipcodes, district="CA",
                                    level_government="Governor", policies_supported="").put()

    eleni_kounalakis_zipcodes = ["CA"]
    eleni_kounalakis_ = Candidate(party="Democrat", name="Eleni Kounalakis",
                                    zipcode=eleni_kounalakis__zipcodes, district="CA",
                                    level_government="Mayor", policies_supported="").put()

    eric_garcetti_zipcodes = ["CA"]
    eric_garcetti_key = Candidate(party="Democrat", name="Eric Garcetti",
                                    zipcode=eric_garcetti_zipcodes, district="CA",
                                    level_government="Mayor", policies_supported="").put()

    event1= Event(zipcode= "90291", district= "33", state="CA",
                  description=("Attend a political rally featuring speakers "
                               "Congress Representative Ted Lieu and Senator "
                               "Kamala Harris"))
    event1.put()

    blog_post_1 = BlogPost(creator_id= "123456789" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_1.put()
    blog_post_2 = BlogPost(creator_id= "898765432" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_2.put()
