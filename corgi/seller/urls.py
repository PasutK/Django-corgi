from django.contrib import admin
from django.urls import path,include
from .views import Homepage

urlpatterns = [
    path('', Homepage.as_view(),name='seller-homepage'),
]
