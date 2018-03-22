import webbrowser


class Movie():
    """
    This class provides a way to store movie related information

    Attributes:
        title(str): Movie title.
        storyline(str): Storyline of a movie.
        poster_image_url(str): Poster image link of a movie.
        trailer_youtube_url(str): Youtube video link of a movie's trailer.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
