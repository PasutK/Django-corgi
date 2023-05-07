from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
import re

# class SellerPermissions:
#     CAN_ADD_PRODUCT = 'can_add_product'

# def create_seller_permissions():
#     permission = Permission.objects.create(
#         codename=SellerPermissions.CAN_ADD_PRODUCT,
#         name='Can add products to marketplace',
#         content_type_id=0)
#     return permission


# sellers_group = Group.objects.create(name='Sellers')
    
class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,max_length=100, null=False, blank=False, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)
    store_address = models.CharField(max_length=300,default=None)
    store_image = models.ImageField(upload_to="seller/media/store/")
    qrcode_image = models.ImageField(upload_to="seller/media/qrcode/")
    last_update = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User) --> fix later

    @staticmethod
    def get_all_sellers():
            return Seller.objects.all()
            
    def __str__(self):
            return self.store_name

class SellerCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='seller/media/category')
    def __str__(self):
        return self.name
    def img_preview(self, obj):
        return format_html('<img src="{}" width="300"/>'.format(obj.image.url))
    
    @staticmethod
    def get_all_categories_by_sellerid(vendor_id):
        if vendor_id:
                return SellerCategory.objects.filter(vendor=vendor_id)
        else:
                return SellerCategory.get_all_categories()

class SellerProduct(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    category = models.ForeignKey(SellerCategory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to="seller/media/product")
    status = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"product: {self.name} from seller: {self.seller.store_name}"
