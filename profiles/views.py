from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from cars.models import PersonalDetails
from checkout.models import Booking
from datetime import datetime, timedelta


def profile(request):
    try:
        customer_details = PersonalDetails.objects.get(user=request.user)
    except PersonalDetails.DoesNotExist:
        customer_details = None

    try:
        bookings = Booking.objects.filter(customer=customer_details) if customer_details else []
        if not bookings:
            messages.info(request, 'Sorry, no bookings yet for this profile.')
    except Exception as e:
        messages.error(request, f'Sorry, an error occurred: {e}')

    context = {
        'customer_details': customer_details,
        'bookings': bookings
    }
    return render(request, 'profiles/profile.html', context)

def booking_details(request, id):

    booking = get_object_or_404(Booking, id=id)

    if booking.customer.user != request.user:
        messages.error(request, "You do not have permission to view this booking.")
        return redirect('profile')
    
    now = datetime.now()
    pick_up_datetime = datetime.combine(booking.pick_up_date, booking.pick_up_time)
    time_difference = pick_up_datetime - now
    disable_delete = time_difference < timedelta(hours=48)

    context = {
        'booking': booking,
    }
    return render(request, 'profiles/booking_details.html', context)