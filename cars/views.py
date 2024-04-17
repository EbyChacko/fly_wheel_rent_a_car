from django.shortcuts import render
from .forms import CarRentalForm
from .models import Car, Booking

def search_cars(request):
    """To load search page"""
    form = CarRentalForm()
    return render(request, 'cars/search_cars.html', {'form': form})


def search_result(request):
    if request.method == 'POST':
        form = CarRentalForm(request.POST)
        if form.is_valid():
            pick_up_location = form.cleaned_data['pick_up_location']
            drop_off_location = form.cleaned_data['drop_off_location']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            drop_off_date = form.cleaned_data['drop_off_date']
            drop_off_time = form.cleaned_data['drop_off_time']

            available_cars = Car.objects.filter(city=pick_up_location)

            booked_cars = Booking.objects.filter(
                pick_up_date__lte=drop_off_date,
                drop_off_date__gte=pick_up_date
            ).values_list('car', flat=True)

            available_cars = available_cars.exclude(id__in=booked_cars)

            return render(request, 'cars/search_result.html', {'form': form, 'cars': available_cars})
        else:
            form = CarRentalForm(request.POST)
            return render(request, 'cars/search_cars.html', {'form': form})
    else:
        form = CarRentalForm()
        return render(request, 'cars/search_cars.html', {'form': form})