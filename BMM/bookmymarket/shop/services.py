from django.db import models
from .customer import Customer
import datetime
class Services(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    Service_name = models.CharField(max_length=50, default="", choices=[('Rotavetor Cultivation','Rotavetor Cultivation'), ('Cultivation','Cultivation'),('Wet Field','Cultivation of Wet Field'),('Irrigation','Irrigation'),('Trolley','Trolley')])
    date = models.DateField(default=datetime.datetime.today)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    Unit = models.CharField(max_length=50, default="",choices=[('Bheega', 'Bheega'),('Mandi', 'Mandi'),('Hour', 'Hour'), ('Minute', 'Minute'),('Kilo Meter', 'Kilo Meter')])

