from django.shortcuts import render
from movieratings.models import Movie
from movieratings.models import Rater
# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def movie_view(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id)
    }
    return render(request, 'movie.html', context)


def rater_view(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id)
    }
    return render(request, 'rater.html', context)


def add_movie(request):
    # add a page with a form to add a movie
    return None