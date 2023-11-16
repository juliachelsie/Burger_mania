from django.contrib import admin
from .models import Customer, Booking, Restaurant, Table

# Register your models here.

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Restaurant)
admin.site.register(Table)
