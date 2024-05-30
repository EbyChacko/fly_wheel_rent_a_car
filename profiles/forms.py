from django import forms
from cars.models import Car
from checkout.models import Booking
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'image', 'make', 'model', 'category', 'year', 'rent', 'fuel', 
            'seats', 'doors', 'gear_box', 'large_bags', 'small_bags', 
            'air_condition', 'abs', 'rating', 'city'
        ]
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1}),
            'year': forms.NumberInput(attrs={'min': 1886}),
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        current_year = datetime.now().year
        if year < 1886 or year > current_year:
            raise forms.ValidationError(f"Enter a valid year between 1886 and {current_year}.")
        return year

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating must be between 0 and 5.")
        return rating


class cancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']