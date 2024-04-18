from django.shortcuts import render
from .forms import CarRentalForm, CarFilterForm
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
            form = CarFilterForm()
            form = CarFilterForm(initial={
                'pick_up_location': pick_up_location,
                'drop_off_location': drop_off_location,
                'pick_up_date': pick_up_date,
                'pick_up_time': pick_up_time,
                'drop_off_date': drop_off_date,
                'drop_off_time': drop_off_time,
            })

            return render(request, 'cars/search_result.html', {'form': form, 'cars': available_cars})
        else:
            form = CarRentalForm(request.POST)
            return render(request, 'cars/search_cars.html', {'form': form})
    else:
        form = CarRentalForm(request.POST)
        return render(request, 'cars/search_cars.html', {'form': form})


def search_result_update(request):
    if request.method == 'POST':
        form = CarFilterForm(request.POST)
        if form.is_valid():
            pick_up_location = form.cleaned_data['pick_up_location']
            drop_off_location = form.cleaned_data['drop_off_location']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            drop_off_date = form.cleaned_data['drop_off_date']
            drop_off_time = form.cleaned_data['drop_off_time']
            category = form.cleaned_data['category']
            fuel = form.cleaned_data['fuel']
            gear_box = form.cleaned_data['gear_box']
            
            available_cars = Car.objects.filter(city=pick_up_location)
            if category:
                available_cars = available_cars.filter(category=category)
            if fuel:
                available_cars = available_cars.filter(fuel=fuel)
            if gear_box:
                available_cars = available_cars.filter(gear_box=gear_box)

            booked_cars = Booking.objects.filter(
                pick_up_date__lte=drop_off_date,
                drop_off_date__gte=pick_up_date
            ).values_list('car', flat=True)

            available_cars = available_cars.exclude(id__in=booked_cars)

            return render(request, 'cars/search_result.html', {'form': form, 'cars': available_cars})
        else:
            form = CarFilterForm(request.POST)
            return render(request, 'cars/search_result.html', {'form': form})
    else:
        form = CarFilterForm(request.POST)
        return render(request, 'cars/search_result.html', {'form': form})