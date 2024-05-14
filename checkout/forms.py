from django import forms
from cars.models import Cities, Categories, Fuel, GearBox, Seats
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms import TypedChoiceField
from django.forms import widgets
from datetime import date, datetime
import time
import re

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['title', 'name', 'email', 'mobile', 'date_of_birth',
                  'address_1', 'address_2', 'town', 'county', 'eir_code',
                  'country', 'licence_number', 'licence_expiry', 'personal_id',
                  'country_issued', 'id_number', 'id_expiry', ]
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
        {
            'title': 'Title',
            'name': 'Name',
            'email': 'E-mail',
            'mobile': 'Mobile number',
            'date_of_birth': 'Date of birth',
            'address_1': 'House number or House name',
            'address_2': 'Place',
            'town': 'Town or City',
            'county': 'County',
            'eir_code': 'Eir code Or Postal code',
            'country': 'Country',
            'licence_number': 'Licence number',
            'licence_expiry': 'Expiry date of your Licence',
            'personal_id': 'Choose Personal ID',
            'id_number': 'ID NUmber',
            'country_issued':'Country that issue your ID',
            'id_expiry': 'Expiry date of your ID',
        }
        self.request = kwargs.pop('request', None)
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