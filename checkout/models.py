from django.db import models

from cars.models import PersonalDetails, Car, Title, County
from cars.models import PersonalId
from django_countries.fields import CountryField
import uuid


class Booking(models.Model):
    """model to store the booking dtails"""
    booking_number = models.CharField(
        max_length=32, null=False, editable=False)
    customer = models.ForeignKey(
        PersonalDetails, on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pick_up_city = models.CharField(max_length=250)
    pick_up_county = models.CharField(max_length=250)
    drop_off_city = models.CharField(max_length=250)
    drop_off_county = models.CharField(max_length=250)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()
    pick_up_time = models.TimeField()
    drop_off_time = models.TimeField()
    booking_time = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    town = models.CharField(max_length=100)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, blank=True, null=True)
    eir_code = models.CharField(max_length=10)
    country = CountryField()
    licence_number = models.CharField(max_length=20)
    licence_expiry = models.DateField()
    personal_id = models.ForeignKey(
        PersonalId, on_delete=models.CASCADE, blank=True, null=True)
    id_number = models.CharField(max_length=20)
    country_issued = CountryField()
    id_expiry = models.DateField()
    booster_seat = models.IntegerField(default=False)
    booster_total = models.IntegerField(default=False)
    child_seat = models.IntegerField(default=False)
    childseat_total = models.IntegerField(default=False)
    infant_car_capsule = models.IntegerField(default=False)
    infant_total = models.IntegerField(default=False)
    total_rent = models.IntegerField()
    grand_total = models.IntegerField()
    days = models.IntegerField()
    hours = models.IntegerField()
    stripe_pid = models.CharField(max_length=254, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def _generate_booking_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        customer_username = (
            self.customer.user.username if self.customer and
            self.customer.user else "Unknown Customer")
        return f"{customer_username} - {self.car}, {self.booking_number}"
