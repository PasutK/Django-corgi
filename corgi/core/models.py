from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from django.core.exceptions import ValidationError

def email_validator(value):
    pattern = r'@.+.chula.ac.th'
    if not re.search(pattern, value):
        raise ValidationError('Email address must end with chula.ac.th')
    
def phone_validator(value):
    pattern = r'^\d{3}[-]?\d{3}[-]?\d{4}$'
    if not re.search(pattern, value):
        raise ValidationError('Invalid Phone number')

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True, validators=[email_validator])
    phone = models.CharField(max_length=10, validators=[phone_validator])
    address = models.CharField(max_length=255)
