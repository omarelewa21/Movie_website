'''This module contanis a list of six favourite movies to be displayed on a local website.
    Each movie object provies 4 types of information abou the movie:
    - title 
    - storyline 
    - poster image
    - youtube trailer'''


import media
import fresh_tomatoes


night_crawler = media.Movie("Night Crawler",
                            "A story of a man who is willing to do anything for getting to his goal",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcSmbiO41jmiTPaGUv1I61kVqe-JPxfpkSfw20i6QfvGv5Zqd7jP",
                            "https://www.youtube.com/watch?v=u1uP_8VJkDQ")

persuit_of_happiness = media.Movie("Persuit of happiness",
                                   "A stroy of man who struggles in life not to fail and be successful",
                                   "http://www.gstatic.com/tv/thumb/movieposters/162523/p162523_p_v8_ad.jpg",
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg")

groundhog_day = media.Movie("Groundhog day",
                            "A weatherman finds himself inexplicably living the same day over and over",
                            "http://www.gstatic.com/tv/thumb/movieposters/14569/p14569_p_v8_ay.jpg",
                            "https://www.youtube.com/watch?v=tSVeDx9fk60")

Novitiate = media.Movie("Novitiate",
                        "A story of a young woman who decides to grant herself for jesus then, starts question herself about her faith.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c2/Novitiate_film_poster.jpg",
                        "https://www.youtube.com/watch?v=8kKexutLfE0")

cast_away = media.Movie("Cast Away",
                        "A man survives alone on an island and finds a way to get home after 4 years there.",
                        "http://www.gstatic.com/tv/thumb/movieposters/26553/p26553_p_v8_at.jpg",
                        "https://www.youtube.com/watch?v=2TWYDogv4WQ")

brave_heart = media.Movie("Braveheart",
                          "William Wallace leads his countryr scotland to a war against English army who slautered his wife",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcSnnenelmzF4MKdtHBnaQYbDstLRExO1brKmrTBe_Ve40Vwq_lO",
                          "https://www.youtube.com/watch?v=1NJO0jxBtMo")

movies = [night_crawler, persuit_of_happiness, groundhog_day, Novitiate, cast_away, brave_heart]
fresh_tomatoes.open_movies_page(movies)
