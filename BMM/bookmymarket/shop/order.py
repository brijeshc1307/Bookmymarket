from django.db import models
from .models import Product
from .customer import Customer
import datetime
from django_countries.fields import CountryField

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    customer_fname = models.CharField(max_length=50)
    customer_lname = models.CharField(max_length=50)
    billing_country = CountryField()
    date = models.DateField(default=datetime.datetime.today)
    street = models.CharField(max_length=50,default='', blank=True)
    apartment = models.CharField(max_length=50,default='', blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    notes = models.CharField(max_length=50, default='', blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def placeOrder(self):
        self.save()

