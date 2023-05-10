from django.db import models
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from seller.models import Seller, SellerProduct
from core.models import User
import re, datetime


class Cart(models.Model):
    is_paid = models.BooleanField(default=False)
    product = models.ForeignKey(SellerProduct, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    date = models.DateField(default=datetime.datetime.today)
    ordernumber = models.CharField(max_length=10,null=True,default=None)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,default=None)


# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     order = models.CharField(primary_key=True,max_length=10,default=None,unique=True)

class CartOrder(models.Model):
    is_check = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(primary_key=True,max_length=10,default=None,unique=True)
# class Order(models.Model):
#     order = models.CharField(primary_key=True,max_length=10,default=None,unique=True)

class Slip(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_check = models.BooleanField(default=False)
    slip_image = models.ImageField(upload_to="buyer/media/slip/", blank=False)