from django.shortcuts import render, redirect
from .forms import TravelerForm, TripForm
from .models import Traveler, Trip

# Create your views here.
def enter_ride(request):
    form = TravelerForm()
    form2 = TripForm()
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        form2 = TripForm(request.POST)
        if form.is_valid():
            ride = form.save()
            if form2.is_valid():
                trip = form2.save(commit=False)
                trip.driver = ride
                trip.save()
    return render(request, 'index.html', {'form': form, 'form2': form2})



def see_drivers(request):
    drivers = Traveler.objects.filter(driver=True)
    return render(request, 'see_drivers.html', {'drivers': drivers})

def find_ride(request):
    passengers = Traveler.objects.filter(driver=False)
    drivers = Traveler.objects.filter(driver=True)
    context = {
        'passengers' : passengers,
        'drivers' : drivers
    }
    return render(request, 'find_ride.html', context)


def see_rides(request, traveler_id):
    trips = Trip.objects.all()
    

    return render(request, 'see_rides.html', {'trips': trips, 'traveler_id': traveler_id})

def join_ride(request, ride_id, traveler_id):
    traveler = Traveler.objects.get(id=traveler_id)
    trip = Trip.objects.get(id=ride_id)
    trip.passengers.add(traveler)
    return redirect('trips', traveler_id)


def start_traveler(request):
    form = TravelerForm()
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            ride = form.save()
            return redirect('trips', ride.id)
    return render(request, 'index.html', {'form': form})




