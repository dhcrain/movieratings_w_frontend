from django.shortcuts import render
from statistics import mean
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating
from movieratings.models import Average
from django.db.models import Avg
from django.db.models import Count
# Create your views here.


def index_view(request):
    context = {
        "top_20": Average.objects.filter(rating_count__gt=100).order_by("-movie_rating")[:20],
        "avg_list": Average.objects.get(id=1)
    }
    return render(request, 'index.html', context)


def movie_view(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "rating": Rating.objects.filter(item_id=movie_id),
        "rating_count": Rating.objects.filter(item_id=movie_id).count(),
        "average_rating": list(Rating.objects.filter(item_id=movie_id).aggregate(Avg('rating')))[0],
        "genre": Movie.genre_getter,
    }
    return render(request, 'movie.html', context)


def rater_view(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "rating": Rating.objects.filter(user_id=rater_id),
        "rating_count": Rating.objects.filter(user_id=rater_id).count()
        # "movies": Movie.objects.filter(id=rater_id),     # get the movies this rater has rated?
    }
    return render(request, 'rater.html', context)


def add_movie(request):
    # add a page with a form to add a movie
    return None