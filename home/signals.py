from django.dispatch import receiver
from django.urls import reverse
from django.http import HttpResponseRedirect
from allauth.account.signals import user_logged_in
from django.shortcuts import redirect
from cars.models import PersonalDetails

@receiver(user_logged_in)
def check_personal_details(sender, request, user, **kwargs):
    try:
        personal_details = PersonalDetails.objects.get(user=user)
        if not personal_details:
            return HttpResponseRedirect(reverse('update_profile'))
    except PersonalDetails.DoesNotExist:
        return HttpResponseRedirect(reverse('update_profile'))
