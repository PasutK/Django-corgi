from django.db import models
from django import forms
from .models import *

class AddtoCart(forms.ModelForm):
    class Meta:
        model = Cartitem
        fields = ["amount"]
