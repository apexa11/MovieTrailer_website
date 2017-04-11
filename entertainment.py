import fresh_tomatoes
import media
fast_and_furious = media.Movie("fast and furious",
                               "its about racing cars",
                               "http://t1.gstatic.com/images?q=tbn:ANd9GcReedjA2vJSO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7",
                               "https://www.youtube.com/watch?v=57_dxsywuQE")
#print(fast_and_furious.poster_image_url)

Bahubali = media.Movie("Bahubali",
                       "Two brothers clash for control of a kingdom.",
                       "http://www.cinejosh.com/newsimg/newsmainimg/bahubali-maa-tv-premieres-on-october-25_b_2909150516.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")
#print(Bahubali.storyline)

stars = media.Movie("fault in our stars",
                    "its about lovestory",
                    "http://wskg.org/wp-content/uploads/2017/01/0421-1.jpg",
                    "https://www.youtube.com/watch?v=9ItBvH5J6ss")
#print(stars.title)

avatar = media.Movie("avatar",
                     "about A",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg ",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4  ")

titanic = media.Movie("titanic",
                      "about love story",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR88,0,630,1200_AL_.jpg ",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ ")

minions = media.Movie("minions",
                   "Evolving from single-celled yellow organisms at the dawn of time, Minions live to serve, but find themselves working for a continual series of unsuccessful masters, from T. Rex to Napoleon. Without a master to grovel for, the Minions fall into a deep depression. ",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MTMyMzU0M15BMl5BanBnXkFtZTgwOTU3ODk4NTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg  ",
                   "https://www.youtube.com/watch?v=GGssZksONtY  ")

movies = [fast_and_furious,Bahubali,stars,avatar,titanic,minions]
print(media.Movie.valid_rating)
#fresh_tomatoes.open_movies_page(movies)



