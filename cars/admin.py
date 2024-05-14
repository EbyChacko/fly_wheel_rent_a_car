
from django.contrib import admin
from .models import Car, Cities, PersonalDetails
from .models import Categories, Fuel, GearBox, Title, Seats
from .models import County, PersonalId

admin.site.register(Car)
admin.site.register(Cities)
admin.site.register(PersonalDetails)
admin.site.register(Categories)
admin.site.register(Fuel)
admin.site.register(GearBox)
admin.site.register(Title)
admin.site.register(Seats)
admin.site.register(County)
admin.site.register(PersonalId)