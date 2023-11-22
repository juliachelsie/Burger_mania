from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.IntegerField()
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
