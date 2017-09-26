import fresh_tomatoes
import media

# List of moviesto feature on site.
Moonlight = media.Movie('Moonlight',
                        'Story about Gay black Boy',
                        'https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png',#noqa
                        'https://www.youtube.com/watch?v=2gCc6kGpXdw')

arrival = media.Movie('Arrival',
                      'versatile science fiction film.',
                      'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg',#noqa
                      'https://www.youtube.com/watch?v=wu8_5TGwr90')

stars = media.Movie('The Fault in Our Stars',
                    'Lovestory About Life & death',
                    'http://wskg.org/wp-content/uploads/2017/01/0421-1.jpg',#noqa
                    'https://www.youtube.com/watch?v=9ItBvH5J6ss')

avatar = media.Movie('Avatar',
                     "lush alien world of Pandora",
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',#noqa
                     'https://www.youtube.com/watch?v=uZNHIU3uHT4')

titanic = media.Movie('Titanic',
                      'Love story',
                      'http://sim03.in.com/62/70f97856e24185ff5343f3b3046d4449_pt_xl.jpg',#noqa
                      'https://www.youtube.com/watch?v=IVqpcSqokkw')

minions = media.Movie('Minions',
                      'American computer-animated comedy film',
                      'https://images-na.ssl-images-amazon.com/images/I/71-Wt11rDvL._SL1500_.jpg',#noqa
                      'https://www.youtube.com/watch?v=TDBYGMe93jo')

Bahubali = media.Movie('Bahubali',
                       'Two brothers clash for control of a kingdom.',
                       'https://images-na.ssl-images-amazon.com/images/I/711eHgGtnFL._SX385_.jpg',#noqa
                       'https://www.youtube.com/watch?v=sOEg_YZQsTI')
Deadpool = media.Movie('Deadpool',
                       'spider and his life story',
                       'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',#noqa
                       'https://www.youtube.com/watch?v=0LmwToJlefE')

fast_and_furious = media.Movie('Fast and Furious',
                               'A film about racing cars',
                               'https://i.pinimg.com/736x/8e/57/d6/8e57d61b4fedcd6e42bdd83ca7e6ed81--fast--fast-and-forious-.jpg',#noqa
                               'https://youtu.be/PrgNK7KKoiw')
# store movies in list
movies = [
    Moonlight,
    arrival,
    stars,
    avatar,
    titanic,
    minions,
    Bahubali,
    Deadpool,
    fast_and_furious,
    ]

# print movie rating
print media.Movie.valid_rating

# prepare movie trailer page and load it.
fresh_tomatoes.open_movies_page(movies)
