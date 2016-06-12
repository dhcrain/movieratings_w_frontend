from django import forms

from movieratings.models import Rating


class RatingForm(forms.ModelForm):


    class Meta:
        model = Rating
        fields = ('rating',)
