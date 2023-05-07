from django.db import models
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from seller.models import Seller, SellerProduct
from core.models import User
import re, datetime


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_paid = models.BooleanField(default=False)
    product = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True) 
    price = models.DecimalField(max_digits=6, decimal_places= 2)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.product,self.customer,self.quantity