from django.contrib import admin
from .models import CustomerMessage, MailChimpMails


# register the Customer message in the admin pannel
@admin.register(CustomerMessage)
class messageAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'message')
    search_fields = ('name', 'mobile', 'email')


@admin.register(MailChimpMails)
class MailChimpMailsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
