from django.db import models

# Create your models here.
class swiggy(models.Model):
    order_no = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    price = models.IntegerField()