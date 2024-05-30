from django.contrib import admin

from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ['name', 'pick_up_city',
              'pick_up_county', 'drop_off_city', 'drop_off_county', 
              'pick_up_date', 'drop_off_date', 'pick_up_time', 'drop_off_time',
              'booster_seat', 'child_seat',
              'infant_car_capsule', 'grand_total', 
              'days', 'hours', 'status', 'booking_number']

admin.site.register(Booking, BookingAdmin)