from django.contrib import admin
from movieratings.models import Rater
from movieratings.models import Rating
from movieratings.models import Movie
from movieratings.models import Average

# Register your models here.
admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Average)
