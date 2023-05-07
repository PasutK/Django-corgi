from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

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

    # def save(self, commit=True):
    #     user = super(FormRegistration, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     user.username = self.cleaned_data["username"]

    #     if commit:
    #         user.save()
    #     return user
    