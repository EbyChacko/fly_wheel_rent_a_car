
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search_cars/', views.search_cars, name='search_cars'),
    path('search_result/', views.search_result, name='search_result'),
    path(
        'search_result_update/',
        views.search_result_update,
        name='search_result_update'),
    path('car_details/<int:id>/', views.car_details, name='car_details'),
    path('terms/', views.terms, name='terms'),
    path('add_extras/<int:id>/', views.add_extras, name='add_extras'),
    path('remove_extras/<int:id>/', views.remove_extras, name='remove_extras'),
]
