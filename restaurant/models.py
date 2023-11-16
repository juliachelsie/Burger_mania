from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Customer(models.Model):
    email = models.EmailField(blank=False, default=None)
    first_name = models.CharField(max_length=200, blank=False, default=None)
    last_name = models.CharField(max_length=200, blank=False, default=None)
    phone_number = models.IntegerField(blank=False, default=None)


class Booking(models.Model):
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    email = models.EmailField(blank=False, default=None)
    first_name = models.CharField(max_length=200, blank=False, default=None)
    last_name = models.CharField(max_length=200, blank=False, default=None)
    phone_number = models.IntegerField(blank=False, default=None)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    size = models.IntegerField()
