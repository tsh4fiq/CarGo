from django.db import models

# Create your models here.


class ListingsModel(models.Model):
    location = models.TextField(max_length=40)
    owner = models.TextField(max_length=40)
    car_type = models.TextField(max_length=40)
    gas_percent = models.IntegerField(max_length=40)
    mileage = models.IntegerField(max_length=40)
    make_model = models.TextField(max_length=40)
    renter = models.TextField(max_length=40, null=True, blank=True)
