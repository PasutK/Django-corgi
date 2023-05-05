from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Seller
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

class NewSellerForm(UserCreationForm):
    # email = forms.EmailField(required=True, validators=[validate_buyer_email])
    # password = forms.CharField(max_length=50)
    # store_name = forms.CharField(max_length=50)
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=100)
    # phone = forms.CharField(max_length=12, validators=[validate_buyer_phone])
    # address = forms.CharField(max_length=100)
    # store_image = forms.ImageField(upload_to="seller/media/store/")
    # qrcode_image = forms.ImageField(upload_to="seller/media/qrcode/")
    # last_update = forms.DateTimeField(auto_now=True)

    class Meta:
        model = Seller
        fields = ("email", "password1", "password2", 
                  "first_name", "last_name", "phone",
                  "address", "store_image", "qrcode_image")

    # def save(self, commit=True):
    #     user = super(NewSellerForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.phone = self.cleaned_data['phone']
    #     user.address = self.cleaned_data['address']


    #     if commit:
    #         user.save()
    #     return user

	
class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)