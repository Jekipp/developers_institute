from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DESTINATIONS = [
    ('tlv', 'Tel Aviv'),
    ('jlm', 'Jerusalem'),
    ('hf', 'Haifa'),
    ('tbr', 'Tiberias'),
    ('br7', 'Ber Sheva'),
]


class Traveler(models.Model):
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Trip(models.Model):
    driver = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='driver_trips')
    passengers = models.ManyToManyField(Traveler, related_name='passengers_trips')
    start = models.CharField(max_length=20, choices=DESTINATIONS, default = 'tlv')
    end = models.CharField(max_length=20, choices=DESTINATIONS, default = 'tlv')
    passenger_seats = models.IntegerField(default=1)

class TripRequest(models.Model):
    requester = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='my_requested_trips')
    waitlist = models.ManyToManyField(Traveler, related_name='waitlists')
    pending = models.BooleanField(default=True)
    start = models.CharField(max_length=20, choices=DESTINATIONS, default = 'tlv')
    end = models.CharField(max_length=20, choices=DESTINATIONS, default = 'tlv')
    