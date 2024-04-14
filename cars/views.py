from django.shortcuts import render
from .forms import CarRentalForm
from .models import Car

def search_cars(request):
    """To load search page"""
    form = CarRentalForm()
    return render(request, 'cars/search_cars.html', {'form': form})


def search_result(request):
    if request.method == 'POST':
        form = CarRentalForm(request.POST)
        cars = Car.objects.all()
        print(cars)
        return render(request, 'cars/search_result.html', {'form': form, 'cars':cars,})
    else:
        form = CarRentalForm()
    return render(request, 'cars/search_result.html', {'form': form})