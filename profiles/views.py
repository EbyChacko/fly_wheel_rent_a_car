from django.shortcuts import render, get_object_or_404, redirect
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
        bookings = Booking.objects.filter(customer=customer_details).order_by('-booking_time') if customer_details else []
    except Exception as e:
        messages.error(request, f'Sorry, an error occurred: {e}')

    now = datetime.now()
    context = {
        'customer_details': customer_details,
        'bookings': bookings,
        'now': now,
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
        'disable_delete': disable_delete,
        'time_difference':time_difference,
        'now':now,
        'pick_up_datetime':pick_up_datetime,
    }
    return render(request, 'profiles/booking_details.html', context)


def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    
    if request.user != booking.customer.user:
        messages.error(request, "You are not authorized to delete this booking.")
        return redirect('profile')

    now = datetime.now()
    pick_up_datetime = datetime.combine(booking.pick_up_date, booking.pick_up_time)
    time_difference = pick_up_datetime - now
    disable_delete = time_difference < timedelta(hours=48)
    if disable_delete:
        messages.error(request, "Cannot delete the booking within 48 hours of the pickup time.")
        return redirect('profile')

    booking.delete()
    messages.success(request, "Booking deleted successfully.")
    return redirect('profile')


def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if booking.customer.user != request.user:
        messages.error(request, 'You do not have permission to cancel this booking.')
        return redirect('profile')

    booking.status = 'Canceled'
    booking.save()

    messages.success(request, 'Booking has been canceled successfully.')
    return redirect('profile')