from django.contrib import admin
from .models import Seller, SellerCategory
# Register your models here.

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',
                    'store_name','address', 'store_image',
                    'qrcode_image', 'last_update')

@admin.register(SellerCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')