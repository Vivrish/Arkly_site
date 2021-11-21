from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=4)
    type = models.CharField(max_length=30)
    quantity = models.SmallIntegerField()
    description = models.CharField(max_length=200)
    is_available = models.BooleanField()
# Create your models here.
