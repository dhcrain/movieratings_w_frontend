from django import forms

from movieratings.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rating',)
        # choices = (1, 2, 3, 4, 5)
        # widgets = {
        #     'rating': forms.ChoiceField(choices),
        # }