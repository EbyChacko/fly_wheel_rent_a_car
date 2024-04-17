from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    image = models.ImageField(upload_to='images/')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    rent = models.IntegerField()
    fuel = models.CharField(max_length=100)
    seats = models.IntegerField()
    doors = models.IntegerField()
    gear_box = models.CharField(max_length=100)
    large_bags = models.IntegerField()
    small_bags = models.IntegerField()
    air_condition = models.BooleanField(default=False)
    abs = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    city = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.make} {self.model}"


class Cities(models.Model):
    city = models.CharField(max_length=250)
    county = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['city','county']
    
    def __str__(self):
        return f"{self.city}, {self.county}"


class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    address_1 = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    eir_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Personal Details"


class Booking(models.Model):
    customer = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pick_up_location = models.CharField(max_length=250)
    drop_off_location = models.CharField(max_length=250)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()
    pick_up_time = models.TimeField()
    drop_off_time = models.TimeField()
    booking_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    eir_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=20)
    licence_expiry = models.DateField()
    personal_id = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    id_expiry = models.DateField()
    full_cover = models.BooleanField(default=False)
    booster_seat = models.BooleanField(default=False)
    child_seat = models.BooleanField(default=False)
    infant_car_capsule = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.customer.user.username} - {self.car}"
