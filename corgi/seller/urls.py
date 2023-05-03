from django.contrib import admin
from django.urls import path,include
from .views import Homepage, Register

urlpatterns = [
    path('', Homepage.as_view(),name='seller-homepage'),
    path('register/', Register.as_view(),name='seller-register'),
]
