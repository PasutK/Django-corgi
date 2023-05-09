from django.db import models
from django import forms
from .models import Cart, User
from django.core.validators import RegexValidator


class AddtoCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["amount"]

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    phone_regex = RegexValidator(
        regex='^09\d{9}$', 
        message='Phone number must be in the format 0XXXXXXXXXX'
    )
    phone_number = forms.CharField(
        validators=[phone_regex],
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class CheckoutForm(forms.ModelForm):
    pass