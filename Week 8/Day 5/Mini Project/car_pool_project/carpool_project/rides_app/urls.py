from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('enter_ride', views.enter_ride, name='travelers'),
    path('see_rides/<int:traveler_id>/', views.see_rides, name='trips'),
    path('see_drivers', views.see_drivers, name='drivers'),
    path('find_ride', views.find_ride, name='select'),
    path('join_ride/<int:ride_id>/<int:traveler_id>/', views.join_ride, name='join_trip'),
    path('create_traveler/', views.start_traveler, name='create_trip'),
    
]