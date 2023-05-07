from django import forms
from django.db import models
from .models import Seller, SellerProduct
import re

class NewSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["store_name", "store_address", "store_image", "qrcode_image"]

	
class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model = SellerProduct
        fields = ('name', 'image', 'category', 'price', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
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