from django.shortcuts import render, redirect, HttpResponse
from .forms import TravelerForm, TripForm, DestinationForm
from .models import Traveler, Trip, TripRequest
# Create your views here.


def traveler(request):
    form = TravelerForm()
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            traveler = form.save()
            if request.POST.get('traveler_type') == 'driver':
                return redirect('new_trip', traveler.id)
            return redirect('all_trips', traveler.id)
    return render(request, 'traveler.html', {'form': form})


def new_trip(request, traveler_id):
    driver = Traveler.objects.get(id=traveler_id)
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.driver = driver
            trip.save()
            return redirect('single_trip', trip.id, traveler_id)
        # add message form failed
    form = TripForm()
    return render(request, 'new_trip.html', {'form': form})
        


def join_trip(request, trip_id, traveler_id):
    passenger = Traveler.objects.get(id=traveler_id)
    trip = Trip.objects.get(id=trip_id)
    trip.passengers.add(passenger)
    return redirect('single_trip', trip_id, traveler_id)


def all_trips(request, traveler_id):
    trips = Trip.objects.all()
    form = DestinationForm()
    traveler = Traveler.objects.get(id = traveler_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')
            if request.POST.get('request_trip') == 'True':
                trip_request = TripRequest.objects.create(start=start, end=end, requester=traveler)
            trips = Trip.objects.filter(start=start, end=end)
    return render(request, 'all_trips.html', {'trips': trips, 'form': form, 'traveler_id': traveler_id, 'traveler': traveler})


def single_trip(request, trip_id, traveler_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'single_trip.html', {'trip': trip, 'traveler_id': traveler_id})


def request_trip(request, traveler_id):
    form = DestinationForm()
    traveler = Traveler.objects.get(id = traveler_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')

def pending_trips(request, traveler_id):
    pending = TripRequest.objects.all()
    request_from = Traveler.objects.filter(id=traveler_id,)

    return render(request, 'pending_trips.html', {'pending': pending, 'request_from': request_from, 'traveler_id': traveler_id})
    
def make_request(request, triprequest_id, traveler_id):
    driver = Traveler.objects.get(id=traveler_id)
    triprequest = TripRequest.objects.get(id=triprequest_id)
    trip = Trip.objects.create(driver = driver, start=triprequest.start, end=triprequest.end)
    trip.passengers.add(triprequest.requester)
    return redirect('single_trip', trip.id, traveler_id)

def waitlist(request, triprequest_id, traveler_id):
    waitlisted = Traveler.objects.get(id=traveler_id)
    triprequest = TripRequest.objects.get(id=triprequest_id)
    triprequest.waitlist.add(waitlisted)
    return redirect('pending_trips', waitlisted.id)



