from django.db import models
from django import forms
from .models import Cart

class AddtoCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["amount"]
