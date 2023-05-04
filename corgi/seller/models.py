from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html
import re

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
    
class Seller(models.Model):
    email = models.EmailField(unique=True, validators=[validate_buyer_email])
    password = models.CharField(max_length=100)
    store_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, validators=[validate_buyer_phone])
    address = models.CharField(max_length=300)
    store_image = models.ImageField(upload_to="seller/media/store/")
    qrcode_image = models.ImageField(upload_to="seller/media/qrcode/")
    last_update = models.DateTimeField(auto_now=True)
    
    def register(self):
        self.save()

class SellerCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='seller/media/category')
    def __str__(self):
        return self.name
    def img_preview(self, obj):
        return format_html('<img src="{}" width="300"/>'.format(obj.image.url))

class SellerProduct(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    category = models.ForeignKey(SellerCategory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to="seller/media/product")
    status = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,default=1)
