
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('booking_details/<int:id>/', views.booking_details, name='booking_details'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),
    path('car_and_city/', views.car_and_city, name='car_and_city'),
    path('add_car/', views.add_car, name='add_car'),
    path('delete_car/<int:id>/', views.delete_car, name='delete_car'),
    path('confirm_delete_car/<int:id>/', views.confirm_delete_car, name='confirm_delete_car'),
    path('add_city/', views.add_city, name='add_city'),
    path('delete_city/<int:id>/', views.delete_city, name='delete_city'),
    path('confirm_delete_city/<int:id>/', views.confirm_delete_city, name='confirm_delete_city'),
]
