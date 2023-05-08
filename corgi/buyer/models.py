from django.db import models
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from seller.models import Seller, SellerProduct
from core.models import User
import re, datetime

class Order(models.Model):
    product = models.ForeignKey(SellerProduct, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    address = models.CharField(max_length=50, default="", blank=True)
    phone = models.CharField(max_length=50, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-date")
    