from django import forms
from django.core.exceptions import ValidationError
from .models import Cities, Categories, Fuel, GearBox, Seats
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
