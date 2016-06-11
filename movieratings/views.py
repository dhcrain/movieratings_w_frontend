from django.shortcuts import render
from statistics import mean
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating
from django.db.models import Avg
# Create your views here.


def index_view(request):
    # pubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]
    # pubs[0].num_books
    context = {
        "top_20": Rating.objects.annotate(top=Avg('rating')).order_by('-top')[:20],
        # "top_20": Rating.objects.annotate(top=Avg('rating')).order_by('top')[:20],

    }
    return render(request, 'index.html', context)


def movie_view(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "rating": Rating.objects.filter(item_id=movie_id),
        "rating_count": Rating.objects.filter(item_id=movie_id).count(),
        "average_rating": Rating.objects.filter(item_id=movie_id).aggregate(Avg('rating'))
    }
    def genre_getter(self):
        if Movie.objects.filter(adventure="1", war="1", comedy="1"):
            print("Adventure")

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