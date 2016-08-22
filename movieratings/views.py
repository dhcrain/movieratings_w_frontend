from django.shortcuts import render
from movieratings.models import Movie
from movieratings.models import Rater
from movieratings.models import Rating
from movieratings.models import Average
from movieratings.forms import RatingForm
import time
from django.shortcuts import redirect


def index_view(request):
    context = {
        "top_20": Average.objects.filter(rating_count__gt=100).order_by("-movie_rating")[:20],
    }
    return render(request, 'index.html', context)


def movie_view(request, movie_id):
    avg_rating = Average.objects.get(movie_id=movie_id)
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "rating": Rating.objects.filter(item_id=movie_id),
        "rating_count": Average.objects.get(movie_id=movie_id),
        "average_rating": avg_rating.movie_rating/5*100,
        "genre": Movie.genre_getter,        # non-functional
        "user_rating": Rating.objects.filter(item_id=movie_id).filter(user_id=944)
    }
    return render(request, 'movie.html', context)


def rater_view(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "rating": Rating.objects.filter(user_id=rater_id),
        "rating_count": Rating.objects.filter(user_id=rater_id).count()
    }
    return render(request, 'rater.html', context)


def rate_movie(request, movie_id):
    # Need to figure out how to add new reviews to the Average table so it is current
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = Rater.objects.get(id=944)        # 944 is the 'WebUser'
            post.item_id = Movie.objects.get(id=movie_id)
            post.rating = form.cleaned_data['rating']
            post.timestamp = time.time()
            post.save()
            return redirect('movieratings.views.movie_view', movie_id=movie_id)
    else:
        form = RatingForm()

    context = {
        "movie": Movie.objects.get(id=movie_id),
        "form": form
    }
    return render(request, 'rate_movie.html', context)
