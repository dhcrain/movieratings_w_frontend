from django.shortcuts import render
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating
from movieratings.models import Average
from movieratings.forms import RatingForm
from django.db.models import Avg
from datetime import datetime
from django.shortcuts import redirect

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
        "rating_count": Average.objects.get(movie_id=movie_id),
        "average_rating": Average.objects.get(movie_id=movie_id),
        "genre": Movie.genre_getter,
    }
    return render(request, 'movie.html', context)
# list(Rating.objects.filter(item_id=movie_id).aggregate(Avg('rating')).values())[0]
# Rating.objects.filter(item_id=movie_id).count()


def rater_view(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "rating": Rating.objects.filter(user_id=rater_id),
        "rating_count": Rating.objects.filter(user_id=rater_id).count()
    }
    return render(request, 'rater.html', context)


def add_movie(request):
    # add a page with a form to add a movie
    return None


def rate_movie(request, movie_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = 944
            post.item_id = movie_id
            post.timestamp = datetime.datetime.now()
            post.save()
            return redirect('movie', movie_id=movie_id)
    else:
        form = RatingForm()

    context = {
        "movie": Movie.objects.get(id=movie_id),
        "form": form
    }
    return render(request, 'rate_movie.html', context)
