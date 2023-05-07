from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.sbase,name='seller-homepage'),
    path('register/', views.register_seller,name='seller-register'),
    # path('login/', views.Slogin,name='seller-login'),
    path('products/', views.seller_product, name='seller_product'),
]
