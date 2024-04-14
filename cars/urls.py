
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search_cars/', views.search_cars, name='search_cars'),
    path('search_result/', views.search_result, name='search_result'),
]
