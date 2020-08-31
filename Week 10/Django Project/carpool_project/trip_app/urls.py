from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('traveler', views.traveler, name='travelers'),
    path('new_trip/<int:traveler_id>', views.new_trip, name='new_trip'),
    path('join_trip/<int:trip_id>/<int:traveler_id>', views.join_trip, name='join'),
    path('all_trips/<int:traveler_id>', views.all_trips, name='all_trips'),
    path('single_trip/<int:trip_id>/<int:traveler_id>', views.single_trip, name='single_trip'),
    path('pending_trips/<int:traveler_id>', views.pending_trips, name='pending_trips'),
    path('make_request/<int:triprequest_id>/<int:traveler_id>', views.make_request, name='make_request'),
    path('waitlist/<int:triprequest_id>/<int:traveler_id>', views.waitlist, name='waitlist')
]

