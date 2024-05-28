
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('booking_details/<int:id>/', views.booking_details, name='booking_details'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
]
