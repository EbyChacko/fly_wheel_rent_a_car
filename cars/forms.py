from django import forms
from django.core.exceptions import ValidationError
from .models import Cities, Categories, Fuel, GearBox, Seats, Booking
from django.utils import timezone
from django.forms import TypedChoiceField
from django.forms import widgets
from datetime import date, datetime
import time
import re

SEATS_CHOICES = [(i, str(i)) for i in range(2, 11)]

class CarRentalForm(forms.Form):
    pick_up_location = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        label='Pick-up Location',
        empty_label="Select Pick-up location")
    drop_off_location = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        label='Drop-off Location',
        empty_label="Select Drop-off location")
    pick_up_date = forms.DateField(
        label='Pick-up Date',
        widget=forms.DateInput(attrs={'type': 'date'}))
    pick_up_time = forms.TimeField(
        label='Pick-up Time',
        widget=forms.TimeInput(attrs={'type': 'time'}))
    drop_off_date = forms.DateField(
        label='Drop-off Date',
        widget=forms.DateInput(attrs={'type': 'date'}))
    drop_off_time = forms.TimeField(
        label='Drop-off Time',
        widget=forms.TimeInput(attrs={'type': 'time'}))

    def clean(self):
        cleaned_data = super().clean()
        pick_up_date = cleaned_data.get("pick_up_date")
        pick_up_time = cleaned_data.get("pick_up_time")
        drop_off_date = cleaned_data.get("drop_off_date")
        drop_off_time = cleaned_data.get("drop_off_time")
        now = timezone.now().date()

        if pick_up_date and pick_up_date < now:
            raise ValidationError("Pick-up date cannot be before today")

        if drop_off_date and drop_off_date < now:
            raise ValidationError("Drop-off date cannot be before today")

        if pick_up_date and drop_off_date and pick_up_date > drop_off_date:
            raise ValidationError("Pick-up date cannot be after drop-off date")

        if pick_up_date == drop_off_date and pick_up_time >= drop_off_time:
            raise ValidationError("Pick-up time must be before drop-off time")



class CarFilterForm(forms.Form):
    pick_up_location = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        label='Pick-up Location',
        empty_label="Select Pick-up location")
    drop_off_location = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        label='Drop-off Location',
        empty_label="Select Drop-off location")
    pick_up_date = forms.DateField(
        label='Pick-up Date',
        widget=forms.DateInput(attrs={'type': 'date'}))
    pick_up_time = forms.TimeField(
        label='Pick-up Time',
        widget=forms.TimeInput(attrs={'type': 'time'}))
    drop_off_date = forms.DateField(
        label='Drop-off Date',
        widget=forms.DateInput(attrs={'type': 'date'}))
    drop_off_time = forms.TimeField(
        label='Drop-off Time',
        widget=forms.TimeInput(attrs={'type': 'time'}))
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        label='Category',
        empty_label="Select Category", required=False)
    fuel = forms.ModelChoiceField(
        queryset=Fuel.objects.all(),
        label='Fuel',
        empty_label="Select Fuel", required=False)
    gear_box = forms.ModelChoiceField(
        queryset=GearBox.objects.all(),
        label='Gear Box',
        empty_label="Select Gear-Box", required=False)
    seats = forms.ModelChoiceField(
        queryset=Seats.objects.all(),
        label="Select Number of Seats",
        empty_label="Choose seats", required=False)

    def clean(self):
        cleaned_data = super().clean()
        pick_up_date = cleaned_data.get("pick_up_date")
        pick_up_time = cleaned_data.get("pick_up_time")
        drop_off_date = cleaned_data.get("drop_off_date")
        drop_off_time = cleaned_data.get("drop_off_time")
        now = timezone.now().date()

        if pick_up_date and pick_up_date < now:
            raise ValidationError("Pick-up date cannot be before today")

        if drop_off_date and drop_off_date < now:
            raise ValidationError("Drop-off date cannot be before today")

        if pick_up_date and drop_off_date and pick_up_date > drop_off_date:
            raise ValidationError("Pick-up date cannot be after drop-off date")

        if pick_up_date == drop_off_date and (pick_up_time is None or drop_off_time is None or pick_up_time >= drop_off_time):
            raise ValidationError(
                "Pick-up time must be before drop-off time if on the same day")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['title', 'name', 'email', 'mobile', 'date_of_birth', 'address_1', 'address_2', 'town', 'county', 'eir_code', 'country', 'licence_number', 'licence_expiry', 'personal_id', 'country_issued', 'id_number', 'id_expiry', ]
        widgets = {
            'title': widgets.Select(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'mobile': widgets.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address_1': widgets.TextInput(attrs={'class': 'form-control'}),
            'address_2': widgets.TextInput(attrs={'class': 'form-control'}),
            'town': widgets.TextInput(attrs={'class': 'form-control'}),
            'county': widgets.Select(attrs={'class': 'form-control'}),
            'eir_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'licence_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'licence_expiry': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'personal_id': widgets.Select(attrs={'class': 'form-control'}),
            'id_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'country_issued':widgets.Select(attrs={'class': 'form-control'}),
            'id_expiry': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get request object from kwargs
        super(BookingForm, self).__init__(*args, **kwargs)

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Please enter a valid email address.")
        return email

    def clean_date_of_birth(self):
        today = date.today()
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > today:
            raise forms.ValidationError("Date of birth cannot be in the future.")
        if date_of_birth:
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise forms.ValidationError("The driver must be at least 18 years old.")
        return date_of_birth

    def clean_licence_expiry(self):
        licence_expiry = self.cleaned_data.get('licence_expiry')
        drop_off_date_str = self.request.session.get('drop_off_date')
        drop_off_date = datetime.strptime(drop_off_date_str, '%Y-%m-%d').date()

        if not licence_expiry:
            raise forms.ValidationError("Please enter your licence expiry date.")

        if licence_expiry <= drop_off_date:
            raise forms.ValidationError("Licence expiry must be after the drop-off date.")

        return licence_expiry

    def clean_id_expiry(self):
        id_expiry = self.cleaned_data.get('id_expiry')
        drop_off_date_str = self.request.session.get('drop_off_date')
        drop_off_date = datetime.strptime(drop_off_date_str, '%Y-%m-%d').date()

        if not id_expiry:
            raise forms.ValidationError("Please enter your ID expiry date.")

        if id_expiry <= drop_off_date:
            raise forms.ValidationError("ID expiry must be after the drop-off date.")

        return id_expiry