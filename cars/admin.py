
from django.contrib import admin
from .models import Car, Cities, PersonalDetails,Booking
from .models import Categories, Fuel, GearBox, Title

admin.site.register(Car)
admin.site.register(Cities)
admin.site.register(PersonalDetails)
admin.site.register(Booking)
admin.site.register(Categories)
admin.site.register(Fuel)
admin.site.register(GearBox)
admin.site.register(Title)