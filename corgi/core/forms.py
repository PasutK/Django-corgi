from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
from django.forms import TextInput, EmailInput, Textarea

def email_validator(value):
    pattern = r'@.+.chula.ac.th'
    if not re.search(pattern, value):
        raise ValidationError('Email address must end with chula.ac.th')

class FormRegistration(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=100,)
    last_name = forms.CharField(max_length=100,)
    phone = forms.CharField(max_length=10,)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "phone", "email", "address", "password1", "password2")

class Editprofile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField(max_length=100,)
    phone_validator = RegexValidator(regex=r'^\d{10}$', message='Phone number must be 10 digits.')
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}), validators=[email_validator])
    phone = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), max_length=10, validators=[phone_validator])
    address = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': '3'}), max_length=255)
    first_name.widget = forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'rows': '1'})
    last_name.widget = forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'rows': '1'})

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', "address"]
