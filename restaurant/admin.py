from django.contrib import admin
from .models import Booking, Restaurant, Table, Reservation

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Booking)
admin.site.register(Restaurant)
admin.site.register(Table)
