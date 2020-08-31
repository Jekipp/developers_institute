from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('order_list', views.see_orders, name='list'),
]