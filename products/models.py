from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django_prices.models import PriceField
import datetime


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = PriceField('Price', currency='USD', max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE,)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])
