from django.contrib import admin
from .models import Seller, SellerCategory, SellerProduct
# Register your models here.

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_image',
                    'qrcode_image', 'last_update',
                    'store_phone')

@admin.register(SellerCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image', 'status', 'quantity')

