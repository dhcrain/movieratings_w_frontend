from django.db import models
from statistics import mean
# Create your models here.


class Rater(models.Model):
    # user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    # movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=15)
    video_release_date = models.CharField(max_length=15, default="")      # empty is OK
    imdb_url = models.CharField(max_length=300)
    unknown = models.CharField(max_length=50)
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    childrens = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentry = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return self.movie_title


class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    # OR user_id = models.ForeignKey("movie.Rater")  ("app_name.Class")
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def top_20(self):
        pass

    # def average_rating(self):
        # for movie in Rating:
        #     all_ratings = []
        #     all_ratings = (Movie.objects.get(Movie.id))
        #
        #     # find the movie is in the Rating table and then get a list of the ratings
        # # all_ratings = map(lambda x: x.rating, self.review_set.all())
        # return mean(all_ratings)

