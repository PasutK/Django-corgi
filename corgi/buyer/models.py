from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.html import format_html
import re
from seller.models import Seller


def is_valid_buyer_phone(phone):
    """
    Returns True if the phone number is valid, False otherwise.
    """
    regex = r'^\d{3}[-]?\d{3}[-]?\d{4}$'
    return re.match(regex, phone) is not None

def validate_buyer_phone(phone):
    """
    Validates that the phone number is a valid 10-digit phone number.
    """
    if not is_valid_buyer_phone(phone):
        raise ValidationError("Please enter a valid 10-digit phone number.")

def is_valid_buyer_email(email):
    """
    Returns True if the email address is valid, False otherwise.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def validate_buyer_email(email):
    """
    Validates that the email address is a valid email address.
    """
    if not is_valid_buyer_email(email):
        raise ValidationError("Please enter a valid email address.")


class BuyerProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_buyer_email])
    phone = models.CharField(max_length=12, validators=[validate_buyer_phone])
    address = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    def __str__(self):
        return self.name
    def img_preview(self, obj):
        return format_html('<img src="{}" width="300"/>'.format(obj.image.url))

class Product(models.Model):
    name = models.CharField(max_length=255)
    describtion = models.CharField(max_length=500)
    price = models.DecimalField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to="uploads/products/")
    status = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,default=1)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    address = models.CharField(max_length=50, default="", blank=True)
    phone = models.CharField(max_length=50, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)