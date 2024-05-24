
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('About_Us/', views.about, name='about'),
    path('login_or_signup/', views.login_or_signup, name='login_or_signup'),
]
