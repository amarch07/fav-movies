import webbrowser   # needed to open web site to show trailers
class Movie(): # blueprint filled with data allowing for multiple instances to be created
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_year_released): #class constructor that initializes all data of instance
    self.title = movie_title   # variables associated with instance
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    self.year_released = movie_year_released
  def show_trailer(self): # instance methods
    webbrowser.open(self.trailer_youtube_url)
