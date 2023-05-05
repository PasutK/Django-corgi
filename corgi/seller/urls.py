from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Slogin, register_seller

urlpatterns = [
    path('', views.sbase,name='seller-homepage'),
    path('register/', views.register_seller,name='seller-register'),
    path('login/', views.Slogin,name='seller-login'),

]
