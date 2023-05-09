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

    def placeOrder(self):
        self.save()
    def __str__(self):
        return f"{self.product}"

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=10,default=None)