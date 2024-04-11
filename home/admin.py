from django.contrib import admin
from .models import CustomerMessage


# register the Customer message in the admin pannel
@admin.register(CustomerMessage)
class messageAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'message')
    search_fields = ('name', 'mobile', 'email')