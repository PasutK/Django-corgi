from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Seller
import re

# def is_valid_buyer_phone(phone):
#     """
#     Returns True if the phone number is valid, False otherwise.
#     """
#     regex = r'^\d{3}[-]?\d{3}[-]?\d{4}$'
#     return re.match(regex, phone) is not None

# def validate_buyer_phone(phone):
#     """
#     Validates that the phone number is a valid 10-digit phone number.
#     """
#     if not is_valid_buyer_phone(phone):
#         raise ValidationError("Please enter a valid 10-digit phone number.")

# def is_valid_buyer_email(email):
#     """
#     Returns True if the email address is valid, False otherwise.
#     """
#     regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(regex, email) is not None

# def validate_buyer_email(email):
#     """
#     Validates that the email address is a valid email address.
#     """
#     if not is_valid_buyer_email(email):
#         raise ValidationError("Please enter a valid email address.")

class NewSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [ 'email', 'password', 'store_name',
                  'first_name', 'last_name', 'phone',
                  'address', 'store_image', 'qrcode_image']

	
class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    
# เพิ่ม/แก้ไข/ลบสินค้า
# class SellerProduct(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="seller/media/product")
#     category = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     status = models.CharField(max_length=20)
#     seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

# class SellerProductForm(forms.ModelForm):
#     class Meta:
#         model = SellerProduct
#         fields = ['name', 'image', 'category', 'description', 'price', 'status']