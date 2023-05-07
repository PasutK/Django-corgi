from django.db import models
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from seller.models import Seller, SellerProduct
from core.models import User
import re, datetime


# class BuyerProfile(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True, validators=[validate_buyer_email])
#     phone = models.CharField(max_length=12, validators=[validate_buyer_phone])
#     address = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    def __str__(self):
        return self.name
    def img_preview(self, obj):
        return format_html('<img src="{}" width="300"/>'.format(obj.image.url))

class Product(models.Model): # ต้องลบ จะเชื่อม product มาจาก seller
    name = models.CharField(max_length=255)
    describtion = models.CharField(max_length=500)
    price = models.DecimalField(max_digits= 7, decimal_places= 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to="uploads/products/")
    status = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,default=1)

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_paid = models.BooleanField(default=False)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) 
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)

    def placeorder(self):
        self.save()

    def __str__(self):
        return self.product,self.customer,self.quantity
    