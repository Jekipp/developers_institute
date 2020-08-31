from django.db import models

# Create your models here.

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.Textfield()
#     price = models.IntegerField()
#     image = models.ImageField(upload_to='images/')
#     optional_item = models.BooleanField(default=False)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    meat_tray = models.BooleanField(default=False)
    fish_tray = models.BooleanField(default=False)
    price = models.IntegerField(default=230)
