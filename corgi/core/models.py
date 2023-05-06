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

    class Role(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        BUYER = "BUYER","Buyer"
        SELLER = "SELLER","Seller"
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        
class CoreBuyerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BUYER)


class CoreBuyer(User):
    base_role = User.Role.BUYER
    buyer = CoreBuyerManager()
    class META:
        proxy=True

class CoreSellerrManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)


class CoreSeller(User):
    base_role = User.Role.SELLER
    buyer = CoreSellerrManager()
    class META:
        proxy=True