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
                             "and for other purposes."),
                             link="https://pelosi.house.gov/").put()

    dianne_feinstein_zipcodes = ["CA"]
    dianne_feinstein_key = Candidate(party="Democrat", name="Dianne Feinstein",
                                    zipcode=dianne_feinstein_zipcodes, district="CA",
                                    level_government="Senator", policies_supported="",
                                    link="https://www.feinstein.senate.gov/public/").put()

    kamala_harris_zipcodes = ["CA"]
    kamala_harris_key = Candidate(party="Democrat", name="Kamala Harris",
                                    zipcode=kamala_harris_zipcodes, district="CA",
                                    level_government="Senator", policies_supported="",
                                    link="https://kamalaharris.org/").put()

    gavin_newsom_zipcodes = ["CA"]
    gavin_newsom_key = Candidate(party="Democrat", name="Gavin Newsom",
                                    zipcode=gavin_newsom_zipcodes, district="CA",
                                    level_government="Governor", policies_supported="",
                                    link= "https://www.gov.ca.gov/").put()

    eleni_kounalakis_zipcodes = ["CA"]
    eleni_kounalakis_ = Candidate(party="Democrat", name="Eleni Kounalakis",
                                    zipcode=eleni_kounalakis__zipcodes, district="CA",
                                    level_government="Mayor", policies_supported="https://ltg.ca.gov/about/").put()

    eric_garcetti_zipcodes = ["90001" "90021" "90044" "90077" "90502" "91330" "91504" "90002"
                            "90023" "90045" "90089" "90710" "91331" "91505" "90003" "90024" "90046"
                            "90094" "90717" "91335" "91601" "90004" "90025" "90047" "90095" "90731"
                            "91340" "91602" "90005" "90026" "90048" "90210" "90732" "91342" "91604"
                            "90005" "90027" "90049" "90211" "90732" "91343" "91605" "90006" "90028"
                            "90056" "90212" "90744" "91344" "91606" "90007" "90029" "90057" "90230"
                            "90810" "91345" "91607" "90008" "90031" "90058" "90232" "91040" "91352"
#                             91608* 90010 90032 90059* 90245* 91042* 91356
# 90011 90033 90061* 90247* 91214* 91364*
# 90012 90034 90062 90248* 91303 91367
# 90013 90035 90063* 90272 91304* 91401
# 90014 90036 90064 90290* 91306 91402
# 90015 90037 90065 90291* 91307 91403
# 90016 90038 90066* 90292* 91311* 91405
# 90017 90039 90067 90293* 91316 91406
# 90018 90041 90068 90302* 91324 91411
# 90019 90042 90069* 90402 * 91325 91423 # 90020 90043* 90071 90501* 91326* 91436"
]
    eric_garcetti_key = Candidate(party="Democrat", name="Eric Garcetti",
                                    zipcode=eric_garcetti_zipcodes, district="CA",
                                    level_government="Mayor", policies_supported="").put()

    event1= Event(zipcode= "90291", district= "33", state="CA",
                  description=("Attend a political rally featuring speakers "
                               "Congress Representative Ted Lieu and Senator "
                               "Kamala Harris"))
    event1.put()
    polling1= Polling_places(zipcode= "90291", address=("720 Venice, CA 90291 Oakwood Recreation Center Gymnasium Green Table"))
    polling1.put()
    polling2= Polling_places(zipcode= "90291", address=("767 California Ave Venice, CA 90291 Penmar Recreation Center Gymnasium/ Orange Table"))
    polling2.put()
    polling3= Polling_places(zipcode= "90291", address=("1341 Lake St Venice, CA 90291 Lifeguard Headquarters Garage/Orange Table"))
    polling3.put()
    polling4= Polling_places(zipcode= "90291", address=("2300 Ocean Front Walk Venice, CA 90291 Adda Paul Safran Sr Housing Community Room"))
    polling4.put()
    polling5= Polling_places(zipcode= "90291", address=("151 Ocean Front Walk Venice, CA 90291 the Bible Tabernacle Church Hall"))
    polling5.put()
    polling6= Polling_places(zipcode= "90291", address=("1761 Washington Way Venice, CA 90291 Westminster Elementary Sch Auditorium"))
    polling6.put()
    polling7= Polling_places(zipcode= "90291", address=("1010 Abbot Kinney Blvd Venice, CA 90291 Venice United Methodist Chr Fellowship Hall"))
    polling7.put()
    polling8= Polling_places(zipcode= "90291", address=("2210 Lincoln Blvd Venice, CA 90291 New Bethel Baptist Church Meeting Room"))
    polling8.put()
    polling9= Polling_places(zipcode= "90291", address=("503 Brooks Ave Venice, CA 90291 Tabor Courts Apartments Recreation Room"))
    polling9.put()
    polling10= Polling_places(zipcode= "90291", address=("345 4th Ave Venice, CA 90291 Coeur D`Alene Ave Elementary Auditorium"))
    polling10.put()
    polling10= Polling_places(zipcode= "90291", address=("810 Coeur D Alene Ave Venice, CA 90291"))
    polling10.put()


    blog_post_1 = BlogPost(creator_id= "123456789" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_1.put()
    blog_post_2 = BlogPost(creator_id= "898765432" , creator_username= "abc", post_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    blog_post_2.put()
