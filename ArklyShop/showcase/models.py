from django.db import models
from django.urls import reverse

ascending_price = 'AP'  # Sorting options
descending_price = 'DP'
ascending_relevance = 'AR'
descending_relevance = 'DR'
ascending_date = 'AD'
descending_date = 'DD'
soring_choices = [
    (ascending_price, 'ascending_price'),
    (descending_price, 'descending_price'),
    (ascending_relevance, 'ascending_relevance'),
    (descending_relevance, 'descending_relevance'),
    (ascending_date, 'ascending_date'),
    (descending_date, 'descending_date')
]


class Stock(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=True)
    sort = models.CharField(max_length=20, choices=soring_choices, default='DP')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('showcase', kwargs={'slug': self.slug})


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    date = models.DateTimeField('date published', default=None)
    relevance = models.SmallIntegerField(default=0)
    image = models.ImageField(upload_to='upload/')
    type = models.CharField(max_length=20)
    size = models.CharField(max_length=4)
    quantity = models.SmallIntegerField()
    is_available = models.BooleanField()
    description = models.CharField(max_length=1000)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)  # A stock should not be deleted as long as it has items
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('showcase', kwargs={'slug': self.slug})
