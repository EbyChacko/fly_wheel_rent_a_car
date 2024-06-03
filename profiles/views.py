from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cars.models import PersonalDetails, Car, Cities
from checkout.models import Booking
from datetime import datetime, timedelta
from .forms import CarForm, CityForm, PersonalDetailsForm
from django.contrib.auth.decorators import login_required


def profile(request):
    try:
        customer_details = PersonalDetails.objects.get(user=request.user)
    except PersonalDetails.DoesNotExist:
        customer_details = None

    try:
       bookings = Booking.objects.filter(customer=customer_details).exclude(status="Deleted").order_by('-booking_time') if customer_details else []
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


def confirm_delete_booking(request, id):
    context = {
        'id': id,
    }
    return render(request, 'profiles/confirm_delete_booking.html', context)


def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if booking.customer.user != request.user:
        messages.error(request, 'You do not have permission to delete this booking.')
        return redirect('profile')

    booking.status = 'Deleted'
    booking.save()

    messages.success(request, 'Booking has been deleted successfully.')
    return redirect('profile')



def confirm_cancel_booking(request, id):
    context = {
        'id': id,
    }
    return render(request, 'profiles/confirm_cancel_booking.html', context)


def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if booking.customer.user != request.user:
        messages.error(request, 'You do not have permission to cancel this booking.')
        return redirect('profile')

    booking.status = 'Canceled'
    booking.save()

    messages.success(request, 'Booking has been canceled successfully.')
    return redirect('profile')


def car_and_city(request):
    return render(request, 'profiles/car_and_city.html')


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_car')
    else:
        form = CarForm()
    cars = Car.objects.all()
    context={
        'form': form,
        'cars': cars,
    }
    return render(request, 'profiles/add_car.html',  context)


def confirm_delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car,
    }
    return render(request, 'profiles/confirm_delete_car.html', context)


def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    messages.success(request, 'Car details has been removed successfully.')
    return redirect('add_car')


def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_city')
    else:
        form = CityForm()
    cities = Cities.objects.all()
    context={
        'form': form,
        'cities': cities,
    }
    return render(request, 'profiles/add_city.html',  context)


def confirm_delete_city(request, id):
    city = get_object_or_404(Cities, id=id)
    context = {
        'city': city,
    }
    return render(request, 'profiles/confirm_delete_city.html', context)


def delete_city(request, id):
    city = get_object_or_404(Cities, id=id)
    city.delete()
    messages.success(request, 'City details has been removed successfully.')
    return redirect('add_city')

@login_required
def update_profile(request):
    try:
        personal_details = PersonalDetails.objects.get(user=request.user)
    except PersonalDetails.DoesNotExist:
        personal_details = PersonalDetails(user=request.user)

    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal details updated successfully.')
            return redirect('profile')
    else:
        form = PersonalDetailsForm(instance=personal_details)

    return render(request, 'profiles/update_profile.html', {'form': form})