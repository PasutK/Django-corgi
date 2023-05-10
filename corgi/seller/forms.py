from django import forms
from django.db import models
from .models import Seller, SellerProduct
import re

class NewSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["store_name", "store_address", "store_image", "qrcode_image"]

class SellerProfile(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["store_name", "store_address", "store_image", "qrcode_image"]
	
class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    # STATUS_CHOICES = (
    #     (True, 'Active'),
    #     (False, 'Out of stock')
    # )
    
    # status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    class Meta:
        model = SellerProduct
        fields = ['name', 'category', 'description', 'quantity', 'price', 'image', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control','rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = SellerProduct
        fields = ['name', 'category', 'description', 'quantity', 'price', 'image', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }