from django.shortcuts import render
from .forms import CarRentalForm, CarFilterForm
from .models import Car, Booking
from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime
from django.shortcuts import render, get_object_or_404
from django.http import QueryDict

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
            seats = form.cleaned_data['seats']
            
            available_cars = Car.objects.filter(city=pick_up_location)
            if category:
                available_cars = available_cars.filter(category=category)
            if fuel:
                available_cars = available_cars.filter(fuel=fuel)
            if gear_box:
                available_cars = available_cars.filter(gear_box=gear_box)
            if seats:
                available_cars = available_cars.filter(seats=seats)
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


def car_details(request, id):
    car = get_object_or_404(Car, pk=id)

    if request.method == 'GET':
        query_params = request.GET.copy()
        print("Query Params:", query_params)

        form_data = {
            'pick_up_date': query_params.get('pick_up_date'),
            'pick_up_time': query_params.get('pick_up_time'),
            'drop_off_date': query_params.get('drop_off_date'),
            'drop_off_time': query_params.get('drop_off_time'),
        }
        print("Form Data:", form_data)

        form = CarFilterForm(initial=form_data)

    else:
        form = CarFilterForm()

    try:
        if form_data['pick_up_date'] and form_data['pick_up_time']:
            pick_up_datetime = datetime.strptime(f"{form_data['pick_up_date']} {form_data['pick_up_time']}", '%B %d, %Y %I:%M %p')
        else:
            pick_up_datetime = None

        if form_data['drop_off_date'] and form_data['drop_off_time']:
            drop_off_datetime = datetime.strptime(f"{form_data['drop_off_date']} {form_data['drop_off_time']}", '%B %d, %Y %I:%M %p')
        else:
            drop_off_datetime = None
    except ValueError:
        pick_up_datetime = None
        drop_off_datetime = None

    if pick_up_datetime and drop_off_datetime:
        total_hours = (drop_off_datetime - pick_up_datetime).total_seconds() / 3600
        days = int(total_hours // 24)
        hours = total_hours % 24

        if  hours > 5:
            days += 1

        total_rent = days * car.rent

    else:
        days = 1
        total_rent = car.rent
        hours = None

    context = {
        'car': car,
        'pick_up_datetime': pick_up_datetime,
        'drop_off_datetime': drop_off_datetime,
        'days': days,
        'total_rent': total_rent,
        'form': form,
    }

    return render(request, 'cars/car_details.html', context)
