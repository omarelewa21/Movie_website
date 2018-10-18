'''This module is called when there is a need to make a list of movies.
    It recieves information regarding movie's:
    - title
    - storyline
    - poster imag
    - youtube trailer
  Then it works with fresh_tomatoes.py to generate a website
  that contains a list of movies'''


import webbrowser


class Movie():
    '''Make movie objects to be displayed'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_trailer_url):
        '''Each movie object should provide 4 types of information:
            movie's title, storyline, poster image and youtube trailer'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer_url

    def show_trailer(self):
        '''Use the module webbrowser
        to open the webbrowser on the movie's youtube trailer'''
        webbrowser.open(self.trailer_youtube_url)#
        