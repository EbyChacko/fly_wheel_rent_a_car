from django import forms
from .models import CustomerMessage
from django.forms import widgets
import re


# form fo the customer message in the contact.html
class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ['name', 'mobile', 'email', 'message']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control text-start', 'placeholder': 'Your Name'}),
            'mobile': widgets.TextInput(attrs={'class': 'form-control text-start', 'placeholder': 'Your Mobile Number'}),
            'email': widgets.TextInput(attrs={'class': 'form-control text-start', 'placeholder': 'Your e-mail address'}),
            'message': widgets.Textarea(attrs={'class': 'form-control text-start', 'placeholder': 'Your Message', 'rows': 15, 'cols': 36}),
        }

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