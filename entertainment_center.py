import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")  # NOQA


wolf_of_wall_street = media.Movie("Wolf of Wall Street",
                                  "A wealthy stock-broker living"
                                  " the high life to his fall",
                                  "https://vignette.wikia.nocookie.net/cinemorgue/images/c/c7/The_Wolf_of_Wall_Street_2013.jpg/revision/latest?cb=20170223001424",  # NOQA
                                  "https://www.youtube.com/watch?v=iszwuX1AK6A")  # NOQA


breaking_bad = media.Movie("Breaking Bad",
                           "A high school teacher who is dying of"
                           " cancer making and selling drugs",
                           "https://vignette.wikia.nocookie.net/breakingbad/images/a/a7/Season_2_poster_2.jpg/revision/latest?cb=20120617210619",  # NOQA
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")  # NOQA

handmaids_tale = media.Movie("The Handmaid's Tale",
                             "In the near future, human fertility rates"
                             " collapse as a result of sexually transmitted"
                             " diseases and environmental pollution",
                             "https://i.ytimg.com/vi/PJTonrzXTJs/maxresdefault.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=PJTonrzXTJs")

prison_break = media.Movie("Prison Break",
                           "A man trying to get his brother out of prison",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Prison_Break_%28miniseries%29.jpg/220px-Prison_Break_%28miniseries%29.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mZwEBHc_PBw")

# list of movie instances
movies = [toy_story, avatar, wolf_of_wall_street,
          breaking_bad, handmaids_tale, prison_break]

if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies)
