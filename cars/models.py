from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid

class Cities(models.Model):
    city = models.CharField(max_length=250)
    county = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['city','county']
    
    def __str__(self):
        return f"{self.city}, {self.county}"


class County(models.Model):
    county = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "counties"
        ordering = ['county']
    def __str__(self):
        return f"{self.county}"


class Categories(models.Model):
    category = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['category']
    
    def __str__(self):
        return f"{self.category}"


class Fuel(models.Model):
    fuel = models.CharField(max_length=250)

    class Meta:
        ordering = ['fuel']
    
    def __str__(self):
        return f"{self.fuel}"


class GearBox(models.Model):
    gear_box = models.CharField(max_length=250)

    class Meta:
        ordering = ['gear_box']
    
    def __str__(self):
        return f"{self.gear_box}"


class Seats(models.Model):
    seats = models.IntegerField()

    class Meta:
        verbose_name_plural = "Seats"
        ordering = ['seats']
    
    def __str__(self):
        return f"{self.seats}"


class Title(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title}"


class PersonalId(models.Model):
    personal_id = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Personal IDs"
        ordering = ['personal_id']
    
    def __str__(self):
        return f" {self.personal_id}"

class Car(models.Model):
    image = models.ImageField(upload_to='images/')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    year = models.IntegerField()
    rent = models.IntegerField()
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    seats = models.ForeignKey(Seats, on_delete=models.CASCADE)
    doors = models.IntegerField()
    gear_box = models.ForeignKey(GearBox, on_delete=models.CASCADE)
    large_bags = models.IntegerField()
    small_bags = models.IntegerField()
    air_condition = models.BooleanField(default=False)
    abs = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model} - {self.city}"


class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address_1 = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    town = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    eir_code = models.CharField(max_length=10)
    country = CountryField()

    def __str__(self):
        return f"{self.user.username}"
    class Meta:
        verbose_name_plural = "Personal Details"
        ordering = ['name']

