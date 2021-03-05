from django.db import models
from django_countries.fields import CountryField

class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    product_made = CountryField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=30, default="", choices=[('Fertilizers','Fertilizers'), ('Agri Machinery','Agri Machinery'),('Pesticide','Pesticide'),('Seeds','Seeds'),('Gardennig','Gardennig')])
    sub_category = models.CharField(max_length=30, default="")
    image = models.ImageField(upload_to="shop/images", default="")
    discount_price = models.IntegerField(default=0)
    img2 = models.ImageField(upload_to="shop/images", default="")

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def after_discount(price, discount_price):
        selling = price*(1- discount_price/100)
        return selling

def __str__(self):
    return self.product_name









