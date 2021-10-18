from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=5)
    type = models.CharField(max_length=30)
    image = models.ImageField(upload_to='C:/Users/kolya/Documents/GitHub/Arkly_site/Uploads')
    is_available = models.BooleanField()
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name




# Create your models here.
