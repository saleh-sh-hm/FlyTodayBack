from django.contrib import admin
from .models import City,Ticket,Booking,Passenger

# Register your models here.
admin.site.register(City)
admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Passenger)