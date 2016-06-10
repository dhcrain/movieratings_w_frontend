from statistics import mean
from movieratings.models import Rating
from movieratings.models import Movie
from movieratings.models import Rater
from django.core.management import setup_environ
from django_movie_ratings_2 import settings

setup_environ(settings)



def average_rating(self):
    # find the movie in the Rating table and then get a list of the ratings
    for movie in Rating.objects.all():
        # all_ratings = []
        # all_ratings = (Movie.objects.get(id=1))
        print(movie.rating)


    # all_ratings = map(lambda x: x.rating, self.review_set.all())

# average_rating()
