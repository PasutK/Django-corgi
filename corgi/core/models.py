from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save
import re

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
    def welcome(self):
        return "Only for Buyers"

@receiver(post_save, sender=User)
def create_buyer_profile(sender, instance, created, **kwargs):
    if created and instance.role == "BUYER":
        BuyerProfile.objects.create(user=instance)

class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buyer_id = models.IntegerField(null=True)

class CoreSellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)

class CoreSeller(User):
    base_role = User.Role.SELLER
    seller = CoreSellerManager()
    class META:
        proxy=True
    def welcome(self):
        return "Only for Sellers"

@receiver(post_save, sender=User)
def create_seller_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SELLER":
        SellerProfile.objects.create(user=instance)

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_id = models.IntegerField(null=True)