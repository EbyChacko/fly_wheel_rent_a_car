from django import forms
from cars.models import Car, Categories, Fuel, GearBox, Seats, Cities, PersonalDetails
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.utils import timezone
from django.forms import ModelChoiceField
from django.forms import widgets

class CarForm(forms.ModelForm):
    category = ModelChoiceField(
        queryset=Categories.objects.all(), empty_label="Select Category", required=False,
        widget=forms.Select(attrs={'placeholder': 'Select Category'})
    )
    fuel = ModelChoiceField(
        queryset=Fuel.objects.all(), empty_label="Select Fuel Type", required=False,
        widget=forms.Select(attrs={'placeholder': 'Select Fuel Type'})
    )
    gear_box = ModelChoiceField(
        queryset=GearBox.objects.all(), empty_label="Select Gear Box", required=False,
        widget=forms.Select(attrs={'placeholder': 'Select Gear Box'})
    )
    city = ModelChoiceField(
        queryset=Cities.objects.all(), empty_label="Select City", required=False,
        widget=forms.Select(attrs={'placeholder': 'Select City'})
    )
    class Meta:
        model = Car
        fields = [
            'image', 'make', 'model', 'category', 'year', 'rent', 'fuel', 
            'seats', 'doors', 'gear_box', 'large_bags', 'small_bags', 
            'air_condition', 'abs', 'rating', 'city'
        ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Upload Image'}),
            'make': forms.TextInput(attrs={'placeholder': 'Car Make'}),
            'model': forms.TextInput(attrs={'placeholder': 'Car Model'}),
            'category': forms.Select(attrs={'placeholder': 'Select Category'}),
            'year': forms.NumberInput(attrs={'min': 1886, 'placeholder': 'Year of Manufacture'}),
            'rent': forms.NumberInput(attrs={'placeholder': 'Rent per Day'}),
            'fuel': forms.Select(attrs={'placeholder': 'Select Fuel Type'}),
            'seats': forms.NumberInput(attrs={'placeholder': 'Number of Seats'}),
            'doors': forms.NumberInput(attrs={'placeholder': 'Number of Doors'}),
            'gear_box': forms.Select(attrs={'placeholder': 'Select Gear Box'}),
            'large_bags': forms.NumberInput(attrs={'placeholder': 'Number of Large Bags'}),
            'small_bags': forms.NumberInput(attrs={'placeholder': 'Number of Small Bags'}),
            'air_condition': forms.CheckboxInput(attrs={'placeholder': 'Air Condition'}),
            'abs': forms.CheckboxInput(attrs={'placeholder': 'ABS'}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1, 'placeholder': 'Rating (0-5)'}),
            'city': forms.Select(attrs={'placeholder': 'Select City'}),
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


class CityForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['city', 'county']
        widgets = {
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter city name',
                'class': 'form-control'
            }),
            'county': forms.TextInput(attrs={
                'placeholder': 'Enter county name',
                'class': 'form-control'
            }),
        }

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city:
            raise ValidationError('City name cannot be empty')
        return city

    def clean_county(self):
        county = self.cleaned_data.get('county')
        if not county:
            raise ValidationError('County name cannot be empty')
        return county


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = [
            'title', 'name', 'date_of_birth', 'mobile', 
            'address_1', 'address_2', 'town', 
            'county', 'eir_code', 'country'
        ]
        widgets = {
            'title': forms.Select(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Date of Birth (YYYY-MM-DD)', 'class': 'form-control', 'type': 'date'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address Line 1', 'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address Line 2', 'class': 'form-control'}),
            'town': forms.TextInput(attrs={'placeholder': 'Town/City', 'class': 'form-control'}),
            'county': forms.Select(attrs={'placeholder': 'County', 'class': 'form-control'}),
            'eir_code': forms.TextInput(attrs={'placeholder': 'Eir Code', 'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("Enter a valid mobile number.")
        if len(mobile) < 10 or len(mobile) > 15:
            raise forms.ValidationError("Mobile number must be between 10 to 15 digits.")
        return mobile

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth >= timezone.now().date():
            raise forms.ValidationError("Date of birth must be in the past.")
        return date_of_birth