from django.db import models
from datetime import date


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_lname = models.CharField(max_length=50, default="")
    customer_gender = models.CharField(max_length=15)
    customer_designation = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dob_date = models.DateField()
    password = models.CharField(max_length=500)
    imgc = models.ImageField(upload_to="shop/customer")


    def register(self):
        self.save()


    @staticmethod 
    def get_cust_by_phone(phone):
        try:
            return Customer.objects.get(phone = phone)
        except:
            return False



    def isExists(self):
        if Customer.objects.filter(phone = self.phone):
            return True

        return False