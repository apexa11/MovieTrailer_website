import webbrowser


class Movie():
    """Stores movie-related information.

    Attributes:
        title: Title of the movie
        storyline: The tagline of the movie (usually printed on its poster)
        poster_image_url: Pointer to the movie poster on WikiMedia
        trailer_youtube_url: Pointer to the official movie trailer on YouTube
    """

    valid_rating = ['G', 'PG', 'PG-13', 'R']

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
        webbrowser.open(self.trailer_youtube_url)
