from django.contrib import admin
from .models import CustomerMessage



@admin.register(CustomerMessage)
class messageAdmin(admin.ModelAdmin):
    """register the Customer message in the admin pannel"""
    list_display = ('name', 'mobile', 'email', 'message')
    search_fields = ('name', 'mobile', 'email')
