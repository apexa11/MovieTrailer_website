import fresh_tomatoes
import media

# create instances for movie list and information

fast_and_furious = media.Movie('fast and furious',
                               'its about racing cars',
                               'http://t1.gstatic.com/'
                               'images?q=tbn:ANd9GcReedjA2vJSO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7',
                               'https://youtu.be/PrgNK7KKoiw' )
                             
Bahubali = media.Movie('Bahubali',
                       'Two brothers clash for control of a kingdom.',
                       'http://www.cinejosh.com/'
                       'newsimg/newsmainimg/bahubali-maa-tv-premieres-on-october-25_b_2909150516.jpg',
                       'https://www.youtube.com/watch?v=sOEg_YZQsTI')

stars = media.Movie('fault in our stars', 'its about lovestory',
                    'http://wskg.org/wp-content/uploads/2017/01/0421-1.jpg'
                    , 'https://www.youtube.com/watch?v=9ItBvH5J6ss')

avatar = media.Movie('avatar',
                     "On the lush alien world of Pandora live the Na'vi"
                     "beings who appear primitive but are highly evolved."
                     "Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars"
                     "must link to human minds to allow for free movement on Pandora.",
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg ',
                     'https://www.youtube.com/watch?v=uZNHIU3uHT4')

titanic = media.Movie('titanic',
                      'about love story',
                      'https://images-na.ssl-images-amazon.com/'
                      'images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR88,0,630,1200_AL_.jpg '
                      ,'https://www.youtube.com/watch?v=IVqpcSqokkw')

minions = media.Movie('minions',
                      'Evolving from single-celled yellow organisms at the dawn of time, Minions live to serve'
                      'but find themselves working for a continual series of unsuccessful masters'
                      'from T. Rex to Napoleon. Without a master to grovel for, the Minions fall into a deep depression. ',
                      'https://images-na.ssl-images-amazon.com/'
                      'images/M/MV5BMTg2MTMyMzU0M15BMl5BanBnXkFtZTgwOTU3ODk4NTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg  '
                      ,'https://www.youtube.com/watch?v=TDBYGMe93jo')

arrival = media.Movie('Arrival',
                      'Linguistics professor Louise Banks (Amy Adams) leads an elite team of investigators when gigantic'
                      'spaceships touch down in 12 locations around the world.',
                      'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg',
                      'https://www.youtube.com/watch?v=wu8_5TGwr90')

Deadpool = media.Movie('Deadpool', 'about spider and their life story',
                       'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
                       'https://www.youtube.com/watch?v=0LmwToJlefE')

Moonlight = media.Movie('Moonlight',
                        'A look at three defining chapters in the life of Chiron, a young black man growing up in Miami.'
                        'His epic journey to manhood is guided by the kindness,'
                        'support and love of the community that helps raise him.'
                        ,'https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png'
                        , 'https://www.youtube.com/watch?v=2gCc6kGpXdw')

# movie list

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

# adding file for outlook or design

fresh_tomatoes.open_movies_page(movies)


			
