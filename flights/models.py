from django.db import models
from django.conf import settings


class City(models.Model):
    CityName = models.CharField()

    def __str__(self):
        return self.CityName
    

class Ticket(models.Model) :
    origin = models.ForeignKey(City,on_delete=models.CASCADE,related_name='origins')
    destination = models.ForeignKey(City,on_delete=models.CASCADE,related_name='destinations')
    date = models.DateField(blank=True,null=True)
    depart_time = models.TimeField(blank=True,null=True)
    arrival_time = models.TimeField(blank=True,null=True)
    travel_time = models.TimeField(blank=True,null=True)
    airline = models.CharField(blank=True,max_length=20)
    flight_number = models.CharField(blank=True,max_length=20)
    cabin_class = models.CharField(blank=True,max_length=20)
    remaining_capacity = models.PositiveIntegerField(blank=True,null=True)
    allowed_loggage = models.PositiveIntegerField(blank=True,null=True)
    price = models.PositiveIntegerField(blank=True,null=True)

    origin_airport = models.CharField(blank=True,max_length=50)
    dest_airport = models.CharField(blank=True,max_length=50)
    airplane_model = models.CharField(blank=True,max_length=50)
    flight_law = models.TextField(blank=True)
    price_detail = models.TextField(blank=True)
    type = models.CharField(blank=True,null=True,max_length=20)
    
    
    def __str__(self):
        return f'{self.origin} - {self.destination} - {self.date} - {self.depart_time}'
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    national_id = models.CharField(max_length=10)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='bookings')
    passengers = models.ManyToManyField(Passenger)

    def __str__(self):
        return f'Booking {self.id} by {self.user.username}'