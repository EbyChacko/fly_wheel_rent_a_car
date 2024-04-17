from django import forms
from django.core.exceptions import ValidationError
from .models import Cities


class CarRentalForm(forms.Form):
    pick_up_location = forms.ModelChoiceField(queryset=Cities.objects.all(),label='Pick-up Location', empty_label="Select Pick-up location")
    drop_off_location = forms.ModelChoiceField(queryset=Cities.objects.all(), label='Drop-off Location', empty_label="Select Drop-off location")
    pick_up_date = forms.DateField(label='Pick-up Date', widget=forms.DateInput(attrs={'type': 'date'}))
    pick_up_time = forms.TimeField(label='Pick-up Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    drop_off_date = forms.DateField(label='Drop-off Date', widget=forms.DateInput(attrs={'type': 'date'}))
    drop_off_time = forms.TimeField(label='Drop-off Time', widget=forms.TimeInput(attrs={'type': 'time'}))

    def clean(self):
        cleaned_data = super().clean()
        pick_up_date = cleaned_data.get("pick_up_date")
        pick_up_time = cleaned_data.get("pick_up_time")
        drop_off_date = cleaned_data.get("drop_off_date")
        drop_off_time = cleaned_data.get("drop_off_time")

        if pick_up_date and drop_off_date and pick_up_date > drop_off_date:
            raise ValidationError("Pick-up date cannot be after drop-off date")

        if pick_up_date == drop_off_date and pick_up_time >= drop_off_time:
            raise ValidationError("Pick-up time must be before drop-off time if on the same day")