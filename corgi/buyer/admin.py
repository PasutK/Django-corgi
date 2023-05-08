from django.contrib import admin
from django.shortcuts import render
from .models import *

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('date','product','price','customer','amount','is_paid')
