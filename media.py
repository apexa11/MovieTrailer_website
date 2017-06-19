import webbrowser


class Movie():
    """This class Provides a wayo store movie related information """

    valid_rating = ['G', 'PG', 'PG-13', 'R'] # attributes share bt all Movies

""" This Method creates new Movie

    :param movie_title:title
    :type  movie_title:str

    :param movie_storyline:storyline
    :type  movie_storyline:str

    :param poster_image:poster imageUrl
    :type  poster_image:str

    :param movie_trailer:YouTube trailerUrl
    :type  movie_trailer:str
"""
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        movie_trailer,
        ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    """Plays the embedded YouTube video."""

    def show_trailer(self):
        """ This method check current movie trailer in class object"""
            :returns: str --the movie trailer , opens the youtube movie preview
        """
        webbrowser.open(self.trailer_youtube_url)