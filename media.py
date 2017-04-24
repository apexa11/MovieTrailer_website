import webbrowser
class Movie():
    valid_rating = ["G","PG","PG-13","R"]
    
    def __init__(self,movie_title,movie_storyline,poster_image,movie_trailer):
         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = movie_trailer
    #show trailer of movies
    def show_trailer(self):
       webbrowser.open(self.trailer_youtube_url)
