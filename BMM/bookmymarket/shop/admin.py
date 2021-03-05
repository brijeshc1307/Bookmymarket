from django.contrib import admin

from . models import Product
from .customer import Customer
from .order import Order
from .services import Services


admin.site.register(Product)

admin.site.register(Customer)

admin.site.register(Order)

admin.site.register(Services)


