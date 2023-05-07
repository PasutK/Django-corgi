from django.db import models
from django import forms
from .models import Cartitems

class AddtoCart(forms.ModelForm):
    class Meta:
        model = Cartitems
        fields = ["amount"]
