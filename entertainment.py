import fresh_tomatoes
import media

# List of moviesto feature on site.
fast_and_furious = media.Movie('fast and furious',
                               'its about racing cars',
                               'http://t1.gstatic.com/'
                               'https://en.wikipedia.org/wiki/The_Fate_of_the_Furious#/media/File:The_Fate_of_The_Furious_Theatrical_Poster.jpg'#noqa
                               'https://youtu.be/PrgNK7KKoiw')

Bahubali = media.Movie('Bahubali',
                       'Two brothers clash for control of a kingdom.',
                       'https://en.wikipedia.org/wiki/Baahubali:_The_Beginning#/media/File:Baahubali_poster.jpg',#noqa
                       'https://www.youtube.com/watch?v=sOEg_YZQsTI')

stars = media.Movie('fault in our stars',
                    'its about lovestory',
                    'http://wskg.org/wp-content/uploads/2017/01/0421-1.jpg',#noqa
                    'https://www.youtube.com/watch?v=9ItBvH5J6ss')

avatar = media.Movie('avatar',
                     "On the lush alien world of Pandora live the Na'vi"
                     "beings who appear primitive but are highly evolved."
                     "Because the planet's environment is poisonous/"
                     "human/Na'vi hybrids, called Avatars/"
                     "must link to human minds to allow for/"
                     " free movement on Pandora.",
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',#noqa
                     'https://www.youtube.com/watch?v=uZNHIU3uHT4')

titanic = media.Movie('titanic',
                      'about love story',
                      'https://images-na.ssl-images-amazon.com/'
                      'https://en.wikipedia.org/wiki/Titanic_(1997_film)#/media/File:Titanic_poster.jpg',#noqa
                      'https://www.youtube.com/watch?v=IVqpcSqokkw')

minions = media.Movie('minions',
                      'Evolving from single-celled yellow organisms/'
                      'at the dawn of time,/'
                      'Minions live to serve/'
                      'but find themselves working for a continual/'
                      'series of unsuccessful masters/'
                      'from T. Rex to Napoleon. Without a master/'
                      'to grovel for, the Minions fall/'
                      'into a deep depression.',
                      'https://images-na.ssl-images-amazon.com/'
                      'https://en.wikipedia.org/wiki/Minions_(film)#/media/File:Minions_poster.jpg'#noqa
                      'https://www.youtube.com/watch?v=TDBYGMe93jo')

arrival = media.Movie('Arrival',
                      'Linguistics professor Louise Banks (Amy Adams)/'
                      ' leads an elite team of investigators when gigantic/'
                      'spaceships touch down in 12 locations around the world',
                      'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg',#noqa
                      'https://www.youtube.com/watch?v=wu8_5TGwr90')

Deadpool = media.Movie('Deadpool', 'about spider and their life story',
                       'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',#noqa
                       'https://www.youtube.com/watch?v=0LmwToJlefE')

Moonlight = media.Movie('Moonlight',
                        'A look at three defining chapters in the life/'
                        'of Chiron, a young black man growing up in Miami./'
                        'His epic journey to manhood is/'
                        ' guided by/the kindness,/'
                        'support and love of the community that/'
                        'helps raise him.',
                        'https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png',#noqa
                        'https://www.youtube.com/watch?v=2gCc6kGpXdw')

# store movies in list
movies = [
    fast_and_furious,
    Bahubali,
    stars,
    avatar,
    titanic,
    minions,
    arrival,
    Deadpool,
    Moonlight,
    ]

# print movie rating
print media.Movie.valid_rating

# prepare movie trailer page and load it.
fresh_tomatoes.open_movies_page(movies)
