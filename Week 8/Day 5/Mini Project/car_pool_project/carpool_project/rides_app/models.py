from django.db import models
from datetime import datetime

# Create your models here.
DESTINATIONS = [
    ('gush dan', 'Gush Dan'),
    ('tel aviv', 'Tel Aviv'),
    ('netanya', 'Netanya'),
    ('jerusalem', 'Jerusalem'),
    ('modiin', 'Modiin'),
    ('judea', 'Judea'),
    ('haifa', 'Haifa'),
    ('kinneret', 'Kinneret'),
    ('ber sheva', 'Ber Sheva'),
    ('dead sea', 'Dead Sea'),
]

class Traveler(models.Model):
    
    destination = models.CharField(max_length=20, choices=DESTINATIONS, default = 'gush dan')
    traveler_name = models.CharField(max_length=100)
    def __str__(self):
        return self.traveler_name
    # driver = models.BooleanField(default=False)
    
class Trip(models.Model):
    driver = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='driver_trips')
    passengers = models.ManyToManyField(Traveler, related_name='passengers_trips')
    ride_start = models.CharField(max_length=20, choices=DESTINATIONS, default = 'gush dan')
    ride_end = models.CharField(max_length=20, choices=DESTINATIONS, default = 'gush dan')
    ride_time = models.DateTimeField(null=True, blank=True)
    num_seats = models.IntegerField(default=1)

