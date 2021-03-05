from django.db import models
import datetime
class Work(models.Model):
    Service_name = models.CharField(max_length=50, default="", choices=[('Rotavetor Cultivation','Rotavetor Cultivation'), ('Cultivation','Cultivation'),('Wet Field','Cultivation of Wet Field'),('Irrigation','Irrigation'),('Trolley','Trolley')])
    date = models.DateField(default=datetime.datetime.today)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    Unit = models.CharField(max_length=50, default="",choices=[('Bheega', 'Bheega'),('Mandi', 'Mandi'),('Hour', 'Hour'), ('Minute', 'Minute'),('Kilo Meter', 'Kilo Meter')])


