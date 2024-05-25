from django.shortcuts import render
from django.contrib import messages
from cars.models import PersonalDetails
from checkout.models import Booking

def profile(request):
    bookings = {}
    try:
        customer_details = PersonalDetails.objects.get(user=request.user)
    except PersonalDetails.DoesNotExist:
        customer_details = PersonalDetails(user=request.user)

    try:
        bookings = Booking.objects.filter(customer=customer_details)
        if not bookings:
            messages.info(request, 'Sorry, no bookings yet for this profile.')
    except Exception as e:
        messages.error(request, f'Sorry, an error occurred: {e}')

    context = {
        'customer_details': customer_details,
        'bookings': bookings
    }
    return render(request, 'profiles/profile.html', context)