from django.db import models

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

    def __str__(self):
        return f"{self.make} {self.model}"